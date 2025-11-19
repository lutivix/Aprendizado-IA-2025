# 🎛️ Semana 3, Dia 2: Hyperparameter Tuning e Cross-Validation

**Data:** 11 de Novembro de 2025  
**Duração:** 4-5 horas  
**Objetivo:** Otimizar modelos ML através de ajuste de hiperparâmetros

---

## 🎯 **Objetivos do Dia**

### Aprendizado
- [x] Entender o que são hiperparâmetros
- [x] Compreender Grid Search vs Random Search
- [x] Dominar técnicas de Cross-Validation
- [x] Interpretar Learning Curves
- [x] Aplicar Pipelines ML completos
- [x] Feature Selection e PCA

### Implementação
- [x] Grid Search CV
- [x] Random Search CV
- [x] K-Fold Cross-Validation
- [x] Learning Curves
- [x] Pipeline completo (preprocessamento + modelo)
- [x] Feature Selection (SelectKBest, RFE)
- [x] Redução de dimensionalidade (PCA)

### Entregáveis
- [x] Notebook completo com otimização de 4 modelos
- [x] Comparação de estratégias de busca
- [x] Visualizações de Learning Curves
- [x] Pipeline produtivo
- [x] Documentação lúdica em Markdown

---

## 📚 **Conceitos Teóricos**

### 1. O que são Hiperparâmetros?

**Definição:** Parâmetros definidos ANTES do treinamento que controlam como o modelo aprende.

#### Diferença: Parâmetros vs Hiperparâmetros

| Aspecto | Parâmetros | Hiperparâmetros |
|---------|-----------|-----------------|
| **Definição** | Aprendidos durante treino | Definidos antes do treino |
| **Exemplo (Linear)** | Coeficientes (w, b) | Taxa de aprendizado |
| **Exemplo (Árvore)** | Splits das árvores | `max_depth`, `min_samples_split` |
| **Otimização** | Gradient descent | Grid/Random Search |
| **Controle** | Automático (algoritmo) | Manual (cientista de dados) |

#### Analogia Lúdica 🎮

Imagine que você está treinando para jogar futebol:

- **Parâmetros:** Técnica de chute, posicionamento → você **aprende jogando**
- **Hiperparâmetros:** Quantos treinos/semana, duração dos treinos → você **decide antes**

---

### 2. Principais Hiperparâmetros por Modelo

#### 🌲 Random Forest

```python
RandomForestClassifier(
    n_estimators=100,      # Quantas árvores (mais = melhor, mas mais lento)
    max_depth=10,          # Profundidade máxima (limita overfitting)
    min_samples_split=20,  # Mínimo de amostras para dividir nó
    min_samples_leaf=5,    # Mínimo de amostras em folha
    max_features='sqrt',   # Features consideradas por split
    random_state=42        # Reprodutibilidade
)
```

**Impacto visual:**
- 🔼 `max_depth` alto → Overfitting (árvores profundas decoram dados)
- 🔽 `max_depth` baixo → Underfitting (árvores rasas, simples demais)

#### ⚡ XGBoost

```python
XGBClassifier(
    n_estimators=100,       # Número de boosting rounds
    learning_rate=0.1,      # Taxa de aprendizado (0.01-0.3)
    max_depth=6,            # Profundidade por árvore
    subsample=0.8,          # Fração de amostras (0.5-1.0)
    colsample_bytree=0.8,   # Fração de features (0.3-1.0)
    gamma=0,                # Regularização (>0 reduz overfitting)
    reg_alpha=0,            # L1 regularization
    reg_lambda=1,           # L2 regularization
    random_state=42
)
```

**Regra de ouro:**
- 🎯 `learning_rate` baixo + `n_estimators` alto = melhor generalização (mais lento)
- ⚡ `learning_rate` alto + `n_estimators` baixo = mais rápido (risco de overfitting)

#### 🔵 Support Vector Machine (SVM)

```python
SVC(
    C=1.0,              # Regularização (menor = mais regularização)
    kernel='rbf',       # 'linear', 'rbf', 'poly', 'sigmoid'
    gamma='scale',      # Influência de cada ponto (auto, scale, ou valor)
    degree=3,           # Grau do polinômio (se kernel='poly')
    random_state=42
)
```

**Trade-off C:**
- 🔼 `C` alto → Margem pequena, menos erros treino (overfitting)
- 🔽 `C` baixo → Margem grande, tolera erros (underfitting)

#### 🧠 Multi-Layer Perceptron (MLP)

```python
MLPClassifier(
    hidden_layer_sizes=(100, 50),  # Arquitetura: 2 camadas (100 e 50 neurônios)
    activation='relu',              # 'relu', 'tanh', 'logistic'
    solver='adam',                  # 'adam', 'sgd', 'lbfgs'
    alpha=0.0001,                   # Regularização L2
    learning_rate_init=0.001,       # Taxa de aprendizado inicial
    max_iter=200,                   # Épocas máximas
    early_stopping=True,            # Para quando não melhora
    validation_fraction=0.1,        # Dados para validação (se early_stopping=True)
    random_state=42
)
```

**Arquitetura:**
- `(100,)` → 1 camada escondida, 100 neurônios
- `(100, 50)` → 2 camadas: 100 → 50 neurônios
- `(64, 32, 16)` → 3 camadas: 64 → 32 → 16 neurônios

---

### 3. Grid Search vs Random Search

#### Grid Search (Busca Exaustiva)

**Como funciona:**
Testa TODAS as combinações de hiperparâmetros.

```python
param_grid = {
    'n_estimators': [50, 100, 200],      # 3 valores
    'max_depth': [5, 10, 15],            # 3 valores
    'min_samples_split': [2, 5, 10]      # 3 valores
}
# Total: 3 × 3 × 3 = 27 combinações
```

**Vantagens:**
- ✅ Garante encontrar a melhor combinação dentro do grid
- ✅ Mais previsível (sabe quantas iterações terá)

**Desvantagens:**
- ❌ Lento (cresce exponencialmente)
- ❌ Pode desperdiçar tempo em regiões ruins

**Quando usar:**
- Poucos hiperparâmetros (<4)
- Espaço de busca pequeno
- Quando performance é crítica

---

#### Random Search (Busca Aleatória)

**Como funciona:**
Testa N combinações ALEATÓRIAS de hiperparâmetros.

```python
param_distributions = {
    'n_estimators': [50, 100, 150, 200],
    'max_depth': [5, 10, 15, 20, None],
    'min_samples_split': [2, 5, 10, 20]
}
# Testa 20 combinações aleatórias (n_iter=20)
```

**Vantagens:**
- ✅ Mais rápido (você controla n_iter)
- ✅ Explora melhor o espaço (pode encontrar combinações não óbvias)
- ✅ Escala melhor com muitos hiperparâmetros

**Desvantagens:**
- ❌ Não garante encontrar o ótimo global
- ❌ Pode ter sorte (ou azar) na amostragem

**Quando usar:**
- Muitos hiperparâmetros (>4)
- Espaço de busca grande
- Tempo/recursos limitados

---

#### Comparação Visual

```
Grid Search:
┌─────┬─────┬─────┐
│ ✓   │ ✓   │ ✓   │  depth=5
├─────┼─────┼─────┤
│ ✓   │ ✓   │ ✓   │  depth=10
├─────┼─────┼─────┤
│ ✓   │ ✓   │ ✓   │  depth=15
└─────┴─────┴─────┘
  n=50  n=100 n=200
(Testa TODAS: 9 combinações)

Random Search:
┌─────┬─────┬─────┐
│     │ ✓   │     │  depth=5
├─────┼─────┼─────┤
│ ✓   │     │ ✓   │  depth=10
├─────┼─────┼─────┤
│     │ ✓   │     │  depth=15
└─────┴─────┴─────┘
  n=50  n=100 n=200
(Testa 5 aleatórias se n_iter=5)
```

---

### 4. Cross-Validation (Validação Cruzada)

**Problema:** Se treinar/testar sempre na mesma divisão, pode ter sorte/azar.

**Solução:** K-Fold Cross-Validation

#### K-Fold Básico

```
Dataset dividido em 5 partes (K=5):

Fold 1: [TEST] [TRAIN] [TRAIN] [TRAIN] [TRAIN]
Fold 2: [TRAIN] [TEST] [TRAIN] [TRAIN] [TRAIN]
Fold 3: [TRAIN] [TRAIN] [TEST] [TRAIN] [TRAIN]
Fold 4: [TRAIN] [TRAIN] [TRAIN] [TEST] [TRAIN]
Fold 5: [TRAIN] [TRAIN] [TRAIN] [TRAIN] [TEST]

Resultado final: Média das 5 acurácias ± desvio padrão
```

**Código:**
```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
print(f"Acurácia: {scores.mean():.3f} ± {scores.std():.3f}")
```

#### Stratified K-Fold (Recomendado)

Mantém a proporção de classes em cada fold.

**Exemplo:** Dataset com 70% classe 0, 30% classe 1
- Cada fold terá ~70% classe 0 e ~30% classe 1

```python
from sklearn.model_selection import StratifiedKFold

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=skf, scoring='accuracy')
```

**Quando usar:**
- ✅ **Sempre** em classificação desbalanceada
- ✅ Default recomendado para classificação

---

### 5. Learning Curves (Curvas de Aprendizado)

**Objetivo:** Diagnosticar overfitting vs underfitting.

#### Interpretação Visual

```
Acurácia
   ↑
100%│            ╱─────── Train
    │          ╱
 80%│    ╱────╱────────── Test
    │  ╱
 60%│╱
    └─────────────────────→ Tamanho do dataset
```

**Cenários:**

#### 1. Overfitting (Sobreajuste)
```
Train: ───────────── (alta, estável)
Test:  ─────╱╱╱╱╱╱  (baixa, crescendo lentamente)
```
**Diagnóstico:** Grande gap entre train e test  
**Solução:** 
- Regularização (↑ `min_samples_split`, ↓ `max_depth`)
- Mais dados de treino
- Feature selection

#### 2. Underfitting (Subajuste)
```
Train: ──────── (baixa, estável)
Test:  ──────── (baixa, estável)
```
**Diagnóstico:** Ambas acurácias baixas  
**Solução:**
- Modelo mais complexo (↑ `max_depth`, ↑ `n_estimators`)
- Mais features
- Feature engineering

#### 3. Modelo Ideal
```
Train: ────────── (alta)
Test:  ───────── (alta, próxima do train)
```
**Diagnóstico:** Gap pequeno, ambas altas  
**Ação:** Modelo pronto! 🎉

---

### 6. Pipeline ML

**Objetivo:** Encapsular preprocessamento + modelo em um único objeto.

**Vantagens:**
- ✅ Previne data leakage (fit apenas no train)
- ✅ Código limpo e reutilizável
- ✅ Fácil de usar com GridSearchCV
- ✅ Deploy simplificado

#### Pipeline Básico

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

pipeline = Pipeline([
    ('scaler', StandardScaler()),       # Passo 1: normalizar
    ('classifier', RandomForestClassifier())  # Passo 2: treinar
])

# Usar como um modelo normal
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
```

#### Pipeline com Grid Search

```python
param_grid = {
    'classifier__n_estimators': [50, 100],
    'classifier__max_depth': [5, 10]
}

grid = GridSearchCV(pipeline, param_grid, cv=5)
grid.fit(X_train, y_train)
```

**Nota:** Use `nome_do_passo__parametro` para acessar hiperparâmetros.

---

### 7. Feature Selection (Seleção de Features)

**Objetivo:** Remover features irrelevantes para melhorar performance e velocidade.

#### Métodos Principais

##### 1. SelectKBest (Univariado)

Seleciona K melhores features baseado em testes estatísticos.

```python
from sklearn.feature_selection import SelectKBest, f_classif

selector = SelectKBest(score_func=f_classif, k=5)
X_new = selector.fit_transform(X, y)
```

**Funções de score:**
- `f_classif`: ANOVA F-value (classificação)
- `chi2`: Chi-quadrado (dados não-negativos)
- `mutual_info_classif`: Informação mútua

##### 2. RFE (Recursive Feature Elimination)

Elimina features recursivamente treinando o modelo.

```python
from sklearn.feature_selection import RFE

rfe = RFE(estimator=RandomForestClassifier(), n_features_to_select=5)
X_new = rfe.fit_transform(X, y)
```

**Como funciona:**
1. Treina modelo com todas features
2. Ranqueia por importância
3. Remove a menos importante
4. Repete até ter K features

##### 3. Feature Importance (Árvores)

```python
rf = RandomForestClassifier()
rf.fit(X_train, y_train)

importances = rf.feature_importances_
indices = np.argsort(importances)[::-1]

# Manter top 5
top_features = [feature_names[i] for i in indices[:5]]
```

---

### 8. PCA (Principal Component Analysis)

**Objetivo:** Reduzir dimensionalidade mantendo variância.

**Conceito:** Cria novas features (componentes) que são combinações lineares das originais.

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)  # Reduz para 2 dimensões
X_pca = pca.fit_transform(X)

print(f"Variância explicada: {pca.explained_variance_ratio_}")
```

**Exemplo de Output:**
```
Variância explicada: [0.65, 0.25]
```
→ PC1 explica 65% da variância, PC2 explica 25% (90% total)

**Quando usar:**
- ✅ Muitas features correlacionadas
- ✅ Visualização (reduzir para 2D/3D)
- ✅ Reduzir ruído
- ❌ Perda de interpretabilidade (componentes são abstratos)

---

## 🛠️ **Implementação Prática**

### Estrutura do Notebook

O notebook `02-hyperparameter-tuning.ipynb` contém:

1. **Setup e Imports**
   - Bibliotecas: scikit-learn, xgboost, pandas, matplotlib, seaborn
   - Configuração de visualizações

2. **Carregamento de Dados**
   - Dataset Titanic (mesmo da Semana 2)
   - URLs com fallback (Stanford CS109 + Pandas GitHub)

3. **Explicações Educativas**
   - DataFrame (conceito + 7 exemplos práticos)
   - Métodos Pandas (fillna, dropna, str, cut, qcut, apply, etc.)
   - Hiperparâmetros (teoria + demonstração prática)

4. **Preprocessamento**
   - Feature engineering
   - Tratamento de valores faltantes
   - Encoding de variáveis categóricas
   - Normalização (quando necessário)

5. **Grid Search**
   - Random Forest otimizado
   - Comparação com baseline
   - Visualização de resultados

6. **Random Search**
   - XGBoost otimizado
   - Comparação Grid vs Random
   - Tempo de execução

7. **Cross-Validation**
   - K-Fold comparativo
   - Stratified K-Fold
   - Análise de estabilidade

8. **Learning Curves**
   - Diagnóstico de overfitting
   - Curvas por modelo
   - Interpretação visual

9. **Pipeline Completo**
   - Preprocessamento + modelo
   - Grid Search com pipeline
   - Validação

10. **Feature Selection**
    - SelectKBest
    - RFE
    - Feature Importance
    - Comparação de performance

11. **PCA**
    - Redução de dimensionalidade
    - Visualização 2D
    - Análise de variância explicada

12. **Comparação Final**
    - Todos os modelos otimizados
    - Tabela comparativa
    - Melhor modelo
    - Recomendações

---

## 📊 **Resultados Esperados**

### Métricas de Sucesso

#### Baseline (sem tuning)
- Random Forest: ~82% accuracy
- XGBoost: ~83% accuracy
- SVM: ~80% accuracy

#### Após Otimização
- Random Forest: ~85% accuracy (+3%)
- XGBoost: ~87% accuracy (+4%)
- SVM: ~84% accuracy (+4%)

### Insights Principais

1. **XGBoost** geralmente vence em performance bruta
2. **Random Forest** é mais rápido de treinar
3. **SVM** precisa de normalização (StandardScaler)
4. **Feature selection** pode melhorar velocidade sem perder acurácia
5. **PCA** útil para visualização, mas pode reduzir performance

---

## 🎓 **Conceitos-Chave para Dominar**

### Checklist de Aprendizado

- [ ] Diferencio parâmetros de hiperparâmetros
- [ ] Sei quando usar Grid vs Random Search
- [ ] Entendo o que é Cross-Validation e por que usar
- [ ] Interpreto Learning Curves (overfitting vs underfitting)
- [ ] Crio Pipelines para prevenir data leakage
- [ ] Aplico feature selection para melhorar modelos
- [ ] Uso PCA para redução de dimensionalidade
- [ ] Comparo múltiplos modelos de forma justa

### Perguntas de Auto-Avaliação

1. **Por que não usar `scaler.fit_transform()` no test set?**
   <details>
   <summary>Ver resposta</summary>
   
   **Data leakage!** O test set representa dados futuros/desconhecidos. Se você `fit` no test, está usando informações (média, desvio) que não teria na produção. Use apenas `transform()` com o scaler já fitado no train.
   </details>

2. **Grid Search com 5 hiperparâmetros (cada um com 4 valores) e CV=5. Quantos modelos são treinados?**
   <details>
   <summary>Ver resposta</summary>
   
   **1280 modelos!**
   - Combinações: 4^5 = 1024
   - Com CV=5: 1024 × 5 = 5120 treinos (mas 1024 modelos únicos)
   
   Por isso Random Search é preferível com muitos hiperparâmetros.
   </details>

3. **Quando usar feature selection?**
   <details>
   <summary>Ver resposta</summary>
   
   **Use quando:**
   - Muitas features (>50)
   - Features correlacionadas
   - Overfitting persistente
   - Velocidade é crítica
   
   **Cuidado:** Pode remover features úteis! Sempre valide com CV.
   </details>

---

## 🔧 **Troubleshooting Comum**

### Problema 1: Grid Search muito lento

**Sintoma:** Leva horas para terminar

**Soluções:**
```python
# 1. Reduzir espaço de busca
param_grid = {
    'n_estimators': [100],  # Em vez de [50, 100, 200]
    'max_depth': [5, 10]    # Em vez de [5, 10, 15, 20]
}

# 2. Usar Random Search
from sklearn.model_selection import RandomizedSearchCV
random_search = RandomizedSearchCV(
    model, param_distributions, 
    n_iter=20,  # Limite de iterações
    cv=3        # Menos folds
)

# 3. Usar menos folds no CV
grid = GridSearchCV(model, param_grid, cv=3)  # Em vez de cv=5

# 4. Paralelizar
grid = GridSearchCV(model, param_grid, n_jobs=-1)  # Usa todos os cores
```

### Problema 2: Overfitting mesmo após tuning

**Sintoma:** Train >> Test mesmo com hiperparâmetros otimizados

**Soluções:**
```python
# 1. Aumentar regularização
RandomForestClassifier(
    max_depth=5,           # Mais raso
    min_samples_split=50,  # Mais restritivo
    min_samples_leaf=20
)

# 2. Feature selection
from sklearn.feature_selection import RFE
selector = RFE(model, n_features_to_select=10)

# 3. Mais dados (se possível)
# 4. Ensemble de modelos simples
```

### Problema 3: PCA piora performance

**Sintoma:** Acurácia cai após aplicar PCA

**Explicação:** PCA descarta informação (componentes com baixa variância)

**Soluções:**
```python
# 1. Manter mais componentes
pca = PCA(n_components=0.95)  # 95% da variância

# 2. Testar sem PCA
# PCA é melhor para visualização que para performance

# 3. Usar PCA apenas se MUITAS features (>100)
```

---

## 📚 **Recursos Adicionais**

### Documentação Complementar

1. **Material Lúdico**
   - 📄 `docs/14-arvores-decisao-explicacao-ludica.md`
   - Exemplos práticos: futebol, filmes, frutas, carros
   - Analogias visuais com emojis

2. **Scikit-learn Docs**
   - [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)
   - [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html)
   - [Feature Selection](https://scikit-learn.org/stable/modules/feature_selection.html)

3. **Tutoriais Interativos**
   - Kaggle Learn: Feature Engineering
   - DataCamp: Hyperparameter Tuning

### Papers e Livros

- **"Random Search for Hyper-Parameter Optimization"** (Bergstra & Bengio, 2012)
  - Por que Random Search > Grid Search

- **"Hands-On Machine Learning"** (Aurélien Géron)
  - Capítulos 2-3: Fine-tuning models

---

## ✅ **Checklist de Conclusão**

Antes de avançar para o Dia 3, você deve:

- [ ] Executou todo o notebook `02-hyperparameter-tuning.ipynb`
- [ ] Entendeu a diferença entre Grid e Random Search
- [ ] Aplicou Cross-Validation com sucesso
- [ ] Interpretou Learning Curves
- [ ] Criou pelo menos 1 Pipeline completo
- [ ] Experimentou feature selection
- [ ] Testou PCA e entendeu o trade-off
- [ ] Comparou 3+ modelos de forma justa
- [ ] Leu o material lúdico (`14-arvores-decisao-explicacao-ludica.md`)
- [ ] Preencheu auto-avaliação

---

## 🚀 **Próximos Passos**

### Dia 3: Dashboard React Interativo

**Objetivo:** Criar interface visual para o modelo treinado

**Tecnologias:**
- Python API (Flask/FastAPI)
- React + TypeScript
- Visualizações D3.js/Recharts

**Preview:**
```
┌─────────────────────────────────┐
│  Titanic Survival Predictor    │
├─────────────────────────────────┤
│  Age: [____]  Sex: [M] [F]      │
│  Class: [1] [2] [3]             │
│  Fare: [____]                   │
│                                  │
│  [PREDICT SURVIVAL]             │
│                                  │
│  ┌─────────────────────────┐   │
│  │ Survival Probability:   │   │
│  │        78%              │   │
│  │  ████████████░░░░░░     │   │
│  └─────────────────────────┘   │
└─────────────────────────────────┘
```

**Entregáveis:**
- API REST com modelo treinado
- Frontend React interativo
- Deploy local (opcional: cloud)

---

## 💡 **Dicas Finais**

### Estratégia de Otimização

1. **Baseline primeiro**
   ```python
   # Sempre comece com padrões
   model = RandomForestClassifier()
   model.fit(X_train, y_train)
   baseline_score = model.score(X_test, y_test)
   ```

2. **Otimização iterativa**
   ```
   1. Random Search (broad search)
      ↓
   2. Grid Search refinado (narrow search)
      ↓
   3. Manual fine-tuning
   ```

3. **Validação rigorosa**
   ```python
   # Use sempre CV para decisões finais
   scores = cross_val_score(best_model, X, y, cv=5)
   print(f"CV Score: {scores.mean():.3f} ± {scores.std():.3f}")
   ```

### Boas Práticas

```python
# ✅ BOM: Reprodutível
GridSearchCV(model, param_grid, cv=5, random_state=42, n_jobs=-1)

# ✅ BOM: Valida com dados não vistos
train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# ✅ BOM: Pipeline previne leakage
pipeline = Pipeline([('scaler', StandardScaler()), ('model', SVC())])

# ❌ RUIM: Sem random_state (não reprodutível)
RandomForestClassifier()

# ❌ RUIM: Fit scaler no test
scaler.fit_transform(X_test)
```

---

**Parabéns por completar o Dia 2! 🎉**

Você agora domina técnicas profissionais de otimização de modelos ML. Continue praticando e explorando!

_Dúvidas? Consulte o material lúdico ou refaça as seções que não ficaram claras._

---

**Última atualização:** 11/11/2025  
**Próxima revisão:** Após Dia 3  
**Versão:** 1.0
