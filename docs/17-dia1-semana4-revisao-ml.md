# 📚 Dia 1 - Semana 4: Revisão e Consolidação de ML

**Data:** 3 Dezembro 2025  
**Duração:** TBD  
**Foco:** 🧘‍♀️ Consolidar conhecimento, não correr

---

## 🎯 Objetivos do Dia

1. **Revisar quando usar cada algoritmo ML**
2. **Criar comparação visual e prática de modelos**
3. **Desenvolver árvore de decisão para escolha de algoritmos**
4. **Praticar cenários reais de decisão**

## 🧠 Por que Esta Revisão é Importante?

Após 3 semanas intensas, você implementou diversos algoritmos ML:
- **Regressão:** Linear Regression, Ridge, Lasso
- **Classificação:** Logistic Regression, Random Forest, XGBoost, SVM, Neural Networks
- **Técnicas:** Cross-Validation, Hyperparameter Tuning, Feature Engineering

**Mas você sabe QUANDO usar cada um?** Esta é a diferença entre alguém que implementa código e alguém que **resolve problemas com ML**. 🎯

---

## 📊 Guia Comparativo de Algoritmos ML

### 1️⃣ Regressão Linear (Linear Regression)

#### ✅ Quando Usar
- Relacionamento **linear** entre features e target
- Dados com **poucas features** (< 10-20)
- Você precisa de **interpretabilidade** (coeficientes claros)
- Baseline rápido para comparação

#### ❌ Quando NÃO Usar
- Relações não-lineares complexas
- Muitas features correlacionadas (multicolinearidade)
- Outliers severos nos dados
- Target não tem distribuição normal

#### 💡 Exemplo Prático
```python
# BOM USO: Prever preço de casa baseado em área
# Features: área (m²), quartos, banheiros
# Target: preço (relação aproximadamente linear)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
```

**Seu Projeto:** Semana 1 - Previsão simples (R² 96.5%)

---

### 2️⃣ Regressão Logística (Logistic Regression)

#### ✅ Quando Usar
- **Classificação binária** (sim/não, 0/1)
- Precisa de **probabilidades** como output
- Dados **linearmente separáveis** (ou quase)
- Baseline rápido para classificação
- Precisa entender **importância das features**

#### ❌ Quando NÃO Usar
- Relações não-lineares complexas
- Múltiplas classes com padrões complexos
- Features altamente correlacionadas sem regularização

#### 💡 Exemplo Prático
```python
# BOM USO: Prever sobrevivência no Titanic
# Features: idade, sexo, classe, tarifa
# Target: survived (0/1)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
```

**Seu Projeto:** Semana 2 - Titanic (79% accuracy)

---

### 3️⃣ Random Forest

#### ✅ Quando Usar
- **Primeira escolha** para muitos problemas
- Dados com **features não-lineares**
- Precisa de **feature importance**
- Dados com outliers (mais robusto)
- Classificação ou regressão
- Não quer gastar muito tempo com feature engineering

#### ❌ Quando NÃO Usar
- Dados com muitas dimensões e poucas amostras
- Precisa de modelo muito rápido em produção
- Memória limitada (armazena múltiplas árvores)

#### 💡 Exemplo Prático
```python
# BOM USO: Qualquer problema tabular balanceado
# Features: mix de categóricas e numéricas
# Target: classificação ou regressão

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Feature importance
importances = model.feature_importances_
```

**Seu Projeto:** Semana 3 - Dia 1 (81% accuracy), Dia 3 (81.46% API)

---

### 4️⃣ XGBoost (Gradient Boosting)

#### ✅ Quando Usar
- Quer a **melhor accuracy** possível
- Dados tabulares estruturados
- Competições de Kaggle 🏆
- Tem tempo para hyperparameter tuning
- Dados desbalanceados (com scale_pos_weight)

#### ❌ Quando NÃO Usar
- Poucos dados de treino (< 1000 amostras)
- Interpretabilidade é prioridade máxima
- Não tem tempo/recursos para tuning
- Dados muito ruidosos (pode overfit)

#### 💡 Exemplo Prático
```python
# BOM USO: Maximizar performance em competição
# Features: bem preparadas, sem missing values tratado
# Target: classificação ou regressão

import xgboost as xgb
model = xgb.XGBClassifier(
    n_estimators=100,
    max_depth=5,
    learning_rate=0.1,
    random_state=42
)
model.fit(X_train, y_train)
```

**Seu Projeto:** Semana 3 - Dia 1 (**85.1% accuracy** - melhor resultado!)

---

### 5️⃣ Support Vector Machine (SVM)

#### ✅ Quando Usar
- Dados **pequenos** mas com **alta dimensionalidade**
- Classificação binária com **margem clara**
- Kernel trick para relações não-lineares (RBF kernel)
- Dados bem escalados e normalizados

#### ❌ Quando NÃO Usar
- Datasets muito grandes (> 10k amostras - lento!)
- Múltiplas classes (pode ser lento)
- Features não escaladas
- Precisa de probabilidades (não nativo)

#### 💡 Exemplo Prático
```python
# BOM USO: Classificação de textos, imagens pequenas
# Features: escaladas (StandardScaler)
# Target: classificação binária ou multi-classe pequena

from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

model = SVC(kernel='rbf', C=1.0, random_state=42)
model.fit(X_train_scaled, y_train)
```

**Seu Projeto:** Semana 3 - Dia 1 (implementado com kernel RBF)

---

### 6️⃣ Neural Networks (MLP)

#### ✅ Quando Usar
- Relações **muito complexas** e não-lineares
- Dados com **padrões ocultos**
- Tem muitos dados de treino (> 10k amostras)
- Features já bem preprocessadas
- Pode usar GPU para treino

#### ❌ Quando NÃO Usar
- Poucos dados (vai overfit)
- Precisa de interpretabilidade
- Dados não estão escalados
- Sem tempo para tuning (muitos hiperparâmetros)
- Baseline ou prototipagem rápida

#### 💡 Exemplo Prático
```python
# BOM USO: Padrões complexos com muitos dados
# Features: escaladas, muitas amostras
# Target: classificação ou regressão complexa

from sklearn.neural_network import MLPClassifier

model = MLPClassifier(
    hidden_layer_sizes=(100, 50),
    max_iter=1000,
    random_state=42,
    early_stopping=True
)
model.fit(X_train, y_train)
```

**Seu Projeto:** Semana 3 - Dia 1 (implementado com early stopping)

---

## 🌳 Árvore de Decisão: Como Escolher seu Algoritmo

```
┌─────────────────────────────────────┐
│    Seu problema é classificação    │
│         ou regressão?               │
└────────────┬────────────────────────┘
             │
      ┌──────┴──────┐
      │             │
 REGRESSÃO    CLASSIFICAÇÃO
      │             │
      │             ├── Binária (0/1)?
      │             │   ├── Sim → LogisticRegression (baseline)
      │             │   │         RandomForest (melhor)
      │             │   │         XGBoost (competição)
      │             │   │
      │             │   └── Multi-classe?
      │             │       └── RandomForest ou XGBoost
      │             │
      │             └── Tem muitos dados (>10k)?
      │                 ├── Sim → XGBoost ou Neural Network
      │                 └── Não → RandomForest ou SVM
      │
      └── LinearRegression (baseline linear)
          RandomForest (não-linear)
          XGBoost (melhor accuracy)
          Neural Network (muito complexo)
```

---

## 🎯 Guia Prático: Seu Fluxo de Trabalho ML

### Etapa 1: Sempre comece com baseline simples ⚡
```python
# CLASSIFICAÇÃO
baseline = LogisticRegression()

# REGRESSÃO  
baseline = LinearRegression()
```
**Por quê?** Dá uma referência rápida. Se modelos complexos não batem baseline, tem problema nos dados!

### Etapa 2: Random Forest como segundo teste 🌲
```python
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
```
**Por quê?** Funciona bem "out of the box", robusto, dá feature importance.

### Etapa 3: Se precisa mais accuracy, XGBoost 🚀
```python
import xgboost as xgb
model = xgb.XGBClassifier(n_estimators=100, max_depth=5, learning_rate=0.1)
```
**Por quê?** Melhor performance, mas precisa tuning.

### Etapa 4: Hyperparameter Tuning 🎛️
```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [3, 5, 7],
    'learning_rate': [0.01, 0.1, 0.3]
}

grid = GridSearchCV(model, param_grid, cv=5, scoring='accuracy')
grid.fit(X_train, y_train)
```

---

## 📋 Checklist de Decisão Rápida

**Antes de escolher um algoritmo, pergunte:**

1. **Quantos dados tenho?**
   - < 1000 → Logistic Regression, SVM
   - 1k-10k → Random Forest
   - > 10k → XGBoost, Neural Network

2. **Preciso interpretar o modelo?**
   - Sim → Linear/Logistic Regression
   - Mais ou menos → Random Forest (feature importance)
   - Não → XGBoost, Neural Network

3. **Quanto tempo tenho para treinar?**
   - Pouco → Logistic Regression, Random Forest
   - Médio → Random Forest, XGBoost
   - Muito → XGBoost tuning, Neural Networks

4. **Os dados são lineares?**
   - Sim → Linear/Logistic Regression
   - Não → Random Forest, XGBoost, Neural Network
   - Não sei → Teste baseline linear primeiro!

5. **Tenho outliers?**
   - Sim → Random Forest (robusto)
   - Não → Qualquer modelo

---

## 💡 Lições Aprendidas nas Semanas 1-3

### ✅ O que Funcionou Bem

1. **Começar simples:** LinearRegression na Semana 1 foi excelente para aprender
2. **Feature Engineering:** Transformações aumentaram accuracy de 76% → 79% (Semana 2)
3. **Cross-Validation:** Evitou overfitting e deu confiança nos resultados
4. **Random Forest primeiro:** Quase sempre deu bons resultados iniciais
5. **XGBoost quando importa:** Melhor accuracy (85.1%) quando otimizado

### ⚠️ Armadilhas Comuns

1. **Esquecer de escalar dados** → SVM e Neural Networks precisam!
2. **Overfit em dados pequenos** → Use cross-validation sempre
3. **Não fazer baseline** → Como saber se modelo complexo vale a pena?
4. **Tuning excessivo antes de entender** → Entenda o modelo primeiro
5. **Ignorar feature importance** → Pode remover features desnecessárias

---

## 🧪 Exercícios Práticos

### Exercício 1: Escolha o Algoritmo
Para cada cenário, escolha o melhor algoritmo inicial:

**A) Dataset:** 500 amostras, 5 features, prever se cliente compra (0/1)  
**Resposta:** `_______________`

**B) Dataset:** 50.000 amostras, 20 features, prever preço de casa  
**Resposta:** `_______________`

**C) Dataset:** 100 amostras, 1000 features (texto), classificação de emails  
**Resposta:** `_______________`

**D) Dataset:** 10.000 amostras, 15 features, competição Kaggle de classificação  
**Resposta:** `_______________`

### Exercício 2: Debug de Modelo
Você treinou um XGBoost e o resultado é:
- Train accuracy: 99%
- Test accuracy: 65%

**O que está acontecendo?** `_______________`  
**Como resolver?** `_______________`

---

## 📚 Notebook Prático

Veja o notebook `01-revisao-algoritmos-ml.ipynb` para:
- ✅ Implementação lado-a-lado dos 6 algoritmos
- ✅ Comparação visual de desempenho
- ✅ Análise de quando cada um funciona melhor
- ✅ Exemplos práticos com dados reais

---

## 🎯 Próximos Passos

- [ ] Completar notebook de revisão
- [ ] Fazer exercícios de escolha de algoritmos
- [ ] Revisar seus projetos anteriores com novo olhar
- [ ] Documentar suas próprias "regras de bolso"

---

## 📝 Reflexões Finais

*"O melhor algoritmo não é o mais complexo, é aquele que resolve seu problema de forma confiável e mantível."*

**Perguntas para reflexão:**
1. Consigo explicar quando usar Random Forest vs XGBoost?
2. Sei por que preciso escalar dados para SVM?
3. Entendo o tradeoff entre interpretabilidade e accuracy?

---

**Tempo Total:** TBD  
**Próximo:** Dia 2 - Feature Engineering na Prática

*Lembre-se: Compreensão profunda > Memorização de código* 🎯
