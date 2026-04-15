# 🔍 Dia 2 - Semana 5: DBSCAN + Detecção de Anomalias

[← Semana 5](../semana-05-ml-nao-supervisionado/README.md)

**Data:** Abril 2026  
**Foco:** DBSCAN, Isolation Forest, LOF, PCA aprofundado  
**Pré-requisito:** Dia 1 concluído (K-Means + Hierárquico dominados)

---

## 📋 Índice

1. [Recap do Dia 1](#1-recap-do-dia-1)
2. [DBSCAN: Clustering por Densidade](#2-dbscan-clustering-por-densidade)
3. [Comparação: K-Means vs DBSCAN vs Hierárquico](#3-comparação-dos-três-métodos)
4. [Detecção de Anomalias](#4-detecção-de-anomalias)
5. [Isolation Forest](#5-isolation-forest)
6. [Local Outlier Factor (LOF)](#6-local-outlier-factor-lof)
7. [PCA Aprofundado](#7-pca-aprofundado)
8. [Dicas e Armadilhas](#8-dicas-e-armadilhas)
9. [Exercícios](#9-exercícios)

---

## 1. Recap do Dia 1

| O que aprendemos | Resultado |
|------------------|-----------|
| K-Means | K=5, Silhouette 0.598 |
| Hierárquico | Silhouette 0.590, dendrograma |
| Concordância | ARI 0.960 (quase idênticos) |
| Métricas | Elbow Method + Silhouette Score |

**Limitações que ficaram:**
- K-Means assume clusters **esféricos** (formatos circulares)
- K-Means e Hierárquico precisam de K **definido antes** (ou cortando dendrograma)
- Nenhum dos dois lida bem com **outliers** ou **formatos irregulares**

> Hoje vamos resolver essas limitações com DBSCAN + detecção de anomalias.

---

## 2. DBSCAN: Clustering por Densidade

### O que é?

**DBSCAN** = Density-Based Spatial Clustering of Applications with Noise

Em vez de centróides ou distâncias hierárquicas, o DBSCAN agrupa pontos que estão **densamente conectados** e marca pontos isolados como **ruído (noise)**.

### Analogia

Imagine uma foto de satélite de cidades à noite:
- **Clusters** = áreas iluminadas (cidades densas)
- **Noise** = pontos de luz isolados (casas rurais)
- DBSCAN encontra as "cidades" sem saber quantas existem

### Parâmetros Fundamentais

| Parâmetro | O que faz | Analogia |
|-----------|-----------|----------|
| **eps** (ε) | Raio de vizinhança | "Quão perto é perto?" |
| **min_samples** | Mínimo de vizinhos para ser core point | "Quantos vizinhos para ser 'cidade'?" |

### Tipos de Pontos no DBSCAN

```
🔴 Core Point     → Tem ≥ min_samples vizinhos dentro de eps
🟡 Border Point   → Vizinho de um core point, mas tem < min_samples
⚫ Noise Point    → Não é core nem border → OUTLIER!
```

### Como Funciona (Passo a Passo)

1. Escolher um ponto aleatório não visitado
2. Encontrar todos os vizinhos dentro do raio `eps`
3. Se tem ≥ `min_samples` vizinhos → é **core point**, criar cluster
4. Expandir o cluster: adicionar vizinhos dos vizinhos (se forem core)
5. Se tem < `min_samples` → marcar como **noise** (por enquanto)
6. Repetir até visitar todos os pontos

### Scikit-learn

```python
from sklearn.cluster import DBSCAN

dbscan = DBSCAN(eps=0.5, min_samples=5)
labels = dbscan.fit_predict(X_scaled)

# Clusters encontrados (noise = -1)
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
n_noise = (labels == -1).sum()
print(f"Clusters: {n_clusters}, Noise: {n_noise}")
```

### Como Escolher eps?

**Método k-distance:**
```python
from sklearn.neighbors import NearestNeighbors

# Calcular distância ao k-ésimo vizinho mais próximo
nn = NearestNeighbors(n_neighbors=min_samples)
nn.fit(X_scaled)
distances, _ = nn.kneighbors(X_scaled)

# Ordenar e plotar (procurar o "cotovelo")
distances = np.sort(distances[:, -1])
plt.plot(distances)
plt.xlabel('Pontos (ordenados)')
plt.ylabel(f'Distância ao {min_samples}º vizinho')
plt.title('k-distance plot — Escolher eps no cotovelo')
plt.show()
```

### Vantagens e Limitações

| ✅ Vantagens | ❌ Limitações |
|-------------|-------------|
| Não precisa definir K | Sensível a eps e min_samples |
| Encontra clusters de qualquer forma | Dificuldade com densidades variadas |
| Detecta outliers nativamente | Não funciona bem em alta dimensionalidade |
| Determinístico (mesma seed = mesmo resultado) | Mais lento que K-Means |

---

## 3. Comparação dos Três Métodos

| Critério | K-Means | Hierárquico | DBSCAN |
|----------|---------|-------------|--------|
| **Define K?** | Sim, antes | Sim (ou corta) | Não! Automático |
| **Forma dos clusters** | Esféricos | Qualquer | Qualquer |
| **Outliers** | ❌ Não detecta | ❌ Não detecta | ✅ Detecta! |
| **Velocidade** | ✅ Rápido | ❌ Lento | ⚠️ Médio |
| **Escalabilidade** | ✅ Datasets grandes | ❌ < 10k | ⚠️ Médio |
| **Parâmetros** | K | K + linkage | eps + min_samples |
| **Determinístico** | ❌ | ✅ | ✅ |

### Quando Usar Cada Um?

```
🔸 K-Means:   Clusters redondos, dataset grande, você sabe ~K
🔸 Hierárquico: Explorar hierarquia, dataset pequeno, não sabe K
🔸 DBSCAN:    Formatos irregulares, outliers presentes, não sabe K
```

---

## 4. Detecção de Anomalias

### O que é?

**Anomaly Detection** = encontrar pontos que são **significativamente diferentes** do padrão normal.

### Anomalias vs Outliers

| Termo | Significado |
|-------|-------------|
| **Outlier** | Ponto estatisticamente distante dos demais |
| **Anomalia** | Ponto que viola o padrão esperado (conceito mais amplo) |
| **Novelty** | Ponto novo que difere do treinamento |

### Aplicações Reais

| Domínio | Exemplo |
|---------|---------|
| 💰 Finanças | Transação de R$5.000 quando a média é R$50 |
| 🏥 Saúde | Batimento cardíaco fora do padrão normal |
| 🏭 Indústria | Sensor de temperatura com leitura anormal |
| 🔒 Segurança | Acesso suspeito em horário incomum |
| 📊 Seu projeto | Despesa fora do padrão histórico da família |

---

## 5. Isolation Forest

### Intuição

A ideia genial: **anomalias são mais fáceis de isolar**.

Se você tentar separar pontos com cortes aleatórios:
- Pontos **normais** (no meio da multidão) → precisam de muitos cortes
- Pontos **anômalos** (isolados) → poucos cortes bastam

### Como Funciona

1. Constrói múltiplas árvores de decisão **aleatórias**
2. Em cada árvore: escolhe feature aleatória + split aleatório
3. Mede o **path length** (quantos splits para isolar cada ponto)
4. Pontos com path curto = **anomalias** (fáceis de isolar)

### Scikit-learn

```python
from sklearn.ensemble import IsolationForest

iso_forest = IsolationForest(
    contamination=0.05,   # ~5% esperados como anomalias
    random_state=42,
    n_estimators=100
)

# -1 = anomalia, 1 = normal
predictions = iso_forest.fit_predict(X_scaled)
anomaly_scores = iso_forest.decision_function(X_scaled)

n_anomalies = (predictions == -1).sum()
print(f"Anomalias detectadas: {n_anomalies}/{len(X_scaled)}")
```

### Parâmetro-chave: contamination

| Valor | Significado |
|-------|-------------|
| 0.01 | 1% são anomalias (conservador) |
| 0.05 | 5% são anomalias (moderado) |
| 0.10 | 10% são anomalias (agressivo) |
| 'auto' | Usa threshold padrão |

> 💡 **Dica:** Se você não sabe a proporção de anomalias, comece com 0.05 e ajuste.

---

## 6. Local Outlier Factor (LOF)

### Intuição

LOF mede a **densidade local** de cada ponto comparada com seus vizinhos.

- Ponto em região **densa** cercado por região **densa** → normal
- Ponto em região **pouco densa** cercado por região **densa** → **anomalia!**

### Diferença do Isolation Forest

| Aspecto | Isolation Forest | LOF |
|---------|-----------------|-----|
| Abordagem | Isolar pontos | Comparar densidades |
| Global vs Local | Mais global | Mais local |
| Melhor para | Anomalias globais | Anomalias locais |
| Velocidade | Mais rápido | Mais lento |

### Scikit-learn

```python
from sklearn.neighbors import LocalOutlierFactor

lof = LocalOutlierFactor(
    n_neighbors=20,
    contamination=0.05
)

# -1 = anomalia, 1 = normal
predictions = lof.fit_predict(X_scaled)
scores = lof.negative_outlier_factor_

n_anomalies = (predictions == -1).sum()
print(f"Anomalias (LOF): {n_anomalies}/{len(X_scaled)}")
```

---

## 7. PCA Aprofundado

### Recap (Semana 3)

Na Semana 3 você já usou PCA para redução de dimensionalidade. Agora vamos aprofundar.

### Por que PCA é Importante em Clustering?

1. **Visualização:** Reduzir para 2D para plotar clusters
2. **Curse of Dimensionality:** Muitas features → distâncias perdem significado
3. **Ruído:** PCA remove dimensões com pouca variância (ruído)

### Variância Explicada

```python
from sklearn.decomposition import PCA

pca = PCA()
X_pca = pca.fit_transform(X_scaled)

# Variância explicada por componente
print("Variância explicada por componente:")
for i, var in enumerate(pca.explained_variance_ratio_):
    print(f"  PC{i+1}: {var:.3f} ({var*100:.1f}%)")

# Variância acumulada
cumvar = np.cumsum(pca.explained_variance_ratio_)
print(f"\nPara 95% da variância: {np.argmax(cumvar >= 0.95) + 1} componentes")
```

### PCA + Clustering = Combinação Poderosa

```python
# 1. Reduzir dimensionalidade
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# 2. Clusterizar no espaço reduzido
kmeans = KMeans(n_clusters=5, random_state=42)
labels = kmeans.fit_predict(X_pca)

# 3. Visualizar
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='viridis')
plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.1%})')
plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.1%})')
plt.show()
```

---

## 8. Dicas e Armadilhas

### ✅ Boas Práticas
1. **Testar múltiplos eps** no DBSCAN usando k-distance plot
2. **Comparar** Isolation Forest + LOF (podem discordar em quais são anomalias)
3. **Validar anomalias manualmente** — verifique se fazem sentido
4. **PCA antes de clustering** quando tem muitas features
5. **Sempre escalar** antes de qualquer método baseado em distância

### ❌ Armadilhas Comuns
1. **eps errado no DBSCAN:** muito pequeno = tudo é noise, muito grande = 1 cluster
2. **contamination arbitrário:** deve refletir conhecimento do domínio
3. **Assumir que toda anomalia é erro:** pode ser dado válido e interessante
4. **PCA demais:** perder informação relevante para economizar componentes
5. **DBSCAN em alta dimensionalidade:** distâncias perdem significado

---

## 9. Exercícios

### Exercício 1: Conceitual
Você tem despesas financeiras onde 95% são de R$10-R$200 e 5% são de R$2.000+.  
Qual método de detecção de anomalias você usaria e por quê?

<details>
<summary>Resposta</summary>

**Isolation Forest** seria uma boa escolha:
- Contamination ≈ 0.05 (já sabe que ~5% são maiores)
- As despesas altas são "fáceis de isolar" (poucos cortes na árvore)
- Funciona bem com dados numéricos
- Alternativa: LOF se quer considerar contexto local (ex: R$2.000 é normal para "moradia" mas anômalo para "alimentação")

</details>

### Exercício 2: DBSCAN
Se você rodar DBSCAN com eps=0.1 e obtiver 50 clusters com 80% dos pontos como noise, o que há de errado?

<details>
<summary>Resposta</summary>

O **eps está muito pequeno!** O raio de vizinhança é tão restritivo que quase nenhum ponto tem vizinhos suficientes. Solução:
1. Plotar o k-distance graph
2. Aumentar eps até encontrar o "cotovelo"
3. Ou diminuir min_samples se quer clusters menores

</details>

### Exercício 3: Comparação
Quando você escolheria DBSCAN em vez de K-Means para segmentar despesas?

<details>
<summary>Resposta</summary>

Escolheria DBSCAN quando:
- Não sabe quantos grupos existem (não quer definir K)
- Suspeita que existem **outliers** (despesas atípicas que não pertencem a nenhum grupo)
- Os grupos podem ter **formatos não esféricos** (ex: faixa de valores alongada)
- Quer que o algoritmo **identifique noise** automaticamente

</details>

---

## 📚 Referências

- [Scikit-learn: DBSCAN](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html)
- [Scikit-learn: Isolation Forest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html)
- [Visualizing DBSCAN](https://www.naftaliharris.com/blog/visualizing-dbscan-clustering/)

---

**Anterior:** [Dia 1 - Fundamentos de Clustering](20-dia1-semana5-clustering-fundamentos.md)  
**Próximo:** [Dia 3 - Segmentação Aplicada (Projeto Financeiro)](22-dia3-semana5-segmentacao-financeiro.md)
