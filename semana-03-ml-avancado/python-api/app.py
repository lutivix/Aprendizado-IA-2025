"""
API FastAPI para predições do modelo Titanic
Dia 3 - Semana 3: Dashboard React Interativo
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import joblib
import pandas as pd
import numpy as np
from pathlib import Path
import json
from typing import Optional

app = FastAPI(
    title="Titanic ML API",
    description="API para predições de sobrevivência no Titanic",
    version="1.0.0"
)

# Configurar CORS para permitir requisições do React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carregar modelo e metadata
MODEL_PATH = Path(__file__).parent / "model.pkl"
METADATA_PATH = Path(__file__).parent / "model_metadata.json"

model = None
metadata = None

@app.on_event("startup")
async def load_model():
    """Carregar modelo ao iniciar a API"""
    global model, metadata
    
    if MODEL_PATH.exists():
        model = joblib.load(MODEL_PATH)
        print(f"✅ Modelo carregado: {MODEL_PATH}")
    else:
        print("⚠️ Modelo não encontrado. Execute train_model.py primeiro.")
    
    if METADATA_PATH.exists():
        with open(METADATA_PATH, 'r') as f:
            metadata = json.load(f)
        print(f"✅ Metadata carregada: {METADATA_PATH}")


class PassengerInput(BaseModel):
    """Schema de entrada para predição"""
    pclass: int = Field(..., ge=1, le=3, description="Classe do passageiro (1, 2 ou 3)")
    sex: str = Field(..., description="Sexo (male ou female)")
    age: float = Field(..., ge=0, le=100, description="Idade")
    sibsp: int = Field(..., ge=0, description="Número de irmãos/cônjuges a bordo")
    parch: int = Field(..., ge=0, description="Número de pais/filhos a bordo")
    fare: float = Field(..., ge=0, description="Tarifa paga")
    
    class Config:
        schema_extra = {
            "example": {
                "pclass": 3,
                "sex": "male",
                "age": 22.0,
                "sibsp": 1,
                "parch": 0,
                "fare": 7.25
            }
        }


class PredictionResponse(BaseModel):
    """Schema de resposta da predição"""
    survived: int
    probability: float
    message: str
    model_name: Optional[str] = None
    model_accuracy: Optional[float] = None


@app.get("/")
async def root():
    """Endpoint raiz"""
    return {
        "message": "Titanic ML API - Semana 3 Dia 3",
        "status": "online",
        "model_loaded": model is not None,
        "endpoints": {
            "health": "/health",
            "predict": "/predict",
            "model_info": "/model/info"
        }
    }


@app.get("/health")
async def health_check():
    """Verificar saúde da API"""
    return {
        "status": "healthy" if model is not None else "degraded",
        "model_loaded": model is not None,
        "metadata_loaded": metadata is not None
    }


@app.get("/model/info")
async def model_info():
    """Retornar informações do modelo"""
    if metadata is None:
        raise HTTPException(status_code=503, detail="Metadata não carregada")
    
    return metadata


@app.post("/predict", response_model=PredictionResponse)
async def predict(passenger: PassengerInput):
    """Realizar predição para um passageiro"""
    if model is None:
        raise HTTPException(
            status_code=503,
            detail="Modelo não carregado. Execute train_model.py primeiro."
        )
    
    try:
        # Converter Sex para numérico (male=1, female=0)
        sex_encoded = 1 if passenger.sex.lower() == 'male' else 0
        
        # Preparar dados para predição
        input_data = pd.DataFrame([{
            'Pclass': passenger.pclass,
            'Sex': sex_encoded,
            'Age': passenger.age,
            'SibSp': passenger.sibsp,
            'Parch': passenger.parch,
            'Fare': passenger.fare
        }])
        
        # Realizar predição
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]  # Probabilidade de sobrevivência
        
        # Preparar resposta
        message = "🎉 Sobreviveu!" if prediction == 1 else "😢 Não sobreviveu"
        
        response = {
            "survived": int(prediction),
            "probability": float(probability),
            "message": message
        }
        
        # Adicionar info do modelo se metadata existir
        if metadata:
            response["model_name"] = metadata.get("model_name")
            response["model_accuracy"] = metadata.get("accuracy")
        
        return response
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao processar predição: {str(e)}"
        )


@app.post("/predict/batch")
async def predict_batch(passengers: list[PassengerInput]):
    """Realizar predições em lote"""
    if model is None:
        raise HTTPException(status_code=503, detail="Modelo não carregado")
    
    try:
        # Preparar dados com conversão de Sex
        input_data = pd.DataFrame([{
            'Pclass': p.pclass,
            'Sex': 1 if p.sex.lower() == 'male' else 0,
            'Age': p.age,
            'SibSp': p.sibsp,
            'Parch': p.parch,
            'Fare': p.fare
        } for p in passengers])
        
        # Realizar predições
        predictions = model.predict(input_data)
        probabilities = model.predict_proba(input_data)[:, 1]
        
        # Preparar respostas
        results = []
        for i, (pred, prob) in enumerate(zip(predictions, probabilities)):
            results.append({
                "index": i,
                "survived": int(pred),
                "probability": float(prob),
                "message": "🎉 Sobreviveu!" if pred == 1 else "😢 Não sobreviveu"
            })
        
        return {
            "predictions": results,
            "total": len(results),
            "survived_count": int(predictions.sum()),
            "survival_rate": float(predictions.mean())
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    print("🚀 Iniciando Titanic ML API...")
    print("📍 Acesse: http://localhost:8000")
    print("📚 Docs: http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000)
