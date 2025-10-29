"""
API REST para predição de sobrevivência no Titanic
Framework: FastAPI
Modelo: Logistic Regression (79% accuracy)
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, validator
import joblib
import json
import pandas as pd
from typing import Dict, List
import os

# Inicializar FastAPI
app = FastAPI(
    title="Titanic Survival Prediction API",
    description="API para predição de sobrevivência no Titanic usando Machine Learning",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carregar modelo e metadados
MODEL_PATH = "model.pkl"
METADATA_PATH = "model_metadata.json"

try:
    model = joblib.load(MODEL_PATH)
    with open(METADATA_PATH, 'r', encoding='utf-8') as f:
        metadata = json.load(f)
    print("✅ Modelo carregado com sucesso!")
except FileNotFoundError as e:
    print(f"❌ Erro: Arquivos do modelo não encontrados. Execute 'train_and_save_model.py' primeiro!")
    raise

# ============================================================================
# MODELOS PYDANTIC (Validação de dados)
# ============================================================================

class PassengerInput(BaseModel):
    """Modelo de entrada para predição"""
    pclass: int = Field(..., ge=1, le=3, description="Classe do passageiro (1, 2 ou 3)")
    sex: str = Field(..., description="Gênero do passageiro (male ou female)")
    age: float = Field(..., ge=0, le=120, description="Idade em anos")
    siblings_spouses: int = Field(..., ge=0, le=10, description="Número de irmãos/cônjuges a bordo")
    parents_children: int = Field(..., ge=0, le=10, description="Número de pais/filhos a bordo")
    fare: float = Field(..., ge=0, description="Tarifa paga")
    
    @validator('sex')
    def validate_sex(cls, v):
        if v.lower() not in ['male', 'female']:
            raise ValueError('Sex deve ser "male" ou "female"')
        return v.lower()
    
    class Config:
        schema_extra = {
            "example": {
                "pclass": 3,
                "sex": "male",
                "age": 22.0,
                "siblings_spouses": 1,
                "parents_children": 0,
                "fare": 7.25
            }
        }

class PredictionResponse(BaseModel):
    """Modelo de resposta da predição"""
    survived: int = Field(..., description="Predição (0=não sobreviveu, 1=sobreviveu)")
    probability: float = Field(..., description="Probabilidade de sobrevivência (0-1)")
    survival_chance: str = Field(..., description="Chance de sobrevivência em texto")
    features_used: Dict[str, float] = Field(..., description="Features utilizadas na predição")
    
class ModelInfo(BaseModel):
    """Informações sobre o modelo"""
    model_type: str
    accuracy: float
    features: List[str]
    feature_descriptions: Dict[str, str]
    training_date: str

# ============================================================================
# FUNÇÕES AUXILIARES
# ============================================================================

def prepare_features(passenger: PassengerInput) -> pd.DataFrame:
    """
    Prepara as features para predição
    Aplica o mesmo feature engineering do treinamento
    """
    # Converter sex para numérico
    sex_numeric = 1 if passenger.sex == 'male' else 0
    
    # Calcular family_size
    family_size = passenger.siblings_spouses + passenger.parents_children + 1
    
    # Calcular is_alone
    is_alone = 1 if family_size == 1 else 0
    
    # Criar DataFrame com as features na ordem correta
    features_dict = {
        'Pclass': passenger.pclass,
        'sex_numeric': sex_numeric,
        'Age': passenger.age,
        'family_size': family_size,
        'is_alone': is_alone,
        'Fare': passenger.fare
    }
    
    return pd.DataFrame([features_dict]), features_dict

def get_survival_text(probability: float) -> str:
    """Retorna texto descritivo da chance de sobrevivência"""
    if probability >= 0.8:
        return "Muito Alta"
    elif probability >= 0.6:
        return "Alta"
    elif probability >= 0.4:
        return "Moderada"
    elif probability >= 0.2:
        return "Baixa"
    else:
        return "Muito Baixa"

# ============================================================================
# ENDPOINTS
# ============================================================================

@app.get("/", tags=["Health"])
async def root():
    """Health check endpoint"""
    return {
        "status": "online",
        "message": "Titanic Survival Prediction API",
        "version": "1.0.0",
        "endpoints": {
            "docs": "/docs",
            "model_info": "/model/info",
            "predict": "/predict"
        }
    }

@app.get("/model/info", response_model=ModelInfo, tags=["Model"])
async def get_model_info():
    """
    Retorna informações sobre o modelo de ML
    - Tipo do modelo
    - Acurácia
    - Features utilizadas
    - Descrição das features
    """
    return metadata

@app.post("/predict", response_model=PredictionResponse, tags=["Prediction"])
async def predict_survival(passenger: PassengerInput):
    """
    Faz predição de sobrevivência para um passageiro do Titanic
    
    Parâmetros:
    - **pclass**: Classe do bilhete (1 = primeira classe, 2 = segunda, 3 = terceira)
    - **sex**: Gênero (male ou female)
    - **age**: Idade em anos
    - **siblings_spouses**: Número de irmãos/cônjuges a bordo
    - **parents_children**: Número de pais/filhos a bordo
    - **fare**: Tarifa paga pelo bilhete
    
    Retorna:
    - **survived**: 0 (não sobreviveu) ou 1 (sobreviveu)
    - **probability**: Probabilidade de sobrevivência (0.0 a 1.0)
    - **survival_chance**: Descrição textual da chance
    - **features_used**: Features utilizadas na predição
    """
    try:
        # Preparar features
        X, features_dict = prepare_features(passenger)
        
        # Fazer predição
        prediction = model.predict(X)[0]
        probability = model.predict_proba(X)[0][1]  # Probabilidade da classe 1 (sobreviveu)
        
        # Montar resposta
        response = PredictionResponse(
            survived=int(prediction),
            probability=round(float(probability), 4),
            survival_chance=get_survival_text(probability),
            features_used=features_dict
        )
        
        return response
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro na predição: {str(e)}")

@app.post("/predict/batch", tags=["Prediction"])
async def predict_batch(passengers: List[PassengerInput]):
    """
    Faz predição em lote para múltiplos passageiros
    
    Aceita uma lista de passageiros e retorna predições para todos
    """
    try:
        results = []
        
        for passenger in passengers:
            X, features_dict = prepare_features(passenger)
            prediction = model.predict(X)[0]
            probability = model.predict_proba(X)[0][1]
            
            results.append({
                "input": passenger.dict(),
                "survived": int(prediction),
                "probability": round(float(probability), 4),
                "survival_chance": get_survival_text(probability)
            })
        
        return {
            "total": len(results),
            "predictions": results
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro na predição em lote: {str(e)}")

# ============================================================================
# EXECUTAR APLICAÇÃO
# ============================================================================

if __name__ == "__main__":
    import uvicorn
    
    print("🚀 Iniciando Titanic Survival Prediction API...")
    print("📚 Documentação: http://localhost:8000/docs")
    print("🔄 ReDoc: http://localhost:8000/redoc")
    
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
