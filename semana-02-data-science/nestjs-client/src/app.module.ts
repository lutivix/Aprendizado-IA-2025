import { Module } from '@nestjs/common';
import { TitanicModule } from './titanic/titanic.module';

@Module({
  imports: [TitanicModule],
  controllers: [],
  providers: [],
})
export class AppModule {}
