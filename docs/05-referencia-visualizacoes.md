# 📊 Guia de Referência: Visualizações com Matplotlib e Seaborn

**Data:** 28 Outubro 2025  
**Contexto:** Semana 2 - Dia 1 (EDA Titanic)

---

## 🎨 **Conceitos Básicos**

### **plt = matplotlib.pyplot**
É a biblioteca principal para criar gráficos em Python.

```python
import matplotlib.pyplot as plt
```

---

## 📏 **figsize - Tamanho da Figura**

Define o tamanho do gráfico em **polegadas** (largura, altura).

```python
plt.figure(figsize=(10, 6))  # 10 polegadas de largura x 6 de altura
```

**Regra prática:**
- `(10, 6)` → Gráfico médio/padrão
- `(12, 8)` → Gráfico grande
- `(8, 5)` → Gráfico pequeno
- `(14, 5)` → Gráfico largo (comparações lado a lado)

---

## 🎨 **Paletas de Cores (palette)**

### **viridis** 
Paleta sequencial com bom contraste, acessível para daltônicos.

```python
sns.countplot(data=df, x='survived', palette='viridis')
```

### **Outras paletas úteis:**

| Paleta | Tipo | Quando usar |
|--------|------|-------------|
| `viridis` | Sequencial | Gráficos simples, contraste suave |
| `Set1` | Qualitativa | Categorias distintas (2-9 cores) |
| `Set2` | Qualitativa | Tons pastéis, mais suaves |
| `coolwarm` | Divergente | Correlações (negativo ↔ positivo) |
| `husl` | Qualitativa | Muitas categorias, cores variadas |
| `rocket` | Sequencial | Dados com intensidade crescente |

**Referência:** [Seaborn Color Palettes](https://seaborn.pydata.org/tutorial/color_palettes.html)

---

## 📊 **Tipos de Gráficos**

### 1. **countplot** - Contagem de Categorias

Conta quantas vezes cada categoria aparece nos dados.

```python
sns.countplot(data=df, x='survived', palette='viridis')
```

**Uso:**
- Distribuição de classes (sobreviveu: sim/não)
- Contagem de categorias (masculino/feminino)

**Equivalente:** Histograma para dados categóricos

---

### 2. **subplots** - Múltiplos Gráficos Lado a Lado

Cria uma grade de gráficos.

```python
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
#                         ↑  ↑
#                      linhas colunas
```

**Interpretação:**
- `(1, 2)` = 1 linha, 2 colunas = 2 gráficos lado a lado
- `(2, 1)` = 2 linhas, 1 coluna = 2 gráficos empilhados
- `(2, 2)` = 2x2 = 4 gráficos em grade

**Acessar cada gráfico:**
```python
fig, axes = plt.subplots(1, 2)

# Plotar no primeiro gráfico
sns.countplot(..., ax=axes[0])

# Plotar no segundo gráfico
sns.countplot(..., ax=axes[1])
```

---

### 3. **Gráfico de Distribuição de Idade** 📈

```python
plt.subplot(1, 2, 1)  # Primeiro gráfico (histograma)
df['age'].hist(bins=30, edgecolor='black', alpha=0.7)

plt.subplot(1, 2, 2)  # Segundo gráfico (boxplot)
df.boxplot(column='age', by='survived')
```

#### **Explicação detalhada:**

##### **A) Histograma (esquerda)**
```python
df['age'].hist(bins=30)
```

- **bins=30** → Divide as idades em 30 "caixas" (intervalos)
  - Exemplo: 0-3 anos, 3-6 anos, 6-9 anos... até 80 anos
- **Eixo X:** Idade
- **Eixo Y:** Frequência (quantas pessoas em cada faixa etária)

**O que você vê:**
- Pico entre 20-30 anos → Maioria dos passageiros era jovem adulto
- Poucos bebês/crianças
- Poucos idosos acima de 60 anos

##### **B) Boxplot (direita)**
```python
df.boxplot(column='age', by='survived')
```

**O que é um Boxplot?**

```
        Outliers (pontos isolados)
            ●
            │
    ┌───────┼───────┐
    │       │       │
────┼───────■───────┼──── 
    │       │       │
    └───────┼───────┘
            │
            ●
    
    │       │       │
   Min    Q1  Mediana Q3   Max
          (25%)  (50%)  (75%)
```

**Elementos:**
- **Linha central** = Mediana (50% dos dados)
- **Caixa** = 50% dos dados centrais (Q1 a Q3)
- **Linhas** (whiskers) = Extensão até valores máximos/mínimos
- **Pontos isolados** = Outliers (valores extremos)

**No gráfico de idade:**
- Compara distribuição de idade entre:
  - `survived=0` (não sobreviveu)
  - `survived=1` (sobreviveu)

**Insight possível:**
- Se as medianas forem diferentes → Idade influenciou sobrevivência
- Se houver muitos outliers → Idosos/crianças são casos especiais

---

## 🔧 **Comandos Essenciais**

### Configurar gráfico
```python
plt.figure(figsize=(10, 6))           # Tamanho
plt.title('Título', fontsize=14)      # Título
plt.xlabel('Eixo X')                  # Rótulo X
plt.ylabel('Eixo Y')                  # Rótulo Y
plt.legend(['Label 1', 'Label 2'])    # Legenda
```

### Finalizar gráfico
```python
plt.tight_layout()  # Ajusta espaçamento automático
plt.show()          # Exibe o gráfico
```

### Adicionar texto
```python
plt.text(x, y, 'Texto', ha='center', fontweight='bold')
#        ↑  ↑   ↑       ↑            ↑
#      pos pos texto  alinhamento   negrito
```

---

## 📚 **Referências Online**

### **Matplotlib**
- [Documentação Oficial](https://matplotlib.org/stable/contents.html)
- [Gallery de Exemplos](https://matplotlib.org/stable/gallery/index.html) ⭐
- [Pyplot Tutorial](https://matplotlib.org/stable/tutorials/introductory/pyplot.html)

### **Seaborn**
- [Documentação Oficial](https://seaborn.pydata.org/)
- [Gallery de Exemplos](https://seaborn.pydata.org/examples/index.html) ⭐
- [Tutorial de Visualizações](https://seaborn.pydata.org/tutorial.html)

### **Cheat Sheets (Cola Visual)**
- [Matplotlib Cheat Sheet (PDF)](https://matplotlib.org/cheatsheets/)
- [Seaborn Cheat Sheet](https://seaborn.pydata.org/_images/function_overview_8_0.png)

---

## 🎯 **Dicas Práticas**

### 1. **Escolher o gráfico certo**

| Objetivo | Gráfico |
|----------|---------|
| Contagem de categorias | `countplot`, `barplot` |
| Distribuição numérica | `histplot`, `kdeplot` |
| Comparar grupos | `boxplot`, `violinplot` |
| Relação entre variáveis | `scatterplot`, `lineplot` |
| Correlações | `heatmap` |

### 2. **Explorar exemplos visuais**

Sempre que precisar de inspiração:
1. Acesse a **Gallery** do Matplotlib/Seaborn
2. Encontre um gráfico similar ao que precisa
3. Copie e adapte o código

### 3. **Experimentar no notebook**

```python
# Teste diferentes paletas
for palette in ['viridis', 'Set1', 'coolwarm', 'rocket']:
    sns.countplot(data=df, x='survived', palette=palette)
    plt.title(f'Paleta: {palette}')
    plt.show()
```

---

## 💡 **Resumo Rápido**

```python
# Template básico de visualização
plt.figure(figsize=(10, 6))           # Tamanho
sns.TIPO_GRAFICO(data=df, x='col')    # Gráfico
plt.title('Título')                   # Título
plt.xlabel('X')                       # Eixo X
plt.ylabel('Y')                       # Eixo Y
plt.tight_layout()                    # Ajustar
plt.show()                            # Exibir
```

**Substitua `TIPO_GRAFICO` por:**
- `countplot` → Contagem
- `histplot` → Histograma
- `boxplot` → Boxplot
- `scatterplot` → Dispersão
- `heatmap` → Mapa de calor

---

**🚀 Mantenha esse guia aberto durante suas análises!**
