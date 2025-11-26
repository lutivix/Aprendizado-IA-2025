# 🚀 Guia Rápido - Dia 3: Dashboard React + FastAPI

## ⚡ Setup Rápido (5 minutos)

### 1️⃣ Backend (Terminal 1)
```bash
cd semana-03-ml-avancado/python-api

# Instalar dependências
pip install -r requirements.txt

# Treinar modelo
python train_model.py

# Iniciar API
python app.py
```

✅ API rodando em: **http://localhost:8000**
📚 Docs: **http://localhost:8000/docs**

---

### 2️⃣ Frontend (Terminal 2)
```bash
cd semana-03-ml-avancado/react-dashboard

# Instalar dependências
npm install

# Iniciar dashboard
npm run dev
```

✅ Dashboard rodando em: **http://localhost:5173**

---

## 🧪 Teste Rápido

### Opção 1: Dashboard Visual
1. Abra **http://localhost:5173**
2. Clique em **"Exemplo: Sobrevivente"**
3. Clique em **"🔮 Prever Sobrevivência"**
4. Veja o resultado! 🎉

### Opção 2: Terminal
```bash
cd semana-03-ml-avancado/python-api
python test_api.py
```

---

## 📊 O que você vai ver

### Card 1: Informações do Modelo
```
📊 Informações do Modelo
├─ Modelo: Random Forest Classifier
├─ Accuracy: 82.68%
├─ N° de Árvores: 100
├─ Profundidade Máxima: 10
└─ Features: Pclass, Sex, Age, SibSp, Parch, Fare, Embarked
```

### Card 2: Formulário de Predição
```
📝 Fazer Predição
├─ [Botão] Exemplo: Sobrevivente
├─ [Botão] Exemplo: Vítima
├─ Classe: [1ª/2ª/3ª]
├─ Sexo: [Masculino/Feminino]
├─ Idade: [0-100]
├─ Irmãos/Cônjuges: [0+]
├─ Pais/Filhos: [0+]
├─ Tarifa: [£]
├─ Porto: [Cherbourg/Queenstown/Southampton]
└─ [Botão] 🔮 Prever Sobrevivência
```

### Card 3: Resultado
```
🎯 Resultado

🎉 (ou 😢)

Sobreviveu! (ou Não sobreviveu)

Probabilidade de sobrevivência: 85.3%

💡 Interpretação:
Com uma probabilidade de 85.3%, o modelo prevê que
este passageiro teria sobrevivido ao desastre do Titanic...
```

---

## 🎨 Exemplos Pré-configurados

### Exemplo 1: Alta Chance de Sobrevivência ✅
```json
{
  "pclass": 1,        // 1ª Classe
  "sex": "female",    // Mulher
  "age": 38,
  "sibsp": 1,
  "parch": 0,
  "fare": 71.28,
  "embarked": "C"     // Cherbourg
}
```
**Resultado esperado:** 🎉 Sobreviveu (~85% probabilidade)

### Exemplo 2: Baixa Chance de Sobrevivência ❌
```json
{
  "pclass": 3,        // 3ª Classe
  "sex": "male",      // Homem
  "age": 22,
  "sibsp": 1,
  "parch": 0,
  "fare": 7.25,
  "embarked": "S"     // Southampton
}
```
**Resultado esperado:** 😢 Não sobreviveu (~12% probabilidade)

---

## 🔧 Estrutura de Arquivos

```
semana-03-ml-avancado/
│
├── python-api/                    # 🐍 Backend
│   ├── app.py                     # FastAPI app
│   ├── train_model.py             # Treino do modelo
│   ├── test_api.py                # Testes
│   ├── requirements.txt           # Dependências
│   ├── model.pkl                  # Modelo treinado
│   └── model_metadata.json        # Metadata
│
└── react-dashboard/               # ⚛️ Frontend
    ├── src/
    │   ├── App.tsx                # Componente principal
    │   ├── App.css                # Estilos
    │   └── components/
    │       ├── ModelInfo.tsx      # Info do modelo
    │       ├── PredictionForm.tsx # Formulário
    │       └── PredictionResult.tsx # Resultado
    └── package.json
```

---

## 🐛 Problemas Comuns

### ❌ "Modelo não carregado"
```bash
cd python-api
python train_model.py
```

### ❌ "API não conecta"
Certifique-se de que a API está rodando:
```bash
curl http://localhost:8000/health
```

### ❌ "CORS Error"
A API já está configurada para aceitar requisições de `localhost:5173`

---

## 📚 Links Úteis

- 🌐 **Dashboard:** http://localhost:5173
- 🔌 **API:** http://localhost:8000
- 📖 **API Docs (Swagger):** http://localhost:8000/docs
- 📘 **API Docs (ReDoc):** http://localhost:8000/redoc

---

## ✅ Checklist

- [ ] Backend instalado e rodando
- [ ] Modelo treinado (model.pkl existe)
- [ ] Frontend instalado e rodando
- [ ] Dashboard abre no navegador
- [ ] Info do modelo carrega
- [ ] Botões de exemplo funcionam
- [ ] Predições funcionam
- [ ] Resultado aparece com animação

---

## 🎉 Pronto!

Você tem um sistema full-stack ML completo rodando localmente!

**Próximos passos:**
1. Experimente diferentes combinações de dados
2. Compare predições de sobreviventes vs vítimas
3. Analise as probabilidades
4. Entenda quais features mais influenciam
5. Adicione melhorias (opcional)

---

**Documentação completa:** `docs/16-dia3-semana3-dashboard-react.md`
