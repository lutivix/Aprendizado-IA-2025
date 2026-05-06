# 🏭 Dia 2 - Semana 6: NN na Prática — BelgoEstoque

[← Semana 6](../semana-06-deep-learning/README.md)

**Data:** Maio 2026  
**Foco:** Aplicar NN em problema realista de previsão de demanda e decidir, com base em dados, se DL ou XGBoost é a escolha certa  
**Pré-requisito:** [Dia 1](23-dia1-semana6-deep-learning-intro.md)

---

## 📋 Índice

1. [Contexto: BelgoEstoque e a Fase 4](#1-contexto-belgoestoque-e-a-fase-4)
2. [Problema: previsão de demanda semanal](#2-problema-previsão-de-demanda-semanal)
3. [Por que comparar NN vs XGBoost?](#3-por-que-comparar-nn-vs-xgboost)
4. [Métricas honestas para forecasting](#4-métricas-honestas-para-forecasting)
5. [Pipeline de avaliação justa](#5-pipeline-de-avaliação-justa)
6. [Quando NN vence XGBoost?](#6-quando-nn-vence-xgboost)
7. [Critérios de decisão BelgoEstoque](#7-critérios-de-decisão-belgoestoque)
8. [Riscos de colocar NN em produção](#8-riscos-de-colocar-nn-em-produção)
9. [Exercícios](#9-exercícios)

---

## 1. Contexto: BelgoEstoque e a Fase 4

**BelgoEstoque** é o sistema de estoque NestJS + React em uso pela Belgo Cercas ES.

**Roadmap planejado:**

| Fase | Foco | Status |
|------|------|--------|
| 1 | Sistema base de estoque | ✅ Em produção |
| 2 | Alertas inteligentes com clustering + threshold | 📋 Próximo |
| 3 | Relatórios automáticos com LLM | 📋 Backlog |
| 4 | **Previsão de demanda** | 🎯 Foco deste dia |

**Pergunta-chave da Fase 4:** _"Vale a pena uma rede neural ou XGBoost resolve melhor?"_

Esse dia existe para responder essa pergunta com **dados, não com hype**.

---

## 2. Problema: previsão de demanda semanal

**Objetivo:** dado o histórico de vendas/saída de cada SKU, prever a demanda da próxima semana.

**Por que importa?**
- 📦 Comprar de menos → ruptura → cliente reclama
- 💰 Comprar de mais → capital parado + risco de perda
- 🎯 Previsão decente já corta dezenas de % do erro de compra manual

**Features típicas disponíveis:**

| Feature | Tipo | Exemplo |
|---------|------|---------|
| `sku_id` | categórico | "TELA-1500-50M" |
| `semana_do_ano` | cíclico | 1 a 52 |
| `mes` | cíclico | 1 a 12 |
| `vendas_lag_1` | numérico | vendas da semana anterior |
| `vendas_lag_4` | numérico | vendas há 1 mês |
| `media_movel_4s` | numérico | média móvel das últimas 4 semanas |
| `tendencia_30d` | numérico | inclinação dos últimos 30 dias |
| `evento_promocional` | binário | houve promoção? |
| `feriado_proximo` | binário | semana com feriado? |

**Target:** `demanda_proxima_semana` (numérica, contínua).

**É uma regressão**, não classificação.

---

## 3. Por que comparar NN vs XGBoost?

| Critério | XGBoost | Neural Network |
|----------|---------|----------------|
| **Tabular pequeno (<50k linhas)** | 🥇 Padrão de mercado | Costuma perder |
| **Sazonalidade explícita em features** | Aprende bem com lags | Aprende, mas precisa de mais dado |
| **Interpretabilidade** | Feature importance + SHAP | Caixa-preta |
| **Tempo de treino** | Segundos a minutos | Minutos a horas |
| **Custo de produção** | CPU basta | GPU acelera, mas opcional |
| **Re-treino diário** | Trivial | Possível, mas mais caro |
| **Dependências** | `xgboost` apenas | TF/Keras + ecossistema |
| **Quando brilha** | Tabular padrão | Sequências longas, multi-saída, embeddings de SKU |

> **Em 80% dos cenários BelgoEstoque, XGBoost vence.** A NN só justifica investimento se houver ganho material e estável.

---

## 4. Métricas honestas para forecasting

Não use accuracy. Para regressão:

| Métrica | Fórmula (intuição) | Quando usar |
|---------|-------------------|-------------|
| **MAE** | média do erro absoluto | Erro médio em unidades reais |
| **RMSE** | raiz da média do erro² | Penaliza erros grandes |
| **MAPE** | média de \|erro/real\|·100% | Comparável entre SKUs |
| **sMAPE** | versão simétrica do MAPE | Lida com zeros melhor |
| **Bias** | média do erro com sinal | Detecta sub/superestimação sistemática |

**Atenção a armadilhas:**
- ❌ MAPE com vendas zero → divisão por zero
- ❌ R² alto pode esconder bias forte
- ❌ Reportar só média esconde caudas — olhe distribuição do erro

**Para BelgoEstoque:** MAE (em unidades) + MAPE (em %) + bias é o trio mínimo.

---

## 5. Pipeline de avaliação justa

Para a comparação ser confiável, ambos os modelos precisam:

1. ✅ **Mesmas features** (mesmo `X_train`, `X_test`)
2. ✅ **Mesmo split temporal** (não embaralhar — usar `TimeSeriesSplit` ou corte por data)
3. ✅ **Mesmas métricas**
4. ✅ **Mesmo budget de tuning** (ou ambos com defaults razoáveis)
5. ✅ **Mesmas seeds** quando possível

```python
# Errado: shuffle quebra a temporalidade
train_test_split(X, y, shuffle=True)

# Certo: corte por data
cutoff = '2026-04-01'
X_train, y_train = X[X.index <  cutoff], y[X.index <  cutoff]
X_test,  y_test  = X[X.index >= cutoff], y[X.index >= cutoff]
```

> **Regra de ouro:** se você embaralhar dados temporais, qualquer modelo vira excelente. Isso é vazamento, não desempenho.

---

## 6. Quando NN vence XGBoost?

NN tende a ganhar quando há **pelo menos um** destes ingredientes:

✅ **Volume:** 100k+ linhas e features ricas  
✅ **Multi-saída:** prever 4 semanas à frente simultaneamente, com correlação entre saídas  
✅ **Embeddings:** muitos SKUs (centenas/milhares) e relações entre eles  
✅ **Sequências longas:** padrão temporal sutil que features manuais não capturam  
✅ **Sinais externos não-tabulares:** texto de promoção, imagem de produto  

XGBoost vence quando:

✅ Tabular puro, <50k linhas  
✅ Lags + features de sazonalidade resolvem 80% do problema  
✅ Interpretabilidade é valiosa  
✅ Re-treino frequente é necessário  

---

## 7. Critérios de decisão BelgoEstoque

Use esta matriz para decidir, depois de rodar o notebook:

| Pergunta | Resposta orienta para |
|----------|----------------------|
| MAE da NN é >5% melhor que XGBoost? | Se **não**, fica XGBoost |
| Diferença de MAE é estável em 3+ SKUs? | Se **não**, fica XGBoost |
| Time tem rotina de re-treino e monitoramento? | Se **não**, fica XGBoost |
| Cliente entende e aceita caixa-preta? | Se **não**, fica XGBoost |
| Há GPU disponível ou orçamento para CPU mais cara? | Se **não**, fica XGBoost |

> Se 4 das 5 respostas favorecem XGBoost, **escolha XGBoost com confiança e siga em frente.** Não é derrota, é boa engenharia.

---

## 8. Riscos de colocar NN em produção

| Risco | Mitigação |
|-------|-----------|
| **Drift silencioso** (modelo degrada) | Monitorar MAE semanal vs janela de referência |
| **Caixa-preta** dificulta auditoria | Manter XGBoost como sombra explicativa |
| **Dependência do TF/Keras** | Containerizar com versão pinada |
| **Treino instável entre seeds** | Treinar 5 seeds + ensemble pela média |
| **Outliers explodindo MAE** | Clip nas previsões + alerta operacional |

---

## 9. Exercícios

1. **Conceitual:** Por que `train_test_split(shuffle=True)` é proibido em forecasting?
2. **Decisão:** No notebook do dia, NN ficou 1% melhor que XGBoost. Você levaria a NN para produção? Justifique usando a matriz de decisão.
3. **Métrica:** Um modelo tem RMSE baixo mas bias = +12 unidades. O que isso significa para o estoque?
4. **Hands-on:** Aumente o ruído do dataset sintético em 3× e veja qual modelo degrada menos.
5. **Reflexão:** Em qual fase do roadmap BelgoEstoque uma NN começaria a fazer sentido de verdade?

<details>
<summary>Gabarito</summary>

1. Embaralhar mistura passado e futuro — o modelo "vê" o futuro durante o treino, dando métrica artificialmente boa que não vai se reproduzir em produção.
2. Não. 1% raramente paga o custo operacional, perda de interpretabilidade e risco de drift. A matriz favorece XGBoost.
3. O modelo sistematicamente sobrestima a demanda em 12 unidades. Em estoque, isso vira capital parado e risco de perda — pior que erro simétrico.
4. XGBoost com regularização tende a degradar menos. NN sem dropout/early-stopping pode entrar em overfit pesado. Vale testar.
5. Quando o catálogo crescer (centenas de SKUs com correlação) ou quando a previsão precisar ser multi-step (4+ semanas) com saídas correlacionadas.

</details>

---

[← Dia 1](23-dia1-semana6-deep-learning-intro.md) · [Semana 6 README](../semana-06-deep-learning/README.md)
