# 📊 Machine Learning Cheatsheet - Python & Scikit-learn

**Guia Rápido de Referência | 4 Páginas para Impressão**

---

## 📦 PÁGINA 1: IMPORTAÇÕES E CARREGAMENTO DE DADOS

### 🔧 Imports Essenciais

```python
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1. MANIPULAÇÃO DE DADOS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
import pandas as pd                # DataFrames e análise
import numpy as np                 # Arrays e matemática

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2. VISUALIZAÇÃO
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
import matplotlib.pyplot as plt    # Gráficos básicos
import seaborn as sns              # Gráficos estatísticos

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 3. PRÉ-PROCESSAMENTO
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
from sklearn.model_selection import train_test_split  # Dividir dados
from sklearn.preprocessing import StandardScaler      # Normalizar
from sklearn.preprocessing import OneHotEncoder       # Encoding

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 4. MODELOS DE CLASSIFICAÇÃO
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
from sklearn.tree import DecisionTreeClassifier       # Árvore
from sklearn.ensemble import RandomForestClassifier   # Random Forest
from sklearn.svm import SVC                           # SVM
from sklearn.neural_network import MLPClassifier      # Neural Network
from xgboost import XGBClassifier                     # XGBoost

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 5. MÉTRICAS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
from sklearn.metrics import (
    accuracy_score,           # Acurácia
    precision_score,          # Precisão
    recall_score,             # Recall
    f1_score,                 # F1-Score
    confusion_matrix,         # Matriz de Confusão
    classification_report,    # Relatório completo
    roc_auc_score,           # ROC-AUC
    roc_curve                # Curva ROC
)
```

---

### 📂 Carregamento de Dados

```python
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CARREGAR CSV
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
df = pd.read_csv('dataset.csv')

# Opções úteis:
df = pd.read_csv('dataset.csv', 
                 encoding='utf-8',      # Encoding
                 sep=',',               # Separador
                 index_col=0)           # Coluna como índice

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXPLORAÇÃO RÁPIDA
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
df.head()                    # Primeiras 5 linhas
df.tail()                    # Últimas 5 linhas
df.shape                     # (linhas, colunas)
df.info()                    # Tipos e memória
df.describe()                # Estatísticas numéricas
df.columns                   # Nomes das colunas
df.dtypes                    # Tipos de cada coluna
df.isnull().sum()           # Valores faltantes por coluna
df['coluna'].value_counts() # Contagem de valores únicos
```

---

### 🔍 EDA - Análise Exploratória

```python
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CORRELAÇÃO
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
correlation = df.corr()

# Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0)
plt.title('Matriz de Correlação')
plt.show()

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# DISTRIBUIÇÕES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
df['coluna'].hist(bins=30)                    # Histograma
df['coluna'].plot(kind='box')                 # Boxplot
sns.countplot(x='coluna', data=df)           # Contagem

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# RELAÇÕES ENTRE VARIÁVEIS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
sns.scatterplot(x='col1', y='col2', hue='target', data=df)
sns.pairplot(df, hue='target')               # Múltiplas relações
```

---

## 🧹 PÁGINA 2: PRÉ-PROCESSAMENTO

### 🔄 Tratamento de Dados Faltantes

```python
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# IDENTIFICAR
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
df.isnull().sum()                    # Quantidade por coluna
df.isnull().sum() / len(df) * 100   # Porcentagem

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# REMOVER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
df.dropna(inplace=True)              # Remove linhas com NaN
df.dropna(subset=['col'], inplace=True)  # Remove NaN de coluna específica
df.drop('coluna', axis=1, inplace=True)  # Remove coluna inteira

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PREENCHER (IMPUTAÇÃO)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
df['col'].fillna(df['col'].mean(), inplace=True)     # Média
df['col'].fillna(df['col'].median(), inplace=True)   # Mediana
df['col'].fillna(0, inplace=True)                    # Valor fixo
df['col'].fillna(method='ffill', inplace=True)       # Forward fill

# Por grupo
df['age'] = df.groupby('sex')['age'].transform(
    lambda x: x.fillna(x.median())
)
```

---

### 🏷️ Encoding de Variáveis Categóricas

```python
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ONE-HOT ENCODING (variáveis nominais)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Exemplo: sex = ['male', 'female']
df = pd.get_dummies(df, columns=['sex', 'embarked'], drop_first=True)

# Resultado: sex_male (0/1), embarked_Q (0/1), embarked_S (0/1)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# LABEL ENCODING (variáveis ordinais)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Exemplo: size = ['Small', 'Medium', 'Large'] (tem ordem!)
size_map = {'Small': 1, 'Medium': 2, 'Large': 3}
df['size_encoded'] = df['size'].map(size_map)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# BINARY ENCODING (2 valores)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
df['sex_binary'] = df['sex'].map({'male': 0, 'female': 1})
# Ou:
df['sex_binary'] = (df['sex'] == 'female').astype(int)
```

---

### ⚖️ Separação Features e Target

```python
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MÉTODO 1: Drop
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
X = df.drop('target', axis=1)       # Features (tudo exceto target)
y = df['target']                    # Target

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MÉTODO 2: Selecionar colunas
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
X = df[['age', 'fare', 'pclass', 'sex_male']]
y = df['survived']

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TRAIN/TEST SPLIT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2,           # 20% para teste
    random_state=42,         # Reprodutibilidade
    stratify=y               # Mantém proporção das classes
)

print(f"Train: {X_train.shape}, Test: {X_test.shape}")
```

---

### 📏 Normalização (StandardScaler)

```python
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# QUANDO USAR:
# - SVM (sensível à escala)
# - Neural Networks (sensível à escala)
# - K-Means, KNN (baseados em distância)
#
# NÃO PRECISA:
# - Random Forest, Decision Tree (baseados em thresholds)
# - XGBoost, LightGBM (baseados em árvores)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

scaler = StandardScaler()

# ⚠️ REGRA DE OURO:
# fit_transform no TRAIN
# transform no TEST
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Transforma em DataFrame (opcional)
X_train_scaled = pd.DataFrame(
    X_train_scaled, 
    columns=X_train.columns,
    index=X_train.index
)
```

---

## 🤖 PÁGINA 3: TREINAMENTO DE MODELOS

### 🌳 Decision Tree

```python
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CRIAR E TREINAR
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
dt_model = DecisionTreeClassifier(
    max_depth=5,              # Limita profundidade (evita overfitting)
    min_samples_split=20,     # Mínimo de amostras para dividir
    random_state=42
)

dt_model.fit(X_train, y_train)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PREVER E AVALIAR
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
y_pred = dt_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia: {accuracy:.2%}")
```

---

### 🌲 Random Forest

```python
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CRIAR E TREINAR
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
rf_model = RandomForestClassifier(
    n_estimators=100,         # Número de árvores
    max_depth=10,             # Profundidade máxima
    min_samples_split=10,     # Mínimo para dividir
    random_state=42,
    n_jobs=-1                 # Usa todos os cores
)

rf_model.fit(X_train, y_train)
y_pred = rf_model.predict(X_test)
y_proba = rf_model.predict_proba(X_test)[:, 1]  # Probabilidades

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# FEATURE IMPORTANCE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
feature_imp = pd.DataFrame({
    'feature': X_train.columns,
    'importance': rf_model.feature_importances_
}).sort_values('importance', ascending=False)

print(feature_imp)
```

---

### ⚡ XGBoost

```python
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CRIAR E TREINAR
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
xgb_model = XGBClassifier(
    n_estimators=100,
    max_depth=5,
    learning_rate=0.1,        # Taxa de aprendizado
    random_state=42,
    eval_metric='logloss'     # Métrica de avaliação
)

xgb_model.fit(X_train, y_train)
y_pred = xgb_model.predict(X_test)
y_proba = xgb_model.predict_proba(X_test)[:, 1]
```

---

### 🎯 SVM (Support Vector Machine)

```python
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⚠️ REQUER NORMALIZAÇÃO!
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
svm_model = SVC(
    kernel='rbf',             # 'linear', 'poly', 'rbf'
    C=1.0,                    # Regularização
    probability=True,         # Habilita predict_proba
    random_state=42
)

svm_model.fit(X_train_scaled, y_train)
y_pred = svm_model.predict(X_test_scaled)
y_proba = svm_model.predict_proba(X_test_scaled)[:, 1]
```

---

### 🧠 Neural Network (MLP)

```python
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⚠️ REQUER NORMALIZAÇÃO!
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
mlp_model = MLPClassifier(
    hidden_layer_sizes=(100, 50, 25),  # 3 camadas ocultas
    activation='relu',                  # 'relu', 'tanh', 'logistic'
    solver='adam',                      # 'adam', 'sgd', 'lbfgs'
    max_iter=500,                       # Iterações máximas
    random_state=42,
    early_stopping=True,                # Para quando não melhora
    validation_fraction=0.1             # 10% para validação
)

mlp_model.fit(X_train_scaled, y_train)
y_pred = mlp_model.predict(X_test_scaled)
y_proba = mlp_model.predict_proba(X_test_scaled)[:, 1]
```

---

## 📊 PÁGINA 4: AVALIAÇÃO E VISUALIZAÇÃO

### 📈 Métricas de Classificação

```python
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MÉTRICAS BÁSICAS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
from sklearn.metrics import *

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1-Score:  {f1:.4f}")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# RELATÓRIO COMPLETO
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print(classification_report(y_test, y_pred))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CROSS-VALIDATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
from sklearn.model_selection import cross_val_score

cv_scores = cross_val_score(model, X_train, y_train, cv=5)
print(f"CV Scores: {cv_scores}")
print(f"CV Mean: {cv_scores.mean():.4f} ± {cv_scores.std():.4f}")
```

---

### 🎨 Matriz de Confusão

```python
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CALCULAR
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
cm = confusion_matrix(y_test, y_pred)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# VISUALIZAR
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Neg', 'Pos'],
            yticklabels=['Neg', 'Pos'])
plt.xlabel('Predito')
plt.ylabel('Real')
plt.title('Matriz de Confusão')
plt.show()

# Interpretação:
#           Predito
#        |  0  |  1  |
# Real 0 | TN  | FP  |  ← Verdadeiros Negativos | Falsos Positivos
#      1 | FN  | TP  |  ← Falsos Negativos | Verdadeiros Positivos
```

---

### 📉 Curva ROC

```python
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CALCULAR ROC-AUC
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
from sklearn.metrics import roc_curve, roc_auc_score

# Probabilidades necessárias!
y_proba = model.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_proba)
auc = roc_auc_score(y_test, y_proba)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PLOTAR
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label=f'ROC (AUC = {auc:.3f})', linewidth=2)
plt.plot([0, 1], [0, 1], 'k--', label='Random')  # Linha de referência
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Curva ROC')
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

---

### 📊 Feature Importance (Random Forest/XGBoost)

```python
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXTRAIR IMPORTÂNCIAS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
feature_imp = pd.DataFrame({
    'feature': X_train.columns,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PLOTAR (Top 10)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
plt.figure(figsize=(10, 6))
plt.barh(feature_imp['feature'][:10], 
         feature_imp['importance'][:10])
plt.xlabel('Importância')
plt.title('Top 10 Features Mais Importantes')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
```

---

### 🔄 Comparação de Múltiplos Modelos

```python
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TREINAR VÁRIOS MODELOS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
models = {
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'Random Forest': RandomForestClassifier(random_state=42),
    'XGBoost': XGBClassifier(random_state=42, eval_metric='logloss'),
    'SVM': SVC(random_state=42),
    'MLP': MLPClassifier(random_state=42, max_iter=500)
}

results = []

for name, model in models.items():
    # Treinar (usar scaled para SVM e MLP)
    if name in ['SVM', 'MLP']:
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
    else:
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
    
    # Métricas
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    results.append({
        'Model': name,
        'Accuracy': acc,
        'Precision': prec,
        'Recall': rec,
        'F1-Score': f1
    })

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# DATAFRAME DE RESULTADOS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Accuracy', ascending=False)
print(results_df.to_string(index=False))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PLOTAR COMPARAÇÃO
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
results_df.set_index('Model')[['Accuracy', 'Precision', 
                                 'Recall', 'F1-Score']].plot(kind='bar', 
                                                              figsize=(12, 6))
plt.title('Comparação de Modelos')
plt.ylabel('Score')
plt.xlabel('Modelo')
plt.xticks(rotation=45)
plt.legend(loc='lower right')
plt.ylim(0, 1)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
```

---

### 💾 Salvar e Carregar Modelos

```python
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SALVAR
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
import joblib

joblib.dump(model, 'modelo_treinado.pkl')
joblib.dump(scaler, 'scaler.pkl')

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CARREGAR
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
model_loaded = joblib.load('modelo_treinado.pkl')
scaler_loaded = joblib.load('scaler.pkl')

# Usar
X_new_scaled = scaler_loaded.transform(X_new)
predictions = model_loaded.predict(X_new_scaled)
```

---

## 🎯 DICAS RÁPIDAS

### ✅ Checklist de Workflow ML

```
1. [ ] Carregar dados (read_csv)
2. [ ] EDA (describe, info, correlação)
3. [ ] Tratar valores faltantes (fillna ou dropna)
4. [ ] Encoding de categóricas (get_dummies)
5. [ ] Separar X e y
6. [ ] Train/Test Split (80-20)
7. [ ] Normalizar SE necessário (StandardScaler)
8. [ ] Treinar modelo (fit)
9. [ ] Fazer previsões (predict)
10. [ ] Avaliar (accuracy, confusion_matrix, etc.)
11. [ ] Comparar modelos
12. [ ] Salvar melhor modelo (joblib)
```

---

### ⚠️ Erros Comuns para Evitar

```python
# ❌ ERRO 1: fit_transform no test
X_test_scaled = scaler.fit_transform(X_test)  # ERRADO!

# ✅ CERTO:
X_test_scaled = scaler.transform(X_test)


# ❌ ERRO 2: Usar dados scaled em modelos de árvore
rf_model.fit(X_train_scaled, y_train)  # Desnecessário!

# ✅ CERTO:
rf_model.fit(X_train, y_train)  # Random Forest não precisa


# ❌ ERRO 3: Esquecer random_state
model = RandomForestClassifier()  # Resultados variam!

# ✅ CERTO:
model = RandomForestClassifier(random_state=42)


# ❌ ERRO 4: Misturar train e test
model.fit(X, y)  # Treinou com tudo!
score = model.score(X, y)  # Testou com tudo = enviesado

# ✅ CERTO:
model.fit(X_train, y_train)
score = model.score(X_test, y_test)
```

---

### 📚 Quando Usar Cada Modelo

| Modelo | Quando Usar | Vantagens | Desvantagens |
|--------|-------------|-----------|--------------|
| **Decision Tree** | Baseline rápido | Interpretável, rápido | Overfit fácil |
| **Random Forest** | Dados tabulares gerais | Robusto, boa acurácia | Lento, menos interpretável |
| **XGBoost** | Competições, máxima performance | Melhor acurácia, rápido | Complexo, muitos hiperparâmetros |
| **SVM** | Dados com boa separação | Eficaz em alta dimensão | Lento, requer normalização |
| **MLP** | Padrões complexos | Aprende relações não-lineares | Caixa-preta, requer normalização |

---

### 🎨 Configuração de Plots (Opcional)

```python
# Configurar estilo global
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Aumentar tamanho padrão de fontes
plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['figure.figsize'] = (10, 6)
```

---

**📄 FIM DO CHEATSHEET | Salve e imprima para consulta rápida! 🚀**

_Criado para: Aprendizado IA 2025 - Semana 3_
