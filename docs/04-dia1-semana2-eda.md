# 📊 Semana 2 - Dia 1: Análise Exploratória de Dados (EDA)

**Data:** 28 Outubro 2025  
**Tempo:** _A registrar_  
**Status:** 🟡 Em progresso

---

## 🎯 Objetivos do Dia

- [ ] Dominar técnicas de EDA (Exploratory Data Analysis)
- [ ] Trabalhar com dataset real (Titanic)
- [ ] Limpeza e preparação de dados profissional
- [ ] Feature engineering básico
- [ ] Comparar múltiplos modelos ML
- [ ] Métricas avançadas (accuracy, precision, recall, F1-score)

---

## 📚 Conceitos a Dominar

### 1. Análise Exploratória de Dados (EDA)
**O que é:** Processo de investigação dos dados para descobrir padrões, detectar anomalias, testar hipóteses e verificar suposições através de estatísticas e visualizações.

**Por que importa:**
- Entender a qualidade dos dados antes de treinar modelos
- Identificar features relevantes
- Detectar valores nulos, outliers, desbalanceamento
- Orientar decisões de feature engineering

### 2. Feature Engineering
**O que é:** Processo de criar novas variáveis (features) a partir das existentes para melhorar a performance do modelo.

**Exemplos no Titanic:**
- `family_size = sibsp + parch + 1` (tamanho da família)
- `is_alone = (family_size == 1)` (viajou sozinho?)
- `age_group` (criança, adulto, idoso)

### 3. Métricas de Classificação

| Métrica | O que mede | Quando usar |
|---------|-----------|-------------|
| **Accuracy** | % de predições corretas | Dados balanceados |
| **Precision** | % de positivos preditos que são realmente positivos | Custo de falso positivo é alto |
| **Recall** | % de positivos reais que foram identificados | Custo de falso negativo é alto |
| **F1-Score** | Média harmônica entre Precision e Recall | Balancear precision e recall |

**Fórmulas:**
```
Accuracy  = (TP + TN) / (TP + TN + FP + FN)
Precision = TP / (TP + FP)
Recall    = TP / (TP + FN)
F1-Score  = 2 × (Precision × Recall) / (Precision + Recall)
```

### 4. Modelos de Classificação

#### Logistic Regression
- **Como funciona:** Usa função sigmoide para calcular probabilidade (0-1)
- **Vantagens:** Simples, interpretável, rápido
- **Limitações:** Assume relação linear, não captura interações complexas

#### Decision Tree
- **Como funciona:** Cria árvore de decisões baseada em regras if/else
- **Vantagens:** Interpretável, captura não-linearidades, não precisa normalizar
- **Limitações:** Tende a overfitting, instável (pequenas mudanças nos dados alteram muito)

---

## 📝 Roteiro do Notebook

### Parte 1: Setup e Carregamento
```python
- Importar bibliotecas (pandas, numpy, matplotlib, seaborn, sklearn)
- Carregar dataset Titanic
- Verificar shape e primeiras linhas
```

### Parte 2: Análise Inicial
```python
- df.info() - tipos de dados e nulos
- df.describe() - estatísticas descritivas
- Identificar valores nulos por coluna
```

### Parte 3: Visualizações Exploratórias
```python
- Taxa de sobrevivência geral
- Sobrevivência por gênero
- Sobrevivência por classe
- Distribuição de idade
- Mapa de correlação
```

### Parte 4: Limpeza de Dados
```python
- Tratar valores nulos (age → mediana, embarked → moda)
- Criar features: family_size, is_alone
- Transformar categóricas em numéricas (sex → sex_numeric)
```

### Parte 5: Machine Learning
```python
- Selecionar features
- Train/Test split (80/20)
- Treinar Logistic Regression
- Treinar Decision Tree
- Comparar métricas
- Matriz de confusão
- Feature importance
```

---

## 🔧 Comandos e Funções Importantes

### Pandas
```python
df.head()                    # Primeiras 5 linhas
df.info()                    # Informações do dataset
df.describe()                # Estatísticas descritivas
df.isnull().sum()           # Contar valores nulos
df['col'].fillna(value)     # Preencher nulos
df['col'].median()          # Mediana
df['col'].mode()[0]         # Moda
df.corr()                   # Matriz de correlação
```

### Scikit-learn
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
accuracy = accuracy_score(y_test, predictions)
```

### Visualizações
```python
import seaborn as sns
sns.countplot(data=df, x='survived')     # Contagem
sns.heatmap(correlation, annot=True)     # Mapa de calor
df['age'].hist(bins=30)                  # Histograma
df.boxplot(column='age', by='survived')  # Boxplot
```

---

## 🎯 Checklist de Conclusão

- [ ] Dataset carregado e explorado
- [ ] Valores nulos tratados
- [ ] Features criadas (family_size, is_alone)
- [ ] Visualizações geradas (mínimo 5)
- [ ] 2 modelos treinados (Logistic Regression + Decision Tree)
- [ ] Métricas calculadas (accuracy, precision, recall, F1)
- [ ] Matriz de confusão visualizada
- [ ] Feature importance analisada
- [ ] Insights documentados no notebook

---

## 📊 Resultados Esperados

**Meta mínima:**
- Accuracy > 75%
- Entender diferença entre métricas
- Identificar features mais importantes

**Meta ideal:**
- Accuracy > 80%
- Comparar 2+ modelos
- Feature engineering criativo
- Insights acionáveis sobre o dataset

---

## 🔮 Próximos Passos

**Dia 2:** Criar API REST em Python (Flask/FastAPI)
- Endpoint de predição usando modelo treinado
- Salvar modelo com pickle/joblib
- Validação de inputs
- Retornar JSON com probabilidades

---

## 📚 Recursos Complementares

### Datasets para praticar:
- **Titanic:** Classificação (sobreviventes) - dataset clássico
- **Iris:** Classificação multi-classe (3 espécies)
- **Wine Quality:** Classificação (qualidade 0-10)
- **House Prices:** Regressão (Kaggle)

### Documentação:
- [Pandas Docs](https://pandas.pydata.org/docs/)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)

---

**🚀 Bora começar! Abra o notebook `01-eda-analise-exploratoria.ipynb`**
