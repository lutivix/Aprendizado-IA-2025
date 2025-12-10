# 🔧 Feature Engineering na Prática

**Semana 4 - Dia 2**  
**Objetivo:** Dominar técnicas de transformação de dados e criação de features  
**Data:** 10 Dez 2025

---

## 📋 Índice

1. [O que é Feature Engineering?](#o-que-é-feature-engineering)
2. [Por que Feature Engineering Importa?](#por-que-feature-engineering-importa)
3. [Tipos de Features](#tipos-de-features)
4. [Técnicas de Feature Engineering](#técnicas-de-feature-engineering)
5. [Transformações Numéricas](#transformações-numéricas)
6. [Transformações Categóricas](#transformações-categóricas)
7. [Feature Creation](#feature-creation)
8. [Feature Selection](#feature-selection)
9. [Boas Práticas](#boas-práticas)
10. [Armadilhas Comuns](#armadilhas-comuns)
11. [Casos Práticos](#casos-práticos)
12. [Checklist de Feature Engineering](#checklist-de-feature-engineering)

---

## 🎯 O que é Feature Engineering?

**Feature Engineering** é o processo de usar o conhecimento de domínio para criar, transformar ou selecionar variáveis (features) que tornam os algoritmos de ML mais eficazes.

### 📊 Analogia

Imagine que você está preparando ingredientes para uma receita:
- **Dados brutos** = ingredientes na feira
- **Feature Engineering** = lavar, descascar, picar, temperar
- **Modelo ML** = cozinhar
- **Resultado** = prato final

> "Features melhores > Algoritmos melhores"
> 
> – Andrew Ng

### 🔍 Exemplo Prático

**Dado bruto:**
```
data_compra = "2025-12-10 14:30:00"
```

**Features criadas:**
```
ano = 2025
mes = 12
dia_semana = "terça"
hora = 14
periodo = "tarde"
fim_semana = False
fim_mes = True
```

---

## 💡 Por que Feature Engineering Importa?

### 📈 Impacto Real

| Aspecto | Sem FE | Com FE | Melhoria |
|---------|--------|--------|----------|
| **Accuracy** | 75% | 89% | +14% |
| **Training Time** | 10 min | 3 min | -70% |
| **Interpretabilidade** | Baixa | Alta | +++++ |
| **Generalização** | Regular | Boa | +++++ |

### 🎯 Benefícios

1. **Performance:** Modelos mais precisos
2. **Velocidade:** Treinamento mais rápido
3. **Interpretabilidade:** Features mais claras
4. **Generalização:** Melhor em dados novos
5. **Simplicidade:** Modelos mais simples funcionam melhor

---

## 🏷️ Tipos de Features

### 1️⃣ Features Numéricas

**Contínuas:**
- Valores em escala contínua
- Exemplo: peso, altura, temperatura, preço

**Discretas:**
- Valores inteiros
- Exemplo: idade, número de filhos, quantidade de produtos

### 2️⃣ Features Categóricas

**Nominais:**
- Sem ordem natural
- Exemplo: cor, cidade, categoria de produto

**Ordinais:**
- Com ordem natural
- Exemplo: tamanho (P, M, G), nível de escolaridade

### 3️⃣ Features Temporais

- Datas e horários
- Exemplo: data_compra, timestamp

### 4️⃣ Features de Texto

- Texto livre
- Exemplo: comentários, descrições, reviews

### 5️⃣ Features Booleanas

- Verdadeiro/Falso
- Exemplo: é_cliente_vip, aceita_marketing

---

## 🛠️ Técnicas de Feature Engineering

### 📊 Visão Geral

```
┌─────────────────────────────────────┐
│     Feature Engineering             │
├─────────────────────────────────────┤
│                                     │
│  1. Transformações Numéricas        │
│     - Scaling/Normalization         │
│     - Log Transform                 │
│     - Binning                       │
│                                     │
│  2. Transformações Categóricas      │
│     - One-Hot Encoding              │
│     - Label Encoding                │
│     - Target Encoding               │
│                                     │
│  3. Feature Creation                │
│     - Combinações                   │
│     - Aggregações                   │
│     - Features de Tempo             │
│                                     │
│  4. Feature Selection               │
│     - Correlação                    │
│     - Feature Importance            │
│     - Recursive Feature Elimination │
│                                     │
└─────────────────────────────────────┘
```

---

## 📐 Transformações Numéricas

### 1️⃣ Scaling e Normalização

#### **StandardScaler (Z-score)**

Transforma para média 0 e desvio padrão 1.

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Fórmula: z = (x - μ) / σ
```

**Quando usar:**
- ✅ Features com distribuição normal
- ✅ Algoritmos sensíveis a escala (SVM, KNN, Redes Neurais)
- ❌ Árvores de decisão (não precisam)

**Exemplo:**
```
Original: [100, 200, 150, 180]
Scaled:   [-1.5, 1.1, -0.2, 0.6]
```

---

#### **MinMaxScaler**

Transforma para range [0, 1].

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Fórmula: x_scaled = (x - min) / (max - min)
```

**Quando usar:**
- ✅ Quando precisa range específico [0, 1]
- ✅ Redes Neurais com ativação sigmoid/tanh
- ✅ Algoritmos de distância (KNN)

**Exemplo:**
```
Original: [10, 20, 15, 18]
MinMax:   [0.0, 1.0, 0.5, 0.8]
```

---

#### **RobustScaler**

Usa mediana e IQR, resistente a outliers.

```python
from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()
X_scaled = scaler.fit_transform(X)

# Fórmula: x_scaled = (x - median) / IQR
```

**Quando usar:**
- ✅ Dados com muitos outliers
- ✅ Distribuições não-normais
- ✅ Dados com valores extremos

---

### 2️⃣ Transformações de Distribuição

#### **Log Transform**

Reduz skewness (assimetria).

```python
import numpy as np

# Log natural
X_log = np.log1p(X)  # log(1 + x) - evita log(0)

# Log base 10
X_log10 = np.log10(X + 1)
```

**Quando usar:**
- ✅ Distribuição muito assimétrica (positiva)
- ✅ Valores em escala exponencial (salários, preços)
- ✅ Variância cresce com média

**Exemplo:**
```
Original: [1, 10, 100, 1000, 10000]
Log:      [0, 1,  2,   3,    4]
```

---

#### **Box-Cox Transform**

Transformação paramétrica que encontra melhor lambda.

```python
from scipy.stats import boxcox

X_boxcox, lambda_param = boxcox(X)
```

**Quando usar:**
- ✅ Quando quer normalizar distribuição
- ✅ Dados só positivos
- ✅ Otimizar transformação automaticamente

---

#### **Yeo-Johnson Transform**

Similar a Box-Cox, mas aceita valores negativos.

```python
from sklearn.preprocessing import PowerTransformer

pt = PowerTransformer(method='yeo-johnson')
X_transformed = pt.fit_transform(X)
```

**Quando usar:**
- ✅ Box-Cox mas com valores negativos
- ✅ Normalizar distribuição geral

---

### 3️⃣ Binning (Discretização)

Transforma features contínuas em categóricas.

```python
import pandas as pd

# Binning com intervalos iguais
pd.cut(df['idade'], bins=5, labels=['Muito Jovem', 'Jovem', 'Adulto', 'Maduro', 'Idoso'])

# Binning com quantis (mesma quantidade em cada bin)
pd.qcut(df['salario'], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])

# Binning manual
bins = [0, 18, 30, 50, 100]
labels = ['Menor', 'Jovem', 'Adulto', 'Senior']
pd.cut(df['idade'], bins=bins, labels=labels)
```

**Quando usar:**
- ✅ Capturar relações não-lineares
- ✅ Reduzir impacto de outliers
- ✅ Criar regras de negócio claras

**Exemplo:**
```
Original: [5000, 8000, 12000, 25000, 45000]
Binned:   ['Baixo', 'Baixo', 'Médio', 'Alto', 'Muito Alto']
```

---

## 🏷️ Transformações Categóricas

### 1️⃣ One-Hot Encoding

Cria coluna binária para cada categoria.

```python
import pandas as pd

# Com Pandas
df_encoded = pd.get_dummies(df, columns=['cor', 'tamanho'])

# Com Scikit-learn
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(sparse=False, drop='first')  # drop='first' evita multicolinearidade
X_encoded = encoder.fit_transform(X[['cor', 'tamanho']])
```

**Quando usar:**
- ✅ Features categóricas nominais (sem ordem)
- ✅ Poucas categorias (< 10-15)
- ✅ Todos os algoritmos ML

**Exemplo:**
```
Original:
  cor
  vermelho
  azul
  verde

One-Hot:
  cor_azul  cor_verde  cor_vermelho
     0         0          1
     1         0          0
     0         1          0
```

**⚠️ Cuidado:**
- Muitas categorias → muitas colunas (curse of dimensionality)
- Use `drop='first'` para evitar multicolinearidade

---

### 2️⃣ Label Encoding

Atribui número inteiro a cada categoria.

```python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['tamanho_encoded'] = le.fit_transform(df['tamanho'])
```

**Quando usar:**
- ✅ Features ordinais (com ordem natural)
- ✅ Target variable (y)
- ✅ Árvores de decisão
- ❌ Regressão Linear (cria ordem artificial)

**Exemplo:**
```
Original: ['P', 'M', 'G', 'M', 'P']
Encoded:  [0, 1, 2, 1, 0]
```

---

### 3️⃣ Ordinal Encoding

Similar a Label, mas você define a ordem.

```python
from sklearn.preprocessing import OrdinalEncoder

categories = [['P', 'M', 'G', 'GG']]
encoder = OrdinalEncoder(categories=categories)
df['tamanho_ord'] = encoder.fit_transform(df[['tamanho']])
```

**Quando usar:**
- ✅ Ordem é importante para o modelo
- ✅ Você conhece a ordem lógica

---

### 4️⃣ Target Encoding (Mean Encoding)

Substitui categoria pela média do target.

```python
# Manual
target_mean = df.groupby('categoria')['target'].mean()
df['categoria_encoded'] = df['categoria'].map(target_mean)

# Com category_encoders
from category_encoders import TargetEncoder

te = TargetEncoder()
df['categoria_encoded'] = te.fit_transform(df['categoria'], df['target'])
```

**Quando usar:**
- ✅ Muitas categorias (> 15)
- ✅ Forte relação entre categoria e target
- ⚠️ Cuidado com overfitting!

**Exemplo:**
```
categoria  |  target  →  categoria_encoded
-----------+---------     -----------------
A          |    1              0.8
A          |    0              0.8
B          |    1              0.5
B          |    0              0.5
C          |    0              0.3
```

---

### 5️⃣ Frequency Encoding

Substitui pela frequência da categoria.

```python
freq = df['categoria'].value_counts(normalize=True)
df['categoria_freq'] = df['categoria'].map(freq)
```

**Quando usar:**
- ✅ Frequência é informativa
- ✅ Reduzir dimensionalidade

---

## 🎨 Feature Creation

### 1️⃣ Combinações de Features

#### **Operações Matemáticas**

```python
# Criar novas features combinando existentes
df['preco_por_m2'] = df['preco'] / df['area']
df['imc'] = df['peso'] / (df['altura'] ** 2)
df['razao_receita_despesa'] = df['receita'] / df['despesa']
df['lucro'] = df['receita'] - df['custo']
```

#### **Interações Polinomiais**

```python
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

# Cria: x1, x2, x1², x1*x2, x2²
```

**Quando usar:**
- ✅ Capturar relações não-lineares
- ✅ Regressão Polinomial
- ⚠️ Aumenta muito a dimensionalidade

---

### 2️⃣ Features de Tempo

```python
import pandas as pd

# Converter para datetime
df['data'] = pd.to_datetime(df['data'])

# Extrair componentes
df['ano'] = df['data'].dt.year
df['mes'] = df['data'].dt.month
df['dia'] = df['data'].dt.day
df['dia_semana'] = df['data'].dt.dayofweek  # 0=Segunda, 6=Domingo
df['hora'] = df['data'].dt.hour
df['minuto'] = df['data'].dt.minute

# Features derivadas
df['trimestre'] = df['data'].dt.quarter
df['dia_do_ano'] = df['data'].dt.dayofyear
df['semana_do_ano'] = df['data'].dt.isocalendar().week
df['fim_semana'] = df['dia_semana'].isin([5, 6]).astype(int)
df['fim_mes'] = df['data'].dt.is_month_end.astype(int)

# Períodos do dia
df['periodo'] = pd.cut(df['hora'], 
                       bins=[0, 6, 12, 18, 24], 
                       labels=['Madrugada', 'Manhã', 'Tarde', 'Noite'])

# Diferenças temporais
df['dias_desde_primeira_compra'] = (df['data'] - df['data'].min()).dt.days
df['meses_cliente'] = ((df['data'] - df['data_cadastro']).dt.days / 30).astype(int)
```

---

### 3️⃣ Features de Agregação

```python
# Estatísticas por grupo
df_agg = df.groupby('cliente_id').agg({
    'valor_compra': ['mean', 'sum', 'std', 'min', 'max', 'count'],
    'desconto': 'mean',
    'data': ['min', 'max']
}).reset_index()

# Renomear colunas
df_agg.columns = ['cliente_id', 'ticket_medio', 'valor_total', 
                  'std_compras', 'min_compra', 'max_compra', 'num_compras',
                  'desconto_medio', 'primeira_compra', 'ultima_compra']

# Features derivadas
df_agg['frequencia_compra'] = (
    (df_agg['ultima_compra'] - df_agg['primeira_compra']).dt.days / df_agg['num_compras']
)
```

---

### 4️⃣ Features de Texto

```python
# Features básicas de texto
df['len_descricao'] = df['descricao'].str.len()
df['num_palavras'] = df['descricao'].str.split().str.len()
df['num_caracteres_maiusculos'] = df['descricao'].str.count(r'[A-Z]')
df['tem_numero'] = df['descricao'].str.contains(r'\d').astype(int)

# TF-IDF para análise mais avançada
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(max_features=100)
X_tfidf = tfidf.fit_transform(df['descricao'])
```

---

### 5️⃣ Features Geográficas

```python
import numpy as np

# Distância entre dois pontos (Haversine)
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Raio da Terra em km
    
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    
    return R * c

df['distancia_centro'] = haversine(
    df['lat'], df['lon'], 
    -23.550520, -46.633308  # Coordenadas do centro (exemplo: São Paulo)
)

# Região geográfica
df['regiao'] = pd.cut(df['lat'], bins=5, labels=['Norte', 'Nordeste', 'Centro', 'Sudeste', 'Sul'])
```

---

## 🎯 Feature Selection

### 1️⃣ Correlação

Remove features altamente correlacionadas.

```python
import pandas as pd
import numpy as np

# Matriz de correlação
corr_matrix = df.corr()

# Encontrar pares com correlação > 0.9
high_corr = []
for i in range(len(corr_matrix.columns)):
    for j in range(i):
        if abs(corr_matrix.iloc[i, j]) > 0.9:
            colname = corr_matrix.columns[i]
            high_corr.append(colname)

# Remover features correlacionadas
df_reduced = df.drop(columns=high_corr)
```

---

### 2️⃣ Feature Importance

```python
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Treinar modelo
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Feature importance
importances = pd.DataFrame({
    'feature': X_train.columns,
    'importance': rf.feature_importances_
}).sort_values('importance', ascending=False)

# Selecionar top features
top_features = importances.head(10)['feature'].tolist()
X_selected = X[top_features]
```

---

### 3️⃣ Recursive Feature Elimination (RFE)

```python
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier

# Selecionar 10 melhores features
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rfe = RFE(estimator=rf, n_features_to_select=10)
rfe.fit(X_train, y_train)

# Features selecionadas
selected_features = X_train.columns[rfe.support_].tolist()
X_selected = X_train[selected_features]
```

---

### 4️⃣ SelectKBest

```python
from sklearn.feature_selection import SelectKBest, f_classif

# Selecionar k melhores features baseado em ANOVA F-value
selector = SelectKBest(score_func=f_classif, k=10)
X_selected = selector.fit_transform(X_train, y_train)

# Nomes das features selecionadas
selected_features = X_train.columns[selector.get_support()].tolist()
```

---

## ✅ Boas Práticas

### 1️⃣ Sempre Separe Train/Test ANTES

```python
from sklearn.model_selection import train_test_split

# CERTO: Separar primeiro
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit scaler apenas no train
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # Usa parâmetros do train!

# ERRADO: Fit em todo dataset
scaler.fit(X)  # ❌ Data leakage!
```

---

### 2️⃣ Use Pipelines

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Pipeline automático
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier())
])

# Fit e predict automático
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
```

---

### 3️⃣ ColumnTransformer para Features Mistas

```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Separar colunas por tipo
numeric_features = ['idade', 'salario', 'experiencia']
categorical_features = ['cidade', 'nivel_educacao']

# Transformador
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(drop='first'), categorical_features)
    ])

# Pipeline completo
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier())
])

pipeline.fit(X_train, y_train)
```

---

### 4️⃣ Validação Cruzada com Feature Engineering

```python
from sklearn.model_selection import cross_val_score

# CV com pipeline completo
scores = cross_val_score(pipeline, X_train, y_train, cv=5, scoring='accuracy')
print(f"CV Accuracy: {scores.mean():.3f} (+/- {scores.std():.3f})")
```

---

### 5️⃣ Documente suas Features

```python
# Criar dicionário de features
feature_dict = {
    'preco_por_m2': 'Preço dividido pela área em m²',
    'dias_desde_compra': 'Dias desde a última compra',
    'ticket_medio': 'Valor médio das compras do cliente',
    'fim_semana': '1 se sábado/domingo, 0 caso contrário'
}

# Salvar metadados
import json
with open('features_metadata.json', 'w') as f:
    json.dump(feature_dict, f, indent=2)
```

---

## ⚠️ Armadilhas Comuns

### 1️⃣ Data Leakage

**Problema:** Informação do futuro "vaza" para o passado.

```python
# ❌ ERRADO: Usar informação do teste no treino
scaler.fit(X)  # Fit em todo dataset
X_scaled = scaler.transform(X)
X_train, X_test = train_test_split(X_scaled, ...)

# ✅ CERTO: Fit apenas no treino
X_train, X_test = train_test_split(X, ...)
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

---

### 2️⃣ Target Leakage

**Problema:** Feature contém informação sobre o target.

```python
# ❌ ERRADO: Feature que só existe quando y=1
df['fraude_confirmada']  # Só existe após investigação (target)

# ✅ CERTO: Features disponíveis antes da decisão
df['valor_transacao'], df['hora_transacao'], df['localizacao']
```

---

### 3️⃣ Overfitting em Feature Engineering

**Problema:** Muitas features criam modelo complexo demais.

```python
# ❌ ERRADO: Criar centenas de features sem critério
for col1 in df.columns:
    for col2 in df.columns:
        df[f'{col1}_x_{col2}'] = df[col1] * df[col2]  # Explosão combinatória!

# ✅ CERTO: Criar features com significado
df['preco_por_unidade'] = df['preco_total'] / df['quantidade']
```

---

### 4️⃣ Ignorar Missing Values

```python
# ❌ ERRADO: Scaler quebra com NaN
X_scaled = scaler.fit_transform(X)  # Error se tem NaN

# ✅ CERTO: Tratar NaN antes
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='median')
X_imputed = imputer.fit_transform(X)
X_scaled = scaler.fit_transform(X_imputed)
```

---

### 5️⃣ Não Testar Impacto

```python
# ❌ ERRADO: Criar features sem validar
df['nova_feature'] = ...
# Assumir que melhora modelo

# ✅ CERTO: Validar com CV
from sklearn.model_selection import cross_val_score

# Sem nova feature
score_before = cross_val_score(model, X, y, cv=5).mean()

# Com nova feature
X_new = X.copy()
X_new['nova_feature'] = ...
score_after = cross_val_score(model, X_new, y, cv=5).mean()

print(f"Melhoria: {score_after - score_before:.3f}")
```

---

## 📚 Casos Práticos

### 🏠 Caso 1: Previsão de Preço de Imóveis

```python
import pandas as pd
import numpy as np

# Features originais
df = pd.DataFrame({
    'area': [80, 120, 100, 90],
    'quartos': [2, 3, 3, 2],
    'banheiros': [1, 2, 2, 1],
    'idade': [5, 10, 2, 8],
    'preco': [200000, 350000, 280000, 220000]
})

# Feature Engineering
df['preco_por_m2'] = df['preco'] / df['area']
df['comodos_total'] = df['quartos'] + df['banheiros']
df['razao_quartos_area'] = df['quartos'] / df['area']
df['imovel_novo'] = (df['idade'] < 3).astype(int)
df['area_log'] = np.log1p(df['area'])

# Binning idade
df['categoria_idade'] = pd.cut(df['idade'], 
                                bins=[0, 3, 7, 100], 
                                labels=['Novo', 'Seminovo', 'Antigo'])
```

**Resultado:** +15% accuracy

---

### 💳 Caso 2: Detecção de Fraude

```python
# Features temporais
df['hora'] = df['timestamp'].dt.hour
df['dia_semana'] = df['timestamp'].dt.dayofweek
df['transacao_noturna'] = (df['hora'].between(0, 6)).astype(int)

# Features de agregação
df_user = df.groupby('user_id').agg({
    'valor': ['mean', 'std', 'max'],
    'timestamp': 'count'
}).reset_index()

df_user.columns = ['user_id', 'ticket_medio', 'std_valor', 
                   'max_valor', 'num_transacoes']

# Anomalias
df = df.merge(df_user, on='user_id')
df['valor_atipico'] = (df['valor'] > df['max_valor'] * 2).astype(int)
df['frequencia_alta'] = (df['num_transacoes'] > 50).astype(int)
```

**Resultado:** +22% precision em fraudes

---

### 🛒 Caso 3: Churn de Clientes

```python
# Features de comportamento
df['dias_ultima_compra'] = (pd.Timestamp.now() - df['ultima_compra']).dt.days
df['frequencia_compra'] = df['num_compras'] / df['dias_cliente']
df['ticket_crescente'] = (df['ticket_medio_3m'] > df['ticket_medio_6m']).astype(int)

# Features de engajamento
df['abre_email'] = df['emails_abertos'] / df['emails_enviados']
df['clica_link'] = df['clicks'] / df['emails_abertos']
df['converte'] = df['compras'] / df['visitas']

# RFM (Recency, Frequency, Monetary)
df['rfm_score'] = (
    df['dias_ultima_compra'].rank(ascending=False) +
    df['num_compras'].rank() +
    df['valor_total'].rank()
) / 3
```

**Resultado:** +18% recall em churn

---

## 📋 Checklist de Feature Engineering

### ✅ Antes de Começar

- [ ] Entendi o problema de negócio?
- [ ] Entendi o significado de cada feature?
- [ ] Fiz EDA (Exploratory Data Analysis)?
- [ ] Identifiquei tipos de features (numéricas, categóricas, etc.)?
- [ ] Verifiquei missing values?
- [ ] Verifiquei outliers?

### ✅ Durante Feature Engineering

- [ ] Separei train/test ANTES de qualquer transformação?
- [ ] Tratei missing values apropriadamente?
- [ ] Escalei features numéricas (se necessário)?
- [ ] Encodei features categóricas corretamente?
- [ ] Criei features de tempo relevantes?
- [ ] Criei features de agregação úteis?
- [ ] Criei features de interação (se necessário)?
- [ ] Documentei cada feature criada?

### ✅ Feature Selection

- [ ] Removi features altamente correlacionadas?
- [ ] Usei feature importance para selecionar?
- [ ] Validei impacto com cross-validation?
- [ ] Removi features com baixa variância?

### ✅ Validação

- [ ] Testei modelo com e sem novas features?
- [ ] Validei que não há data leakage?
- [ ] Validei que não há target leakage?
- [ ] Features fazem sentido de negócio?
- [ ] Modelo generalizou bem no teste?

### ✅ Produção

- [ ] Criei pipeline reproduzível?
- [ ] Salvei scalers/encoders treinados?
- [ ] Documentei processo completo?
- [ ] Código está versionado?

---

## 🎓 Resumo Executivo

### 🔑 Pontos-Chave

1. **Features > Algoritmos:** Boas features melhoram mais que trocar algoritmo
2. **Conheça seus dados:** EDA é essencial antes de FE
3. **Evite data leakage:** Fit apenas em train, transform em test
4. **Use pipelines:** Automatiza e previne erros
5. **Valide tudo:** CV para medir impacto real
6. **Documente:** Você (e outros) vão agradecer depois

### 📊 Impacto Real

| Técnica | Dificuldade | Impacto | Quando Usar |
|---------|-------------|---------|-------------|
| **Scaling** | Fácil | Alto | SVM, KNN, Neural Nets |
| **One-Hot Encoding** | Fácil | Alto | Features categóricas |
| **Log Transform** | Fácil | Médio | Distribuições assimétricas |
| **Features de Tempo** | Médio | Alto | Dados temporais |
| **Aggregações** | Médio | Alto | Múltiplas linhas/cliente |
| **Interações Polinomiais** | Médio | Médio | Relações não-lineares |
| **Target Encoding** | Difícil | Alto | Muitas categorias |
| **Feature Selection** | Médio | Médio | Muitas features |

### 🎯 Próximos Passos

1. ✅ Praticar no notebook `02-feature-engineering.ipynb`
2. ✅ Aplicar em projeto real (Dia 3)
3. ✅ Criar seu próprio checklist de FE
4. ✅ Documentar aprendizados

---

## 📚 Recursos Adicionais

### 📖 Leitura Recomendada

- [Feature Engineering for Machine Learning (O'Reilly)](https://www.oreilly.com/library/view/feature-engineering-for/9781491953235/)
- [Scikit-learn Preprocessing Guide](https://scikit-learn.org/stable/modules/preprocessing.html)
- [Kaggle Feature Engineering](https://www.kaggle.com/learn/feature-engineering)

### 🎥 Vídeos

- [Feature Engineering by Andrew Ng](https://www.youtube.com/watch?v=bmjamLZ3v8A)
- [Applied ML 2020 - Feature Engineering](https://www.youtube.com/watch?v=82I5zTdS7E8)

### 🛠️ Ferramentas

- **category_encoders:** Encoders avançados
- **featuretools:** AutoML para feature engineering
- **tsfresh:** Features automáticas para séries temporais

---

## 🎉 Conclusão

Feature Engineering é uma **arte e ciência**:
- **Arte:** Requer criatividade e conhecimento de domínio
- **Ciência:** Deve ser validado com métricas objetivas

> "Feature engineering is the key to applied machine learning."
> 
> – Pedro Domingos

**Lembre-se:**
- Comece simples, complexifique gradualmente
- Valide cada mudança com CV
- Documente tudo
- Aprenda com cada projeto

---

**Próximo passo:** Pratique tudo isso no notebook! 🚀

**Boa sorte e bom código!** 💪
