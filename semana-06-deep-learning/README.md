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

### 🛠️ Dia 2: NN na prática — BelgoEstoque
- [ ] NN aplicada a previsão de demanda (contexto real de produto)
- [ ] Comparação NN vs XGBoost no mesmo problema
- [ ] Decisão fundamentada: quando DL vale, quando ML clássico vence
- [ ] Primeiros passos do pipeline BelgoEstoque Fase 4

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
├── README.md                            # Este arquivo
└── notebooks/
    └── 01-deep-learning-intro.ipynb     # Fundamentos + primeira NN
```

## 📈 Progresso

```
██████████ 100% Dia 1 - Fundamentos + Primeira NN ✅ CONCLUÍDO
░░░░░░░░░░   0% Dia 2 - NN na prática — BelgoEstoque
░░░░░░░░░░   0% Dia 3 - Ponte para LLMs
```

## 📚 Documentação

- [Dia 1 — Deep Learning Intro](../docs/23-dia1-semana6-deep-learning-intro.md)
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
