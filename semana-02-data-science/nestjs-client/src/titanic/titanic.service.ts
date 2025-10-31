import { Injectable, Logger, HttpException, HttpStatus } from '@nestjs/common';
import { HttpService } from '@nestjs/axios';
import { firstValueFrom } from 'rxjs';
import { PassengerDto, PredictionResponse, ModelInfo, HealthResponse } from './titanic.dto';

/**
 * Serviço para comunicação com a API Python FastAPI
 */
@Injectable()
export class TitanicService {
  private readonly logger = new Logger(TitanicService.name);
  private readonly pythonApiUrl = 'http://127.0.0.1:8000';

  constructor(private readonly httpService: HttpService) {}

  /**
   * Health check da API Python
   */
  async checkPythonApiHealth(): Promise<HealthResponse> {
    try {
      this.logger.log('🔍 Verificando saúde da API Python...');
      this.logger.debug(`URL: ${this.pythonApiUrl}/`);
      
      const response = await firstValueFrom(
        this.httpService.get<HealthResponse>(`${this.pythonApiUrl}/`)
      );
      
      this.logger.log('✅ API Python está online!');
      return response.data;
    } catch (error) {
      this.logger.error('❌ Erro ao conectar com API Python:');
      this.logger.error(`Mensagem: ${error.message}`);
      this.logger.error(`Código: ${error.code}`);
      this.logger.error(`Stack: ${error.stack}`);
      throw new HttpException(
        `API Python não está disponível: ${error.message}`,
        HttpStatus.SERVICE_UNAVAILABLE
      );
    }
  }

  /**
   * Obter informações do modelo ML
   */
  async getModelInfo(): Promise<ModelInfo> {
    try {
      this.logger.log('📊 Buscando informações do modelo...');
      
      const response = await firstValueFrom(
        this.httpService.get<ModelInfo>(`${this.pythonApiUrl}/model/info`)
      );
      
      this.logger.log(`✅ Modelo: ${response.data.model_type} (${response.data.accuracy * 100}% accuracy)`);
      return response.data;
    } catch (error) {
      this.logger.error('❌ Erro ao buscar info do modelo:', error.message);
      throw new HttpException(
        'Erro ao buscar informações do modelo',
        HttpStatus.INTERNAL_SERVER_ERROR
      );
    }
  }

  /**
   * Fazer predição individual
   */
  async predict(passenger: PassengerDto): Promise<PredictionResponse> {
    try {
      this.logger.log('🤖 Fazendo predição...');
      this.logger.debug(`Dados: ${JSON.stringify(passenger)}`);
      
      const response = await firstValueFrom(
        this.httpService.post<PredictionResponse>(
          `${this.pythonApiUrl}/predict`,
          passenger
        )
      );
      
      const result = response.data;
      this.logger.log(
        `✅ Predição: ${result.survived === 1 ? 'SOBREVIVEU' : 'NÃO SOBREVIVEU'} (${(result.probability * 100).toFixed(2)}%)`
      );
      
      return result;
    } catch (error) {
      this.logger.error('❌ Erro na predição:', error.message);
      
      if (error.response?.status === 422) {
        throw new HttpException(
          'Dados inválidos. Verifique os valores enviados.',
          HttpStatus.BAD_REQUEST
        );
      }
      
      throw new HttpException(
        'Erro ao fazer predição',
        HttpStatus.INTERNAL_SERVER_ERROR
      );
    }
  }

  /**
   * Fazer predição em lote
   */
  async predictBatch(passengers: PassengerDto[]): Promise<any> {
    try {
      this.logger.log(`🤖 Fazendo predição em lote (${passengers.length} passageiros)...`);
      
      const response = await firstValueFrom(
        this.httpService.post(
          `${this.pythonApiUrl}/predict/batch`,
          passengers
        )
      );
      
      this.logger.log(`✅ Predições em lote concluídas!`);
      return response.data;
    } catch (error) {
      this.logger.error('❌ Erro na predição em lote:', error.message);
      throw new HttpException(
        'Erro ao fazer predição em lote',
        HttpStatus.INTERNAL_SERVER_ERROR
      );
    }
  }
}
