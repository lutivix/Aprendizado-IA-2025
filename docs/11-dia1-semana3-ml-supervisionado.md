# 📊 Semana 3, Dia 1: ML Supervisionado Avançado

**Data:** 04 de Novembro de 2025  
**Duração:** TBD  
**Objetivo:** Implementar modelos ML avançados e comparar performance

---

## 🎯 **Objetivos do Dia**

### Aprendizado
- [x] Entender ensemble methods (Random Forest, Gradient Boosting)
- [ ] Compreender Support Vector Machines (SVM)
- [ ] Feature engineering avançado
- [ ] Métricas de avaliação detalhadas
- [ ] Visualizações profissionais

### Implementação
- [ ] Random Forest Classifier
- [ ] XGBoost/LightGBM
- [ ] Support Vector Machine (SVM)
- [ ] Perceptron Multicamadas (MLP)
- [ ] Comparação estatística entre modelos

### Entregáveis
- [ ] Notebook completo com 4-5 modelos
- [ ] Visualizações comparativas
- [ ] Feature importance analysis
- [ ] Documentação técnica

---

## 📚 **Conceitos Teóricos**

### 1. Ensemble Methods

#### Random Forest
**Conceito:** Combina múltiplas árvores de decisão para reduzir overfitting.

**Como funciona:**
1. Cria N árvores de decisão independentes
2. Cada árvore treina em uma amostra diferente dos dados (bootstrap)
3. Cada split considera apenas um subconjunto aleatório de features
4. Predição final = votação majoritária (classificação) ou média (regressão)

**Vantagens:**
- ✅ Robusto contra overfitting
- ✅ Lida bem com features irrelevantes
- ✅ Feature importance automático
- ✅ Funciona bem "out of the box"

**Hiperparâmetros principais:**
- `n_estimators`: Número de árvores (padrão: 100)
- `max_depth`: Profundidade máxima das árvores
- `min_samples_split`: Mínimo de amostras para split
- `max_features`: Features consideradas em cada split

#### Gradient Boosting (XGBoost/LightGBM)
**Conceito:** Constrói árvores sequencialmente, cada uma corrigindo erros da anterior.

**Como funciona:**
1. Treina primeira árvore nos dados
2. Calcula erros (resíduos)
3. Treina próxima árvore para prever esses erros
4. Repete N vezes, combinando todas as árvores
5. Usa gradient descent para otimizar

**Vantagens:**
- ✅ Alta performance (frequentemente vence competições Kaggle)
- ✅ Lida bem com dados desbalanceados
- ✅ Regularização embutida
- ✅ Extremamente flexível

**XGBoost vs LightGBM:**
- **XGBoost:** Mais maduro, maior comunidade
- **LightGBM:** Mais rápido, menor uso de memória

**Hiperparâmetros principais:**
- `n_estimators`: Número de árvores
- `learning_rate`: Taxa de aprendizado (0.01-0.3)
- `max_depth`: Profundidade das árvores
- `subsample`: Fração de amostras por árvore
- `colsample_bytree`: Fração de features por árvore

### 2. Support Vector Machines (SVM)

**Conceito:** Encontra o hiperplano que melhor separa as classes.

**Como funciona:**
1. Projeta dados em espaço de alta dimensão (kernel trick)
2. Encontra hiperplano com máxima margem entre classes
3. Usa apenas "support vectors" (pontos mais próximos da fronteira)

**Kernels:**
- **Linear:** Separação linear simples
- **RBF (Radial Basis Function):** Não-linear, mais comum
- **Polynomial:** Não-linear, grau configurável
- **Sigmoid:** Similar a redes neurais

**Vantagens:**
- ✅ Eficaz em alta dimensionalidade
- ✅ Memória eficiente (usa apenas support vectors)
- ✅ Versátil (diferentes kernels)

**Desvantagens:**
- ❌ Lento com grandes datasets
- ❌ Sensível a escala dos dados (requer normalização)
- ❌ Difícil interpretar

**Hiperparâmetros principais:**
- `C`: Regularização (menor = mais regularização)
- `kernel`: Tipo de kernel ('rbf', 'linear', 'poly')
- `gamma`: Coeficiente do kernel ('scale', 'auto', ou float)

### 3. Neural Networks (MLP)

**Conceito:** Rede de neurônios artificiais em camadas.

**Arquitetura:**
```
Input Layer → Hidden Layers → Output Layer
```

**Como funciona:**
1. Cada neurônio aplica: `output = activation(sum(weights * inputs) + bias)`
2. Backpropagation ajusta pesos para minimizar erro
3. Múltiplas camadas permitem aprender relações complexas

**Vantagens:**
- ✅ Aprende relações não-lineares complexas
- ✅ Flexível (arquitetura customizável)
- ✅ Pode ser muito poderoso

**Desvantagens:**
- ❌ Requer mais dados
- ❌ Risco de overfitting
- ❌ Difícil interpretar
- ❌ Muitos hiperparâmetros

---

## 🔧 **Implementação**

### Setup Inicial

```python
# Imports principais
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Modelos
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier

# Métricas
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_curve, roc_auc_score
)

# Validação
from sklearn.model_selection import train_test_split, cross_val_score

# Preprocessing
from sklearn.preprocessing import StandardScaler

# Visualizações avançadas
import plotly.express as px
import plotly.graph_objects as go

# XGBoost/LightGBM (se instalados)
try:
    import xgboost as xgb
    import lightgbm as lgb
    BOOSTING_AVAILABLE = True
except ImportError:
    BOOSTING_AVAILABLE = False
    print("XGBoost/LightGBM não disponíveis. Instale com:")
    print("pip install xgboost lightgbm")
```

---

## 📊 **Estrutura do Notebook**

### 1. Carregamento e Preparação dos Dados
- Carregar dataset Titanic (ou outro)
- Feature engineering
- Tratamento de valores faltantes
- Encoding de variáveis categóricas
- Split train/test
- **Normalização (importante para SVM e MLP!)**

### 2. Baseline Model
- Treinar Decision Tree simples como baseline
- Avaliar métricas básicas

### 3. Random Forest
- Treinar com hiperparâmetros padrão
- Analisar feature importance
- Avaliar performance

### 4. Gradient Boosting
- Treinar XGBoost (se disponível)
- Treinar LightGBM (se disponível)
- Comparar com Random Forest

### 5. Support Vector Machine
- **Normalizar dados (StandardScaler)**
- Testar kernel RBF
- Avaliar performance

### 6. Neural Network (MLP)
- **Normalizar dados**
- Definir arquitetura (ex: 100-50-25)
- Treinar com early stopping
- Avaliar performance

### 7. Comparação Final
- Tabela comparativa de métricas
- Gráficos de barras
- Confusion matrices lado a lado
- ROC curves sobrepostas
- Análise de trade-offs

---

## 📈 **Visualizações Esperadas**

### 1. Feature Importance (Random Forest)
```python
# Extrair importâncias
importances = rf_model.feature_importances_
feature_names = X_train.columns

# Criar DataFrame
feat_imp_df = pd.DataFrame({
    'feature': feature_names,
    'importance': importances
}).sort_values('importance', ascending=False)

# Plotar
plt.figure(figsize=(10, 6))
sns.barplot(data=feat_imp_df, x='importance', y='feature')
plt.title('Feature Importance - Random Forest')
plt.tight_layout()
plt.show()
```

### 2. Confusion Matrix Comparativa
```python
# Para cada modelo
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
models = [dt, rf, xgb, svm, mlp]
names = ['Decision Tree', 'Random Forest', 'XGBoost', 'SVM', 'MLP']

for ax, model, name in zip(axes.flat, models, names):
    cm = confusion_matrix(y_test, model.predict(X_test))
    sns.heatmap(cm, annot=True, fmt='d', ax=ax, cmap='Blues')
    ax.set_title(f'{name}\nAccuracy: {accuracy_score(y_test, model.predict(X_test)):.3f}')
```

### 3. ROC Curves
```python
plt.figure(figsize=(10, 8))

for model, name in zip(models, names):
    y_proba = model.predict_proba(X_test)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, y_proba)
    auc = roc_auc_score(y_test, y_proba)
    plt.plot(fpr, tpr, label=f'{name} (AUC={auc:.3f})')

plt.plot([0, 1], [0, 1], 'k--', label='Random Guess')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curves Comparison')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

### 4. Comparação de Métricas
```python
# Criar DataFrame de resultados
results = []
for model, name in zip(models, names):
    y_pred = model.predict(X_test)
    results.append({
        'Model': name,
        'Accuracy': accuracy_score(y_test, y_pred),
        'Precision': precision_score(y_test, y_pred),
        'Recall': recall_score(y_test, y_pred),
        'F1-Score': f1_score(y_test, y_pred)
    })

results_df = pd.DataFrame(results)

# Plotar
results_df.set_index('Model').plot(kind='bar', figsize=(12, 6))
plt.title('Model Performance Comparison')
plt.ylabel('Score')
plt.legend(loc='lower right')
plt.xticks(rotation=45)
plt.ylim(0, 1)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

---

## 🎯 **Critérios de Sucesso**

### Performance
- [ ] Accuracy > 85% no test set
- [ ] F1-Score > 0.83
- [ ] AUC > 0.90
- [ ] Pelo menos 1 modelo supera baseline em 5%+

### Código
- [ ] Código limpo e comentado
- [ ] Funções reutilizáveis
- [ ] Sem warnings
- [ ] Reproduzível (random_state fixo)

### Visualizações
- [ ] 5+ gráficos profissionais
- [ ] Todos com títulos e labels
- [ ] Paleta de cores consistente
- [ ] Comparações claras

### Documentação
- [ ] Explicação de cada modelo
- [ ] Interpretação dos resultados
- [ ] Análise de trade-offs
- [ ] Recomendações finais

---

## 📝 **Cronograma da Sessão**

| Tempo | Atividade |
|-------|-----------|
| 0-15min | Setup + revisão Semana 2 |
| 15-30min | Feature engineering avançado |
| 30-60min | Random Forest + análise |
| 60-90min | Gradient Boosting (XGB/LGB) |
| 90-120min | SVM + MLP |
| 120-150min | Comparação e visualizações |
| 150-180min | Documentação e conclusões |

---

## 🎓 **Aprendizados do Dia**

_A ser preenchido ao final da sessão..._

### Insights Técnicos
- TBD

### Desafios Encontrados
- TBD

### Próximos Passos
- TBD

---

## 🔗 **Recursos Adicionais**

### Documentação Oficial
- [Scikit-learn Ensemble Methods](https://scikit-learn.org/stable/modules/ensemble.html)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- [LightGBM Documentation](https://lightgbm.readthedocs.io/)
- [SVM Guide](https://scikit-learn.org/stable/modules/svm.html)

### Tutoriais Recomendados
- Random Forest: [StatQuest Video](https://www.youtube.com/watch?v=J4Wdy0Wc_xQ)
- Gradient Boosting: [XGBoost Tutorial](https://xgboost.readthedocs.io/en/latest/tutorials/model.html)
- SVM: [Understanding SVM](https://www.youtube.com/watch?v=efR1C6CvhmE)

---

**Status:** 🔄 Em andamento  
**Próxima atualização:** Fim da sessão Dia 1
