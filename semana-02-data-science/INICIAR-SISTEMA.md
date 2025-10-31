# 🚀 Guia de Inicialização - Full Stack Titanic

Este guia mostra como iniciar todo o sistema integrado: **React → NestJS → Python → ML Model**

## 📋 Pré-requisitos

- ✅ Python 3.13 com FastAPI e scikit-learn
- ✅ Node.js 18.20.7
- ✅ npm instalado

## 🏗️ Arquitetura

```
┌─────────────┐      ┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│   React     │──────▶│   NestJS    │──────▶│   FastAPI   │──────▶│  ML Model   │
│   (5173)    │ HTTP  │   (3001)    │ HTTP  │   (8000)    │      │ (model.pkl) │
└─────────────┘      └─────────────┘      └─────────────┘      └─────────────┘
  Frontend UI        Backend Proxy       REST API          Logistic Regression
```

## 🎯 Iniciar Sistema Completo

### **Terminal 1 - Python FastAPI** (Backend ML)

```bash
cd semana-02-data-science/python-api
py app.py
```

✅ **Verificação**: API rodando em `http://localhost:8000`

```bash
curl http://localhost:8000
# Deve retornar: {"status":"online","message":"Titanic Survival Prediction API",...}
```

---

### **Terminal 2 - NestJS Client** (Proxy Backend)

```bash
cd semana-02-data-science/nestjs-client
npm run start:dev
```

✅ **Verificação**: NestJS rodando em `http://localhost:3001`

```bash
curl http://localhost:3001/titanic/health
# Deve retornar status da API Python
```

---

### **Terminal 3 - React Frontend** (Interface Web)

```bash
cd semana-02-data-science/react-vite-app
npm run dev
```

✅ **Verificação**: React rodando em `http://localhost:5173`

Abra no navegador: `http://localhost:5173`

---

## 🧪 Testar Integração

### 1️⃣ Teste Direto (React → Python)

No navegador `http://localhost:5173`:
- **Desmarque** o checkbox "NestJS (Proxy)"
- Preencha os dados do passageiro
- Clique em "Fazer Predição"

**Fluxo**: `React (5173) → Python (8000)`

---

### 2️⃣ Teste com Proxy (React → NestJS → Python)

No navegador `http://localhost:5173`:
- **Marque** o checkbox "NestJS (Proxy)"
- Preencha os dados do passageiro
- Clique em "Fazer Predição"

**Fluxo**: `React (5173) → NestJS (3001) → Python (8000)`

---

### 3️⃣ Teste via cURL (NestJS → Python)

```bash
# Health check
curl http://localhost:3001/titanic/health

# Model info
curl http://localhost:3001/titanic/model

# Predição individual
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

---

## 📊 Exemplos de Teste

### ✅ **Alta Chance de Sobrevivência** (1ª Classe, Mulher)
```json
{
  "pclass": 1,
  "sex": "female",
  "age": 29,
  "siblings_spouses": 0,
  "parents_children": 0,
  "fare": 211.5
}
```
**Resultado esperado**: ~90% de sobrevivência

---

### ❌ **Baixa Chance de Sobrevivência** (3ª Classe, Homem)
```json
{
  "pclass": 3,
  "sex": "male",
  "age": 22,
  "siblings_spouses": 1,
  "parents_children": 0,
  "fare": 7.25
}
```
**Resultado esperado**: ~10% de sobrevivência

---

## 🐛 Troubleshooting

### Erro: "API não está disponível"
- Verifique se o Python FastAPI está rodando (Terminal 1)
- Teste: `curl http://localhost:8000`

### Erro CORS no navegador
- Certifique-se que o NestJS está com CORS habilitado (já configurado)
- Verifique se as portas estão corretas (5173, 3001, 8000)

### NestJS não conecta ao Python
- Verifique se a porta 8000 está livre
- Confira URL no `titanic.service.ts`: `http://localhost:8000`

### React não encontra o NestJS
- Verifique se a porta 3001 está livre
- Confira URL no `TitanicPredictor.tsx`: `http://localhost:3001`

---

## 📦 Portas Utilizadas

| Serviço       | Porta | URL                      |
|---------------|-------|--------------------------|
| React (Vite)  | 5173  | http://localhost:5173    |
| NestJS        | 3001  | http://localhost:3001    |
| Python FastAPI| 8000  | http://localhost:8000    |

---

## 🎯 Endpoints Disponíveis

### NestJS (`http://localhost:3001`)
- `GET /titanic/health` - Verifica se Python API está online
- `GET /titanic/model` - Informações do modelo ML
- `POST /titanic/predict` - Predição individual
- `POST /titanic/predict/batch` - Predição em lote

### Python FastAPI (`http://localhost:8000`)
- `GET /` - Health check
- `GET /model/info` - Informações do modelo
- `POST /predict` - Predição individual
- `POST /predict/batch` - Predição em lote

---

## ✅ Checklist de Verificação

- [ ] Python FastAPI iniciado (porta 8000)
- [ ] NestJS iniciado (porta 3001)
- [ ] React iniciado (porta 5173)
- [ ] Navegador aberto em `http://localhost:5173`
- [ ] Teste direto (React → Python) funcionando
- [ ] Teste com proxy (React → NestJS → Python) funcionando
- [ ] cURL no NestJS funcionando

---

## 🚀 Comandos Rápidos

```bash
# Iniciar tudo de uma vez (3 terminais separados)

# Terminal 1
cd semana-02-data-science/python-api && py app.py

# Terminal 2
cd semana-02-data-science/nestjs-client && npm run start:dev

# Terminal 3
cd semana-02-data-science/react-vite-app && npm run dev
```

---

## 📚 Próximos Passos

1. ✅ Sistema funcionando end-to-end
2. 📝 Documentar resultados e prints
3. 🧪 Testes automatizados (Jest + pytest)
4. 📊 Melhorias no UI (gráficos, histórico)
5. 🐳 Containerizar com Docker
6. ☁️ Deploy na nuvem (Azure/AWS)

---

**Desenvolvido por**: Lutivix  
**Data**: Janeiro 2025  
**Projeto**: Aprendizado IA 2025 - Semana 02 Dia 03
