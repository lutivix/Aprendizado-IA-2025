# 🐍 Python API - FastAPI

API REST para predições do modelo Titanic usando FastAPI.

## 🚀 Setup

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Treinar o modelo

```bash
python train_model.py
```

Isso vai:
- Baixar o dataset Titanic
- Treinar um Random Forest
- Salvar `model.pkl` e `model_metadata.json`

### 3. Iniciar a API

```bash
python app.py
```

A API estará disponível em: `http://localhost:8000`

## 📚 Documentação

### Swagger UI (Interativa)
`http://localhost:8000/docs`

### ReDoc
`http://localhost:8000/redoc`

## 🧪 Testar a API

```bash
python test_api.py
```

## 📍 Endpoints

### `GET /`
Informações gerais da API

### `GET /health`
Verificar saúde da API

### `GET /model/info`
Informações do modelo (accuracy, features, etc.)

### `POST /predict`
Predição única

**Exemplo:**
```json
{
  "pclass": 3,
  "sex": "male",
  "age": 22.0,
  "sibsp": 1,
  "parch": 0,
  "fare": 7.25,
  "embarked": "S"
}
```

**Resposta:**
```json
{
  "survived": 0,
  "probability": 0.12,
  "message": "😢 Não sobreviveu",
  "model_name": "Random Forest Classifier",
  "model_accuracy": 0.8268
}
```

### `POST /predict/batch`
Predições em lote (array de passageiros)

## 🔧 Tecnologias

- **FastAPI** - Framework web moderno
- **Pydantic** - Validação de dados
- **Scikit-learn** - Machine Learning
- **Uvicorn** - ASGI server
