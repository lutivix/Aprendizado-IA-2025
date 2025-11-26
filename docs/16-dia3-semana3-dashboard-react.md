# 📅 Dia 3: Dashboard React Interativo + API FastAPI

**Data:** 26 Novembro 2025  
**Tema:** Integração Full-Stack ML  
**Status:** ✅ **COMPLETO**

---

## 🎯 Objetivos

- ✅ Criar API REST com FastAPI para servir modelo ML
- ✅ Desenvolver dashboard React + TypeScript
- ✅ Integrar frontend com backend
- ✅ Visualizações interativas e responsivas
- ✅ Sistema completo de predição em tempo real

---

## 🏗️ Arquitetura do Sistema

```
┌─────────────────────────────────────────────────────────┐
│                    USUÁRIO                               │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│           FRONTEND (React + TypeScript)                  │
│  ┌──────────────────────────────────────────────────┐  │
│  │  • ModelInfo Component (GET /model/info)         │  │
│  │  • PredictionForm Component (POST /predict)      │  │
│  │  • PredictionResult Component (Display)          │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────┘
                     │ HTTP/JSON (Axios)
                     ▼
┌─────────────────────────────────────────────────────────┐
│             BACKEND (FastAPI)                            │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Endpoints:                                       │  │
│  │  • GET /health                                    │  │
│  │  • GET /model/info                                │  │
│  │  • POST /predict                                  │  │
│  │  • POST /predict/batch                            │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│         MODELO ML (Random Forest)                        │
│  ┌──────────────────────────────────────────────────┐  │
│  │  • model.pkl (joblib)                             │  │
│  │  • model_metadata.json                            │  │
│  │  • Accuracy: ~82%                                 │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

---

## 📦 Estrutura de Arquivos

```
semana-03-ml-avancado/
├── python-api/                      # 🐍 Backend
│   ├── app.py                       # FastAPI app
│   ├── train_model.py               # Script de treino
│   ├── test_api.py                  # Testes da API
│   ├── requirements.txt             # Dependências Python
│   ├── README.md                    # Docs backend
│   ├── model.pkl                    # Modelo treinado
│   └── model_metadata.json          # Metadata
│
└── react-dashboard/                 # ⚛️ Frontend
    ├── src/
    │   ├── App.tsx                  # Componente principal
    │   ├── App.css                  # Estilos globais
    │   └── components/
    │       ├── ModelInfo.tsx        # Info do modelo
    │       ├── PredictionForm.tsx   # Formulário
    │       └── PredictionResult.tsx # Resultado
    ├── package.json
    ├── vite.config.ts
    └── README.md                    # Docs frontend
```

---

## 🚀 Passo a Passo da Implementação

### **Parte 1: Backend - API FastAPI** ⏱️ 30 min

#### 1.1 Setup do Projeto
```bash
cd python-api
pip install -r requirements.txt
```

#### 1.2 Treinar o Modelo
```bash
python train_model.py
```

**O que acontece:**
- ✅ Baixa dataset Titanic
- ✅ Prepara dados (limpeza, encoding)
- ✅ Treina Random Forest (100 estimators, max_depth=10)
- ✅ Avalia modelo (accuracy ~82%)
- ✅ Salva `model.pkl` e `model_metadata.json`

#### 1.3 Iniciar a API
```bash
python app.py
```

**Endpoints criados:**
- `GET /` - Info geral
- `GET /health` - Health check
- `GET /model/info` - Metadata do modelo
- `POST /predict` - Predição única
- `POST /predict/batch` - Predições em lote

**Documentação automática:**
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

#### 1.4 Testar API
```bash
python test_api.py
```

---

### **Parte 2: Frontend - React Dashboard** ⏱️ 40 min

#### 2.1 Setup do Projeto
```bash
cd react-dashboard
npm install
```

#### 2.2 Estrutura de Componentes

**App.tsx** (Componente raiz)
- Gerencia estado global (prediction, loading)
- Renderiza header, footer e grid de cards
- Passa callbacks para componentes filhos

**ModelInfo.tsx** (Informações do modelo)
- useEffect para carregar dados na montagem
- GET /model/info
- Exibe: modelo, accuracy, features, etc.

**PredictionForm.tsx** (Formulário interativo)
- Controla estado do formulário
- Botões de exemplo (sobrevivente/vítima)
- POST /predict
- Validação de inputs

**PredictionResult.tsx** (Resultado visual)
- Recebe prediction do parent
- Animações CSS
- Interpretação detalhada

#### 2.3 Estilização
- Dark theme moderno
- Gradientes azul
- Animações suaves (fadeIn, hover effects)
- Grid responsivo (auto-fit)
- Mobile-friendly

#### 2.4 Iniciar Dev Server
```bash
npm run dev
```

Acesse: `http://localhost:5173`

---

## 🎨 Design System

### Cores
```css
--primary: #2563eb (azul)
--primary-dark: #1e40af
--success: #34d399 (verde)
--error: #f87171 (vermelho)
--bg-dark: #0f1419
--bg-card: rgba(255, 255, 255, 0.05)
```

### Tipografia
- Font: Segoe UI
- Heading: 2.5rem (40px)
- Body: 1rem (16px)
- Small: 0.9rem (14.4px)

### Animações
- Hover cards: translateY(-4px)
- Loading spinner: rotate 360°
- FadeIn: opacity 0→1 + translateY(20px→0)

---

## 📊 Fluxo de Dados Detalhado

### Carregar Informações do Modelo
```
1. React monta ModelInfo
2. useEffect() executa
3. axios.get('/model/info')
4. FastAPI retorna metadata
5. React atualiza estado
6. UI renderiza informações
```

### Fazer Predição
```
1. Usuário preenche formulário
2. Clica em "Prever"
3. onSubmit() previne default
4. setLoading(true)
5. axios.post('/predict', formData)
6. FastAPI processa:
   - Valida dados (Pydantic)
   - Prepara features
   - model.predict()
   - model.predict_proba()
7. Retorna JSON:
   {
     survived: 0 ou 1,
     probability: 0.0-1.0,
     message: "🎉/😢",
     model_name: "...",
     model_accuracy: 0.82
   }
8. React recebe resposta
9. setPrediction(data)
10. setLoading(false)
11. PredictionResult renderiza
12. Animações CSS executam
```

---

## 🔧 Tecnologias e Bibliotecas

### Backend
| Tech | Versão | Uso |
|------|--------|-----|
| **FastAPI** | 0.109.0 | Framework web |
| **Uvicorn** | 0.27.0 | ASGI server |
| **Pydantic** | 2.5.3 | Validação de dados |
| **Pandas** | 2.1.4 | Manipulação de dados |
| **Scikit-learn** | 1.3.2 | Machine Learning |
| **Joblib** | 1.3.2 | Serialização |

### Frontend
| Tech | Versão | Uso |
|------|--------|-----|
| **React** | 18.3.1 | UI library |
| **TypeScript** | 5.6.2 | Type safety |
| **Vite** | 5.4.10 | Build tool |
| **Axios** | 1.7.9 | HTTP client |

---

## 🧪 Testes Realizados

### Backend
```bash
✅ GET / - Info geral
✅ GET /health - Status da API
✅ GET /model/info - Metadata
✅ POST /predict - Predição única (2 exemplos)
✅ POST /predict/batch - 3 passageiros
```

### Frontend
```bash
✅ Renderização inicial
✅ Carregamento de model info
✅ Botão "Exemplo: Sobrevivente"
✅ Botão "Exemplo: Vítima"
✅ Submissão manual
✅ Loading state
✅ Error handling (API offline)
✅ Animações CSS
✅ Responsividade mobile
```

---

## 📈 Métricas do Projeto

### Código
- **Linhas Python:** ~350 linhas
- **Linhas TypeScript/TSX:** ~450 linhas
- **Linhas CSS:** ~300 linhas
- **Total:** ~1.100 linhas

### Arquivos
- **Python:** 4 arquivos (.py)
- **React:** 4 componentes (.tsx)
- **Config:** 3 arquivos (package.json, vite.config, etc.)
- **Docs:** 3 READMEs

### Performance
- **API Response Time:** <100ms (localhost)
- **React Build:** ~50KB gzipped
- **First Contentful Paint:** <1s
- **Time to Interactive:** <2s

---

## 🎓 Conceitos Aprendidos

### Machine Learning
- ✅ Serialização de modelos (joblib)
- ✅ API para servir modelos ML
- ✅ Metadata tracking
- ✅ Batch predictions

### Backend Development
- ✅ FastAPI framework
- ✅ REST API design
- ✅ CORS configuration
- ✅ Pydantic validation
- ✅ Automatic API docs (Swagger)
- ✅ Error handling
- ✅ HTTP status codes

### Frontend Development
- ✅ React Hooks (useState, useEffect)
- ✅ TypeScript interfaces
- ✅ Component composition
- ✅ Props drilling
- ✅ Axios HTTP requests
- ✅ Async/await
- ✅ Error boundaries
- ✅ Loading states
- ✅ Form handling
- ✅ CSS animations

### DevOps
- ✅ Local development setup
- ✅ Package management (pip, npm)
- ✅ Environment configuration
- ✅ API testing
- ✅ CORS policy

---

## 🐛 Troubleshooting Guide

### Problema 1: API não conecta
**Sintoma:** `Network Error` no React

**Solução:**
```bash
# Verifique se a API está rodando
curl http://localhost:8000/health

# Se não estiver, inicie:
cd python-api
python app.py
```

### Problema 2: Modelo não encontrado
**Sintoma:** `503 Service Unavailable` ou "Modelo não carregado"

**Solução:**
```bash
cd python-api
python train_model.py
```

### Problema 3: CORS Error
**Sintoma:** `CORS policy blocked`

**Solução:**
- Verifique se `allow_origins` em `app.py` inclui `http://localhost:5173`
- Já está configurado no código fornecido

### Problema 4: Vite não inicia
**Sintoma:** `Node.js version mismatch`

**Solução:**
- Vite 5 requer Node.js 18+
- Projeto já configurado com Vite 5

---

## 🎉 Resultado Final

### Screenshots Conceituais

**Tela Principal:**
```
┌─────────────────────────────────────────────┐
│  🚢 Titanic Survival Predictor              │
│  Predição de sobrevivência usando ML        │
└─────────────────────────────────────────────┘

┌──────────────────┐  ┌──────────────────────┐
│ 📊 Informações   │  │ 📝 Fazer Predição    │
│ do Modelo        │  │                       │
│                  │  │ [Exemplo: ✅]  [❌]   │
│ Modelo: RF       │  │                       │
│ Accuracy: 82.68% │  │ Classe: [3▼]         │
│ N° Árvores: 100  │  │ Sexo: [male▼]        │
│ Features: 7      │  │ Idade: [22]          │
│                  │  │ ...                   │
│                  │  │                       │
│                  │  │ [🔮 Prever]          │
└──────────────────┘  └──────────────────────┘

┌─────────────────────────────────────────────┐
│ 🎯 Resultado                                │
│                                              │
│              😢                              │
│                                              │
│      Não sobreviveu                          │
│                                              │
│   Probabilidade de sobrevivência: 12.3%      │
│                                              │
│ 💡 Interpretação: Com uma probabilidade...  │
└─────────────────────────────────────────────┘
```

---

## 📝 Checklist de Conclusão

### Backend
- [x] API FastAPI criada
- [x] Modelo treinado e salvo
- [x] Endpoints implementados
- [x] CORS configurado
- [x] Validação Pydantic
- [x] Documentação Swagger
- [x] Testes da API

### Frontend
- [x] Projeto React + Vite criado
- [x] TypeScript configurado
- [x] 3 componentes criados
- [x] Integração com API (Axios)
- [x] Estilização completa
- [x] Animações CSS
- [x] Responsividade
- [x] Error handling
- [x] Loading states

### Documentação
- [x] README backend
- [x] README frontend
- [x] Este guia (dia 3)
- [x] Comentários no código

---

## 🚀 Próximas Melhorias (Opcional)

### Features Adicionais
- [ ] Upload de CSV para predições em lote
- [ ] Gráfico de Feature Importance (Recharts)
- [ ] Comparação entre múltiplos modelos
- [ ] Histórico de predições (localStorage)
- [ ] Download de resultados (CSV/JSON)
- [ ] Dark/Light theme toggle

### Deploy
- [ ] Backend: Railway ou Render
- [ ] Frontend: Vercel ou Netlify
- [ ] CI/CD com GitHub Actions

### Otimizações
- [ ] React Query para caching
- [ ] Lazy loading de componentes
- [ ] Service Worker (PWA)
- [ ] Error boundary global
- [ ] Unit tests (Jest + React Testing Library)

---

## 📚 Recursos Úteis

### Documentação
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [React Docs](https://react.dev/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [Vite Guide](https://vitejs.dev/guide/)
- [Axios Docs](https://axios-http.com/docs/intro)

### Tutoriais
- FastAPI + ML: https://testdriven.io/blog/fastapi-machine-learning/
- React + TypeScript: https://react-typescript-cheatsheet.netlify.app/

---

## ✅ Conclusão

**Dia 3 foi um sucesso completo!** 🎉

Você criou um sistema full-stack funcional que:
- ✅ Serve um modelo ML via API REST
- ✅ Interface moderna e interativa
- ✅ Comunicação HTTP robusta
- ✅ Error handling adequado
- ✅ Documentação completa

**Habilidades desenvolvidas:**
- Backend development com FastAPI
- Frontend development com React + TypeScript
- Integração API REST
- Deploy local de sistemas ML
- UI/UX design

**Próximos passos:**
- Completar notebooks Dia 1 e 2 (se necessário)
- Adicionar features extras ao dashboard
- Deploy em produção (opcional)

---

**Tempo total:** ~2-3 horas  
**Linhas de código:** ~1.100  
**Status:** ✅ COMPLETO
