# Semana 6: Deep Learning — Fundamentos

## 📋 Visão Geral

**Período:** Abril–Maio 2026  
**Foco Principal:** 🧠 **FUNDAMENTOS DE DL — BASE PARA LLMS**  
**Filosofia:** Entender o que uma NN faz por dentro para depois trabalhar com LLMs de forma consciente

> Até aqui dominamos ML clássico (sup + unsup). A Semana 6 fecha o ciclo de teoria e abre a ponte para a Fase 2: LLM Integration e aplicação nos produtos reais.

## 🎯 Objetivos da Semana

### 📚 Dia 1: Fundamentos + Primeira NN com Keras ✅ CONCLUÍDO
- [x] Diferença entre ML clássico e Deep Learning
- [x] Anatomia: neurônio, camada densa, função de ativação
- [x] Forward pass, loss, backpropagation (intuição)
- [x] Otimizadores (SGD, Adam) + learning rate
- [x] Regularização: Dropout, BatchNorm, Early Stopping
- [x] Primeira rede com Keras em dataset tabular
- [x] Comparação NN vs RandomForest no mesmo problema

### 🛠️ Dia 2: NN na prática — BelgoEstoque ⏳ EM ANDAMENTO
- [x] Dataset sintético realista de demanda (3 SKUs, 3 anos, sazonalidade + promo + ruído)
- [x] Feature engineering temporal (lags, médias móveis, ciclos sin/cos)
- [x] Split temporal correto (sem shuffle)
- [x] Comparação NN vs XGBoost com mesmas features
- [x] Métricas honestas (MAE, RMSE, sMAPE, bias) + tempo + interpretabilidade
- [x] Matriz de decisão aplicada → conclusão fundamentada para Fase 4

### 💡 Dia 3: Ponte para LLMs
- [ ] Como o aprendizado de 6 semanas conecta com GPT/Claude
- [ ] Transformers em termos intuitivos (sem matemática pesada)
- [ ] Embeddings: o que são e onde aparecem nos produtos reais
- [ ] Preparação conceitual para Bloco 1 (LLM Integration)

## 🆕 O que muda em relação à Semana 5

| Aspecto | Sem 1-5 (ML Clássico) | Sem 6+ (Deep Learning) |
|---------|----------------------|------------------------|
| Features | Você projeta | Rede aprende |
| Modelo | Árvore / linear / kernel | Pilha de camadas |
| Treinamento | `.fit(X, y)` | Forward + Backprop por epoch |
| Hiperparâmetros | n_estimators, max_depth... | Camadas, neurônios, lr, dropout, batch_size |
| Bibliotecas | scikit-learn | TensorFlow/Keras (e/ou PyTorch) |

## 📊 Estrutura de Arquivos

```
semana-06-deep-learning/
├── README.md                                # Este arquivo
└── notebooks/
    ├── 01-deep-learning-intro.ipynb         # Fundamentos + primeira NN
    └── 02-nn-belgoestoque-demanda.ipynb     # NN vs XGBoost em previsão de demanda
```

## 📈 Progresso

```
██████████ 100% Dia 1 - Fundamentos + Primeira NN ✅ CONCLUÍDO
██████████ 100% Dia 2 - NN na prática — BelgoEstoque ✅ CONCLUÍDO (6 Mai)
░░░░░░░░░░   0% Dia 3 - Ponte para LLMs
```

## 📚 Documentação

- [Dia 1 — Deep Learning Intro](../docs/23-dia1-semana6-deep-learning-intro.md)
- [Dia 2 — NN na prática BelgoEstoque](../docs/24-dia2-semana6-nn-belgoestoque.md)
- [AUTOAVALIACAO geral](../docs/AUTOAVALIACAO.md)

## 💡 Por que passar por Deep Learning?

**DL aqui não é o destino — é a ponte:**
- 🧠 **Entender LLMs** (GPT, Claude) requer saber o que são camadas, atenção, embeddings
- 🔗 **BelgoEstoque Fase 4** pode usar NN para previsão de demanda (Dia 2 decide se vale)
- 📐 **Vocabulário técnico** para conversar com engenheiros de IA e avaliar soluções
- 🚀 **Fase 2 (LLM Integration)** começa aqui — Dia 3 faz a ponte explícita

> ⚠️ **Lembrete honesto:** para tabular pequeno (como o `lancamentos` atual), XGBoost ainda costuma vencer NN. Use Deep Learning quando o problema realmente pede.

## ✅ Pré-requisitos

- Python + NumPy + Pandas (Sem 1)
- Sklearn pipelines + métricas (Sem 2-4)
- Clustering + PCA (Sem 5)
- TensorFlow ≥ 2.10 ou PyTorch ≥ 2.0 instalado no ambiente
