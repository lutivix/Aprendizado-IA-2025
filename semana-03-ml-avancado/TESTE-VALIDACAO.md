# 🧪 Teste de Validação - Semana 3: ML Supervisionado Avançado

## ⏱️ Tempo estimado total: 40 minutos
- Dia 1 (Modelos Avançados): 20 minutos
- Dia 2 (Hyperparameter Tuning): 20 minutos

---

# 📅 DIA 1: Modelos Avançados

## 📋 Parte 1: Conceitos (múltipla escolha)

### Questão 1: Ensemble Methods
Você tem um dataset pequeno (500 amostras) e precisa de alta acurácia. Qual modelo seria mais adequado?

**A)** Decision Tree (árvore única)  
**B)** Random Forest  
**C)** XGBoost  
**D)** SVM  

<details>
<summary>💡 Ver resposta</summary>

**Resposta: B) Random Forest**

**Por quê:**
- Decision Tree: Tende a overfitting com poucos dados
- **Random Forest: Reduz overfitting usando várias árvores, ideal para dados pequenos**
- XGBoost: Excelente, mas pode ser overkill e mais complexo de configurar
- SVM: Bom também, mas precisa de normalização e ajuste de hiperparâmetros

**Conceito-chave:** Random Forest é o "safe choice" para maioria dos problemas tabulares.
</details>

---

### Questão 2: Normalização
Você vai treinar 3 modelos: Random Forest, SVM e MLP. Para quais você DEVE aplicar StandardScaler?

**A)** Apenas Random Forest  
**B)** Apenas SVM  
**C)** SVM e MLP  
**D)** Todos os três  

<details>
<summary>💡 Ver resposta</summary>

**Resposta: C) SVM e MLP**

**Por quê:**
- **Random Forest:** Baseado em árvores, **não é afetado** por escala
- **SVM:** Usa distâncias euclidianas, **sensível à escala**
- **MLP:** Usa gradientes, **sensível à escala**

**Código correto:**
```python
# ❌ ERRADO
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
# Treinar todos os modelos com X_train_scaled

# ✅ CERTO
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Random Forest: usa X_train original
# SVM e MLP: usa X_train_scaled
```

**Conceito-chave:** Modelos baseados em distância precisam de normalização.
</details>

---

### Questão 3: Feature Importance
Você treinou um Random Forest e a feature `age` tem importância 0.35 e `fare` tem 0.05. O que isso significa?

**A)** `age` é 7x mais importante que `fare`  
**B)** Devo remover `fare` do modelo  
**C)** `age` contribui 35% para as decisões do modelo  
**D)** Devo normalizar `age` porque o valor é muito alto  

<details>
<summary>💡 Ver resposta</summary>

**Resposta: C) `age` contribui 35% para as decisões do modelo**

**Por quê:**
- A) Incorreto: Não é uma relação linear direta de "vezes"
- B) Incorreto: Features com baixa importância ainda podem ser úteis
- **C) Correto: Feature importance soma 1.0 (100%), então 0.35 = 35% de contribuição**
- D) Incorreto: Valor alto de importance é DESEJÁVEL, não um problema

**Quando remover features:**
- Importância próxima de **zero** (<0.001)
- **Causa overfitting** (modelo muito complexo)
- **Custo de coleta** é alto demais para o benefício

**Conceito-chave:** Feature importance mostra contribuição relativa, não valor absoluto.
</details>

---

### Questão 4: Overfitting
Seu modelo tem:
- **Train accuracy:** 98%
- **Test accuracy:** 75%

O que está acontecendo e como corrigir?

**A)** Underfitting - aumentar complexidade do modelo  
**B)** Overfitting - reduzir complexidade ou adicionar regularização  
**C)** Modelo perfeito - nenhuma ação necessária  
**D)** Dataset ruim - coletar mais dados  

<details>
<summary>💡 Ver resposta</summary>

**Resposta: B) Overfitting - reduzir complexidade ou adicionar regularização**

**Por quê:**
Grande diferença entre train e test (23%) indica **overfitting** = modelo decorou os dados de treino.

**Soluções práticas:**

1. **Random Forest:**
```python
# ❌ Overfitting
RandomForestClassifier(n_estimators=200, max_depth=None)

# ✅ Melhor
RandomForestClassifier(
    n_estimators=100,
    max_depth=10,        # Limita profundidade
    min_samples_split=20 # Exige mais amostras para dividir
)
```

2. **Neural Network:**
```python
# ❌ Overfitting
MLPClassifier(hidden_layer_sizes=(200, 100, 50))

# ✅ Melhor
MLPClassifier(
    hidden_layer_sizes=(50, 25),  # Menos neurônios
    early_stopping=True,           # Para quando não melhora
    validation_fraction=0.2        # Valida durante treino
)
```

**Conceito-chave:** Train >> Test = Overfitting. Simplificar ou regularizar.
</details>

---

## 🖥️ Parte 2: Prática (código)

### Desafio: Completar o Pipeline

Você tem este código com **3 erros**. Encontre e corrija:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Carregar dados
df = pd.read_csv('dataset.csv')
X = df.drop('target', axis=1)
y = df['target']

# Dividir dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Normalizar
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)  # ❌ ERRO 1

# Treinar Random Forest
rf_model = RandomForestClassifier()
rf_model.fit(X_train_scaled, y_train)  # ❌ ERRO 2
y_pred_rf = rf_model.predict(X_test_scaled)

# Treinar SVM
svm_model = SVC()
svm_model.fit(X_train, y_train)  # ❌ ERRO 3
y_pred_svm = svm_model.predict(X_test_scaled)

# Avaliar
print(f"RF Accuracy: {accuracy_score(y_test, y_pred_rf)}")
print(f"SVM Accuracy: {accuracy_score(y_test, y_pred_svm)}")
```

<details>
<summary>💡 Ver resposta e explicação</summary>

### Erros e Correções:

#### ❌ ERRO 1: `scaler.fit_transform(X_test)`
```python
# ERRADO
X_test_scaled = scaler.fit_transform(X_test)

# CERTO
X_test_scaled = scaler.transform(X_test)
```
**Por quê:** `fit_transform` recalcula média/desvio no test set = **data leakage**!  
**Regra:** `fit` apenas no train, `transform` no test.

---

#### ❌ ERRO 2: Random Forest com dados normalizados
```python
# ERRADO
rf_model.fit(X_train_scaled, y_train)

# CERTO
rf_model.fit(X_train, y_train)  # Dados originais
```
**Por quê:** Random Forest não precisa de normalização (baseado em thresholds, não distâncias).

---

#### ❌ ERRO 3: SVM sem normalização
```python
# ERRADO
svm_model.fit(X_train, y_train)

# CERTO
svm_model.fit(X_train_scaled, y_train)
```
**Por quê:** SVM é **sensível à escala** das features (usa distâncias).

---

### ✅ Código Correto Completo:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Carregar dados
df = pd.read_csv('dataset.csv')
X = df.drop('target', axis=1)
y = df['target']

# Dividir dados
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42  # ✅ Adicione random_state!
)

# Normalizar
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # ✅ transform, não fit_transform

# Treinar Random Forest
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)  # ✅ Dados originais
y_pred_rf = rf_model.predict(X_test)  # ✅ Dados originais

# Treinar SVM
svm_model = SVC(random_state=42)
svm_model.fit(X_train_scaled, y_train)  # ✅ Dados normalizados
y_pred_svm = svm_model.predict(X_test_scaled)  # ✅ Dados normalizados

# Avaliar
print(f"RF Accuracy: {accuracy_score(y_test, y_pred_rf):.4f}")
print(f"SVM Accuracy: {accuracy_score(y_test, y_pred_svm):.4f}")
```

### 📊 Checklist de Validação:

| Modelo | Dados de Treino | Dados de Teste | Por quê? |
|--------|----------------|----------------|----------|
| Random Forest | `X_train` | `X_test` | Não precisa normalização |
| XGBoost | `X_train` | `X_test` | Não precisa normalização |
| SVM | `X_train_scaled` | `X_test_scaled` | Precisa normalização |
| MLP | `X_train_scaled` | `X_test_scaled` | Precisa normalização |

</details>

---

## 📊 Parte 3: Interpretação de Resultados

Você treinou 4 modelos no Titanic e obteve:

| Modelo | Train Acc | Test Acc | CV Score | Tempo (s) |
|--------|-----------|----------|----------|-----------|
| Decision Tree | 98.5% | 76.2% | 75.1% ± 3.2% | 0.05 |
| Random Forest | 95.3% | 83.8% | 82.9% ± 2.1% | 1.2 |
| XGBoost | 96.8% | 85.1% | 84.3% ± 1.8% | 2.5 |
| MLP | 89.2% | 81.5% | 80.2% ± 4.5% | 3.8 |

### Questão: Qual modelo você escolheria para produção? Por quê?

<details>
<summary>💡 Ver resposta e análise</summary>

### 🏆 Resposta: **XGBoost**

### 📊 Análise Detalhada:

#### 1. **Decision Tree** ❌
- **Train 98.5% vs Test 76.2%** = Overfitting severo (22.3% diferença!)
- CV score baixo e alta variância (±3.2%)
- **Veredicto:** Não confiável para produção

#### 2. **Random Forest** ✅ (2ª opção)
- Train vs Test: 95.3% - 83.8% = 11.5% (razoável)
- Boa estabilidade (CV ±2.1%)
- **Rápido** (1.2s)
- **Veredicto:** Excelente opção se tempo de inferência é crítico

#### 3. **XGBoost** 🏆 (MELHOR)
- **Melhor test accuracy:** 85.1%
- **Melhor CV score:** 84.3%
- **Menor variância:** ±1.8% (mais estável)
- Train vs Test: 96.8% - 85.1% = 11.7% (similar ao RF)
- Tempo aceitável (2.5s para treino)
- **Veredicto:** Melhor generalização + estabilidade

#### 4. **MLP** ⚠️
- Performance OK (81.5%)
- **Problema:** Alta variância (±4.5%) = instável
- Mais lento (3.8s)
- Train-Test gap pequeno (7.7%), mas CV ruim
- **Veredicto:** Necessita mais tuning de hiperparâmetros

---

### 🎯 Critérios de Decisão:

```
Escolha baseado em:

1. Test Accuracy (principal métrica)
   ✅ XGBoost: 85.1%

2. Estabilidade (CV variance)
   ✅ XGBoost: ±1.8%

3. Generalização (Train-Test gap)
   ✅ RF e XGBoost: ~11%

4. Tempo de treino/inferência
   ✅ RF: 1.2s (se crítico)

5. Interpretabilidade
   ✅ RF: Mais fácil de explicar
```

### 💼 Decisão para Produção:

**Cenário 1: Performance máxima**
→ **XGBoost** (85.1% acc, mais estável)

**Cenário 2: Tempo real crítico**
→ **Random Forest** (83.8% acc, 2x mais rápido)

**Cenário 3: Interpretabilidade crítica**
→ **Random Forest** (feature importance mais clara)

---

### ⚠️ Red Flags a Observar:

1. **Train >> Test** (>15% diferença) = Overfitting
2. **CV variance alta** (>3%) = Modelo instável
3. **Test < 80%** no Titanic = Modelo fraco
4. **Tempo > 10s** = Pode não escalar

</details>

---

## 🎓 Gabarito de Auto-Avaliação

### Pontuação:

- **Parte 1 (Conceitos):** 4 questões × 2 pontos = **8 pontos**
- **Parte 2 (Código):** 3 erros × 2 pontos = **6 pontos**  
- **Parte 3 (Interpretação):** 1 questão × 6 pontos = **6 pontos**

**TOTAL:** 20 pontos

---

### 📊 Interpretação da sua nota:

#### 🏆 18-20 pontos: EXCELENTE!
**Você está PRONTO para Semana 4!**

✅ Domina os conceitos principais  
✅ Identifica erros comuns  
✅ Interpreta resultados corretamente  

**Próximos passos:**
- Avançar para Semana 4 com confiança
- Considere fazer um mini-projeto de consolidação (opcional)

---

#### 💪 14-17 pontos: BOM!
**Você pode avançar, mas revise alguns pontos.**

✅ Entende a maioria dos conceitos  
⚠️ Pode ter dúvidas em situações específicas  

**Próximos passos:**
- Revise as questões que errou (leia as explicações)
- Pratique um pouco mais os conceitos fracos
- Avançar para Semana 4, mas mantenha o material da S3 à mão

---

#### 🔄 10-13 pontos: PARCIAL
**Recomendado revisar antes de avançar.**

⚠️ Alguns conceitos não estão claros  
⚠️ Pode ter dificuldade na Semana 4  

**Próximos passos:**
- Refaça o notebook da Semana 3
- Foque nos conceitos que errou aqui
- Tente o teste novamente após 2-3 dias
- **Só avance quando se sentir mais confiante**

---

#### 📚 0-9 pontos: REVISAR
**É importante refazer o conteúdo da Semana 3.**

❌ Conceitos fundamentais precisam de atenção  

**Próximos passos:**
1. **Não se desanime!** Isso é aprendizado, não prova
2. Releia o material da Semana 3
3. Execute o notebook célula por célula, entendendo cada parte
4. Faça anotações com suas palavras
5. Retome este teste em 1 semana

**Dica:** Foque em entender O PORQUÊ, não em memorizar código.

---

## 🧩 Teste Bônus: Cenário Real

### 💼 Desafio Profissional (avançado)

Você é contratado para prever churn (cancelamento) de clientes de uma empresa de streaming. O time te passa:

- **Dataset:** 10.000 clientes, 25 features
- **Target:** `churn` (0 = fica, 1 = cancela)
- **Deadline:** 1 semana
- **Requisito:** Mínimo 80% de recall (não perder clientes que vão sair)

**Seu plano de ação:**

```markdown
## Dia 1-2: EDA
- [ ] ___________
- [ ] ___________

## Dia 3-4: Feature Engineering
- [ ] ___________
- [ ] ___________

## Dia 5: Modelagem
- [ ] Modelos a testar: __________, __________, __________
- [ ] Por que esses modelos? ___________

## Dia 6: Otimização
- [ ] ___________

## Dia 7: Deploy
- [ ] ___________
```

<details>
<summary>💡 Ver exemplo de plano profissional</summary>

## ✅ Exemplo de Plano:

### Dia 1-2: EDA
- [ ] Verificar missing values e outliers
- [ ] Analisar distribuição do target (balanceamento)
- [ ] Correlação entre features e churn
- [ ] Identificar features mais importantes visualmente

### Dia 3-4: Feature Engineering
- [ ] Criar features de comportamento (média de uso, frequência)
- [ ] Encoding de variáveis categóricas
- [ ] Tratar valores faltantes
- [ ] Normalizar features numéricas (se necessário)

### Dia 5: Modelagem
- **Modelos:** Random Forest, XGBoost, Logistic Regression
- **Por quê:**
  - RF: Baseline sólido, lida com imbalance
  - XGBoost: Melhor performance geralmente
  - LogReg: Rápido, interpretável para stakeholders

### Dia 6: Otimização
- [ ] Hyperparameter tuning (GridSearch/RandomSearch)
- [ ] Ajustar threshold para priorizar recall (>80%)
- [ ] Validar com cross-validation
- [ ] Analisar feature importance para insights de negócio

### Dia 7: Deploy
- [ ] Salvar modelo final (pickle/joblib)
- [ ] Criar script de predição
- [ ] Documentar pipeline
- [ ] Apresentar insights para o time

### 📊 Métricas a Focar:
- **Recall:** >80% (requisito principal)
- **Precision:** Quanto maior melhor (evitar falsos positivos)
- **F1-Score:** Balancear recall e precision
- **ROC-AUC:** Avaliar separação geral

### 💡 Dica Profissional:
Em problemas de churn, **recall é mais importante** que accuracy!
É melhor contatar 100 clientes (10 falsos alarmes) que perder 10 clientes reais.

</details>

---

## 🎯 Reflexão Final

Responda honestamente (só para você):

1. **Consegui entender o propósito de cada modelo?**  
   [ ] Sim, totalmente  
   [ ] Mais ou menos  
   [ ] Preciso revisar  

2. **Sei quando usar normalização?**  
   [ ] Sim, com confiança  
   [ ] Tenho dúvidas  
   [ ] Não entendi bem  

3. **Interpreto matriz de confusão e feature importance?**  
   [ ] Sim, tranquilamente  
   [ ] Com ajuda do material  
   [ ] Ainda confuso  

4. **Me sinto confortável para tentar um problema novo similar?**  
   [ ] Sim, vou tentar!  
   [ ] Com o material ao lado, sim  
   [ ] Acho que não ainda  

---

## ✅ Decisão Final

Com base nas suas respostas:

### ➡️ AVANCE se:
- Acertou 14+ pontos no teste
- Respondeu "Sim" ou "Mais ou menos" na maioria das reflexões
- Sente que, **com consulta ao material**, consegue fazer

### 🔄 REVISE se:
- Acertou <10 pontos
- Respondeu "Preciso revisar" ou "Não entendi" em 3+ reflexões
- Sente que **não conseguiria nem com material ao lado**

---

---

# 📅 DIA 2: Hyperparameter Tuning e Cross-Validation

## 📋 Parte 1: Conceitos (múltipla escolha)

### Questão 1: Parâmetros vs Hiperparâmetros
Qual das seguintes afirmações está CORRETA?

**A)** Parâmetros são definidos antes do treino, hiperparâmetros são aprendidos durante  
**B)** Hiperparâmetros são definidos antes do treino, parâmetros são aprendidos durante  
**C)** Ambos são aprendidos durante o treino  
**D)** Ambos são definidos antes do treino  

<details>
<summary>💡 Ver resposta</summary>

**Resposta: B) Hiperparâmetros são definidos antes do treino, parâmetros são aprendidos durante**

**Exemplos:**

| Modelo | Parâmetros (aprendidos) | Hiperparâmetros (definidos antes) |
|--------|------------------------|-----------------------------------|
| Linear Regression | Coeficientes (w, b) | Taxa de aprendizado |
| Random Forest | Splits das árvores | `max_depth`, `n_estimators` |
| Neural Network | Pesos das conexões | Arquitetura, learning rate |

**Analogia:** 
- **Hiperparâmetros:** Configurações do treino (quantos dias treinar por semana)
- **Parâmetros:** O que você aprende durante o treino (técnica de chute)

**Conceito-chave:** Hiperparâmetros controlam COMO o modelo aprende, parâmetros são O QUE ele aprende.
</details>

---

### Questão 2: Grid Search vs Random Search
Você tem 5 hiperparâmetros, cada um com 4 possíveis valores, e tempo limitado (30 minutos). O que fazer?

**A)** Grid Search com todos os valores (4^5 = 1024 combinações)  
**B)** Random Search com n_iter=50  
**C)** Testar manualmente 10 combinações  
**D)** Usar valores padrão (não fazer tuning)  

<details>
<summary>💡 Ver resposta</summary>

**Resposta: B) Random Search com n_iter=50**

**Por quê:**

**Grid Search:**
- 1024 combinações × CV=5 = **5120 treinos**
- Tempo: Inviável em 30 minutos

**Random Search (n_iter=50):**
- 50 combinações × CV=5 = **250 treinos**
- Tempo: Viável em 30 minutos
- Explora melhor o espaço (pode encontrar combinações não óbvias)

**Manual (10 combinações):**
- Muito poucas para espaço grande
- Depende de intuição (pode errar)

**Valores padrão:**
- Rápido mas pode ter performance ruim

**Regra prática:**
```
Hiperparâmetros ≤ 3 → Grid Search
Hiperparâmetros > 3 → Random Search
Tempo muito limitado → Valores padrão + tuning simples
```

**Conceito-chave:** Random Search é mais eficiente para espaços grandes de hiperparâmetros.
</details>

---

### Questão 3: Cross-Validation
Você tem um dataset com 1000 amostras (700 classe 0, 300 classe 1). Qual estratégia de CV usar?

**A)** K-Fold com k=5 (sem stratify)  
**B)** Stratified K-Fold com k=5  
**C)** Leave-One-Out CV  
**D)** Holdout (train/test único)  

<details>
<summary>💡 Ver resposta</summary>

**Resposta: B) Stratified K-Fold com k=5**

**Por quê:**

Dataset desbalanceado (70% vs 30%) precisa de **Stratified K-Fold**.

**Comparação:**

| Método | Classe 0 | Classe 1 | Problema |
|--------|----------|----------|----------|
| K-Fold normal | Varia por fold | Varia por fold | ❌ Alguns folds podem ter poucos exemplos da classe 1 |
| **Stratified K-Fold** | **~70% em cada fold** | **~30% em cada fold** | ✅ Proporção mantida |
| Leave-One-Out | - | - | ❌ Muito lento (1000 iterações!) |
| Holdout | 70% | 30% | ❌ Não valida variância |

**Código correto:**
```python
from sklearn.model_selection import StratifiedKFold

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=skf)
```

**Conceito-chave:** Use SEMPRE Stratified K-Fold em classificação, especialmente se desbalanceado.
</details>

---

### Questão 4: Learning Curves
Você treinou um modelo e viu estas curvas:

```
Train accuracy: ████████████████ 95%
Test accuracy:  ████████▒▒▒▒▒▒▒▒ 60%
```

O que fazer?

**A)** Aumentar complexidade (mais features, modelo maior)  
**B)** Reduzir complexidade (regularização, menos features)  
**C)** Coletar mais dados  
**D)** B ou C (ambas podem ajudar)  

<details>
<summary>💡 Ver resposta</summary>

**Resposta: D) B ou C (ambas podem ajudar)**

**Diagnóstico: OVERFITTING**
- Train >> Test (35% gap)
- Modelo decorou os dados de treino

**Soluções:**

**1. Reduzir complexidade (B):**
```python
# Random Forest
RandomForestClassifier(
    max_depth=5,           # ↓ profundidade
    min_samples_split=50,  # ↑ amostras mínimas
    min_samples_leaf=20    # ↑ amostras por folha
)

# XGBoost
XGBClassifier(
    max_depth=3,           # ↓ profundidade
    learning_rate=0.01,    # ↓ taxa aprendizado
    reg_alpha=1.0,         # ↑ regularização L1
    reg_lambda=1.0         # ↑ regularização L2
)
```

**2. Mais dados (C):**
- Mais exemplos → modelo generaliza melhor
- Se possível, sempre ajuda

**3. Feature Selection:**
```python
from sklearn.feature_selection import RFE
selector = RFE(model, n_features_to_select=10)
```

**Cenários de Learning Curves:**

```
1. Overfitting:
   Train: ──────────── (alta)
   Test:  ────▁▁▁▁▁▁  (baixa)
   → Solução: Regularizar ou mais dados

2. Underfitting:
   Train: ──────── (baixa)
   Test:  ──────── (baixa)
   → Solução: Modelo mais complexo

3. Ideal:
   Train: ──────────── (alta)
   Test:  ─────────── (alta, próxima)
   → Solução: Nenhuma, está ótimo! ✅
```

**Conceito-chave:** Gap grande entre train/test = Overfitting → Regularizar ou mais dados.
</details>

---

## 🖥️ Parte 2: Prática (código)

### Desafio: Pipeline com Grid Search

Complete o código abaixo corrigindo os **4 erros**:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, train_test_split
import pandas as pd

# Carregar dados
df = pd.read_csv('titanic.csv')
X = df.drop('survived', axis=1)
y = df['survived']

# Dividir dados
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Pipeline para SVM
pipeline_svm = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', SVC())
])

# Grid Search para SVM
param_grid_svm = {
    'C': [0.1, 1, 10],              # ❌ ERRO 1: Falta prefixo
    'kernel': ['linear', 'rbf']
}

grid_svm = GridSearchCV(pipeline_svm, param_grid_svm, cv=5)
grid_svm.fit(X_train, y_train)

# Pipeline para Random Forest
pipeline_rf = Pipeline([
    ('scaler', StandardScaler()),   # ❌ ERRO 2: RF não precisa
    ('classifier', RandomForestClassifier())
])

# Treinar Random Forest
pipeline_rf.fit(X_train, y_train)

# Avaliar SVM
y_pred_svm = grid_svm.predict(X_test)
print(f"SVM Accuracy: {grid_svm.score(X_test, y_test)}")

# Avaliar Random Forest
scaler = StandardScaler()
X_test_scaled = scaler.fit_transform(X_test)  # ❌ ERRO 3: Data leakage
y_pred_rf = pipeline_rf.predict(X_test_scaled)  # ❌ ERRO 4: Dados errados

print(f"RF Accuracy: {pipeline_rf.score(X_test, y_test)}")
```

<details>
<summary>💡 Ver resposta completa</summary>

### ❌ Erros e Correções:

#### ERRO 1: Parâmetros do Grid sem prefixo do pipeline
```python
# ERRADO
param_grid_svm = {
    'C': [0.1, 1, 10],
    'kernel': ['linear', 'rbf']
}

# CERTO
param_grid_svm = {
    'classifier__C': [0.1, 1, 10],           # Prefixo: nome_do_passo__
    'classifier__kernel': ['linear', 'rbf']
}
```
**Por quê:** No Pipeline, parâmetros são acessados com `nome_passo__parametro`.

---

#### ERRO 2: Random Forest não precisa de normalização
```python
# ERRADO
pipeline_rf = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier())
])

# CERTO
pipeline_rf = Pipeline([
    ('classifier', RandomForestClassifier())  # Sem scaler
])

# OU SIMPLESMENTE
rf_model = RandomForestClassifier()
```
**Por quê:** RF é baseado em árvores (thresholds), não é afetado por escala.

---

#### ERRO 3: `fit_transform` no test set
```python
# ERRADO
scaler = StandardScaler()
X_test_scaled = scaler.fit_transform(X_test)  # ❌ Data leakage!

# CERTO
# Não precisa escalar separadamente, o pipeline já faz isso!
# Mas se fosse necessário:
scaler = StandardScaler()
scaler.fit(X_train)  # Fit apenas no train
X_test_scaled = scaler.transform(X_test)  # Transform no test
```

---

#### ERRO 4: Passar dados errados para o pipeline
```python
# ERRADO
y_pred_rf = pipeline_rf.predict(X_test_scaled)

# CERTO
y_pred_rf = pipeline_rf.predict(X_test)  # Dados originais
```
**Por quê:** O pipeline já faz o preprocessamento internamente (se tivesse scaler).

---

### ✅ Código Correto Completo:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, train_test_split
import pandas as pd

# Carregar dados
df = pd.read_csv('titanic.csv')
X = df.drop('survived', axis=1)
y = df['survived']

# Dividir dados
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y  # ✅ Bonus: stratify
)

# ====== SVM (precisa de normalização) ======
pipeline_svm = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', SVC(random_state=42))
])

# Grid Search para SVM
param_grid_svm = {
    'classifier__C': [0.1, 1, 10],              # ✅ Com prefixo
    'classifier__kernel': ['linear', 'rbf'],
    'classifier__gamma': ['scale', 'auto']      # ✅ Bonus: testar gamma
}

grid_svm = GridSearchCV(
    pipeline_svm, 
    param_grid_svm, 
    cv=5,
    scoring='accuracy',
    n_jobs=-1  # ✅ Paralelizar
)
grid_svm.fit(X_train, y_train)

print(f"Melhores hiperparâmetros SVM: {grid_svm.best_params_}")
print(f"SVM CV Score: {grid_svm.best_score_:.3f}")

# ====== Random Forest (NÃO precisa normalização) ======
pipeline_rf = Pipeline([
    ('classifier', RandomForestClassifier(random_state=42))  # ✅ Sem scaler
])

# Grid Search para Random Forest
param_grid_rf = {
    'classifier__n_estimators': [50, 100],
    'classifier__max_depth': [5, 10, None],
    'classifier__min_samples_split': [2, 5, 10]
}

grid_rf = GridSearchCV(
    pipeline_rf,
    param_grid_rf,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)
grid_rf.fit(X_train, y_train)

print(f"Melhores hiperparâmetros RF: {grid_rf.best_params_}")
print(f"RF CV Score: {grid_rf.best_score_:.3f}")

# ====== Avaliação Final ======
svm_test_score = grid_svm.score(X_test, y_test)  # ✅ Pipeline faz tudo
rf_test_score = grid_rf.score(X_test, y_test)    # ✅ Pipeline faz tudo

print(f"\n=== Resultados no Test Set ===")
print(f"SVM Test Accuracy: {svm_test_score:.3f}")
print(f"RF Test Accuracy: {rf_test_score:.3f}")

# Comparação
if svm_test_score > rf_test_score:
    print("\n🏆 Melhor modelo: SVM")
else:
    print("\n🏆 Melhor modelo: Random Forest")
```

### 📊 Checklist de Validação:

| Modelo | Precisa Normalização? | Pipeline Correto |
|--------|-----------------------|------------------|
| Random Forest | ❌ Não | `Pipeline([('classifier', RF())])` |
| XGBoost | ❌ Não | `Pipeline([('classifier', XGB())])` |
| SVM | ✅ Sim | `Pipeline([('scaler', SS()), ('classifier', SVC())])` |
| MLP | ✅ Sim | `Pipeline([('scaler', SS()), ('classifier', MLP())])` |

### 🎯 Conceitos Aplicados:

1. ✅ Pipeline previne data leakage
2. ✅ `classifier__param` para acessar hiperparâmetros
3. ✅ Grid Search otimiza automaticamente
4. ✅ CV valida durante otimização
5. ✅ Test set apenas para avaliação final

</details>

---

## 📊 Parte 3: Diagnóstico de Learning Curves

Analise as 3 curvas abaixo e identifique o problema:

### Modelo A:
```
Train: ████████████████████ 99%
Test:  ████████▒▒▒▒▒▒▒▒▒▒▒ 65%
```

### Modelo B:
```
Train: ████████▒▒▒▒▒▒▒▒▒▒▒ 68%
Test:  ███████▒▒▒▒▒▒▒▒▒▒▒▒ 65%
```

### Modelo C:
```
Train: ████████████████▒▒▒ 87%
Test:  ███████████████▒▒▒▒ 84%
```

**Qual modelo escolher e por quê?**

<details>
<summary>💡 Ver análise completa</summary>

### 📊 Diagnóstico:

#### Modelo A: OVERFITTING SEVERO ❌
```
Train: 99% | Test: 65% | Gap: 34%
```

**Problema:** Modelo decorou os dados de treino  
**Sintomas:** 
- Train muito alta
- Test muito baixa
- Gap enorme (>30%)

**Soluções:**
```python
# 1. Reduzir complexidade
RandomForestClassifier(
    max_depth=5,           # Limitar profundidade
    min_samples_split=50,  # Mais restritivo
    n_estimators=50        # Menos árvores
)

# 2. Regularização
XGBClassifier(
    learning_rate=0.01,    # Menor learning rate
    reg_alpha=1.0,         # L1 regularization
    reg_lambda=1.0         # L2 regularization
)

# 3. Feature Selection
from sklearn.feature_selection import RFE
selector = RFE(model, n_features_to_select=10)
```

---

#### Modelo B: UNDERFITTING ⚠️
```
Train: 68% | Test: 65% | Gap: 3%
```

**Problema:** Modelo muito simples, não aprende padrões  
**Sintomas:**
- Train e Test ambas baixas
- Gap pequeno (bom sinal)
- Performance geral ruim (<70%)

**Soluções:**
```python
# 1. Aumentar complexidade
RandomForestClassifier(
    max_depth=None,        # Sem limite
    n_estimators=200,      # Mais árvores
    min_samples_split=2    # Menos restritivo
)

# 2. Mais features
# - Feature engineering
# - Interaction terms
# - Polynomial features

# 3. Modelo mais poderoso
from xgboost import XGBClassifier
model = XGBClassifier(n_estimators=200, max_depth=6)
```

---

#### Modelo C: IDEAL ✅ 🏆
```
Train: 87% | Test: 84% | Gap: 3%
```

**Análise:**
- ✅ Test accuracy boa (>80%)
- ✅ Gap pequeno (<5%)
- ✅ Generaliza bem
- ✅ Não overfitting nem underfitting

**Por que escolher:**
1. **Generalização:** Test próximo de Train
2. **Performance:** 84% é boa para maioria dos problemas
3. **Estabilidade:** Gap pequeno indica modelo robusto
4. **Confiabilidade:** Funcionará bem em produção

**Quando NÃO escolher:**
- Se o problema exige >90% accuracy
- Se há classes desbalanceadas (olhar outras métricas)

---

### 🎯 Regras de Decisão:

| Train | Test | Gap | Diagnóstico | Ação |
|-------|------|-----|-------------|------|
| >95% | <70% | >25% | **Overfitting severo** | ❌ Regularizar forte |
| >90% | <80% | >10% | **Overfitting** | ⚠️ Regularizar |
| >85% | >80% | <5% | **Ideal** | ✅ Usar! |
| <75% | <75% | <5% | **Underfitting** | ⚠️ Aumentar complexidade |

### 💡 Dica Profissional:

```python
# Visualizar Learning Curves no código
from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt

train_sizes, train_scores, test_scores = learning_curve(
    model, X, y, cv=5, 
    train_sizes=np.linspace(0.1, 1.0, 10),
    scoring='accuracy'
)

plt.plot(train_sizes, train_scores.mean(axis=1), label='Train')
plt.plot(train_sizes, test_scores.mean(axis=1), label='Test')
plt.xlabel('Training Set Size')
plt.ylabel('Accuracy')
plt.legend()
plt.title('Learning Curves')
plt.show()
```

**O que procurar:**
- Curvas convergindo → Bom sinal ✅
- Curvas divergindo → Overfitting ❌
- Ambas baixas → Underfitting ⚠️

</details>

---

## 🎓 Gabarito de Auto-Avaliação - Dia 2

### Pontuação:

- **Parte 1 (Conceitos):** 4 questões × 2.5 pontos = **10 pontos**
- **Parte 2 (Código):** 4 erros × 2.5 pontos = **10 pontos**  
- **Parte 3 (Learning Curves):** 1 questão × 10 pontos = **10 pontos**

**TOTAL:** 30 pontos

---

### 📊 Interpretação da sua nota (Dia 2):

#### 🏆 27-30 pontos: EXCELENTE!
**Você domina Hyperparameter Tuning!**

✅ Entende Grid vs Random Search  
✅ Aplica Cross-Validation corretamente  
✅ Diagnostica overfitting/underfitting  
✅ Usa Pipelines sem data leakage  

**Próximos passos:**
- Avançar para Dia 3 (Dashboard React)
- Aplicar tuning em projeto pessoal

---

#### 💪 20-26 pontos: BOM!
**Você entende os conceitos principais.**

✅ Conceitos gerais claros  
⚠️ Pode ter dúvidas em implementação  

**Próximos passos:**
- Revisar Pipeline e prefixos (`classifier__param`)
- Praticar mais Grid/Random Search
- Pode avançar, mas mantenha material à mão

---

#### 🔄 15-19 pontos: PARCIAL
**Recomendado praticar mais antes de avançar.**

⚠️ Alguns conceitos não estão sólidos  
⚠️ Pode ter dificuldade no Dia 3  

**Próximos passos:**
- Refazer notebook `02-hyperparameter-tuning.ipynb`
- Focar em Pipeline e Cross-Validation
- Ler material lúdico (`14-arvores-decisao-explicacao-ludica.md`)
- Repetir teste em 2-3 dias

---

#### 📚 0-14 pontos: REVISAR
**É importante refazer o Dia 2.**

❌ Conceitos fundamentais precisam de atenção  

**Próximos passos:**
1. **Não desanime!** Hyperparameters são complexos
2. Releia `docs/15-dia2-semana3-hyperparameter-tuning.md`
3. Execute notebook célula por célula
4. Foque em entender O PORQUÊ de cada decisão
5. Retome este teste em 1 semana

---

## 🧩 Teste Bônus: Cenário Real - Otimização Completa

### 💼 Desafio Profissional

Você está otimizando um modelo de detecção de fraude:

**Dataset:**
- 50.000 transações
- 20 features numéricas
- Target: `is_fraud` (desbalanceado: 98% legítimo, 2% fraude)

**Requisitos:**
- Recall mínimo: 85% (não perder fraudes)
- Tempo de inferência: <100ms por predição
- Explicabilidade: Importante (stakeholders não-técnicos)

**Seu plano:**

```markdown
## Escolha do Modelo
Modelo principal: __________
Por quê: __________

Modelo alternativo (backup): __________
Por quê: __________

## Estratégia de Otimização
[ ] Grid Search ou Random Search? __________
[ ] Hiperparâmetros prioritários: __________, __________, __________
[ ] Cross-Validation: K-Fold ou Stratified K-Fold? __________

## Preprocessing
[ ] Normalização necessária? __________
[ ] Feature Selection? __________
[ ] Balanceamento de classes? __________

## Validação
Métrica principal: __________
Por quê: __________
```

<details>
<summary>💡 Ver exemplo de plano profissional</summary>

## ✅ Exemplo de Plano:

### Escolha do Modelo

**Modelo principal: Random Forest**

**Por quê:**
- ✅ Explicabilidade: Feature importance clara
- ✅ Performance: Boa em dados tabulares
- ✅ Velocidade: <100ms factível
- ✅ Lida bem com desbalanceamento (ajustando `class_weight`)

**Modelo alternativo: XGBoost**

**Por quê:**
- ✅ Melhor performance (backup se RF não atingir 85% recall)
- ✅ Feature importance disponível
- ⚠️ Menos interpretável que RF
- ⚠️ Pode ser mais lento

---

### Estratégia de Otimização

**Random Search (n_iter=50)**

**Por quê:**
- 5+ hiperparâmetros para otimizar
- Tempo limitado
- Espaço de busca grande

**Hiperparâmetros prioritários:**

```python
param_distributions = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, None],
    'min_samples_split': [10, 20, 50],
    'min_samples_leaf': [5, 10, 20],
    'class_weight': ['balanced', 'balanced_subsample'],  # CRUCIAL para desbalanceamento
    'max_features': ['sqrt', 'log2', None]
}
```

**Cross-Validation: Stratified K-Fold (k=5)**

**Por quê:**
- Dataset desbalanceado (98/2)
- Garante 2% fraude em cada fold
- Validação mais confiável

---

### Preprocessing

**Normalização: NÃO**
- Random Forest não precisa
- Se usar XGBoost: também não precisa

**Feature Selection: SIM (se performance permitir)**
```python
from sklearn.feature_selection import SelectKBest, f_classif
selector = SelectKBest(f_classif, k=15)  # Reduzir de 20 para 15
```
**Por quê:**
- Melhora velocidade de inferência
- Reduz ruído
- Aumenta explicabilidade

**Balanceamento: SIM**
```python
RandomForestClassifier(
    class_weight='balanced',  # Penaliza erro em classe minoritária
    ...
)

# OU SMOTE (se necessário)
from imblearn.over_sampling import SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)
```

---

### Validação

**Métrica principal: RECALL (classe fraude)**

**Por quê:**
- Requisito: 85% recall mínimo
- Detecção de fraude: **Falso Negativo é MUITO pior** que Falso Positivo
- Melhor perder 10 transações legítimas (FP) que deixar passar 1 fraude (FN)

**Métricas secundárias:**
- **Precision:** Evitar muitos falsos alarmes
- **F1-Score:** Balancear recall e precision
- **ROC-AUC:** Separação geral das classes

**Pipeline completo:**

```python
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV, StratifiedKFold

# Pipeline
pipeline = Pipeline([
    ('selector', SelectKBest(f_classif, k=15)),
    ('classifier', RandomForestClassifier(random_state=42, n_jobs=-1))
])

# Parâmetros
param_distributions = {
    'selector__k': [10, 15, 20],
    'classifier__n_estimators': [100, 200, 300],
    'classifier__max_depth': [10, 20, None],
    'classifier__min_samples_split': [10, 20, 50],
    'classifier__class_weight': ['balanced', 'balanced_subsample']
}

# Stratified K-Fold
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Random Search
random_search = RandomizedSearchCV(
    pipeline,
    param_distributions,
    n_iter=50,
    cv=cv,
    scoring='recall',  # MÉTRICA PRINCIPAL
    n_jobs=-1,
    random_state=42,
    verbose=2
)

# Treinar
random_search.fit(X_train, y_train)

# Melhor modelo
best_model = random_search.best_estimator_

# Avaliar no test
from sklearn.metrics import classification_report, recall_score

y_pred = best_model.predict(X_test)
recall = recall_score(y_test, y_pred, pos_label=1)  # Classe fraude

print(f"Recall (fraude): {recall:.3f}")
print(classification_report(y_test, y_pred))

# Validar requisito
if recall >= 0.85:
    print("✅ Requisito de recall atingido!")
else:
    print(f"❌ Recall abaixo do mínimo. Falta: {0.85 - recall:.3f}")
```

---

### 🎯 Decisão Final

**SE recall < 85%:**
1. Ajustar threshold de decisão
```python
# Reduzir threshold para aumentar recall
y_proba = best_model.predict_proba(X_test)[:, 1]
y_pred_adjusted = (y_proba > 0.3).astype(int)  # Em vez de 0.5
```

2. Tentar XGBoost (modelo alternativo)

3. Aplicar SMOTE (oversampling)

**SE recall >= 85%:**
✅ Modelo pronto para produção!

---

### 📊 Entregáveis

1. Modelo salvo (`fraud_detector.pkl`)
2. Pipeline de preprocessamento
3. Relatório de performance
4. Feature importance (top 10)
5. Documentação para stakeholders

</details>

---

## 💬 Mensagem Final - Dia 2

> **"Eu entendi, mas não faço sozinho sem consultar"**  
> **Isso é NORMAL e ESPERADO!** 👍

Profissionais consultam:
- Documentação do Scikit-learn
- Stack Overflow
- Notebooks anteriores
- Papers acadêmicos

**A diferença é:** eles sabem **o que procurar** e **como aplicar**.

Se você chegou até aqui, executou tudo, e entende os conceitos quando lê as explicações, **você está no caminho certo!** 🎯

---

**Sucesso na sua jornada! 🚀**

_Este teste pode ser refeito quantas vezes quiser. Use-o como ferramenta de aprendizado, não como prova!_
