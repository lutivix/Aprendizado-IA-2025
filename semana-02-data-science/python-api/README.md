# 🚀 Titanic Survival Prediction API

API REST em Python usando FastAPI para predição de sobrevivência no Titanic usando Machine Learning.

## 📊 Sobre o Modelo

- **Algoritmo:** Logistic Regression
- **Acurácia:** 79% (acima da média Kaggle!)
- **Features utilizadas:**
  - `Pclass`: Classe do passageiro (1, 2 ou 3)
  - `sex_numeric`: Gênero (0=feminino, 1=masculino)
  - `Age`: Idade em anos
  - `family_size`: Tamanho da família
  - `is_alone`: Viajando sozinho (sim/não)
  - `Fare`: Tarifa paga

## 🛠️ Setup e Instalação

### 1. Criar ambiente virtual

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente (Windows)
venv\Scripts\activate

# Ativar ambiente (Linux/Mac)
source venv/bin/activate
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Treinar e salvar o modelo

```bash
python train_and_save_model.py
```

Este script vai:
- ✅ Carregar o dataset do Titanic
- ✅ Aplicar feature engineering
- ✅ Treinar o modelo Logistic Regression
- ✅ Avaliar a performance
- ✅ Salvar `model.pkl` e `model_metadata.json`

### 4. Executar a API

```bash
python app.py
```

ou com uvicorn:

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

## 📚 Documentação da API

Após iniciar a API, acesse:

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc
- **Health Check:** http://localhost:8000/

## 🔌 Endpoints

### 1. Health Check
```http
GET /
```

Retorna status da API.

### 2. Informações do Modelo
```http
GET /model/info
```

Retorna informações sobre o modelo (tipo, acurácia, features).

**Resposta:**
```json
{
  "model_type": "LogisticRegression",
  "accuracy": 0.79,
  "features": ["Pclass", "sex_numeric", "Age", "family_size", "is_alone", "Fare"],
  "feature_descriptions": {...},
  "training_date": "2025-10-29"
}
```

### 3. Predição Individual
```http
POST /predict
```

Faz predição para um passageiro.

**Request Body:**
```json
{
  "pclass": 3,
  "sex": "male",
  "age": 22.0,
  "siblings_spouses": 1,
  "parents_children": 0,
  "fare": 7.25
}
```

**Response:**
```json
{
  "survived": 0,
  "probability": 0.0912,
  "survival_chance": "Muito Baixa",
  "features_used": {
    "Pclass": 3,
    "sex_numeric": 1,
    "Age": 22.0,
    "family_size": 2,
    "is_alone": 0,
    "Fare": 7.25
  }
}
```

### 4. Predição em Lote
```http
POST /predict/batch
```

Faz predição para múltiplos passageiros.

**Request Body:**
```json
[
  {
    "pclass": 1,
    "sex": "female",
    "age": 29.0,
    "siblings_spouses": 0,
    "parents_children": 0,
    "fare": 211.5
  },
  {
    "pclass": 3,
    "sex": "male",
    "age": 22.0,
    "siblings_spouses": 1,
    "parents_children": 0,
    "fare": 7.25
  }
]
```

## 🧪 Testar a API

### Com cURL

```bash
# Health check
curl http://localhost:8000/

# Info do modelo
curl http://localhost:8000/model/info

# Predição
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "pclass": 1,
    "sex": "female",
    "age": 29.0,
    "siblings_spouses": 0,
    "parents_children": 0,
    "fare": 211.5
  }'
```

### Com Python

```python
import requests

# Predição
response = requests.post(
    "http://localhost:8000/predict",
    json={
        "pclass": 1,
        "sex": "female",
        "age": 29.0,
        "siblings_spouses": 0,
        "parents_children": 0,
        "fare": 211.5
    }
)

print(response.json())
```

### Com JavaScript/Fetch

```javascript
fetch('http://localhost:8000/predict', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    pclass: 1,
    sex: 'female',
    age: 29.0,
    siblings_spouses: 0,
    parents_children: 0,
    fare: 211.5
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

## 📊 Exemplos de Uso

### Passageiro de 1ª Classe (Alta chance)
```json
{
  "pclass": 1,
  "sex": "female",
  "age": 29.0,
  "siblings_spouses": 0,
  "parents_children": 0,
  "fare": 211.5
}
```
**Resultado esperado:** `survived: 1` (Alta probabilidade)

### Passageiro de 3ª Classe (Baixa chance)
```json
{
  "pclass": 3,
  "sex": "male",
  "age": 22.0,
  "siblings_spouses": 1,
  "parents_children": 0,
  "fare": 7.25
}
```
**Resultado esperado:** `survived: 0` (Baixa probabilidade)

## 🔧 Tecnologias Utilizadas

- **FastAPI:** Framework web moderno e rápido
- **Uvicorn:** Servidor ASGI de alta performance
- **Pydantic:** Validação de dados com type hints
- **scikit-learn:** Machine Learning
- **pandas:** Manipulação de dados
- **joblib:** Serialização do modelo

## 📁 Estrutura de Arquivos

```
python-api/
├── app.py                      # API FastAPI
├── train_and_save_model.py    # Script de treinamento
├── requirements.txt            # Dependências
├── model.pkl                   # Modelo treinado (gerado)
├── model_metadata.json         # Metadados do modelo (gerado)
├── .gitignore                  # Arquivos ignorados pelo git
└── README.md                   # Este arquivo
```

## ✅ Checklist de Funcionalidades

- [x] API REST com FastAPI
- [x] Endpoints GET e POST funcionando
- [x] Modelo ML integrado
- [x] Validação de entrada com Pydantic
- [x] Documentação automática (Swagger)
- [x] CORS habilitado
- [x] Tratamento de erros
- [x] Predição individual
- [x] Predição em lote
- [x] Metadados do modelo
- [x] Health check endpoint

## 🚀 Próximos Passos (Dia 3)

- [ ] Integrar com NestJS
- [ ] Criar frontend React/Vite
- [ ] Deploy da aplicação

## 📝 Notas

- Certifique-se de treinar o modelo primeiro antes de iniciar a API
- A API roda na porta 8000 por padrão
- CORS está habilitado para facilitar integração com frontend
- Use ambiente virtual para evitar conflitos de dependências
