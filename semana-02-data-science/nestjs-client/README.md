# 🚀 NestJS Titanic Client

Cliente NestJS que consome a API Python FastAPI de predição de sobrevivência no Titanic.

## 📋 Descrição

Este serviço atua como **intermediário** entre o frontend (React/Vite) e a API Python (FastAPI), fornecendo uma camada adicional de:
- ✅ Validação de dados
- ✅ Logging estruturado
- ✅ Tratamento de erros
- ✅ TypeScript type safety
- ✅ Documentação de API

## 🏗️ Arquitetura

```
Frontend (React/Vite)
         ↓
    HTTP Request
         ↓
NestJS Client (porta 3001)
         ↓
    HTTP Request
         ↓
Python FastAPI (porta 8000)
         ↓
    Modelo ML
         ↓
    Resposta JSON
```

## 📁 Estrutura

```
nestjs-client/
├── src/
│   ├── titanic/
│   │   ├── titanic.controller.ts    # Endpoints REST
│   │   ├── titanic.service.ts       # Lógica de negócio
│   │   ├── titanic.module.ts        # Módulo NestJS
│   │   └── titanic.dto.ts           # Data Transfer Objects
│   ├── app.module.ts                # Módulo raiz
│   └── main.ts                      # Bootstrap da aplicação
├── package.json
├── tsconfig.json
└── nest-cli.json
```

## 🚀 Como Executar

### 1. Instalar Dependências

```bash
npm install
```

### 2. Garantir que a API Python está rodando

```bash
# Em outro terminal, na pasta python-api/
python app.py
# Ou
uvicorn app:app --reload --port 8000
```

### 3. Iniciar o NestJS

```bash
# Modo desenvolvimento (com hot-reload)
npm run start:dev

# Modo produção
npm run build
npm run start:prod
```

A aplicação estará rodando em: **http://localhost:3001**

## 🔌 Endpoints

### 1. Health Check

```bash
GET http://localhost:3001/titanic/health
```

**Resposta:**
```json
{
  "status": "online",
  "message": "Titanic Survival Prediction API",
  "version": "1.0.0"
}
```

---

### 2. Informações do Modelo

```bash
GET http://localhost:3001/titanic/model
```

**Resposta:**
```json
{
  "model_type": "LogisticRegression",
  "accuracy": 0.7528,
  "features": ["Pclass", "sex_numeric", "Age", "family_size", "is_alone", "Fare"],
  "training_date": "2025-10-29"
}
```

---

### 3. Predição Individual

```bash
POST http://localhost:3001/titanic/predict
Content-Type: application/json

{
  "pclass": 1,
  "sex": "female",
  "age": 29,
  "siblings_spouses": 0,
  "parents_children": 0,
  "fare": 211.5
}
```

**Resposta:**
```json
{
  "survived": 1,
  "probability": 0.9615,
  "survival_chance": "Muito Alta",
  "features_used": {
    "Pclass": 1,
    "sex_numeric": 0,
    "Age": 29,
    "family_size": 1,
    "is_alone": 1,
    "Fare": 211.5
  }
}
```

---

### 4. Predição em Lote

```bash
POST http://localhost:3001/titanic/predict/batch
Content-Type: application/json

[
  {
    "pclass": 1,
    "sex": "female",
    "age": 25,
    "siblings_spouses": 0,
    "parents_children": 0,
    "fare": 100
  },
  {
    "pclass": 3,
    "sex": "male",
    "age": 22,
    "siblings_spouses": 1,
    "parents_children": 0,
    "fare": 7.25
  }
]
```

**Resposta:**
```json
{
  "total": 2,
  "predictions": [
    {
      "survived": 1,
      "probability": 0.9502,
      "survival_chance": "Muito Alta"
    },
    {
      "survived": 0,
      "probability": 0.1504,
      "survival_chance": "Muito Baixa"
    }
  ]
}
```

## 🧪 Testar com cURL

```bash
# Health check
curl http://localhost:3001/titanic/health

# Info do modelo
curl http://localhost:3001/titanic/model

# Predição
curl -X POST http://localhost:3001/titanic/predict \
  -H "Content-Type: application/json" \
  -d '{
    "pclass": 1,
    "sex": "female",
    "age": 29,
    "siblings_spouses": 0,
    "parents_children": 0,
    "fare": 211.5
  }'
```

## 📊 Exemplo com JavaScript/Fetch

```javascript
// Fazer predição
const response = await fetch('http://localhost:3001/titanic/predict', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    pclass: 1,
    sex: 'female',
    age: 29,
    siblings_spouses: 0,
    parents_children: 0,
    fare: 211.5
  })
});

const result = await response.json();
console.log(result);
// { survived: 1, probability: 0.9615, survival_chance: "Muito Alta", ... }
```

## 🎯 Conceitos NestJS

### 1. **Decorators**
```typescript
@Controller('titanic')  // Define rota base
@Get('health')         // GET /titanic/health
@Post('predict')       // POST /titanic/predict
@Body()                // Extrai body da requisição
```

### 2. **Dependency Injection**
```typescript
constructor(private readonly titanicService: TitanicService) {}
// NestJS injeta o serviço automaticamente
```

### 3. **HttpModule**
```typescript
// Fazer requisições HTTP para outras APIs
this.httpService.get('http://localhost:8000/')
```

### 4. **Exception Handling**
```typescript
throw new HttpException('Erro', HttpStatus.SERVICE_UNAVAILABLE);
// Retorna status HTTP apropriado
```

## 🔧 Tecnologias

- **NestJS** 10.0.0 - Framework Node.js
- **TypeScript** 5.1.3 - Type safety
- **Axios** 1.6.0 - HTTP client
- **RxJS** 7.8.1 - Programação reativa
- **Class-validator** 0.14.0 - Validação

## 📝 Scripts Disponíveis

```bash
npm run start          # Iniciar aplicação
npm run start:dev      # Modo desenvolvimento (hot-reload)
npm run start:prod     # Modo produção
npm run build          # Compilar TypeScript
npm run test           # Executar testes
npm run lint           # Verificar código
```

## 🚨 Troubleshooting

### Erro: "API Python não está disponível"
✅ Certifique-se de que a API Python está rodando em http://localhost:8000

### Erro: "Cannot find module"
✅ Execute `npm install`

### Erro de CORS
✅ CORS já está habilitado no `main.ts` para localhost:5173 (Vite) e localhost:3000 (React)

## 🔗 Próximos Passos

- [ ] Frontend React/Vite consumindo este serviço
- [ ] Dashboard com gráficos de predições
- [ ] Cache de resultados
- [ ] Rate limiting
- [ ] Autenticação JWT

---

**Status:** ✅ NestJS Client funcional  
**Porta:** 3001  
**Comunicação:** NestJS ↔ Python API ↔ ML Model
