# 📅 Dia 2 - Semana 2: API REST com Python (FastAPI)

**Data:** 29 Out 2025  
**Status:** ✅ **CONCLUÍDO**  
**Tempo:** ~4 horas

---

## 🎯 Objetivos do Dia

- [x] Criar API REST com FastAPI
- [x] Integrar modelo ML treinado
- [x] Implementar endpoints GET e POST
- [x] Validação de dados com Pydantic
- [x] Documentação automática (Swagger)
- [x] Testes automatizados
- [x] CORS habilitado

---

## 📊 Resultados Alcançados

### ✅ API REST Completa

**Framework:** FastAPI 0.115.0  
**Servidor:** Uvicorn 0.32.0  
**Modelo:** LogisticRegression (75.28% accuracy)  
**Endpoints:** 4 funcionais  
**Testes:** 6/6 passando (100%)

### 📈 Performance

```
✅ Health Check         → 200 OK (5ms)
✅ Model Info          → 200 OK (8ms)
✅ Predict Individual  → 200 OK (12ms)
✅ Predict Batch       → 200 OK (35ms)
✅ Validation Error    → 422 Unprocessable Entity
```

---

## 🛠️ Tecnologias Utilizadas

### Backend
- **FastAPI** - Framework web moderno e rápido
- **Uvicorn** - Servidor ASGI de alta performance
- **Pydantic** - Validação de dados com type hints

### Machine Learning
- **scikit-learn** 1.7.2 - Modelo de ML
- **pandas** 2.2.3 - Manipulação de dados
- **numpy** 2.2.5 - Operações numéricas
- **joblib** 1.5.2 - Serialização do modelo

### Desenvolvimento
- **requests** 2.32.5 - Testes HTTP
- **pytest** (opcional) - Framework de testes

---

## 📁 Estrutura Criada

```
semana-02-data-science/python-api/
├── app.py                      # 🚀 API FastAPI (247 linhas)
├── train_and_save_model.py     # 🤖 Script de treinamento (180 linhas)
├── test_api.py                 # 🧪 Testes automatizados (280 linhas)
├── requirements.txt            # 📦 Dependências
├── model.pkl                   # 💾 Modelo treinado (3.2 KB)
├── model_metadata.json         # 📊 Metadados do modelo
├── README.md                   # 📚 Documentação completa
└── .gitignore                  # 🙈 Arquivos ignorados
```

**Total:** ~707 linhas de código Python  
**Arquivos criados:** 8

---

## 🔌 API Endpoints

### 1. **GET /** - Health Check
```bash
curl http://localhost:8000/
```

**Resposta:**
```json
{
  "status": "online",
  "message": "Titanic Survival Prediction API",
  "version": "1.0.0",
  "endpoints": {
    "docs": "/docs",
    "model_info": "/model/info",
    "predict": "/predict"
  }
}
```

---

### 2. **GET /model/info** - Informações do Modelo
```bash
curl http://localhost:8000/model/info
```

**Resposta:**
```json
{
  "model_type": "LogisticRegression",
  "accuracy": 0.7528089887640449,
  "features": [
    "Pclass",
    "sex_numeric",
    "Age",
    "family_size",
    "is_alone",
    "Fare"
  ],
  "feature_descriptions": {
    "Pclass": "Classe do passageiro (1, 2 ou 3)",
    "sex_numeric": "Gênero (0=feminino, 1=masculino)",
    "Age": "Idade em anos",
    "family_size": "Tamanho da família (incluindo passageiro)",
    "is_alone": "Viajando sozinho (0=não, 1=sim)",
    "Fare": "Tarifa paga"
  },
  "training_date": "2025-10-29"
}
```

---

### 3. **POST /predict** - Predição Individual

**Request:**
```bash
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

**Response:**
```json
{
  "survived": 1,
  "probability": 0.9615,
  "survival_chance": "Muito Alta",
  "features_used": {
    "Pclass": 1,
    "sex_numeric": 0,
    "Age": 29.0,
    "family_size": 1,
    "is_alone": 1,
    "Fare": 211.5
  }
}
```

**Interpretação:**
- ✅ **Sobreviveu:** `survived = 1`
- 📊 **Probabilidade:** 96.15% de chance
- 📈 **Avaliação:** Muito Alta

---

### 4. **POST /predict/batch** - Predição em Lote

**Request:**
```bash
curl -X POST http://localhost:8000/predict/batch \
  -H "Content-Type: application/json" \
  -d '[
    {
      "pclass": 1,
      "sex": "female",
      "age": 25.0,
      "siblings_spouses": 0,
      "parents_children": 0,
      "fare": 100.0
    },
    {
      "pclass": 3,
      "sex": "male",
      "age": 22.0,
      "siblings_spouses": 1,
      "parents_children": 0,
      "fare": 7.25
    }
  ]'
```

**Response:**
```json
{
  "total": 2,
  "predictions": [
    {
      "input": { "pclass": 1, "sex": "female", ... },
      "survived": 1,
      "probability": 0.9502,
      "survival_chance": "Muito Alta"
    },
    {
      "input": { "pclass": 3, "sex": "male", ... },
      "survived": 0,
      "probability": 0.1504,
      "survival_chance": "Muito Baixa"
    }
  ]
}
```

---

## 🧪 Testes Automatizados

### Resultados dos Testes

```bash
$ python test_api.py

🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
TESTE COMPLETO DA API TITANIC
🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀

✅ PASSOU - Health Check
✅ PASSOU - Model Info
✅ PASSOU - Predição Alta Chance
✅ PASSOU - Predição Baixa Chance
✅ PASSOU - Predição em Lote
✅ PASSOU - Validação de Entrada

============================================================
📊 Total: 6/6 testes passaram
📈 Taxa de sucesso: 100.0%
============================================================

🎉 TODOS OS TESTES PASSARAM! API FUNCIONANDO PERFEITAMENTE!
```

---

## 📚 Conceitos Aprendidos

### 1. **FastAPI Framework**

**O que é:**
- Framework web moderno para Python
- Baseado em type hints
- Documentação automática (Swagger/ReDoc)
- Validação automática de dados

**Por que usar:**
- ✅ Mais rápido que Flask
- ✅ Async/await nativo
- ✅ Validação com Pydantic
- ✅ Auto-documentação

**Comparação:**
```python
# Flask (tradicional)
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Validação manual necessária
    
# FastAPI (moderno)
@app.post('/predict')
async def predict(passenger: PassengerInput):
    # Validação automática!
```

---

### 2. **Pydantic - Validação de Dados**

**O que é:**
- Biblioteca para validação de dados
- Usa Python type hints
- Converte tipos automaticamente

**Exemplo:**
```python
from pydantic import BaseModel, Field

class PassengerInput(BaseModel):
    pclass: int = Field(..., ge=1, le=3)  # Entre 1 e 3
    sex: str                               # String obrigatória
    age: float = Field(..., ge=0, le=120) # Entre 0 e 120
```

**Vantagens:**
- ✅ Validação automática
- ✅ Mensagens de erro claras
- ✅ Documentação automática
- ✅ Type safety

---

### 3. **Serialização de Modelos ML**

**Joblib vs Pickle vs JSON:**

| Método | Uso | Vantagens | Limitações |
|--------|-----|-----------|------------|
| **joblib** | Modelos ML | Rápido, compressão | Só Python |
| **pickle** | Objetos Python | Nativo | Lento com arrays |
| **JSON** | Dados simples | Universal | Não salva modelos |

**Implementação:**
```python
# Salvar modelo
joblib.dump(model, 'model.pkl')

# Carregar modelo
model = joblib.load('model.pkl')
```

---

### 4. **CORS (Cross-Origin Resource Sharing)**

**O que é:**
- Mecanismo de segurança do navegador
- Controla quais domínios podem acessar a API

**Por que configurar:**
- Frontend em outro domínio/porta
- Desenvolvimento local
- Integração com apps externos

**Configuração:**
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],           # Qualquer origem
    allow_credentials=True,
    allow_methods=["*"],           # GET, POST, etc
    allow_headers=["*"],
)
```

---

### 5. **Uvicorn - Servidor ASGI**

**O que é:**
- Servidor web para aplicações assíncronas
- Baseado em uvloop (mais rápido que asyncio)
- Suporta WebSockets

**Como usar:**
```bash
# Modo desenvolvimento (com reload)
uvicorn app:app --reload --port 8000

# Modo produção
uvicorn app:app --host 0.0.0.0 --port 8000 --workers 4
```

---

## 🔍 Fluxo de Execução

### Inicialização da API

```
1. Importações
   ↓
2. Criar app = FastAPI()
   ↓
3. Configurar CORS
   ↓
4. Carregar model.pkl ← 🤖 MODELO PRONTO!
   ↓
5. Definir schemas Pydantic
   ↓
6. Registrar endpoints (@app.get, @app.post)
   ↓
7. uvicorn.run() ← 🚀 SERVIDOR INICIADO!
```

### Processamento de Requisição

```
Cliente → POST /predict
   ↓
FastAPI recebe requisição
   ↓
Pydantic valida dados automaticamente
   ↓
Chama função predict_survival()
   ↓
Prepara features (feature engineering)
   ↓
model.predict(features) ← 🤖 PREDIÇÃO
   ↓
Formata resposta JSON
   ↓
Cliente ← Retorna resultado
```

---

## 💡 Boas Práticas Implementadas

### 1. **Validação de Entrada**
```python
class PassengerInput(BaseModel):
    pclass: int = Field(..., ge=1, le=3)  # Validação de range
    
    @validator('sex')
    def validate_sex(cls, v):
        if v.lower() not in ['male', 'female']:
            raise ValueError('Sex deve ser "male" ou "female"')
        return v.lower()
```

### 2. **Tratamento de Erros**
```python
try:
    model = joblib.load(MODEL_PATH)
except FileNotFoundError:
    print("❌ Erro: Modelo não encontrado!")
    raise
```

### 3. **Documentação Automática**
```python
@app.post("/predict", response_model=PredictionResponse)
async def predict_survival(passenger: PassengerInput):
    """
    Faz predição de sobrevivência para um passageiro do Titanic
    
    Parâmetros:
    - **pclass**: Classe do bilhete (1, 2 ou 3)
    - **sex**: Gênero (male ou female)
    ...
    """
```

### 4. **Type Hints**
```python
def prepare_features(passenger: PassengerInput) -> pd.DataFrame:
    ...
    return pd.DataFrame([features_dict])
```

### 5. **Separação de Concerns**
```python
# Preparação de dados
def prepare_features() -> pd.DataFrame: ...

# Lógica de negócio
def get_survival_text(probability: float) -> str: ...

# Endpoints
@app.post("/predict")
async def predict_survival(): ...
```

---

## 📊 Casos de Teste

### Teste 1: Mulher, 1ª Classe (Alta Chance)
```python
Input:  pclass=1, sex="female", age=29, fare=211.5
Output: survived=1, probability=96.15%
Status: ✅ PASSOU
```

### Teste 2: Homem, 3ª Classe (Baixa Chance)
```python
Input:  pclass=3, sex="male", age=22, fare=7.25
Output: survived=0, probability=15.04%
Status: ✅ PASSOU
```

### Teste 3: Validação - Classe Inválida
```python
Input:  pclass=5 (inválido)
Output: 422 Unprocessable Entity
Status: ✅ PASSOU (erro esperado)
```

---

## 🚀 Como Executar

### 1. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 2. Treinar Modelo
```bash
python train_and_save_model.py
```

**Saída esperada:**
```
✅ Dataset carregado: 887 registros
✅ Acurácia: 75.28%
✅ Modelo salvo: model.pkl
```

### 3. Iniciar API
```bash
python app.py
# ou
uvicorn app:app --reload
```

**Saída esperada:**
```
✅ Modelo carregado com sucesso!
🚀 Iniciando Titanic Survival Prediction API...
📚 Documentação: http://localhost:8000/docs
INFO: Uvicorn running on http://0.0.0.0:8000
```

### 4. Testar API
```bash
python test_api.py
```

**Saída esperada:**
```
✅ PASSOU - Health Check
✅ PASSOU - Model Info
✅ PASSOU - Predição Alta Chance
✅ PASSOU - Predição Baixa Chance
✅ PASSOU - Predição em Lote
✅ PASSOU - Validação de Entrada
📊 Total: 6/6 testes passaram
```

---

## 🌐 Acessar Documentação

Após iniciar a API, acesse:

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc
- **Health Check:** http://localhost:8000/

---

## 🎓 Diferenças: FastAPI vs NestJS

| Aspecto | FastAPI (Python) | NestJS (TypeScript) |
|---------|------------------|---------------------|
| **Estrutura** | 1 arquivo possível | Múltiplos arquivos obrigatórios |
| **Decorators** | `@app.get()` | `@Controller()`, `@Get()` |
| **Validação** | Pydantic (automática) | class-validator (manual) |
| **Documentação** | Automática (Swagger) | Precisa configurar |
| **Async** | `async def` nativo | `async/await` nativo |
| **Type Safety** | Type hints (opcional) | TypeScript (obrigatório) |
| **Servidor** | Uvicorn (manual) | Integrado no framework |
| **Modularização** | Opcional | Obrigatória (modules) |

**Conclusão:**
- **FastAPI:** Mais rápido para prototipar, flexível
- **NestJS:** Mais estruturado, escalável desde o início

---

## 🔗 Recursos Adicionais

### Documentação Oficial
- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/)
- [scikit-learn](https://scikit-learn.org/)

### Tutoriais
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Pydantic Validation](https://docs.pydantic.dev/latest/concepts/validators/)
- [ML Model Deployment](https://fastapi.tiangolo.com/deployment/)

---

## 📝 Próximos Passos (Dia 3)

- [ ] Integrar API Python com NestJS
- [ ] Consumer NestJS para API Python
- [ ] Frontend React/Vite (bônus)
- [ ] Sistema full stack integrado

---

## ✅ Checklist de Conclusão

- [x] API REST criada com FastAPI
- [x] 4 endpoints funcionando
- [x] Modelo ML integrado (75% accuracy)
- [x] Validação com Pydantic
- [x] CORS configurado
- [x] Documentação Swagger automática
- [x] 6 testes automatizados (100% passando)
- [x] README completo
- [x] Código comentado e organizado

---

## 🎉 Conquistas do Dia

✅ **API REST funcional** em Python  
✅ **Modelo ML em produção** (75.28% accuracy)  
✅ **Documentação automática** com Swagger  
✅ **Validação robusta** com Pydantic  
✅ **Testes automatizados** (100% sucesso)  
✅ **~707 linhas** de código Python  
✅ **8 arquivos** criados  

**Status:** 🟢 DIA 2 CONCLUÍDO COM SUCESSO! 🎯

---

**Próximo desafio:** Dia 3 - Integração Full Stack (Python + NestJS + React) 🚀
