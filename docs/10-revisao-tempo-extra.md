# 📚 Guia de Revisão - Tempo Extra

**Para quando sobrar tempo (spoiler: não vai sobrar muito)**

Este guia contém exercícios rápidos e práticos de revisão que você pode fazer quando tiver alguns minutos livres. Organizados por tempo disponível.

---

## ⚡ **5 Minutos Livres**

### Opção 1: Redesenhar Arquitetura
- Pegar papel e caneta
- Desenhar: React → NestJS → Python → Model
- Anotar as portas (5173, 3001, 8000)
- **Ganho**: Fixar na memória

### Opção 2: Reler Problema IPv6/IPv4
- Abrir `docs/09-dia3-integracao-fullstack.md`
- Ir direto na seção "Problema 3: NestJS não conecta ao Python"
- Entender: `localhost` vs `127.0.0.1`
- **Ganho**: Entender networking

### Opção 3: Ver Fluxo de Erro
- Desligar o Python (Ctrl+C)
- Tentar predição no navegador
- Ver erro no console
- Religar Python
- **Ganho**: Debug visual

---

## ⏱️ **15 Minutos Livres**

### Opção 1: Entender React Hooks ⭐ RECOMENDADO
**Arquivo**: `react-vite-app/src/components/TitanicPredictor.tsx`

**O que procurar**:
```typescript
// 1. useState - Gerenciamento de estado
const [useNestJS, setUseNestJS] = useState(false);
const [loading, setLoading] = useState(false);
const [error, setError] = useState<string | null>(null);
const [result, setResult] = useState<PredictionResult | null>(null);
const [formData, setFormData] = useState<PassengerData>({...});

// 2. Async/Await - Requisições HTTP
const handleSubmit = async (e: React.FormEvent) => {
  const response = await fetch(apiUrl, {...});
}

// 3. Conditional Rendering
{error && <div className="error-box">...</div>}
{result && <div className="result-box">...</div>}
```

**Perguntas para si mesmo**:
- Por que `useState` e não variável normal?
- Por que `setLoading(true)` antes do fetch?
- Como `useNestJS` muda a URL da API?

---

### Opção 2: Entender NestJS Decorators
**Arquivo**: `nestjs-client/src/titanic/titanic.controller.ts`

**O que procurar**:
```typescript
@Controller('titanic')  // Rota base: /titanic
export class TitanicController {
  
  @Get('health')       // GET /titanic/health
  async checkHealth()
  
  @Post('predict')     // POST /titanic/predict
  async predict(@Body() passenger: PassengerDto)
}
```

**Perguntas**:
- O que são decorators? (@Get, @Post)
- Por que `@Body()` no parâmetro?
- Como NestJS sabe validar os dados?

---

### Opção 3: Simular Erros Comuns
**Cenários**:

1. **Erro 503** (Python offline):
   - Desligar Python
   - Tentar via NestJS
   - Ver mensagem: "API Python não está disponível"

2. **Erro de Validação** (dados inválidos):
   - Idade negativa: -5
   - Classe inválida: 5
   - Ver como FastAPI rejeita

3. **Erro de CORS** (origem errada):
   - Comentar `app.enableCors()` no NestJS
   - Recompilar
   - Ver erro no browser console

**Ganho**: Aprender a diagnosticar problemas

---

## 🕐 **30 Minutos Livres**

### Combo Full Stack + Debug ⭐⭐⭐ MELHOR OPÇÃO

**Parte 1 (15 min): Entender Arquitetura**

1. **Desenhar no papel**:
   ```
   ┌─────────────┐
   │   React     │ localhost:5173
   │   (Vite)    │
   └──────┬──────┘
          │ HTTP POST /predict
          ↓
   ┌─────────────┐
   │   NestJS    │ localhost:3001
   │   (Proxy)   │
   └──────┬──────┘
          │ HTTP POST /predict
          ↓
   ┌─────────────┐
   │   FastAPI   │ localhost:8000
   │   (Python)  │
   └──────┬──────┘
          │ model.predict()
          ↓
   ┌─────────────┐
   │   ML Model  │ model.pkl
   │ (LogReg)    │ 75% accuracy
   └─────────────┘
   ```

2. **Anotar os problemas resolvidos**:
   - Node 18 → Vite 4 (não 5)
   - `python` → `py` (Windows)
   - `localhost` → `127.0.0.1` (IPv6/IPv4)
   - CORS nos 2 backends

3. **Listar tecnologias por camada**:
   - Frontend: React, TypeScript, Vite, CSS3
   - Proxy: NestJS, Axios, class-validator
   - API: FastAPI, Uvicorn, Pydantic
   - ML: scikit-learn, pandas, pickle

**Parte 2 (15 min): Praticar Debug**

1. **Desligar Python** (5 min):
   - Ctrl+C no terminal do Python
   - Tentar predição via NestJS
   - Observar erro 503 no browser
   - Ver log no NestJS: "ECONNREFUSED"
   - Religar Python

2. **Enviar dados inválidos** (5 min):
   - Idade: -10
   - Ver erro 422 do FastAPI
   - Classe: 5 (não existe)
   - Ver validação do Pydantic

3. **Acompanhar requisição completa** (5 min):
   - Abrir DevTools (F12)
   - Aba Network
   - Fazer predição
   - Ver request/response
   - Verificar tempo de resposta

---

## 📖 **1 Hora Livre** (improvável, mas vai que...)

### Projeto: Adicionar Nova Feature

**Opção A: Campo de "Embarked" (Porto de Embarque)**

1. Adicionar ao formulário React:
```typescript
<select name="embarked">
  <option value="S">Southampton</option>
  <option value="C">Cherbourg</option>
  <option value="Q">Queenstown</option>
</select>
```

2. Atualizar DTO no NestJS
3. Atualizar schema no Python
4. (Não precisa retreinar modelo, só passar adiante)

**Opção B: Histórico de Predições**

1. Salvar predições no `localStorage`:
```typescript
const history = JSON.parse(localStorage.getItem('predictions') || '[]');
history.push({ date: new Date(), ...result });
localStorage.setItem('predictions', JSON.stringify(history));
```

2. Criar componente `HistoryTable`
3. Botão "Limpar Histórico"

**Opção C: Loading Melhorado**

1. Skeleton screen durante loading
2. Progress bar
3. Animação de barco 🚢

---

## 🎯 **Conceitos-Chave para Revisar**

### TypeScript
- Interfaces vs Types
- Generics (ex: `useState<string | null>`)
- Type inference
- Optional chaining (`?.`)

### React
- `useState` - Estado local
- `useEffect` - Efeitos colaterais
- Conditional rendering (`&&`, ternário)
- Event handlers
- Controlled inputs

### NestJS
- Decorators (`@Controller`, `@Get`, `@Post`)
- Dependency Injection
- Modules, Controllers, Services
- DTOs e Validação
- HttpModule do Axios

### FastAPI
- Path operations (`@app.get`, `@app.post`)
- Pydantic models
- Automatic validation
- CORS middleware
- Uvicorn server

### Networking
- HTTP methods (GET, POST)
- Status codes (200, 422, 500, 503)
- CORS (Cross-Origin Resource Sharing)
- localhost vs 127.0.0.1
- IPv6 (`::1`) vs IPv4 (`127.0.0.1`)

### Machine Learning
- Logistic Regression
- Features engineering
- Probability vs Prediction
- Model accuracy (75%)
- Pickle (serialização)

---

## 📝 **Checklist Rápido de Revisão**

Marque conforme revisar:

### Arquitetura
- [ ] Sei desenhar a arquitetura de memória
- [ ] Entendo o papel de cada camada
- [ ] Sei explicar por que usar proxy (NestJS)
- [ ] Entendo o fluxo de dados end-to-end

### Frontend (React)
- [ ] Entendo todos os `useState` no código
- [ ] Sei como funciona o `fetch` async/await
- [ ] Entendo conditional rendering
- [ ] Sei como CSS é aplicado

### Backend (NestJS)
- [ ] Entendo decorators (`@Controller`, etc)
- [ ] Sei como funciona Dependency Injection
- [ ] Entendo o HttpModule/Axios
- [ ] Sei o que são DTOs

### API (Python)
- [ ] Entendo os 4 endpoints
- [ ] Sei como Pydantic valida dados
- [ ] Entendo transformação de features
- [ ] Sei como modelo faz predição

### Problemas
- [ ] Entendo problema IPv6/IPv4
- [ ] Sei por que usar `py` no Windows
- [ ] Entendo CORS e por que precisa
- [ ] Sei debugar erros comuns

---

## 🚀 **Quando Revisar**

### Cenários Ideais:
- ✅ Esperando build/deploy
- ✅ Pausa para café (5 min)
- ✅ Antes de dormir (mental review)
- ✅ Fim de semana (30 min)
- ✅ Commute (mental review no transporte)

### Não Force:
- ❌ Está cansado demais
- ❌ Tem prazo urgente de outra coisa
- ❌ Está com problema mais prioritário
- ❌ Mente não está absorvendo

**Lembre**: Qualidade > Quantidade. 5 minutos focados > 30 minutos distraído.

---

## 💡 **Dicas de Revisão Eficaz**

1. **Spaced Repetition**: Revise hoje, amanhã, semana que vem
2. **Active Recall**: Tente lembrar sem olhar docs
3. **Feynman Technique**: Explique como se ensinasse alguém
4. **Prática > Teoria**: Rode o código, quebre coisas, conserte
5. **Notas Manuais**: Escrever à mão fixa melhor que digitar

---

## 📊 **Prioridade de Revisão**

Se só tiver tempo para 1 coisa, faça nessa ordem:

1. 🥇 **Arquitetura Full Stack** - Base de tudo
2. 🥈 **React Hooks** - Muito usado no mercado
3. 🥉 **Problema IPv6/IPv4** - Diferencial técnico
4. **NestJS Decorators** - Padrão enterprise
5. **ML Concepts** - Fundamento

---

## 🎓 **Para Entrevistas**

Se te perguntarem sobre este projeto:

**Pergunta**: "Me fale sobre um projeto Full Stack que você fez"

**Resposta estruturada**:
1. **Contexto**: "Construí uma aplicação de predição com ML"
2. **Arquitetura**: "React + NestJS + Python, 3 camadas"
3. **Tecnologias**: "TypeScript em 2 layers, FastAPI no backend"
4. **Desafio**: "Enfrentei problema IPv6/IPv4, resolvi usando 127.0.0.1"
5. **Resultado**: "75% accuracy, interface responsiva, funcional"

---

**Última atualização**: 31/10/2025  
**Versão**: 1.0  
**Quando usar**: Sempre que sobrar tempinho! 😄
