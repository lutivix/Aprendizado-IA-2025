import { Controller, Get, Post, Body, Logger } from '@nestjs/common';
import { TitanicService } from './titanic.service';
import { PassengerDto, PredictionResponse, ModelInfo, HealthResponse } from './titanic.dto';

/**
 * Controller que expõe endpoints REST para integração com frontend
 * Atua como proxy/intermediário entre frontend e API Python
 */
@Controller('titanic')
export class TitanicController {
  private readonly logger = new Logger(TitanicController.name);

  constructor(private readonly titanicService: TitanicService) {}

  /**
   * GET /titanic/health
   * Verifica se a API Python está rodando
   */
  @Get('health')
  async checkHealth(): Promise<HealthResponse> {
    this.logger.log('🏥 Health check solicitado');
    return await this.titanicService.checkPythonApiHealth();
  }

  /**
   * GET /titanic/model
   * Retorna informações sobre o modelo ML
   */
  @Get('model')
  async getModelInfo(): Promise<ModelInfo> {
    this.logger.log('📊 Informações do modelo solicitadas');
    return await this.titanicService.getModelInfo();
  }

  /**
   * POST /titanic/predict
   * Faz predição de sobrevivência para um passageiro
   * 
   * Body exemplo:
   * {
   *   "pclass": 1,
   *   "sex": "female",
   *   "age": 29,
   *   "siblings_spouses": 0,
   *   "parents_children": 0,
   *   "fare": 211.5
   * }
   */
  @Post('predict')
  async predict(@Body() passenger: PassengerDto): Promise<PredictionResponse> {
    this.logger.log('🎯 Predição solicitada');
    return await this.titanicService.predict(passenger);
  }

  /**
   * POST /titanic/predict/batch
   * Faz predição para múltiplos passageiros
   * 
   * Body: array de PassengerDto
   */
  @Post('predict/batch')
  async predictBatch(@Body() passengers: PassengerDto[]): Promise<any> {
    this.logger.log(`🎯 Predição em lote solicitada (${passengers.length} passageiros)`);
    return await this.titanicService.predictBatch(passengers);
  }
}
