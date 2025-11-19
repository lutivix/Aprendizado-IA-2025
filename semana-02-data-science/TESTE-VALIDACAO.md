# 🧪 Teste de Validação - Semana 2: Data Science e EDA

## ⏱️ Tempo estimado: 20 minutos

---

## 📋 Parte 1: Conceitos (múltipla escolha)

### Questão 1: Análise Exploratória de Dados (EDA)
Por que fazer EDA antes de treinar modelos?

**A)** Para deixar o código mais bonito  
**B)** Para identificar padrões, problemas e features importantes  
**C)** Porque é obrigatório no Scikit-learn  
**D)** Para fazer o modelo treinar mais rápido  

<details>
<summary>💡 Ver resposta</summary>

**Resposta: B) Para identificar padrões, problemas e features importantes**

**Por quê EDA é crucial:**

### 🔍 Objetivos da EDA:

1. **Identificar Problemas:**
```python
# Valores faltantes
df.isnull().sum()

# Outliers
df.describe()

# Tipos de dados incorretos
df.dtypes
```

2. **Descobrir Padrões:**
```python
# Correlações
df.corr()

# Distribuições
df['age'].hist()

# Relações entre variáveis
sns.scatterplot(x='age', y='fare', data=df)
```

3. **Selecionar Features:**
```python
# Quais features são mais informativas?
correlation_matrix = df.corr()
correlation_matrix['survived'].sort_values(ascending=False)
```

---

### 📊 Exemplo Real: Titanic

**Sem EDA:**
```python
# Treinar direto com todos os dados
model.fit(X, y)  # ❌ Pode ter problemas!
```

**Com EDA:**
```python
# Descobertas importantes:
✅ Age tem 177 valores faltantes → preencher
✅ Cabin tem 687 valores faltantes → remover ou criar feature
✅ Sex correlaciona fortemente com sobrevivência → manter!
✅ Pclass correlaciona com sobrevivência → manter!
✅ Fare tem outliers extremos → normalizar
```

---

### 🎯 Checklist EDA Básico:

- [ ] `.info()` - Tipos de dados e valores nulos
- [ ] `.describe()` - Estatísticas numéricas
- [ ] `.isnull().sum()` - Quantos valores faltantes
- [ ] `.corr()` - Correlações entre variáveis
- [ ] Visualizações (histogramas, boxplots, scatter)

**Conceito-chave:** EDA evita surpresas ruins depois do treino!

</details>

---

### Questão 2: Correlação
Você tem este heatmap de correlação:

```
          survived  age   fare  pclass
survived   1.00    -0.08  0.26  -0.34
age       -0.08     1.00  0.09  -0.37
fare       0.26     0.09  1.00  -0.55
pclass    -0.34    -0.37 -0.55   1.00
```

Qual feature tem **correlação negativa mais forte** com `survived`?

**A)** age  
**B)** fare  
**C)** pclass  
**D)** Todas têm correlação positiva  

<details>
<summary>💡 Ver resposta</summary>

**Resposta: C) pclass (correlação: -0.34)**

### 📊 Análise das Correlações:

#### 1️⃣ **pclass → survived: -0.34**
```
Correlação NEGATIVA MODERADA
```
**Interpretação:**
- Quanto **maior** a classe (3ª classe), **menor** a chance de sobreviver
- Ou: Quanto **menor** a classe (1ª classe), **maior** a chance

**Por quê?**
- Passageiros de 1ª classe (pclass=1): acesso a botes salva-vidas
- Passageiros de 3ª classe (pclass=3): mais distantes dos botes

```python
# Verificar na prática:
df.groupby('pclass')['survived'].mean()
# 1ª classe: 63% sobreviveram
# 2ª classe: 47% sobreviveram
# 3ª classe: 24% sobreviveram ← Confirmado!
```

---

#### 2️⃣ **fare → survived: +0.26**
```
Correlação POSITIVA FRACA/MODERADA
```
**Interpretação:**
- Quanto **maior** a tarifa, **maior** a chance de sobreviver
- Tarifas altas = classes melhores = mais segurança

---

#### 3️⃣ **age → survived: -0.08**
```
Correlação NEGATIVA MUITO FRACA (quase zero!)
```
**Interpretação:**
- Idade quase **não influencia** sobrevivência (surpresa!)
- Embora tenhamos "mulheres e crianças primeiro", a correlação é fraca

**Por quê?**
- Efeito neutralizado por outros fatores (classe, sexo)
- Crianças de 1ª classe sobreviveram, mas de 3ª não

---

### 📏 Escala de Correlação:

```
Valor         Interpretação
━━━━━━━━━━━━━━━━━━━━━━━━━━━
+1.00         Correlação positiva perfeita
+0.70 a +1.00 Correlação positiva forte
+0.30 a +0.70 Correlação positiva moderada
+0.00 a +0.30 Correlação positiva fraca
 0.00         Sem correlação
-0.00 a -0.30 Correlação negativa fraca
-0.30 a -0.70 Correlação negativa moderada  ← pclass está aqui!
-0.70 a -1.00 Correlação negativa forte
-1.00         Correlação negativa perfeita
```

---

### 🎨 Visualização Útil:

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Heatmap de correlação
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', center=0)
plt.title('Correlação entre Variáveis')
plt.show()

# Cores:
# Vermelho = correlação positiva
# Azul = correlação negativa
# Branco = sem correlação
```

---

### ⚠️ Cuidados com Correlação:

**1. Correlação ≠ Causalidade**
```
Exemplo:
Vendas de sorvete ↔ Afogamentos (correlação +0.8)
Mas sorvete NÃO causa afogamento!
Ambos aumentam no verão (variável oculta)
```

**2. Apenas Variáveis Numéricas**
```python
# ❌ Correlação com categóricas não faz sentido
df[['survived', 'sex']].corr()  # sex é texto!

# ✅ Converter para numérico primeiro
df['sex_encoded'] = df['sex'].map({'male': 0, 'female': 1})
df[['survived', 'sex_encoded']].corr()  # Agora sim!
```

**Conceito-chave:** Correlação mostra ASSOCIAÇÃO, não causa e efeito!

</details>

---

### Questão 3: Encoding de Variáveis Categóricas
Você tem uma coluna `embarked` com valores: S, C, Q

Qual o método correto para usar no modelo?

**A)** Usar diretamente: `X = df[['embarked']]`  
**B)** One-Hot Encoding: `pd.get_dummies(df['embarked'])`  
**C)** Converter para números: `{'S': 1, 'C': 2, 'Q': 3}`  
**D)** Remover a coluna  

<details>
<summary>💡 Ver resposta</summary>

**Resposta: B) One-Hot Encoding: `pd.get_dummies(df['embarked'])`**

### 🎯 Por quê?

#### ❌ Opção A: Usar texto diretamente
```python
X = df[['embarked']]  # ['S', 'C', 'Q', ...]

model.fit(X, y)  # ❌ ERRO!
# ValueError: could not convert string to float
```
**Problema:** Modelos ML só entendem números!

---

#### ❌ Opção C: Label Encoding (1, 2, 3)
```python
embarked_map = {'S': 1, 'C': 2, 'Q': 3}
df['embarked_encoded'] = df['embarked'].map(embarked_map)
```

**Problema:** Cria **ordem artificial**!
```
S=1 < C=2 < Q=3
Modelo pensa: Q é "maior" que S
Mas não há ordem! São apenas portos diferentes!
```

**Quando usar Label Encoding:**
- Variáveis **ordinais** (tem ordem natural)
- Exemplos: `tamanho = ['P', 'M', 'G']`, `nota = ['Ruim', 'Bom', 'Ótimo']`

---

#### ✅ Opção B: One-Hot Encoding
```python
# Antes:
embarked
---------
S
C
S
Q

# Depois:
embarked_S  embarked_C  embarked_Q
1           0           0
0           1           0
1           0           0
0           0           1
```

**Vantagens:**
- ✅ Sem ordem artificial
- ✅ Cada categoria vira coluna binária (0/1)
- ✅ Modelo trata cada categoria independentemente

**Código:**
```python
# Método 1: Pandas
df_encoded = pd.get_dummies(df, columns=['embarked'], drop_first=False)

# Método 2: Scikit-learn
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(sparse_output=False)
embarked_encoded = encoder.fit_transform(df[['embarked']])
```

---

### 🎓 Quando Usar Cada Método:

| Tipo de Variável | Método | Exemplo |
|------------------|--------|---------|
| **Nominal** (sem ordem) | One-Hot Encoding | Cor, Porto, País |
| **Ordinal** (com ordem) | Label Encoding | Tamanho (P/M/G), Nota (1-5) |
| **Binária** (2 valores) | 0/1 ou One-Hot | Sim/Não, Masculino/Feminino |

---

### ⚠️ Problema: Dummy Variable Trap

```python
# ❌ Com drop_first=False (padrão):
embarked_S  embarked_C  embarked_Q
1           0           0
0           1           0
0           0           1

# Redundância: Se S=0 e C=0, então Q=1 (sempre!)
# Causa multicolinearidade

# ✅ Com drop_first=True:
embarked_C  embarked_Q
0           0          # S está "implícito" (ambas são 0)
1           0          # C
0           1          # Q
```

**Regra:**
```python
pd.get_dummies(df, columns=['embarked'], drop_first=True)
# Cria n-1 colunas (n = número de categorias)
```

---

### 💻 Exemplo Completo:

```python
import pandas as pd

# Dataset original
df = pd.DataFrame({
    'name': ['John', 'Anna', 'Peter'],
    'embarked': ['S', 'C', 'S'],
    'age': [22, 38, 25]
})

# Aplicar One-Hot Encoding
df_encoded = pd.get_dummies(df, columns=['embarked'], drop_first=True)

print(df_encoded)
#    name  age  embarked_C  embarked_Q  embarked_S
# 0  John   22           0           0           1
# 1  Anna   38           1           0           0
# 2  Peter  25           0           0           1

# Usar no modelo
X = df_encoded[['age', 'embarked_C', 'embarked_Q', 'embarked_S']]
y = df['survived']

model.fit(X, y)  # ✅ Funciona!
```

**Conceito-chave:** Categóricas nominais → One-Hot Encoding!

</details>

---

### Questão 4: Valores Faltantes (Missing Values)
Você tem uma coluna `age` com 20% de valores NaN. O que fazer?

**A)** Remover todas as linhas com NaN  
**B)** Preencher com a média ou mediana  
**C)** Deixar NaN (o modelo aceita)  
**D)** Remover a coluna `age`  

<details>
<summary>💡 Ver resposta</summary>

**Resposta: B) Preencher com a média ou mediana**

### 🎯 Por quê?

#### ❌ Opção A: Remover linhas
```python
df_clean = df.dropna(subset=['age'])
```

**Problemas:**
- ❌ Perde 20% dos dados (177 linhas no Titanic!)
- ❌ Reduz poder estatístico
- ❌ Pode introduzir viés (se NaNs não são aleatórios)

**Quando usar:**
- <5% de valores faltantes
- Muitos dados disponíveis (milhões de linhas)

---

#### ❌ Opção C: Deixar NaN
```python
model.fit(X, y)  # ❌ ValueError: Input contains NaN
```

**Problema:** A maioria dos modelos não aceita NaN!

**Exceções:**
- XGBoost e LightGBM (lidam nativamente com NaN)
- Alguns modelos do scikit-learn com `SimpleImputer`

---

#### ❌ Opção D: Remover coluna
```python
df.drop('age', axis=1)
```

**Problemas:**
- ❌ Perde informação potencialmente útil
- ❌ Age pode ser importante para previsão

**Quando usar:**
- >70% de valores faltantes
- Feature demonstra não ser importante (correlação ~0)

---

#### ✅ Opção B: Imputação (Preencher)

### 1. **Média vs Mediana**

```python
# Média (se distribuição normal)
df['age'].fillna(df['age'].mean(), inplace=True)

# Mediana (se tem outliers)
df['age'].fillna(df['age'].median(), inplace=True)
```

**Quando usar cada uma:**
```
Distribuição Normal → Média
Distribuição Assimétrica → Mediana
Outliers presentes → Mediana
```

---

### 2. **Métodos Avançados**

#### a) **Preencher por Grupo**
```python
# Preencher age baseado na média por sexo
df['age'] = df.groupby('sex')['age'].transform(
    lambda x: x.fillna(x.median())
)

# Lógica: Homens e mulheres podem ter idades médias diferentes
```

#### b) **Forward Fill / Backward Fill**
```python
# Para séries temporais
df['age'].fillna(method='ffill')  # Usa valor anterior
df['age'].fillna(method='bfill')  # Usa próximo valor
```

#### c) **Interpolação**
```python
df['age'].interpolate(method='linear')
# Estima baseado em valores vizinhos
```

#### d) **Criar Feature Indicadora**
```python
# Adicionar coluna "age_was_missing"
df['age_missing'] = df['age'].isnull().astype(int)
df['age'].fillna(df['age'].median(), inplace=True)

# Permite ao modelo saber quando age foi imputado
```

---

### 3. **Scikit-learn SimpleImputer**

```python
from sklearn.impute import SimpleImputer

# Estratégias: 'mean', 'median', 'most_frequent', 'constant'
imputer = SimpleImputer(strategy='median')

df[['age']] = imputer.fit_transform(df[['age']])
```

---

### 📊 Exemplo Completo:

```python
import pandas as pd
import numpy as np

# Dataset com NaNs
df = pd.DataFrame({
    'age': [25, np.nan, 30, np.nan, 40],
    'sex': ['M', 'F', 'M', 'F', 'M']
})

print("Antes:")
print(df)
#    age sex
# 0  25.0   M
# 1   NaN   F
# 2  30.0   M
# 3   NaN   F
# 4  40.0   M

# Preencher com mediana por sexo
df['age'] = df.groupby('sex')['age'].transform(
    lambda x: x.fillna(x.median())
)

print("\nDepois:")
print(df)
#    age sex
# 0  25.0   M
# 1  30.0   F  ← Preenchido com mediana de F (se houver)
# 2  30.0   M
# 3  30.0   F
# 4  40.0   M
```

---

### 🎯 Checklist de Decisão:

```
Valores Faltantes
    ↓
< 5% dos dados?
    ├─ Sim → Remover linhas (dropna)
    └─ Não → Continuar
        ↓
    Feature importante?
        ├─ Não → Remover coluna
        └─ Sim → Imputar
            ↓
        Distribuição normal?
            ├─ Sim → Média
            └─ Não → Mediana
```

**Conceito-chave:** Escolha o método baseado nos dados e no problema!

</details>

---

## 🖥️ Parte 2: Prática (código)

### Desafio: Pipeline Completo de EDA

Complete o código abaixo:

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar dados
df = pd.read_csv('titanic.csv')

# 1️⃣ PREENCHA: Informações básicas do dataset
print("Shape:", __________)
print("\nTipos de dados:")
print(__________)
print("\nValores faltantes:")
print(__________)

# 2️⃣ PREENCHA: Estatísticas descritivas
print("\nEstatísticas:")
print(__________)

# 3️⃣ PREENCHA: Preencher valores faltantes de 'age' com mediana
df['age'].fillna(__________, inplace=True)

# 4️⃣ PREENCHA: Criar encoding para 'sex'
df['sex_encoded'] = df['sex'].map(__________)

# 5️⃣ PREENCHA: Calcular correlação com target
correlation = __________
print("\nCorrelação com survived:")
print(correlation['survived'].sort_values(ascending=False))

# 6️⃣ Visualizar (já preenchido)
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Heatmap de Correlação')
plt.show()
```

<details>
<summary>💡 Ver resposta completa</summary>

### ✅ Código Completo:

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar dados
df = pd.read_csv('titanic.csv')

# 1️⃣ Informações básicas do dataset
print("Shape:", df.shape)
print("\nTipos de dados:")
print(df.dtypes)
print("\nValores faltantes:")
print(df.isnull().sum())

# 2️⃣ Estatísticas descritivas
print("\nEstatísticas:")
print(df.describe())

# 3️⃣ Preencher valores faltantes de 'age' com mediana
df['age'].fillna(df['age'].median(), inplace=True)

# 4️⃣ Criar encoding para 'sex'
df['sex_encoded'] = df['sex'].map({'male': 0, 'female': 1})

# 5️⃣ Calcular correlação com target
# Selecionar apenas colunas numéricas
correlation = df[['survived', 'pclass', 'age', 'sibsp', 
                  'parch', 'fare', 'sex_encoded']].corr()
print("\nCorrelação com survived:")
print(correlation['survived'].sort_values(ascending=False))

# 6️⃣ Visualizar
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0)
plt.title('Heatmap de Correlação')
plt.tight_layout()
plt.show()
```

---

### 📝 Explicação Linha por Linha:

#### 1️⃣ Informações Básicas
```python
df.shape         # (891, 12) = 891 linhas, 12 colunas
df.dtypes        # int64, float64, object (string)
df.isnull().sum() # Quantidade de NaNs por coluna
```

**Output esperado:**
```
Shape: (891, 12)

Tipos de dados:
survived      int64
pclass        int64
name         object  ← String
sex          object  ← String
age         float64
...

Valores faltantes:
survived      0
pclass        0
name          0
sex           0
age         177  ← Tem NaNs!
cabin       687  ← Muitos NaNs!
embarked      2
...
```

---

#### 2️⃣ Estatísticas
```python
df.describe()
```

**Mostra:** count, mean, std, min, 25%, 50%, 75%, max

**Útil para:**
- Identificar outliers (max muito diferente do 75%)
- Ver distribuição (mean vs 50%)
- Detectar valores impossíveis (idade negativa)

---

#### 3️⃣ Imputação
```python
df['age'].fillna(df['age'].median(), inplace=True)
```

**Alternativas:**
```python
# Média
df['age'].fillna(df['age'].mean(), inplace=True)

# Valor constante
df['age'].fillna(0, inplace=True)

# Por grupo
df['age'] = df.groupby('pclass')['age'].transform(
    lambda x: x.fillna(x.median())
)
```

---

#### 4️⃣ Encoding
```python
df['sex_encoded'] = df['sex'].map({'male': 0, 'female': 1})
```

**Resultado:**
```
sex       sex_encoded
male      0
female    1
male      0
female    1
```

**Alternativa (One-Hot):**
```python
df = pd.get_dummies(df, columns=['sex'], drop_first=True)
# Cria: sex_male (0/1)
```

---

#### 5️⃣ Correlação
```python
# Selecionar apenas numéricas
correlation = df[['survived', 'pclass', 'age', 'sibsp', 
                  'parch', 'fare', 'sex_encoded']].corr()

# Ver correlação com target
correlation['survived'].sort_values(ascending=False)
```

**Output esperado:**
```
survived        1.00   ← Sempre 1 (consigo mesmo)
sex_encoded     0.54   ← Forte correlação positiva!
fare            0.26
parch           0.08
age            -0.08
sibsp          -0.04
pclass         -0.34   ← Correlação negativa moderada
```

**Interpretação:**
- `sex_encoded` (female=1) tem correlação +0.54 → Mulheres sobreviveram mais!
- `pclass` tem correlação -0.34 → Classe baixa sobreviveu menos

---

### 📊 Visualizações Adicionais Úteis:

```python
# Distribuição de idade
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
df['age'].hist(bins=30, edgecolor='black')
plt.title('Distribuição de Idade')

# Sobrevivência por sexo
plt.subplot(1, 2, 2)
df.groupby('sex')['survived'].mean().plot(kind='bar')
plt.title('Taxa de Sobrevivência por Sexo')
plt.ylabel('Taxa')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Pairplot (relações entre variáveis)
sns.pairplot(df[['survived', 'age', 'fare', 'pclass']], hue='survived')
plt.show()
```

**Conceito-chave:** EDA é exploração visual + numérica!

</details>

---

## 📊 Parte 3: Interpretação de Visualização

Você criou este gráfico:

```python
df.groupby('pclass')['survived'].mean().plot(kind='bar')
```

Resultado:
```
1ª classe: 0.63 (63%)
2ª classe: 0.47 (47%)
3ª classe: 0.24 (24%)
```

### Questão: O que você pode concluir e como isso afeta seu modelo?

<details>
<summary>💡 Ver resposta e análise</summary>

### 📊 Conclusões e Implicações:

#### 1️⃣ **Conclusão Principal:**
```
Classe social influencia FORTEMENTE a sobrevivência!
1ª classe: 2.6x mais chance que 3ª classe
```

**Por quê isso aconteceu:**
- 1ª classe: Quartos próximos aos botes salva-vidas
- 3ª classe: Quartos no fundo do navio, mais longe
- Prioridade no resgate para passageiros de 1ª classe

---

#### 2️⃣ **Implicações para o Modelo:**

**a) Feature Importance**
```python
# pclass é uma feature MUITO IMPORTANTE!
# NÃO remover essa coluna

✅ Incluir pclass no modelo
✅ Considerar criar features derivadas
```

**b) Features Derivadas**
```python
# Exemplo: criar feature "is_first_class"
df['is_first_class'] = (df['pclass'] == 1).astype(int)

# Exemplo: agrupar classes
df['high_class'] = (df['pclass'] <= 2).astype(int)
```

**c) Interações entre Features**
```python
# pclass pode interagir com outras features
# Exemplo: Mulheres de 1ª classe sobreviveram MUITO mais

# Criar feature de interação
df['female_first_class'] = (
    (df['sex'] == 'female') & (df['pclass'] == 1)
).astype(int)
```

---

#### 3️⃣ **Análise Mais Profunda:**

```python
# Sobrevivência por classe E sexo
survival_by_class_sex = df.groupby(['pclass', 'sex'])['survived'].mean()

print(survival_by_class_sex)
```

**Resultado esperado:**
```
pclass  sex
1       female    0.97  ← 97%! Quase todas sobreviveram
        male      0.37
2       female    0.92
        male      0.16
3       female    0.50
        male      0.14  ← Apenas 14%
```

**Insights:**
- Mulheres de 1ª e 2ª classe: >90% sobreviveram
- Homens de 2ª e 3ª classe: <20% sobreviveram
- Sexo + Classe combinados explicam MUITO da sobrevivência

---

#### 4️⃣ **Estratégias de Modelagem:**

**a) Feature Engineering**
```python
# Criar combinações de features
df['sex_class'] = df['sex'] + '_' + df['pclass'].astype(str)
# Valores: 'female_1', 'male_1', 'female_2', etc.

# One-Hot Encoding
df = pd.get_dummies(df, columns=['sex_class'])
```

**b) Modelos Baseados em Árvore**
```python
# Random Forest, XGBoost, Decision Tree
# Naturalmente capturam interações entre features

model = RandomForestClassifier()
model.fit(X_train, y_train)

# Verificar importância
feature_importance = pd.DataFrame({
    'feature': X_train.columns,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

# Esperado: pclass e sex no topo!
```

**c) Balanceamento de Classes**
```python
# Se dataset estiver desbalanceado
from sklearn.utils import resample

# Oversample da classe minoritária
# Ou usar class_weight='balanced' no modelo
```

---

#### 5️⃣ **Comunicação de Resultados:**

**Para Stakeholders:**
```markdown
# Principais Achados:

1. **Classe social é fator crítico:**
   - Passageiros de 1ª classe: 63% sobreviveram
   - Passageiros de 3ª classe: 24% sobreviveram

2. **Combinação de fatores:**
   - Mulheres de 1ª classe: 97% de sobrevivência
   - Homens de 3ª classe: 14% de sobrevivência

3. **Recomendações para o modelo:**
   - Incluir `pclass` como feature principal
   - Considerar interações com `sex`
   - Explorar features derivadas da classe
```

---

### 📊 Visualização Completa:

```python
import matplotlib.pyplot as plt
import seaborn as sns

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Gráfico 1: Sobrevivência por classe
survival_by_class = df.groupby('pclass')['survived'].mean()
axes[0].bar([1, 2, 3], survival_by_class, 
            color=['gold', 'silver', 'brown'], edgecolor='black')
axes[0].set_xlabel('Classe')
axes[0].set_ylabel('Taxa de Sobrevivência')
axes[0].set_title('Sobrevivência por Classe Social')
axes[0].set_ylim(0, 1)
axes[0].axhline(y=0.5, color='r', linestyle='--', alpha=0.5)

# Gráfico 2: Sobrevivência por classe e sexo
survival_matrix = df.groupby(['pclass', 'sex'])['survived'].mean().unstack()
survival_matrix.plot(kind='bar', ax=axes[1], color=['#e74c3c', '#2ecc71'])
axes[1].set_xlabel('Classe')
axes[1].set_ylabel('Taxa de Sobrevivência')
axes[1].set_title('Sobrevivência por Classe e Sexo')
axes[1].set_xticklabels(['1ª', '2ª', '3ª'], rotation=0)
axes[1].legend(['Masculino', 'Feminino'])
axes[1].axhline(y=0.5, color='gray', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
```

---

**Conceito-chave:** Visualizações revelam insights que direcionam feature engineering!

</details>

---

## 🎓 Gabarito de Auto-Avaliação

### Pontuação:

- **Parte 1 (Conceitos):** 4 questões × 2.5 pontos = **10 pontos**
- **Parte 2 (Código):** 1 exercício × 5 pontos = **5 pontos**  
- **Parte 3 (Interpretação):** 1 questão × 5 pontos = **5 pontos**

**TOTAL:** 20 pontos

---

### 📊 Interpretação da sua nota:

#### 🏆 17-20 pontos: EXCELENTE!
**Você dominou EDA e Data Science básico!**

✅ Entende o propósito da EDA  
✅ Sabe interpretar correlações  
✅ Domina encoding e tratamento de dados  
✅ Consegue extrair insights de visualizações  

**Próximos passos:**
- ✅ AVANÇAR para Semana 3 com confiança!
- Continue praticando EDA em outros datasets

---

#### 💪 13-16 pontos: BOM!
**Você entende os conceitos principais, reforce alguns pontos.**

✅ EDA básico está claro  
⚠️ Alguns detalhes precisam de atenção  

**Próximos passos:**
- Revise as questões que errou
- Pratique mais visualizações
- Pode avançar para Semana 3, mas consulte material S2

---

#### 🔄 9-12 pontos: PARCIAL
**Recomendado revisar antes de avançar.**

⚠️ Conceitos de EDA não estão totalmente claros  
⚠️ Pode ter dificuldade na Semana 3  

**Próximos passos:**
- Refaça o notebook de EDA da Semana 2
- Foque em correlação e encoding
- Pratique interpretação de gráficos
- Refaça o teste após 2-3 dias

---

#### 📚 0-8 pontos: REVISAR
**EDA é crucial para ML. Vale a pena reforçar!**

❌ Fundamentos de análise de dados precisam de atenção  

**Próximos passos:**
1. Releia a documentação da Semana 2
2. Execute cada visualização com atenção
3. Pratique com outros datasets (Kaggle)
4. Anote os insights de cada gráfico
5. Retome este teste em 1 semana

---

## 🎯 Reflexão Final

Responda honestamente (só para você):

1. **Sei fazer EDA básico (correlação, visualizações)?**  
   [ ] Sim [ ] Mais ou menos [ ] Preciso revisar  

2. **Entendo quando usar One-Hot vs Label Encoding?**  
   [ ] Sim [ ] Mais ou menos [ ] Preciso revisar  

3. **Consigo tratar valores faltantes adequadamente?**  
   [ ] Sim [ ] Mais ou menos [ ] Preciso revisar  

4. **Me sinto confortável interpretando gráficos e correlações?**  
   [ ] Sim [ ] Com ajuda [ ] Ainda não  

---

## ✅ Decisão Final

### ➡️ AVANCE para Semana 3 se:
- Acertou 13+ pontos
- Respondeu "Sim" ou "Mais ou menos" na maioria das reflexões
- Sente que consegue fazer EDA em novos datasets

### 🔄 REVISE Semana 2 se:
- Acertou <9 pontos
- Respondeu "Preciso revisar" em 3+ reflexões
- Visualizações e correlações ainda confusas

---

## 💡 Dica Final

**EDA é 50% do trabalho em Data Science!**

```
Data Science = 50% EDA + 30% Feature Engineering + 20% Modelagem
```

**Tempo bem investido em EDA:**
- ✅ Evita erros bobos (dados faltantes)
- ✅ Revela features importantes
- ✅ Sugere feature engineering
- ✅ Melhora performance do modelo

**"Se você tortura os dados por tempo suficiente, eles confessam tudo!"** 📊

---

**Sucesso! EDA é uma habilidade que você usará SEMPRE! 🎯**

_Este teste pode ser refeito sempre que quiser. Pratique com novos datasets!_
