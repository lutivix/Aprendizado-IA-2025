# 🔗 Correlação e Pipeline de Machine Learning

**Data:** 28 Outubro 2025  
**Contexto:** Semana 2 - Dia 1 (Insights do Titanic)

---

## 🎯 **O que é Correlação?**

**Correlação** mede **como duas variáveis se relacionam**.

### **Escala de Valores**
- **-1 a +1**
- **Quanto mais próximo de 1 ou -1** → Relação mais forte
- **Próximo de 0** → Pouca ou nenhuma relação

---

## 📊 **Interpretando Correlação**

### **Escala de Cores (Heatmap)**

| Cor | Valor | Significado | Exemplo |
|-----|-------|-------------|---------|
| 🔴 Vermelho escuro | **+1.00** | Correlação PERFEITA positiva | Temperatura °C vs °F |
| 🟠 Laranja | **+0.5 a +0.8** | Correlação FORTE positiva | Altura vs Peso |
| 🟡 Bege claro | **+0.2 a +0.4** | Correlação FRACA positiva | Preço bilhete vs Sobrevivência |
| ⚪ Cinza | **0.0** | SEM correlação | Idade vs Cor de cabelo |
| 🔵 Azul claro | **-0.2 a -0.4** | Correlação FRACA negativa | Classe vs Sobrevivência |
| 🔵 Azul escuro | **-0.5 a -0.8** | Correlação FORTE negativa | Classe vs Preço bilhete |
| 🟣 Roxo | **-1.00** | Correlação PERFEITA negativa | Altitude vs Temperatura |

---

## 💡 **Tipos de Correlação (Exemplos Visuais)**

### **Correlação Positiva (+0.8)**
```
Variável A ↑ → Variável B ↑
Exemplo: Preço do bilhete ↑ → Sobrevivência ↑
```
**Interpretação:** Quando uma aumenta, a outra também aumenta

### **Correlação Negativa (-0.8)**
```
Variável A ↑ → Variável B ↓
Exemplo: Classe ↑ (pior) → Sobrevivência ↓
```
**Interpretação:** Quando uma aumenta, a outra diminui

### **Sem Correlação (0.0)**
```
Variável A ↑↓ → Variável B ↑↓ (aleatório)
Exemplo: Idade ↑↓ → Sobrevivência ↑↓
```
**Interpretação:** Não existe relação aparente

---

## 🚢 **Exemplo Prático: Titanic**

### **Mapa de Correlação Analisado**

| Variáveis | Correlação | Interpretação |
|-----------|-----------|---------------|
| **survived × pclass** | **-0.34** | 🔥 Classe social foi decisiva! Quanto pior a classe, menor sobrevivência |
| **survived × fare** | **+0.26** | 💰 Preço indica classe. Bilhetes caros = mais sobrevivência |
| **survived × age** | **-0.06** | 😐 Idade quase não influenciou. "Mulheres e crianças primeiro" não foi dominante |
| **survived × sibsp** | **-0.04** | 😐 Ter irmãos/cônjuges não ajudou muito |
| **survived × parch** | **+0.08** | 😐 Ter filhos ajudou um pouquinho |
| **pclass × fare** | **-0.55** | 🔄 Redundância! Classe e preço são quase a mesma informação |
| **sibsp × parch** | **+0.41** | 👨‍👩‍👧‍👦 Famílias grandes viajavam juntas |

### **Insights Principais**

✅ **Dinheiro/Classe social salvou mais vidas que idade!**  
✅ **Features mais importantes:** `pclass` e `fare`  
✅ **Features fracas:** `age`, `sibsp`, `parch`  
✅ **Redundância detectada:** `pclass` ≈ `fare` (usar apenas uma)

---

## ⚠️ **CUIDADOS com Correlação**

### **1. Correlação ≠ Causação**

```
❌ ERRADO:
"Vendas de sorvete ↑ → Afogamentos ↑"
Correlação: SIM (+0.8)
Causação: NÃO! (ambos aumentam no verão)

✅ CORRETO:
"Temperatura ↑ → Sorvete ↑"
"Temperatura ↑ → Mais praia → Afogamentos ↑"
```

**Regra de ouro:** Correlação mostra relação, mas não prova que uma **causa** a outra.

### **2. Correlação mede apenas relação LINEAR**

```python
# Relação não-linear pode ter correlação baixa
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]  # y = x²

# Correlação linear pode ser 0.8
# Mas relação real é x²!
```

**Solução:** Use scatter plots para ver relações não-lineares.

### **3. Outliers distorcem correlação**

```python
# Dados normais: correlação = 0.3
# Adiciona 1 outlier extremo
# Nova correlação: 0.9 (falso positivo!)
```

**Solução:** Remover outliers antes de calcular correlação.

---

## 🔄 **Pipeline Completo de Machine Learning**

### **1️⃣ ENTENDER O PROBLEMA**
```
❓ Qual pergunta queremos responder?
   → "Quem sobreviveu no Titanic?"
   
🎯 Tipo de problema?
   → Classificação (sim/não)
   → Regressão (valor numérico)
   → Clustering (agrupar)
```

### **2️⃣ COLETAR DADOS**
```
📊 Obter o dataset
   → CSV, banco de dados, API, web scraping
   
✅ Verificar:
   → Tamanho suficiente? (mínimo 100-1000 linhas)
   → Qualidade boa? (poucos nulos/erros)
```

### **3️⃣ EDA - ANÁLISE EXPLORATÓRIA** ⭐

```python
# a) Carregar dados
df = pd.read_csv('dados.csv')

# b) Análise inicial
df.info()        # Tipos, nulos, memória
df.describe()    # Estatísticas (média, min, max)
df.head()        # Ver primeiras linhas

# c) Visualizar distribuições
df['idade'].hist()                    # Histograma
sns.countplot(data=df, x='classe')    # Contagem

# d) Verificar valores nulos
df.isnull().sum()
df.isnull().sum() / len(df) * 100    # Porcentagem

# e) Analisar correlações ← AQUI!
correlation = df.corr()
sns.heatmap(correlation, annot=True)

# f) Gerar insights
# "Classe social > Idade"
# "Preço e classe são redundantes"
```

**Tempo estimado:** 30-50% do projeto

### **4️⃣ LIMPEZA E PREPARAÇÃO**

```python
# a) Tratar valores nulos
df['age'].fillna(df['age'].median(), inplace=True)  # Mediana
df['embarked'].fillna(df['embarked'].mode()[0])     # Moda
df.dropna(subset=['critical_column'])               # Remover

# b) Remover outliers
Q1 = df['fare'].quantile(0.25)
Q3 = df['fare'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['fare'] >= Q1 - 1.5*IQR) & (df['fare'] <= Q3 + 1.5*IQR)]

# c) Encoding (texto → número)
df['sex_numeric'] = (df['sex'] == 'male').astype(int)
df['embarked_encoded'] = df['embarked'].map({'S': 0, 'C': 1, 'Q': 2})

# d) Normalização (se necessário)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df[['age', 'fare']] = scaler.fit_transform(df[['age', 'fare']])
```

### **5️⃣ FEATURE ENGINEERING**

```python
# Criar novas variáveis úteis baseadas nas existentes

# Titanic - Exemplos:
df['family_size'] = df['sibsp'] + df['parch'] + 1
df['is_alone'] = (df['family_size'] == 1).astype(int)
df['age_group'] = pd.cut(df['age'], bins=[0, 12, 18, 60, 100], 
                         labels=['criança', 'adolescente', 'adulto', 'idoso'])

# Dicas:
# - Combine variáveis relacionadas
# - Crie categorias de faixas
# - Extraia informações (ex: nome → título)
```

### **6️⃣ SELECIONAR FEATURES**

```python
# Baseado na correlação + conhecimento de domínio

# ✅ INCLUIR:
features = ['pclass', 'sex_numeric', 'fare', 'family_size', 'is_alone']
# - Alta correlação com target (> 0.2 ou < -0.2)
# - Faz sentido para o problema

# ❌ REMOVER:
# - Identificadores únicos (name, ticket)
# - Correlação muito fraca (< 0.1)
# - Redundantes (pclass e fare são similares, escolha 1)

X = df[features]
y = df['survived']
```

### **7️⃣ DIVIDIR DADOS (Train/Test Split)**

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2,      # 20% para teste
    random_state=42     # Reproduzibilidade
)

# 80% → Treinar modelo (ensinar)
# 20% → Testar modelo (validar)
```

### **8️⃣ TREINAR MODELOS** 🤖

```python
# Testar múltiplos modelos

# Modelo 1: Logistic Regression
from sklearn.linear_model import LogisticRegression
lr_model = LogisticRegression(max_iter=1000)
lr_model.fit(X_train, y_train)

# Modelo 2: Decision Tree
from sklearn.tree import DecisionTreeClassifier
dt_model = DecisionTreeClassifier(max_depth=5)
dt_model.fit(X_train, y_train)

# Modelo 3: Random Forest
from sklearn.ensemble import RandomForestClassifier
rf_model = RandomForestClassifier(n_estimators=100)
rf_model.fit(X_train, y_train)
```

### **9️⃣ AVALIAR MODELOS**

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Fazer predições
predictions = lr_model.predict(X_test)

# Calcular métricas
accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)
f1 = f1_score(y_test, predictions)

print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1-Score:  {f1:.4f}")

# Comparar modelos e escolher o melhor
```

**Métricas - Quando usar:**
- **Accuracy:** Dados balanceados (50% sim, 50% não)
- **Precision:** Custo de falso positivo é alto (ex: spam)
- **Recall:** Custo de falso negativo é alto (ex: doença)
- **F1-Score:** Balancear precision e recall

### **🔟 MELHORAR (Iteração)**

```python
# a) Ajustar hiperparâmetros
from sklearn.model_selection import GridSearchCV

params = {
    'max_depth': [3, 5, 7, 10],
    'min_samples_split': [2, 5, 10]
}

grid = GridSearchCV(DecisionTreeClassifier(), params, cv=5)
grid.fit(X_train, y_train)
best_model = grid.best_estimator_

# b) Criar novas features
# c) Remover features ruins
# d) Testar outros algoritmos
# e) Coletar mais dados
```

### **1️⃣1️⃣ DEPLOY (Produção)**

```python
# Salvar modelo treinado
import pickle

with open('modelo_titanic.pkl', 'wb') as file:
    pickle.dump(best_model, file)

# Carregar depois
with open('modelo_titanic.pkl', 'rb') as file:
    modelo = pickle.load(file)

# Usar para predições novas
novo_passageiro = [[3, 1, 7.25, 1, 1]]  # pclass, sex, fare, family_size, is_alone
predicao = modelo.predict(novo_passageiro)
print(f"Sobreviveu? {predicao[0]}")
```

---

## 🎯 **Papel da Correlação no Pipeline**

### **Onde a correlação entra?**

```
1. Entender problema
2. Coletar dados
3. Análise inicial (info, describe, visualizar)
4. Verificar nulos
5. CORRELAÇÃO ← Etapa 3e (EDA)
6. Limpeza
7. Feature Engineering
8. Selecionar features (usa correlação!)
9. Treinar ML
```

### **Para que serve?**

✅ **Identificar features relevantes** (correlação forte com target)  
✅ **Detectar redundância** (features correlacionadas entre si)  
✅ **Gerar insights** (entender relações nos dados)  
✅ **Guiar feature engineering** (combinar variáveis relacionadas)

### **Limitações**

❌ Não detecta relações não-lineares  
❌ Não prova causalidade  
❌ Sensível a outliers  
❌ Só funciona para variáveis numéricas

---

## 💪 **Como Usar Correlação Efetivamente**

### **1. Selecionar Features Importantes**

```python
# Pegar correlação com target
correlation_with_target = df.corr()['survived'].abs().sort_values(ascending=False)

print(correlation_with_target)
# survived    1.00  ← Óbvio
# pclass     0.34   ← USAR! 🔥
# fare       0.26   ← USAR! 🔥
# parch      0.08   ← Fraco, talvez remover
# age        0.06   ← Fraco, talvez remover
# sibsp      0.04   ← Fraco, talvez remover

# Filtrar features com correlação > 0.2
strong_features = correlation_with_target[correlation_with_target > 0.2].index.tolist()
```

### **2. Remover Redundância**

```python
# Encontrar features muito correlacionadas entre si
correlation_matrix = df.corr().abs()

# Pares com correlação > 0.7
high_corr_pairs = []
for i in range(len(correlation_matrix.columns)):
    for j in range(i+1, len(correlation_matrix.columns)):
        if correlation_matrix.iloc[i, j] > 0.7:
            high_corr_pairs.append((correlation_matrix.columns[i], 
                                   correlation_matrix.columns[j], 
                                   correlation_matrix.iloc[i, j]))

print(high_corr_pairs)
# [('pclass', 'fare', 0.55)]  ← Usar apenas 1 delas!
```

### **3. Validar Hipóteses**

```python
# Hipótese: "Classe social influenciou mais que idade"
print(f"Correlação pclass: {df['survived'].corr(df['pclass']):.2f}")  # -0.34
print(f"Correlação age: {df['survived'].corr(df['age']):.2f}")        # -0.06

# Conclusão: Hipótese confirmada! ✅
```

---

## 📚 **Resumo Executivo**

### **Correlação é importante?**
✅ **SIM!** É ferramenta essencial para EDA e seleção de features.

### **É o primeiro passo?**
❌ **NÃO!** Vem depois de entender dados e visualizar.

### **Quando usar?**
- Durante EDA (etapa 3e)
- Para selecionar features (etapa 6)
- Para detectar redundância
- Para gerar insights

### **Limitações:**
- Não detecta não-linearidade
- Não prova causação
- Sensível a outliers

---

## 🎓 **Analogia Final: Receita de Bolo**

| Etapa ML | Analogia |
|----------|----------|
| **Entender problema** | Decidir que bolo fazer |
| **Coletar dados** | Comprar ingredientes |
| **EDA inicial** | Ler receita básica |
| **Correlação** | Descobrir o que combina (açúcar deixa doce, sal estraga) |
| **Limpeza** | Peneirar farinha, quebrar ovos |
| **Feature Engineering** | Criar cobertura especial |
| **Selecionar features** | Escolher melhores ingredientes |
| **Train/Test split** | Separar massa para testar |
| **Treinar ML** | Assar o bolo |
| **Avaliar** | Provar e ajustar receita |
| **Deploy** | Servir o bolo! |

---

## ✅ **Checklist: Pipeline Completo**

- [ ] 1. Definir problema (classificação/regressão/clustering)
- [ ] 2. Coletar dados (CSV, API, banco)
- [ ] 3. EDA - Análise exploratória
  - [ ] df.info(), df.describe(), df.head()
  - [ ] Visualizações (histogramas, countplots)
  - [ ] Verificar nulos
  - [ ] **Mapa de correlação** ⭐
  - [ ] Gerar insights
- [ ] 4. Limpeza (nulos, outliers, encoding)
- [ ] 5. Feature Engineering (criar variáveis)
- [ ] 6. Selecionar features (baseado em correlação)
- [ ] 7. Train/Test split (80/20)
- [ ] 8. Treinar múltiplos modelos
- [ ] 9. Avaliar métricas (accuracy, precision, recall, F1)
- [ ] 10. Melhorar (hiperparâmetros, features)
- [ ] 11. Deploy (salvar modelo, criar API)

---

**🚀 Pipeline completo documentado e pronto para referência futura!**
