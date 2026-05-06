# 🧠 Dia 1 - Semana 6: Deep Learning — Fundamentos e Primeira Rede Neural

[← Semana 6](../semana-06-deep-learning/README.md)

**Data:** Abril/Maio 2026  
**Foco:** Anatomia de uma rede neural, treino do zero (NumPy) e Keras tabular  
**Pré-requisito:** Semanas 1–5 concluídas (ML supervisionado e não supervisionado dominados)

---

## 📋 Índice

1. [Por que Deep Learning agora?](#1-por-que-deep-learning-agora)
2. [ML clássico vs Deep Learning](#2-ml-clássico-vs-deep-learning)
3. [Anatomia de uma rede neural](#3-anatomia-de-uma-rede-neural)
4. [Funções de ativação](#4-funções-de-ativação)
5. [Forward pass + Loss](#5-forward-pass--loss)
6. [Backpropagation (intuição)](#6-backpropagation-intuição)
7. [Otimizadores e learning rate](#7-otimizadores-e-learning-rate)
8. [Regularização: Dropout, BatchNorm, Early Stopping](#8-regularização)
9. [Sua primeira NN com Keras](#9-sua-primeira-nn-com-keras)
10. [Quando NÃO usar Deep Learning](#10-quando-não-usar-deep-learning)
11. [Exercícios](#11-exercícios)

---

## 1. Por que Deep Learning agora?

Você já tem nas mãos:

- ✅ Modelos lineares e baseados em árvore (Sem 1–4)
- ✅ Pipelines de feature engineering (Sem 4)
- ✅ Clustering, anomalia, PCA (Sem 5)

Tudo isso é **ML clássico**: depende de você desenhar boas features e escolher o modelo certo. Deep Learning vira o jogo quando:

- 🖼️ Os dados são **brutos e de alta dimensão** (imagem, áudio, texto longo)
- 🔁 Existe **estrutura sequencial/espacial** que árvores não capturam bem
- 📈 Você tem **muito dado** para alimentar a rede (caso contrário, RF/XGBoost ainda vencem)

> **Regra prática:** em dados tabulares pequenos/médios, XGBoost normalmente bate uma NN. Em texto/imagem/áudio, NN domina.

---

## 2. ML clássico vs Deep Learning

| Aspecto | ML Clássico (Sem 1-5) | Deep Learning (Sem 6+) |
|---------|----------------------|------------------------|
| **Features** | Você projeta | Rede aprende sozinha |
| **Tamanho dos dados** | Funciona com pouco | Precisa de muito |
| **Hardware** | CPU basta | GPU acelera bastante |
| **Interpretabilidade** | Alta (importância, SHAP) | Baixa (caixa-preta) |
| **Tempo de treino** | Segundos a minutos | Minutos a horas |
| **Aplicações fortes** | Tabular, finanças, fraude | Visão, NLP, áudio, gerativo |

---

## 3. Anatomia de uma rede neural

Uma rede neural é uma **pilha de camadas** que aplicam transformações lineares + não-lineares aos dados.

```
Entrada (X)
   │
   ▼
[Linear: Wx + b]   ← camada densa
   │
   ▼
[Ativação: ReLU]   ← introduz não-linearidade
   │
   ▼
[Linear: Wx + b]
   │
   ▼
[Ativação: Sigmoid/Softmax]  ← converte em probabilidade
   │
   ▼
Saída (ŷ)
```

### O neurônio

Cada neurônio computa:

$$ z = w_1 x_1 + w_2 x_2 + \dots + w_n x_n + b $$

E depois aplica uma função de ativação $\sigma$:

$$ a = \sigma(z) $$

- $w_i$ = pesos (aprendidos)
- $b$ = bias (aprendido)
- $\sigma$ = função de ativação (escolhida por você)

### Camadas densas (fully connected)

Uma camada com $m$ neurônios e entrada de dimensão $n$ tem:

- Matriz de pesos $W \in \mathbb{R}^{m \times n}$
- Vetor de bias $b \in \mathbb{R}^{m}$
- $m \cdot n + m$ parâmetros aprendidos

> **Por que "deep"?** Empilhar 3+ camadas dá poder de representação suficiente para aproximar quase qualquer função (Teorema da Aproximação Universal).

---

## 4. Funções de ativação

| Função | Fórmula | Uso típico |
|--------|---------|------------|
| **ReLU** | $\max(0, x)$ | Padrão para camadas ocultas |
| **Sigmoid** | $\frac{1}{1+e^{-x}}$ | Saída binária |
| **Softmax** | $\frac{e^{x_i}}{\sum_j e^{x_j}}$ | Saída multiclasse |
| **Tanh** | $\tanh(x)$ | Alternativa centralizada (RNNs antigas) |
| **Leaky ReLU** | $\max(0.01x, x)$ | Quando ReLU "morre" |

**Por que precisamos de não-linearidade?** Sem ela, empilhar camadas é equivalente a uma única camada linear — você perde poder de representação.

---

## 5. Forward pass + Loss

**Forward pass** = passar a entrada pela rede e calcular a previsão.

**Loss (perda)** = quão errada está a previsão.

| Tipo de problema | Loss | Por quê |
|------------------|------|---------|
| Regressão | MSE / MAE | Penaliza erro contínuo |
| Classificação binária | Binary Crossentropy | Combina com Sigmoid |
| Classificação multiclasse | Categorical Crossentropy | Combina com Softmax |

$$ \text{BCE} = -\frac{1}{N}\sum_{i=1}^{N} \big[ y_i \log(\hat{y}_i) + (1-y_i)\log(1-\hat{y}_i) \big] $$

---

## 6. Backpropagation (intuição)

Depois do forward, a rede precisa **aprender com o erro**:

1. Calcula loss
2. Calcula o **gradiente** da loss em relação a cada peso (regra da cadeia)
3. Atualiza os pesos na direção que reduz a loss

$$ w_{novo} = w_{antigo} - \eta \cdot \frac{\partial L}{\partial w} $$

- $\eta$ = learning rate
- $\frac{\partial L}{\partial w}$ = quanto a loss varia se eu mexer em $w$

> **Analogia:** é descer uma montanha com olhos vendados. Você sente a inclinação (gradiente) e dá um passo (learning rate) na direção mais íngreme para baixo.

---

## 7. Otimizadores e learning rate

| Otimizador | Quando usar |
|------------|-------------|
| **SGD** | Baseline, simples, mas precisa tunar |
| **SGD + Momentum** | Acelera em direções consistentes |
| **Adam** | **Padrão moderno**: ajusta lr por parâmetro |
| **RMSProp** | Bom para RNNs |

### Learning rate: o hiperparâmetro mais importante

| LR muito alto | LR muito baixo | LR adequado |
|---------------|----------------|-------------|
| Loss explode/oscila | Treino lento, fica preso | Loss desce suavemente |

Estratégias úteis:
- **Learning rate scheduler** (reduzir ao longo do tempo)
- **Warmup** (começar baixo, subir, depois reduzir)
- **ReduceLROnPlateau** (reduzir quando val_loss estabiliza)

---

## 8. Regularização

Redes têm **muitos parâmetros** → tendem a decorar (overfit). Ferramentas:

| Técnica | O que faz |
|---------|-----------|
| **Dropout** | Desliga neurônios aleatoriamente no treino |
| **BatchNorm** | Normaliza ativações intermediárias |
| **L2 weight decay** | Penaliza pesos grandes |
| **Early Stopping** | Para o treino quando val_loss para de cair |
| **Data Augmentation** | Aumenta dataset com transformações |

> **Mantra:** se train_loss << val_loss, está overfit. Ataque com Dropout + Early Stopping primeiro.

---

## 9. Sua primeira NN com Keras

```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    layers.Input(shape=(n_features,)),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='sigmoid'),  # binária
])

model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=1e-3),
    loss='binary_crossentropy',
    metrics=['accuracy', keras.metrics.AUC(name='auc')]
)

history = model.fit(
    X_train, y_train,
    validation_split=0.2,
    epochs=50,
    batch_size=32,
    callbacks=[
        keras.callbacks.EarlyStopping(patience=5, restore_best_weights=True)
    ],
    verbose=0
)
```

### Anatomia do `compile`
- **optimizer**: como atualizar pesos
- **loss**: o que minimizar
- **metrics**: o que reportar (não é o que treina)

### Anatomia do `fit`
- **epochs**: quantas vezes percorrer todo o dataset
- **batch_size**: quantos exemplos por update de gradiente
- **validation_split**: separa pedaço para acompanhar overfit
- **callbacks**: ganchos de controle (EarlyStopping, ModelCheckpoint, ReduceLROnPlateau)

---

## 10. Quando NÃO usar Deep Learning

❌ Datasets pequenos (<10k linhas) e tabulares → use XGBoost  
❌ Quando interpretabilidade for obrigatória (regulamentação) → use lineares/árvores  
❌ Quando recursos computacionais forem escassos  
❌ Quando o problema já é resolvido bem com método clássico  

✅ Use NN quando: dados não estruturados, dataset grande, problema com estrutura espacial/temporal, ou quando feature engineering manual já saturou.

---

## 11. Exercícios

1. **Conceitual:** Explique com suas palavras por que precisamos de função de ativação não-linear entre as camadas.
2. **Conta de neurônio:** Uma rede com entrada de 10 features, camada oculta de 64 neurônios e saída de 1 neurônio tem quantos parâmetros aprendidos?
3. **Diagnóstico:** Você treina uma NN e vê `train_loss=0.05` e `val_loss=0.42`. O que está acontecendo? Cite 3 estratégias de mitigação.
4. **Comparação:** No notebook do dia, compare a NN contra um RandomForest no mesmo dataset. Em que cenário a NN venceria?
5. **Hands-on:** Aumente uma camada da rede, dobre o número de neurônios e refaça o treino. Compare AUC e tempo de treino.

<details>
<summary>Gabarito</summary>

1. Sem ativação não-linear, qualquer pilha de camadas colapsa para uma única transformação linear — a rede fica equivalente a uma regressão logística.
2. $10 \times 64 + 64 + 64 \times 1 + 1 = 705$ parâmetros.
3. Overfitting. Estratégias: Dropout, Early Stopping, mais dados, data augmentation, regularização L2, reduzir capacidade da rede.
4. NN tende a vencer com mais dados (>50k linhas) e features brutas; RF vence em tabular pequeno e interpretável.

</details>

---

[← Semana 5 (concluída)](../semana-05-ml-nao-supervisionado/README.md) · [Semana 6 README](../semana-06-deep-learning/README.md)
