# 📅 Semana 2: Python Data Science + API REST

**Período:** 28 Out - 1 Nov 2025  
**Status:** 🟡 **EM PROGRESSO** (67% - 2/3 dias)  
**Tempo total:** ~8 horas

---

## 🎯 **Objetivos da Semana**

### Dia 1: Python Data Science Avançado ✅ CONCLUÍDO
- [x] Análise exploratória de dados (EDA) completa
- [x] Limpeza e preparação de dados
- [x] Modelo ML mais complexo (Logistic Regression/Decision Tree)
- [x] Métricas avançadas (accuracy, precision, recall, F1)
- [x] **Resultado:** 79% accuracy (acima da média Kaggle!)

### Dia 2: API REST Python (FastAPI) ✅ CONCLUÍDO
- [x] Criar API Python com FastAPI
- [x] 4 Endpoints GET/POST funcionando
- [x] Integrar modelo ML na API (75% accuracy)
- [x] Validação com Pydantic
- [x] Documentação automática (Swagger/ReDoc)
- [x] CORS configurado
- [x] 6 Testes automatizados (100% sucesso)
- [x] **Resultado:** ~707 linhas de código Python, API funcional!

## 📅 Cronograma

### ✅ Dia 1: Análise Exploratória de Dados (EDA)
- **Status**: Completo
- **Data**: 29/10/2025
- **Progresso**: 100%

### ✅ Dia 2: Machine Learning REST API
- **Status**: Completo
- **Data**: 30/10/2025
- **Progresso**: 100%

### ✅ Dia 3: Integração Full Stack
- **Status**: Completo
- **Data**: 31/10/2025
- **Progresso**: 100%

---

## 📁 **Estrutura da Semana**

```
semana-02-data-science/
├── notebooks/
│   ├── 01-eda-analise-exploratoria.ipynb
│   ├── 02-modelo-ml-avancado.ipynb
│   └── 03-preparacao-api.ipynb
├── python-api/
│   ├── app.py                  # Flask/FastAPI
│   ├── model.pkl              # Modelo treinado
│   └── requirements.txt
└── integracao/
    ├── nestjs-client/         # Consumer da API Python
    └── react-vite-app/        # Frontend (bônus)
```

---

## 📊 **Progresso**

```
██████████ 100% Dia 1 - CONCLUÍDO ✅
░░░░░░░░░░   0% Dia 2 - Pendente
░░░░░░░░░░   0% Dia 3 - Pendente
```

**Dia 1:** 28/10 - ✅ **CONCLUÍDO COM SUCESSO!**
- Tempo: ~3-4 horas
- Dataset: 887 linhas (Titanic)
- Modelo: 79% accuracy (Logistic Regression + Decision Tree)
- Conquistas: 5 visualizações + 2 modelos + Feature Engineering

---

## 📚 **Recursos e Datasets Sugeridos**

### Datasets para EDA:
- **Titanic** - Classificação (sobreviventes)
- **Iris** - Classificação (espécies de flores)
- **House Prices** - Regressão (preços de imóveis)
- **Wine Quality** - Classificação (qualidade de vinhos)

### Bibliotecas a explorar:
- **Pandas** - Manipulação de dados
- **Seaborn** - Visualizações estatísticas
- **Scikit-learn** - Modelos ML avançados
- **Flask/FastAPI** - APIs REST em Python

---

## 🎯 **Entregáveis**

- [x] Notebook EDA completo com insights ✅
- [x] Modelo ML com métricas documentadas ✅
- [x] API Python funcionando (Dia 2) ✅
- [x] 6 testes automatizados (100% sucesso) ✅
- [x] Sistema integrado Full Stack (React + NestJS + Python) ✅
- [x] Interface web moderna e responsiva ✅
- [x] Documentação completa de 3 dias ✅

**Status Final**: 🎉 **Semana 02 - 100% COMPLETA!**

---

## 📝 **Detalhamento dos Dias**

### ✅ Dia 1: Análise Exploratória de Dados (29/10/2025)

**Objetivo**: Análise completa do dataset Titanic com EDA e treinamento de modelos ML.

**Tarefas Realizadas**:
- ✅ Carregamento e exploração inicial do dataset (887 registros)
- ✅ Limpeza de dados (tratamento de valores nulos)
- ✅ Feature Engineering (family_size, is_alone, age_group)
- ✅ 5 Visualizações com Seaborn (distribuições, correlações)
- ✅ Treinamento de 2 modelos (Logistic Regression + Decision Tree)
- ✅ Métricas: 79% accuracy, precision, recall, F1-score
- ✅ Documentação completa (~5000 palavras)

**Arquivos**:
- `notebooks/01-eda-analise-exploratoria.ipynb`
- `docs/06-dia1-analise-exploratoria.md`

**Principais Conquistas**:
- Dataset limpo e preparado
- Features engineered que melhoraram o modelo
- Accuracy de 79% (acima da média Kaggle)
- Insights sobre fatores de sobrevivência

---

### ✅ Dia 2: Machine Learning REST API (30/10/2025)

**Objetivo**: ✅ Criar API REST com FastAPI para servir o modelo ML.

**Tecnologias**:
- ✅ Python 3.13
- ✅ FastAPI 0.115.5
- ✅ Uvicorn (ASGI server)
- ✅ Pydantic (validação)
- ✅ pytest (testes)

**Tarefas Realizadas**:
- ✅ Setup do projeto Python com FastAPI
- ✅ Serialização do modelo (model.pkl) com pickle
- ✅ Implementação de 4 endpoints REST:
  - `GET /` - Health check
  - `GET /model/info` - Informações do modelo
  - `POST /predict` - Predição individual
  - `POST /predict/batch` - Predição em lote
- ✅ Validação de dados com Pydantic
- ✅ Documentação automática (Swagger UI + ReDoc)
- ✅ CORS configurado para frontend
- ✅ 6 testes automatizados com pytest (100% sucesso)
- ✅ Documentação completa (~5000 palavras)

**Arquivos**:
```
python-api/
├── app.py                 # 247 linhas
├── model.pkl             # Modelo serializado
├── test_api.py           # 6 testes
└── requirements.txt
```

**Endpoints Criados**:
| Endpoint | Método | Descrição |
|----------|--------|-----------|
| `/` | GET | Health check da API |
| `/model/info` | GET | Informações do modelo ML |
| `/predict` | POST | Predição individual |
| `/predict/batch` | POST | Predição em lote |

**Resultados**:
- ✅ API funcional em `http://localhost:8000`
- ✅ Documentação em `http://localhost:8000/docs`
- ✅ 75.28% accuracy nas predições
- ✅ Tempo de resposta: ~50ms
- ✅ 6/6 testes passando

**Documentação**: [08-dia2-api-rest-ml.md](../docs/08-dia2-api-rest-ml.md)

---

### ✅ Dia 3: Integração Full Stack (31/10/2025)

**Objetivo**: ✅ Criar aplicação web completa com React + NestJS + Python.

**Tecnologias**:
- ✅ Frontend: React 18 + TypeScript + Vite 4
- ✅ Backend: NestJS 10 (Proxy Layer)
- ✅ ML API: FastAPI (do Dia 2)

**Tarefas Realizadas**:
- ✅ Setup do projeto React com Vite 4 (Node 18 compatible)
- ✅ Criar componentes de interface (TitanicPredictor)
- ✅ Implementar formulário de predição com validação
- ✅ Setup do projeto NestJS com TypeScript
- ✅ Criar endpoints proxy (4 endpoints)
- ✅ Integrar com API Python (HTTP + CORS)
- ✅ Testes de integração E2E (manual)
- ✅ Documentação completa (5000+ palavras)

**Estrutura**:
```
semana-02-data-science/
├── react-vite-app/           # Frontend (5173)
│   └── src/components/
│       └── TitanicPredictor.tsx
├── nestjs-client/            # Backend Proxy (3001)
│   └── src/titanic/
│       ├── titanic.controller.ts
│       ├── titanic.service.ts
│       ├── titanic.module.ts
│       └── titanic.dto.ts
└── python-api/               # ML API (8000)
    └── app.py
```

**Arquitetura**:
```
┌─────────────┐      ┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│   React     │─────▶│   NestJS    │─────▶│   FastAPI   │─────▶│  ML Model   │
│   (5173)    │ HTTP │   (3001)    │ HTTP │   (8000)    │      │ (model.pkl) │
└─────────────┘      └─────────────┘      └─────────────┘      └─────────────┘
```

**Principais Conquistas**:
- ✅ Interface web moderna e responsiva
- ✅ Toggle para escolher API (direto ou proxy)
- ✅ Comunicação full stack funcionando
- ✅ Tratamento de erros em todas camadas
- ✅ Resolvido problema IPv6/IPv4 (`localhost` vs `127.0.0.1`)
- ✅ CORS configurado corretamente

**Features Implementadas**:
- Formulário com 6 campos (classe, gênero, idade, etc)
- Botões de exemplo (alta/baixa chance)
- Predição em tempo real
- Exibição detalhada dos resultados
- Loading states e error handling
- Design responsivo com gradiente

**Problemas Resolvidos**:
1. ✅ Node 18 compatibility → Vite 4 (não 5)
2. ✅ Comando Python no Windows → `py` ao invés de `python`
3. ✅ IPv6/IPv4 → `127.0.0.1` ao invés de `localhost`
4. ✅ CORS em 2 backends (NestJS + FastAPI)

**Documentação**: [09-dia3-integracao-fullstack.md](../docs/09-dia3-integracao-fullstack.md)

**Guia de Inicialização**: [INICIAR-SISTEMA.md](INICIAR-SISTEMA.md)

---

**🚀 Próxima semana: Deep Learning com TensorFlow/PyTorch!**
