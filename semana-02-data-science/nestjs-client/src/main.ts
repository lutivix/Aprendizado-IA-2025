import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { Logger } from '@nestjs/common';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  const logger = new Logger('Bootstrap');

  // Habilitar CORS para comunicação com frontend
  app.enableCors({
    origin: ['http://localhost:5173', 'http://localhost:3000'], // Vite e React
    methods: 'GET,HEAD,PUT,PATCH,POST,DELETE,OPTIONS',
    credentials: true,
  });

  const port = 3001; // Porta diferente da API Python (8000)
  
  await app.listen(port);
  
  logger.log('🚀 ================================================');
  logger.log('🚀 NestJS Titanic Client está rodando!');
  logger.log('🚀 ================================================');
  logger.log(`📍 URL: http://localhost:${port}`);
  logger.log(`🔗 Python API: http://localhost:8000`);
  logger.log('');
  logger.log('📌 Endpoints disponíveis:');
  logger.log('   GET  /titanic/health          - Health check');
  logger.log('   GET  /titanic/model           - Info do modelo');
  logger.log('   POST /titanic/predict         - Predição individual');
  logger.log('   POST /titanic/predict/batch   - Predição em lote');
  logger.log('🚀 ================================================');
}

bootstrap();
