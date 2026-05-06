# Semana 5: ML Não Supervisionado + Clustering

## 📋 Visão Geral

**Período:** Abril 2026  
**Foco Principal:** 🔍 **DESCOBRIR PADRÕES SEM RÓTULOS**  
**Filosofia:** Entender quando e por que usar aprendizado não supervisionado

> Até agora, todos os modelos que treinamos tinham **rótulos** (sobreviveu/não sobreviveu, estourou/não estourou).  
> Agora vamos aprender a encontrar **estrutura nos dados sem supervisão** — agrupando, detectando anomalias e reduzindo dimensionalidade.

## 🎯 Objetivos da Semana

### 📚 Dia 1: Fundamentos de Clustering (K-Means + Hierárquico) ✅ CONCLUÍDO
- [x] Conceitos: supervisionado vs não supervisionado (aprofundar)
- [x] K-Means: algoritmo, centroides, inércia
- [x] Método do Cotovelo (Elbow) e Silhouette Score
- [x] Clustering Hierárquico: dendrogramas
- [x] Visualização de clusters em 2D
- [x] Interpretação e nomeação de perfis de clusters
- **Resultado:** K=5, Silhouette 0.598, 5 perfis identificados (Premium, Econômicos, Gastadores, Conservadores, Classe Média)

### 🛠️ Dia 2: DBSCAN + Detecção de Anomalias ✅ CONCLUÍDO
- [x] DBSCAN: densidade, eps, min_samples
- [x] Comparação K-Means vs DBSCAN vs Hierárquico
- [x] Anomaly Detection: Isolation Forest, LOF
- [x] PCA aprofundado (redução de dimensionalidade)
- [x] Aplicação: detectar padrões anormais em dados
- **Resultados:**
  - DBSCAN Moons: 2 clusters, 0 noise (K-Means errou, DBSCAN acertou ✅)
  - DBSCAN Outliers: 14/20 outliers detectados como noise, 0 falsos positivos
  - Isolation Forest: 19/20 outliers, 3 FP | LOF: 19/20 outliers, 3 FP
  - PCA: 8→7 features para 95% variância, Silhouette PCA 2D: 0.4718 (+133% vs original)
  - Pipeline: PCA 2D → DBSCAN (2 clusters) + Isolation Forest (15 anomalias)

### 💰 Dia 3: Projeto Prático — Segmentação Aplicada ✅ CONCLUÍDO
- [x] Segmentação de despesas do projeto Financeiro (banco SQLite real)
- [x] Pipeline completo: pré-processamento → clustering → interpretação
- [x] Comparação K-Means vs Agglomerative vs DBSCAN
- [x] PCA 2D para visualização dos clusters
- [x] Baseline supervisionado (LogReg + RandomForest) para validar features
- [x] Cluster profiling (médias, taxa de estouro, categoria dominante)
- [x] Nomeação automática de perfis + recomendações acionáveis
- **Resultado:** Pipeline executado de ponta-a-ponta sobre dados reais (`lancamentos` + `weekly_budgets`); perfis nomeados (ex.: Pressionado, Equilibrado, Folgado) com recomendações específicas por cluster

## 🎓 O que Você Já Domina (Recap Semanas 1-4)

| Semana | Tema | Destaques |
|--------|------|-----------|
| 1 | Fundamentos + Setup | Python, NumPy, Pandas, primeiro modelo (R² 96.5%) |
| 2 | Data Science + APIs | EDA, FastAPI, integração Full Stack |
| 3 | ML Supervisionado Avançado | RF, XGBoost, SVM, MLP, Hyperparameter Tuning |
| 4 | Consolidação + Projeto Real | Feature Engineering, Projeto Financeiro (XGBoost F1 0.667) |

## 🆕 O que Há de Novo na Semana 5

### Supervisionado vs Não Supervisionado

| Aspecto | Supervisionado (Sem 1-4) | Não Supervisionado (Sem 5) |
|---------|--------------------------|---------------------------|
| **Dados** | Com rótulos (y) | Sem rótulos |
| **Objetivo** | Prever resultado | Descobrir estrutura |
| **Avaliação** | Accuracy, F1, AUC | Silhouette, Inércia |
| **Exemplos** | Classificar, regredir | Agrupar, detectar anomalias |
| **Uso real** | Previsão de estouro | Segmentar despesas por perfil |

## 📊 Estrutura de Arquivos

```
semana-05-ml-nao-supervisionado/
├── README.md                              # Este arquivo
├── notebooks/
│   ├── 01-clustering-fundamentos.ipynb    # K-Means + Hierárquico
│   ├── 02-dbscan-anomalias.ipynb          # DBSCAN + Anomaly Detection
│   └── 03-segmentacao-financeiro.ipynb    # Projeto prático aplicado
```

## 📈 Progresso

```
██████████ 100% Dia 1 - Clustering Fundamentos  ✅ CONCLUÍDO (8 Abr)
██████████ 100% Dia 2 - DBSCAN + Anomalias       ✅ CONCLUÍDO (9 Abr)
██████████ 100% Dia 3 - Segmentação Aplicada     ✅ CONCLUÍDO (29 Abr)
```

**🎉 Semana 5 100% concluída!** Próximo passo: [Semana 6 — Deep Learning Intro](../semana-06-deep-learning/README.md)

## 💡 Por que ML Não Supervisionado?

**Casos de uso reais para seus projetos:**
- 🏷️ **Segmentação de despesas:** Agrupar gastos por comportamento (não apenas por categoria manual)
- 🚨 **Detecção de anomalias:** Identificar despesas fora do padrão automaticamente
- 📊 **Redução de dimensionalidade:** Simplificar datasets complexos para visualização
- 👥 **Perfis de usuário:** Descobrir padrões de consumo diferentes entre membros da família
