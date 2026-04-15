# 🔍 Dia 1 - Semana 5: Fundamentos de Clustering

[← Semana 5](../semana-05-ml-nao-supervisionado/README.md)

**Data:** Abril 2026  
**Foco:** K-Means, Clustering Hierárquico, métricas de avaliação  
**Pré-requisito:** Semanas 1-4 concluídas (supervisionado dominado)

---

## 📋 Índice

1. [Supervisionado vs Não Supervisionado](#1-supervisionado-vs-não-supervisionado)
2. [O que é Clustering?](#2-o-que-é-clustering)
3. [K-Means: O Algoritmo Fundamental](#3-k-means-o-algoritmo-fundamental)
4. [Como Escolher K? Elbow + Silhouette](#4-como-escolher-k)
5. [Clustering Hierárquico](#5-clustering-hierárquico)
6. [Comparação: K-Means vs Hierárquico](#6-comparação)
7. [Dicas e Armadilhas](#7-dicas-e-armadilhas)
8. [Exercícios](#8-exercícios)

---

## 1. Supervisionado vs Não Supervisionado

### O Que Mudou?

Nas semanas 1-4, sempre tínhamos um **alvo** (target/y):
- Titanic: `survived` (0 ou 1)
- Financeiro: `estourou` (0 ou 1)
- Regressão: `preço` (valor contínuo)

Agora, **não temos rótulos**. O algoritmo precisa descobrir a estrutura sozinho.

### Analogia Prática

Imagine que você tem uma pilha de 3.668 despesas do projeto Financeiro:

| Abordagem | O que faz | Exemplo |
|-----------|-----------|---------|
| **Supervisionado** | "Esta despesa vai estourar o orçamento?" | Previsão com rótulo |
| **Não Supervisionado** | "Existem grupos naturais de despesas?" | Descobre padrões |

### Tipos de Aprendizado Não Supervisionado

```
ML Não Supervisionado
├── Clustering (agrupamento)
│   ├── K-Means          ← hoje
│   ├── Hierárquico      ← hoje
│   ├── DBSCAN           ← Dia 2
│   └── Gaussian Mixture
├── Redução de Dimensionalidade
│   ├── PCA              ← introduzido Sem 3, aprofundar Dia 2
│   ├── t-SNE
│   └── UMAP
└── Detecção de Anomalias
    ├── Isolation Forest  ← Dia 2
    └── LOF               ← Dia 2
```

---

## 2. O que é Clustering?

**Clustering** = agrupar objetos similares sem saber de antemão os grupos.

### Onde Clustering é Usado?

| Domínio | Aplicação | Exemplo |
|---------|-----------|---------|
| Marketing | Segmentação de clientes | Grupos: econômico, médio, premium |
| Finanças | Perfis de gasto | Grupos: essencial, lazer, investimento |
| Saúde | Agrupamento de pacientes | Perfis de risco similares |
| E-commerce | Recomendação | Clientes com comportamento similar |

### O que Define "Similar"?

A métrica mais comum é a **distância Euclidiana**:

$$d(p, q) = \sqrt{\sum_{i=1}^{n}(p_i - q_i)^2}$$

> ⚠️ **Implicação prática:** como usamos distância, **escalar as features é OBRIGATÓRIO** (lembra do StandardScaler da Semana 3?).

---

## 3. K-Means: O Algoritmo Fundamental

### Como Funciona (Passo a Passo)

1. **Escolher K** (número de clusters)
2. **Inicializar** K centróides aleatoriamente
3. **Atribuir** cada ponto ao centróide mais próximo
4. **Recalcular** centróides como a média dos pontos do cluster
5. **Repetir** passos 3-4 até convergir

### Pseudocódigo

```
K-Means(dados, K):
    centróides = escolher_K_pontos_aleatórios(dados)
    
    repetir até convergir:
        para cada ponto em dados:
            cluster[ponto] = centróide_mais_próximo(ponto, centróides)
        
        para cada cluster c:
            centróides[c] = média(pontos_do_cluster_c)
    
    retornar clusters, centróides
```

### Scikit-learn

```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# SEMPRE escalar antes de clustering!
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Treinar K-Means
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = kmeans.fit_predict(X_scaled)

# Resultados
print(f"Centróides: {kmeans.cluster_centers_}")
print(f"Inércia: {kmeans.inertia_}")  # soma das distâncias ao quadrado
```

### Limitações do K-Means

| Limitação | Por quê? | Solução |
|-----------|----------|---------|
| Precisa definir K | Não descobre automaticamente | Elbow / Silhouette |
| Clusters esféricos | Assume formato circular | Usar DBSCAN (Dia 2) |
| Sensível a outliers | Centróide puxado por extremos | Remover outliers antes |
| Sensível à escala | Distância domina features maiores | StandardScaler |

---

## 4. Como Escolher K?

### Método do Cotovelo (Elbow Method)

Plota a **inércia** (soma das distâncias intra-cluster) para diferentes valores de K:

```python
inertias = []
K_range = range(2, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)

plt.plot(K_range, inertias, 'bo-')
plt.xlabel('Número de Clusters (K)')
plt.ylabel('Inércia')
plt.title('Método do Cotovelo')
plt.show()
```

> O "cotovelo" é onde a curva **para de cair significativamente**. Depois desse ponto, adicionar mais clusters não melhora muito.

### Silhouette Score

Mede a **qualidade** dos clusters (-1 a 1):

$$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$$

Onde:
- $a(i)$ = distância média aos pontos do **mesmo cluster**
- $b(i)$ = distância média aos pontos do **cluster mais próximo**

| Valor | Significado |
|-------|-------------|
| ~1.0 | Clusters bem separados |
| ~0.0 | Sobrepostos |
| < 0 | Ponto provavelmente no cluster errado |

```python
from sklearn.metrics import silhouette_score

scores = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X_scaled)
    score = silhouette_score(X_scaled, labels)
    scores.append(score)
    print(f"K={k}: Silhouette = {score:.3f}")
```

> 📌 **Na prática:** use os dois métodos juntos. O Elbow sugere uma faixa, o Silhouette confirma o melhor K.

---

## 5. Clustering Hierárquico

### Diferença Fundamental

| Aspecto | K-Means | Hierárquico |
|---------|---------|-------------|
| Define K antes? | Sim | Não (corta depois) |
| Resultado visual | Scatter plot | **Dendrograma** |
| Complexidade | O(n·K·iter) | O(n²) ou O(n³) |
| Melhor para | Datasets grandes | Datasets pequenos/médios |

### Tipos

- **Aglomerativo** (bottom-up): cada ponto começa como cluster → vai juntando
- **Divisivo** (top-down): tudo começa como 1 cluster → vai dividindo

### Como Funciona (Aglomerativo)

1. Cada ponto = 1 cluster
2. Encontrar os 2 clusters mais próximos
3. Juntar em 1 cluster
4. Repetir até ter 1 cluster (ou K clusters)

### Dendrograma

O dendrograma mostra a **hierarquia** de merges:

```python
from scipy.cluster.hierarchy import dendrogram, linkage

# Calcular linkage
Z = linkage(X_scaled, method='ward')  # ward minimiza variância

# Plotar dendrograma
plt.figure(figsize=(12, 6))
dendrogram(Z, truncate_mode='lastp', p=20)
plt.title('Dendrograma - Clustering Hierárquico')
plt.xlabel('Amostras')
plt.ylabel('Distância')
plt.axhline(y=threshold, color='r', linestyle='--', label='Corte')
plt.show()
```

### Métodos de Linkage

| Método | Distância entre clusters | Quando usar |
|--------|------------------------|-------------|
| **ward** | Minimiza variância total | Mais comum, clusters compactos |
| single | Mínima entre pontos | Clusters alongados |
| complete | Máxima entre pontos | Clusters compactos |
| average | Média entre pontos | Equilíbrio |

### Scikit-learn

```python
from sklearn.cluster import AgglomerativeClustering

agg = AgglomerativeClustering(n_clusters=3, linkage='ward')
labels = agg.fit_predict(X_scaled)
```

---

## 6. Comparação: K-Means vs Hierárquico

| Critério | K-Means | Hierárquico |
|----------|---------|-------------|
| Velocidade | ✅ Rápido | ❌ Lento (n²) |
| Escalabilidade | ✅ Datasets grandes | ❌ < 10k pontos |
| Forma dos clusters | Esféricos | Qualquer forma |
| Número de clusters | Definir antes | Pode escolher depois |
| Interpretabilidade | Centróides | Dendrograma |
| Determinístico | ❌ (depende da inicialização) | ✅ Sempre o mesmo |

### Quando Usar Cada Um?

```
Escolhendo entre K-Means e Hierárquico:

1. Dataset grande (>10k pontos)?
   → K-Means ✅

2. Não sabe quantos clusters?
   → Hierárquico (olhar dendrograma) ✅

3. Precisa de centróides para interpretar?
   → K-Means ✅

4. Quer explorar diferentes "resoluções" de agrupamento?
   → Hierárquico (cortando em alturas diferentes) ✅
```

---

## 7. Dicas e Armadilhas

### ✅ Boas Práticas
1. **Sempre escalar** os dados antes de clustering (StandardScaler)
2. **Testar vários K** e comparar com Elbow + Silhouette
3. **Visualizar** os clusters (PCA 2D se necessário)
4. **Interpretar** os centróides — não basta agrupar, precisa entender o que cada cluster significa
5. **Rodar múltiplas vezes** com seeds diferentes (K-Means não é determinístico)

### ❌ Armadilhas Comuns
1. **Não escalar:** feature com range [0, 100000] domina a distância
2. **Escolher K arbitrariamente:** sempre validar com métricas
3. **Clustering sem propósito:** "agrupei, e daí?" — sempre ter uma pergunta de negócio
4. **Ignorar outliers:** podem distorcer centróides do K-Means
5. **Assumir que clusters = verdade:** clustering é exploratório, não definitivo

---

## 8. Exercícios

### Exercício 1: Conceitual
Você tem dados de despesas com as colunas: `valor`, `dia_do_mes`, `categoria`.  
Antes de aplicar K-Means, o que você **deve** fazer com os dados?

<details>
<summary>Resposta</summary>

1. **Escalar** com StandardScaler (valor tem range diferente de dia_do_mes)
2. **Codificar** categoria (One-Hot ou similar — K-Means trabalha com números)
3. **Tratar outliers** (despesas muito altas podem distorcer)

</details>

### Exercício 2: Interpretação
Você rodou K-Means com K=3 e obteve:
- Silhouette Score = 0.45
- Cluster 0: média R$25, categoria "alimentação", dia ~15
- Cluster 1: média R$350, categoria "moradia", dia ~5
- Cluster 2: média R$80, categoria "lazer", dia ~20

O que esses clusters representam?

<details>
<summary>Resposta</summary>

- **Cluster 0:** Gastos pequenos do cotidiano (alimentação, meado do mês)
- **Cluster 1:** Despesas fixas grandes (moradia/aluguel, início do mês)
- **Cluster 2:** Gastos moderados de lazer (finais de semana/fim do mês)
- Silhouette 0.45 = separação razoável (não perfeita, mas útil)

</details>

### Exercício 3: Prático
Ao olhar seu dendrograma, você vê 3 branches principais que se juntam em alturas muito diferentes. O que isso sugere sobre seus dados?

<details>
<summary>Resposta</summary>

Sugere que K=3 é um bom número de clusters! As alturas diferentes indicam que os 3 grupos são bastante distintos entre si. Se os branches se juntassem em alturas similares, a separação entre clusters seria menos clara.

</details>

---

## 📚 Referências

- [Scikit-learn: Clustering](https://scikit-learn.org/stable/modules/clustering.html)
- [K-Means Visualization](https://www.naftaliharris.com/blog/visualizing-k-means-clustering/)
- [Silhouette Analysis](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html)

---

**Próximo:** [Dia 2 - DBSCAN + Detecção de Anomalias](21-dia2-semana5-dbscan-anomalias.md)
