# 💰 Dia 3 - Semana 5: Projeto Prático de Segmentação Financeira

[← Semana 5](../semana-05-ml-nao-supervisionado/README.md)

**Data:** Abril 2026  
**Foco:** Pipeline completo de clustering aplicado ao projeto financeiro  
**Pré-requisito:** Dias 1 e 2 concluídos (K-Means, Hierárquico, DBSCAN, Anomalias)

---

## 📋 Índice

1. [Objetivo do Dia](#1-objetivo-do-dia)
2. [Contexto de Negócio](#2-contexto-de-negócio)
3. [Dataset e Features](#3-dataset-e-features)
4. [Pipeline Profissional de Segmentação](#4-pipeline-profissional-de-segmentação)
5. [Modelagem: K-Means, Hierárquico e DBSCAN](#5-modelagem-k-means-hierárquico-e-dbscan)
6. [Interpretação dos Clusters](#6-interpretação-dos-clusters)
7. [Visualizações Recomendadas](#7-visualizações-recomendadas)
8. [Insights Acionáveis](#8-insights-acionáveis)
9. [Checklist de Entrega](#9-checklist-de-entrega)
10. [Exercícios Finais](#10-exercícios-finais)

---

## 1. Objetivo do Dia

Hoje você vai fechar a Semana 5 com um projeto aplicado de ponta a ponta:

- Construir segmentação de despesas reais (sem rótulos)
- Comparar algoritmos e justificar escolha
- Nomear perfis financeiros de forma clara
- Gerar recomendações acionáveis por perfil
- Entregar um mini-relatório técnico + executivo

Resultado esperado: sair de "clusters numéricos" para "perfis com significado de negócio".

---

## 2. Contexto de Negócio

Você já tem um histórico de despesas da família/projeto financeiro. A pergunta agora não é:

"Essa despesa vai estourar orçamento?" (supervisionado)

A pergunta é:

"Que padrões naturais de comportamento financeiro existem nos dados?"

### Exemplos de uso real

- Identificar grupo de gastos impulsivos
- Encontrar padrão de despesas essenciais recorrentes
- Separar períodos de maior risco financeiro
- Detectar anomalias para revisão manual

---

## 3. Dataset e Features

### Estrutura mínima recomendada

- valor
- categoria
- tipo (fixa/variável)
- dia da semana
- mês
- recorrência
- forma de pagamento
- indicador de parcelamento

### Engenharia de features sugerida

- valor_log = log(1 + valor)
- dia_do_mes
- fim_de_semana (0/1)
- categoria_encoded (one-hot)
- sazonalidade mensal
- frequência por categoria

### Cuidados

- Tratar nulos antes de escalar
- Evitar vazamento temporal se usar janelas
- Padronizar com StandardScaler

---

## 4. Pipeline Profissional de Segmentação

Use este fluxo como padrão:

```text
Coleta/Leitura
  -> Limpeza
  -> Feature Engineering
  -> Escalonamento
  -> Redução de dimensionalidade (PCA opcional)
  -> Clustering (K-Means / Hierárquico / DBSCAN)
  -> Métricas (Silhouette, Davies-Bouldin)
  -> Interpretação e nomeação
  -> Visualização
  -> Plano de ação por cluster
```

### Exemplo de pipeline em pseudocódigo

```python
# 1) preparar dados
X = preparar_features(df)
X_scaled = scaler.fit_transform(X)

# 2) testar K-Means em faixa de K
melhor_k, melhor_score = selecionar_k_por_silhouette(X_scaled)
labels_kmeans = treinar_kmeans(X_scaled, melhor_k)

# 3) comparar com hierárquico
labels_h = treinar_hierarquico(X_scaled, melhor_k)

# 4) testar DBSCAN para formas não esféricas/outliers
labels_db = treinar_dbscan(X_scaled, eps=..., min_samples=...)

# 5) interpretar
resumo = resumo_por_cluster(df, labels_kmeans)
```

---

## 5. Modelagem: K-Means, Hierárquico e DBSCAN

### Estratégia prática recomendada

1. Começar com K-Means para baseline
2. Validar com Hierárquico para consistência
3. Rodar DBSCAN para verificar ruídos e estruturas irregulares

### Escolha final

Use critérios objetivos:

- Silhouette mais alto (quando aplicável)
- Coerência de negócio dos grupos
- Estabilidade dos clusters
- Facilidade de explicação para público não técnico

### Exemplo de decisão

- K-Means: Silhouette 0.52, interpretação excelente
- Hierárquico: Silhouette 0.49, perfis parecidos
- DBSCAN: identifica anomalias relevantes, mas sem separar bem perfis principais

Decisão: K-Means para segmentação principal + DBSCAN para camada de risco.

---

## 6. Interpretação dos Clusters

Este é o passo mais importante do projeto.

### Estrutura de leitura por cluster

Para cada cluster, responda:

- Qual o ticket médio?
- Quais categorias dominam?
- É recorrente ou episódico?
- Há padrão temporal?
- Existe risco financeiro associado?

### Exemplo de nomeação

- Cluster 0: Essencial Controlado
- Cluster 1: Lazer Volátil
- Cluster 2: Alto Valor Planejado
- Cluster 3: Risco de Estouro

Dica: evite nomes técnicos como "Cluster A" no relatório final.

---

## 7. Visualizações Recomendadas

### Gráficos principais

- Scatter PCA 2D com cor por cluster
- Boxplot de valor por cluster
- Barras de categoria dominante por cluster
- Heatmap de médias das features por cluster
- Série temporal de frequência por cluster

### Boa prática

Sempre combinar:

- uma visualização técnica (PCA/cluster)
- uma visualização de negócio (categoria, valor, frequência)

---

## 8. Insights Acionáveis

Transforme análise em ação.

### Exemplo de plano por perfil

- Essencial Controlado: manter padrão e monitorar inflação
- Lazer Volátil: criar teto mensal e alerta em tempo real
- Alto Valor Planejado: reforçar reserva e calendário de pagamentos
- Risco de Estouro: aplicar limite por categoria e revisão semanal

### Framework de recomendação

- Ação imediata (esta semana)
- Ação tática (este mês)
- Ação estratégica (próximos 3 meses)

---

## 9. Checklist de Entrega

Use este checklist no fim do notebook/projeto:

- [ ] Dados limpos e documentados
- [ ] Features justificadas
- [ ] Escalonamento aplicado
- [ ] Comparação entre algoritmos
- [ ] Métricas reportadas
- [ ] Clusters nomeados com sentido de negócio
- [ ] Visualizações claras
- [ ] Recomendações acionáveis por perfil
- [ ] Conclusão executiva em linguagem simples

---

## 10. Exercícios Finais

1. Rodar o pipeline com e sem PCA e comparar interpretações.
2. Alterar K em ±1 e avaliar estabilidade dos perfis.
3. Inserir 10 despesas anômalas simuladas e testar DBSCAN + Isolation Forest.
4. Criar um "score de risco por cluster" de 0 a 100.
5. Escrever um resumo executivo de 10 linhas para alguém não técnico.

---

## ✅ Encerramento da Semana 5

Se você concluiu este Dia 3, agora domina:

- Segmentação completa sem rótulos
- Clustering orientado a decisão
- Detecção de padrões e anomalias
- Tradução de resultados técnicos para ação prática

Próximo passo natural: levar esses perfis para dashboard e monitoramento contínuo.
