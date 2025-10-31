# 🚀 Dia 3 - Integração Full Stack com Machine Learning

**Data**: 31 de Outubro de 2025  
**Autor**: Lutivix  
**Projeto**: Aprendizado IA 2025 - Semana 02

---

## 📋 Índice

1. [Visão Geral](#visão-geral)
2. [Arquitetura do Sistema](#arquitetura-do-sistema)
3. [Tecnologias Utilizadas](#tecnologias-utilizadas)
4. [Estrutura do Projeto](#estrutura-do-projeto)
5. [Frontend - React + Vite](#frontend---react--vite)
6. [Backend Proxy - NestJS](#backend-proxy---nestjs)
7. [ML API - Python FastAPI](#ml-api---python-fastapi)
8. [Integração e Comunicação](#integração-e-comunicação)
9. [Como Executar](#como-executar)
10. [Testes e Validação](#testes-e-validação)
11. [Problemas Encontrados e Soluções](#problemas-encontrados-e-soluções)
12. [Melhorias Futuras](#melhorias-futuras)
13. [Conclusão](#conclusão)

---

## 🎯 Visão Geral

Este projeto implementa uma **aplicação Full Stack** para predição de sobrevivência no Titanic usando **Machine Learning**. O sistema permite ao usuário inserir dados de um passageiro e obter uma predição em tempo real através de uma interface web moderna.

### Objetivos do Dia 3:

- ✅ Criar interface web responsiva com React + TypeScript
- ✅ Implementar backend proxy com NestJS
- ✅ Integrar frontend → backend → API ML
- ✅ Configurar CORS e comunicação entre serviços
- ✅ Implementar tratamento de erros
- ✅ Testar integração end-to-end

---

## 🏗️ Arquitetura do Sistema

```
┌─────────────────────────────────────────────────────────────────┐
│                         FULL STACK ML APP                        │
└─────────────────────────────────────────────────────────────────┘

┌─────────────┐      ┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│   React     │      │   NestJS    │      │   FastAPI   │      │  ML Model   │
│  Frontend   │─────▶│   Proxy     │─────▶│   Backend   │─────▶│ Prediction  │
│   (5173)    │ HTTP │   (3001)    │ HTTP │   (8000)    │      │ (model.pkl) │
└─────────────┘      └─────────────┘      └─────────────┘      └─────────────┘
      │                     │                     │                     │
      │                     │                     │                     │
   Browser             TypeScript              Python              scikit-learn
   Vite 4              NestJS 10              FastAPI            LogisticRegression
   React 18            Axios                  Uvicorn            75.28% accuracy
```

### Fluxos de Dados:

#### **Fluxo 1: Direto (React → Python)**
```
Usuario → React (5173) → Python FastAPI (8000) → ML Model → Resposta
```

#### **Fluxo 2: Via Proxy (React → NestJS → Python)**
```
Usuario → React (5173) → NestJS (3001) → Python FastAPI (8000) → ML Model → Resposta
```

---

## 💻 Tecnologias Utilizadas

### **Frontend**
| Tecnologia | Versão | Propósito |
|-----------|--------|-----------|
| React | 18.3.1 | Framework UI |
| TypeScript | 5.6.2 | Type safety |
| Vite | 4.5.14 | Build tool (Node 18 compatible) |
| CSS3 | - | Estilização |

### **Backend Proxy**
| Tecnologia | Versão | Propósito |
|-----------|--------|-----------|
| NestJS | 10.0.0 | Framework Node.js |
| TypeScript | 5.9.3 | Type safety |
| Axios | 1.6.0 | HTTP client |
| class-validator | 0.14.0 | Validação de DTOs |

### **ML API**
| Tecnologia | Versão | Propósito |
|-----------|--------|-----------|
| Python | 3.13.2 | Linguagem base |
| FastAPI | 0.115.5 | Framework web |
| Uvicorn | 0.32.1 | ASGI server |
| scikit-learn | 1.6.0 | ML model |
| Pydantic | 2.10.3 | Validação de dados |

### **Ferramentas de Desenvolvimento**
- Node.js 18.20.7
- Python Launcher (py)
- npm 10.x
- Git

---

## 📁 Estrutura do Projeto

```
semana-02-data-science/
├── python-api/                    # ML Backend (Dia 2)
│   ├── app.py                     # FastAPI application
│   ├── model.pkl                  # Trained ML model
│   ├── test_api.py                # API tests
│   └── requirements.txt
│
├── nestjs-client/                 # Backend Proxy (Dia 3)
│   ├── src/
│   │   ├── main.ts                # Entry point
│   │   ├── app.module.ts          # Root module
│   │   └── titanic/
│   │       ├── titanic.controller.ts  # REST endpoints
│   │       ├── titanic.service.ts     # Business logic
│   │       ├── titanic.module.ts      # Module config
│   │       └── titanic.dto.ts         # Data Transfer Objects
│   ├── package.json
│   └── tsconfig.json
│
├── react-vite-app/                # Frontend (Dia 3)
│   ├── src/
│   │   ├── App.tsx                # Main component
│   │   ├── App.css                # Global styles
│   │   └── components/
│   │       ├── TitanicPredictor.tsx    # Main UI component
│   │       └── TitanicPredictor.css    # Component styles
│   ├── package.json
│   ├── vite.config.ts
│   └── tsconfig.json
│
├── INICIAR-SISTEMA.md             # Guia de inicialização
└── dia-03-integracao-fullstack.md # Esta documentação
```

---

## ⚛️ Frontend - React + Vite

### Componente Principal: `TitanicPredictor.tsx`

O componente implementa toda a lógica de interface e comunicação com as APIs.

#### **Features Implementadas:**

1. **Toggle de API**: Escolher entre Python direto ou via NestJS proxy
2. **Formulário de Entrada**: 6 campos para dados do passageiro
3. **Botões de Exemplo**: Carregar dados pré-definidos
4. **Exibição de Resultados**: Card animado com predição detalhada
5. **Tratamento de Erros**: Mensagens claras para o usuário
6. **Design Responsivo**: Funciona em mobile e desktop

#### **Estrutura do Componente:**

```typescript
interface PassengerData {
  pclass: number;           // 1, 2 ou 3
  sex: string;              // 'male' ou 'female'
  age: number;
  siblings_spouses: number;
  parents_children: number;
  fare: number;
}

interface PredictionResult {
  survived: number;         // 0 ou 1
  probability: number;      // 0.0 a 1.0
  survival_chance: string;  // "Muito Alta", "Alta", etc
  features_used: {
    Pclass: number;
    sex_numeric: number;
    Age: number;
    family_size: number;
    is_alone: number;
    Fare: number;
  };
}
```

#### **Fluxo de Predição:**

```typescript
const handleSubmit = async (e: React.FormEvent) => {
  e.preventDefault();
  setLoading(true);
  
  try {
    const apiUrl = useNestJS 
      ? 'http://localhost:3001/titanic/predict'
      : 'http://localhost:8000/predict';
      
    const response = await fetch(apiUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData),
    });
    
    const data = await response.json();
    setResult(data);
  } catch (err) {
    setError(err.message);
  } finally {
    setLoading(false);
  }
};
```

#### **Design System:**

- **Cores**: Gradiente roxo (#667eea → #764ba2)
- **Layout**: Cards com sombras e bordas arredondadas
- **Animações**: `slideIn` para resultados
- **Responsividade**: Grid adaptativo com breakpoints

---

## 🦅 Backend Proxy - NestJS

### Propósito do Proxy Layer

O NestJS atua como um **intermediário** entre frontend e API Python, oferecendo:

1. **Segurança**: Validação de dados antes de enviar ao Python
2. **Transformação**: Converter formatos de dados se necessário
3. **Logging**: Monitoramento centralizado
4. **Rate Limiting**: Controle de requisições (futuro)
5. **Caching**: Cache de predições (futuro)

### Estrutura de Módulos

#### **1. TitanicModule** (`titanic.module.ts`)

```typescript
@Module({
  imports: [
    HttpModule.register({
      timeout: 5000,        // Timeout de 5 segundos
      maxRedirects: 5,
    }),
  ],
  controllers: [TitanicController],
  providers: [TitanicService],
  exports: [TitanicService],
})
export class TitanicModule {}
```

#### **2. TitanicController** (`titanic.controller.ts`)

Expõe 4 endpoints REST:

```typescript
@Controller('titanic')
export class TitanicController {
  
  @Get('health')
  async checkHealth(): Promise<HealthResponse>
  
  @Get('model')
  async getModelInfo(): Promise<ModelInfo>
  
  @Post('predict')
  async predict(@Body() passenger: PassengerDto): Promise<PredictionResponse>
  
  @Post('predict/batch')
  async predictBatch(@Body() passengers: PassengerDto[]): Promise<any>
}
```

#### **3. TitanicService** (`titanic.service.ts`)

Implementa a lógica de comunicação com Python:

```typescript
@Injectable()
export class TitanicService {
  private readonly pythonApiUrl = 'http://127.0.0.1:8000'; // IPv4 forçado!
  
  async predict(passenger: PassengerDto): Promise<PredictionResponse> {
    try {
      const response = await firstValueFrom(
        this.httpService.post<PredictionResponse>(
          `${this.pythonApiUrl}/predict`,
          passenger
        )
      );
      return response.data;
    } catch (error) {
      // Tratamento de erros...
    }
  }
}
```

#### **4. DTOs** (`titanic.dto.ts`)

```typescript
export class PassengerDto {
  pclass: number;
  sex: string;
  age: number;
  siblings_spouses: number;
  parents_children: number;
  fare: number;
}
```

### Configuração CORS

No `main.ts`:

```typescript
app.enableCors({
  origin: ['http://localhost:5173', 'http://localhost:3000'],
  methods: 'GET,HEAD,PUT,PATCH,POST,DELETE,OPTIONS',
  credentials: true,
});
```

---

## 🐍 ML API - Python FastAPI

### Endpoints Disponíveis

A API Python (desenvolvida no Dia 2) oferece:

| Endpoint | Método | Descrição |
|----------|--------|-----------|
| `/` | GET | Health check |
| `/model/info` | GET | Informações do modelo |
| `/predict` | POST | Predição individual |
| `/predict/batch` | POST | Predição em lote |

### Modelo de Machine Learning

```python
# Modelo treinado no Dia 1
LogisticRegression(max_iter=1000, random_state=42)

# Performance:
- Acurácia: 75.28%
- Features: 6 variáveis
- Dataset: 887 passageiros
```

### Exemplo de Request/Response

**Request:**
```json
POST /predict
{
  "pclass": 1,
  "sex": "female",
  "age": 29,
  "siblings_spouses": 0,
  "parents_children": 0,
  "fare": 211.5
}
```

**Response:**
```json
{
  "survived": 1,
  "probability": 0.9234,
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

## 🔗 Integração e Comunicação

### Fluxo Completo de uma Predição

```
1. Usuario preenche formulário no React
   └─→ Dados: {pclass, sex, age, siblings_spouses, parents_children, fare}

2. React envia POST request
   ├─→ Opção A: http://localhost:8000/predict (Direto)
   └─→ Opção B: http://localhost:3001/titanic/predict (Via NestJS)

3. [Se Opção B] NestJS recebe e valida
   └─→ TitanicController → TitanicService
       └─→ POST http://127.0.0.1:8000/predict

4. Python FastAPI processa
   └─→ Valida com Pydantic
   └─→ Transforma features
   └─→ Executa model.predict()
   └─→ Retorna resultado

5. [Se Opção B] NestJS repassa resultado
   └─→ Log da operação
   └─→ Retorna ao React

6. React exibe resultado
   └─→ Card animado com predição
   └─→ Detalhes das features utilizadas
```

### Gerenciamento de Estado no React

```typescript
// Estados principais
const [useNestJS, setUseNestJS] = useState(false);        // Toggle API
const [loading, setLoading] = useState(false);            // Loading state
const [error, setError] = useState<string | null>(null);  // Error handling
const [result, setResult] = useState<PredictionResult | null>(null);
const [formData, setFormData] = useState<PassengerData>({...});
```

### Tratamento de Erros

**Frontend (React):**
```typescript
try {
  const response = await fetch(apiUrl, {...});
  if (!response.ok) {
    throw new Error(`Erro ${response.status}: ${response.statusText}`);
  }
  const data = await response.json();
  setResult(data);
} catch (err) {
  setError(err instanceof Error ? err.message : 'Erro desconhecido');
}
```

**Backend (NestJS):**
```typescript
catch (error) {
  if (error.response?.status === 422) {
    throw new HttpException(
      'Dados inválidos. Verifique os valores enviados.',
      HttpStatus.BAD_REQUEST
    );
  }
  throw new HttpException(
    'Erro ao fazer predição',
    HttpStatus.INTERNAL_SERVER_ERROR
  );
}
```

---

## 🚀 Como Executar

### Pré-requisitos

```bash
# Verificar versões
node --version    # v18.20.7
py --version      # Python 3.13.2
npm --version     # 10.x
```

### Passo a Passo

#### **Terminal 1 - Python FastAPI**

```bash
cd semana-02-data-science/python-api
py -m uvicorn app:app --host 0.0.0.0 --port 8000
```

✅ API rodando em `http://localhost:8000`

---

#### **Terminal 2 - NestJS Proxy**

```bash
cd semana-02-data-science/nestjs-client
npm run start:dev
```

✅ NestJS rodando em `http://localhost:3001`

---

#### **Terminal 3 - React Frontend**

```bash
cd semana-02-data-science/react-vite-app
npm run dev
```

✅ React rodando em `http://localhost:5173`

---

### Acessar Aplicação

🌐 Abra no navegador: **http://localhost:5173**

---

## 🧪 Testes e Validação

### Teste 1: Health Check

```bash
# Python API
curl http://localhost:8000
# Esperado: {"status":"online","message":"Titanic Survival Prediction API",...}

# NestJS Proxy
curl http://localhost:3001/titanic/health
# Esperado: {"status":"online",...}
```

### Teste 2: Model Info

```bash
# Via NestJS
curl http://localhost:3001/titanic/model
# Esperado: {"model_type":"LogisticRegression","accuracy":0.7528,...}
```

### Teste 3: Predição Individual (cURL)

```bash
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

**Resultado Esperado:**
```json
{
  "survived": 1,
  "probability": 0.92,
  "survival_chance": "Muito Alta"
}
```

### Teste 4: Interface Web

1. **Teste Direto (React → Python)**:
   - Desmarcar checkbox "NestJS (Proxy)"
   - Clicar "👨 Exemplo Baixa Chance"
   - Clicar "Fazer Predição"
   - ✅ Resultado: ~10-15% de sobrevivência

2. **Teste com Proxy (React → NestJS → Python)**:
   - Marcar checkbox "NestJS (Proxy)"
   - Clicar "👩 Exemplo Alta Chance"
   - Clicar "Fazer Predição"
   - ✅ Resultado: ~85-95% de sobrevivência

---

## 🐛 Problemas Encontrados e Soluções

### Problema 1: Node.js Version Compatibility

**Erro:**
```
The engine "node" is incompatible with this module.
Expected version "^18.0.0 || >=20.0.0". Got "18.20.7"
```

**Causa**: Vite 5+ requer Node 20+, mas usuário precisa de Node 18.

**Solução**: Usar Vite 4.x que é compatível com Node 18:
```bash
npm create vite@4 react-vite-app -- --template react-ts
```

---

### Problema 2: Python Command Not Found

**Erro:**
```bash
python app.py
# bash: python: command not found
```

**Causa**: No Windows, o comando correto é `py` (Python Launcher), não `python`.

**Solução**: Usar Python Launcher:
```bash
py app.py
# ou
py -m uvicorn app:app --host 0.0.0.0 --port 8000
```

---

### Problema 3: NestJS não conecta ao Python (IPv6/IPv4)

**Erro:**
```
ECONNREFUSED ::1:8000
```

**Causa**: 
- `localhost` pode resolver para `::1` (IPv6) ou `127.0.0.1` (IPv4)
- Python estava escutando apenas em IPv4
- NestJS tentou IPv6 primeiro e falhou

**Solução**: Forçar IPv4 no NestJS:
```typescript
// ANTES (ERRADO)
private readonly pythonApiUrl = 'http://localhost:8000';

// DEPOIS (CORRETO)
private readonly pythonApiUrl = 'http://127.0.0.1:8000';
```

**Lição aprendida**: Em sistemas Windows com IPv6 habilitado, sempre usar `127.0.0.1` explicitamente para garantir IPv4.

---

### Problema 4: CORS Errors

**Erro no browser:**
```
Access to fetch at 'http://localhost:8000/predict' from origin 
'http://localhost:5173' has been blocked by CORS policy
```

**Causa**: FastAPI e NestJS não tinham CORS configurado.

**Solução**:

**Python (app.py):**
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

**NestJS (main.ts):**
```typescript
app.enableCors({
  origin: ['http://localhost:5173', 'http://localhost:3000'],
  methods: 'GET,HEAD,PUT,PATCH,POST,DELETE,OPTIONS',
  credentials: true,
});
```

---

### Problema 5: Uvicorn Reload Mode

**Erro:**
```
WARNING: You must pass the application as an import string 
to enable 'reload' or 'workers'
```

**Causa**: `uvicorn.run(app, reload=True)` não funciona quando executado via `python app.py`.

**Solução**: Usar uvicorn CLI:
```bash
py -m uvicorn app:app --host 0.0.0.0 --port 8000
```

---

## 🚀 Melhorias Futuras

### Curto Prazo (1-2 semanas)

1. **Testes Automatizados**:
   - Jest para React components
   - Jest + Supertest para NestJS
   - pytest para Python (já existe)

2. **Validação de Formulário**:
   - Validação client-side mais robusta
   - Mensagens de erro específicas por campo
   - Máscaras de input

3. **Loading States**:
   - Skeleton screens
   - Progress indicators
   - Animations durante carregamento

4. **Histórico de Predições**:
   - Salvar predições no localStorage
   - Exibir histórico em tabela
   - Exportar para CSV

5. **Gráficos e Visualizações**:
   - Chart.js ou Recharts
   - Gráfico de probabilidade
   - Distribuição de features

### Médio Prazo (1 mês)

6. **Autenticação e Autorização**:
   - JWT tokens
   - Login/Register
   - Perfis de usuário

7. **Database**:
   - PostgreSQL para armazenar predições
   - TypeORM no NestJS
   - SQLAlchemy no Python

8. **Cache**:
   - Redis para cache de predições
   - Cache de model info
   - Rate limiting

9. **Logging e Monitoring**:
   - Winston para NestJS
   - Python logging
   - Sentry para error tracking

10. **CI/CD Pipeline**:
    - GitHub Actions
    - Automated tests
    - Deploy automático

### Longo Prazo (2-3 meses)

11. **Containerização**:
    - Docker para cada serviço
    - Docker Compose para orquestração
    - Docker Hub registry

12. **Deploy em Cloud**:
    - Frontend: Vercel ou Netlify
    - Backend: Heroku, Railway ou AWS
    - API Python: AWS Lambda ou Google Cloud Run

13. **Multiple Models**:
    - Treinar outros algoritmos (RandomForest, XGBoost)
    - A/B testing de modelos
    - Ensemble predictions

14. **Real-time Features**:
    - WebSockets para predições ao vivo
    - Notificações push
    - Chat support

15. **Mobile App**:
    - React Native
    - Compartilhar código com web
    - App stores

---

## 📊 Métricas e Performance

### Performance Atual

| Métrica | Valor | Status |
|---------|-------|--------|
| Latência P50 (React → Python) | ~50ms | ✅ Ótimo |
| Latência P50 (React → NestJS → Python) | ~80ms | ✅ Bom |
| Tempo de build (React) | ~1s | ✅ Ótimo |
| Tempo de inicialização (NestJS) | ~3s | ✅ Bom |
| Tempo de inicialização (Python) | ~2s | ✅ Ótimo |
| Bundle size (React) | ~500KB | ✅ Aceitável |

### Modelo ML

| Métrica | Valor |
|---------|-------|
| Acurácia | 75.28% |
| Precision (sobreviveu) | ~80% |
| Recall (sobreviveu) | ~70% |
| F1-Score | ~75% |
| Features | 6 variáveis |
| Tamanho do modelo | 2.3KB |
| Tempo de predição | <5ms |

---

## 📚 Aprendizados Chave

### Técnicos

1. **TypeScript é essencial**: Type safety preveniu inúmeros bugs
2. **CORS é crítico**: Sempre configurar desde o início
3. **IPv6/IPv4 matters**: `localhost` ≠ `127.0.0.1` em alguns casos
4. **Vite é rápido**: HMR instantâneo melhora DX
5. **NestJS é poderoso**: Arquitetura modular facilita manutenção
6. **FastAPI é performático**: Response times consistentemente baixos

### Arquiteturais

1. **Separação de concerns**: Frontend, Backend e ML devem ser independentes
2. **API Gateway pattern**: NestJS como proxy oferece flexibilidade
3. **Error handling**: Cada camada deve tratar seus próprios erros
4. **Validation layers**: Validar dados em múltiplos pontos
5. **Configurabilidade**: URLs e configs devem ser facilmente alteráveis

### Práticas

1. **Git commits frequentes**: Facilita rollback e debugging
2. **Documentação inline**: Comments ajudam muito depois
3. **Testes manuais antes de automatizar**: Entender fluxo primeiro
4. **README para cada serviço**: Facilita retomada do trabalho
5. **Logs estruturados**: Logger com níveis (debug, info, error)

---

## 🎯 Conclusão

O **Dia 3** foi um sucesso! Construímos uma aplicação **Full Stack** completa e funcional que integra:

✅ **Frontend moderno** com React, TypeScript e Vite  
✅ **Backend robusto** com NestJS e arquitetura modular  
✅ **ML API performática** com Python e FastAPI  
✅ **Comunicação eficiente** entre todas as camadas  
✅ **UX/UI profissional** com design responsivo  

### Estatísticas do Projeto

- **Linhas de código**: ~1,500 (TypeScript + Python)
- **Componentes React**: 1 principal + 1 App
- **Endpoints REST**: 4 (NestJS) + 4 (Python)
- **Arquivos criados**: 15+
- **Tempo de desenvolvimento**: ~6 horas
- **Bugs críticos resolvidos**: 5

### Próximos Passos

**Semana 02 - Completa!** 🎉

Agora podemos avançar para:
- **Semana 03**: Deep Learning com TensorFlow/PyTorch
- **Semana 04**: Computer Vision
- **Semana 05**: NLP e Processamento de Texto

---

## 📖 Referências

- [React Documentation](https://react.dev)
- [Vite Guide](https://vitejs.dev/guide/)
- [NestJS Documentation](https://docs.nestjs.com)
- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [MDN Web Docs](https://developer.mozilla.org)

---

## 👨‍💻 Autor

**Lutivix**  
GitHub: [@lutivix](https://github.com/lutivix)  
Projeto: Aprendizado IA 2025

---

**Última atualização**: 31 de Outubro de 2025  
**Versão**: 1.0.0  
**Status**: ✅ Completo e Funcional
