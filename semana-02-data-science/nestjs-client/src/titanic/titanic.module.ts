import { Module } from '@nestjs/common';
import { HttpModule } from '@nestjs/axios';
import { TitanicController } from './titanic.controller';
import { TitanicService } from './titanic.service';

@Module({
  imports: [
    HttpModule.register({
      timeout: 30000, // 30 segundos
      maxRedirects: 5,
    }),
  ],
  controllers: [TitanicController],
  providers: [TitanicService],
  exports: [TitanicService],
})
export class TitanicModule {}
