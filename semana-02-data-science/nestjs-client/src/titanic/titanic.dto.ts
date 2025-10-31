/**
 * DTO para entrada de dados do passageiro
 */
export class PassengerDto {
  pclass: number;  // 1, 2 ou 3
  sex: string;     // 'male' ou 'female'
  age: number;
  siblings_spouses: number;
  parents_children: number;
  fare: number;
}

/**
 * Resposta da predição do modelo
 */
export class PredictionResponse {
  survived: number;           // 0 ou 1
  probability: number;        // 0.0 a 1.0
  survival_chance: string;    // "Muito Alta", "Alta", etc
  features_used: {
    Pclass: number;
    sex_numeric: number;
    Age: number;
    family_size: number;
    is_alone: number;
    Fare: number;
  };
}

/**
 * Informações do modelo ML
 */
export class ModelInfo {
  model_type: string;
  accuracy: number;
  features: string[];
  feature_descriptions: Record<string, string>;
  training_date: string;
}

/**
 * Health check response
 */
export class HealthResponse {
  status: string;
  message: string;
  version: string;
  endpoints: Record<string, string>;
}
