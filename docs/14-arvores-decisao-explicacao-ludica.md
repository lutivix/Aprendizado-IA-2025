# 🌳 Árvores de Decisão: Explicação Lúdica e Didática

**Data:** 11/11/2025  
**Tema:** Como funcionam as Árvores de Decisão e seus hiperparâmetros

---

## 🎯 O que é uma Árvore de Decisão?

Imagine que você é um **médico veterinário** tentando identificar se um animal é um **cachorro** ou um **gato** fazendo perguntas do tipo "sim/não":

```
                    [Tem mais de 10kg?]
                          /        \
                       SIM          NÃO
                        /              \
              [Late muito?]        [Ronrona?]
                /      \              /      \
             SIM      NÃO          SIM      NÃO
              |        |            |        |
          CACHORRO  CACHORRO      GATO    GATO
```

Cada **pergunta** é um **nó** (node), cada **resposta** é um **ramo** (branch), e cada **conclusão** é uma **folha** (leaf).

---

## 🎮 Exemplo Lúdico: "Devo Jogar Futebol Hoje?"

Vamos criar uma árvore de decisão para decidir se você deve jogar futebol:

### 📊 Dataset de Exemplo:

| Clima | Temperatura | Vento | Cansado? | **Jogar?** |
|-------|-------------|-------|----------|---------|
| Sol   | 25°C        | Fraco | Não      | ✅ SIM  |
| Chuva | 15°C        | Forte | Não      | ❌ NÃO  |
| Sol   | 30°C        | Fraco | Sim      | ❌ NÃO  |
| Nublado | 20°C      | Fraco | Não      | ✅ SIM  |
| Chuva | 10°C        | Forte | Sim      | ❌ NÃO  |
| Sol   | 28°C        | Médio | Não      | ✅ SIM  |

### 🌳 Árvore de Decisão Resultante:

```
                    [Está chovendo?]
                         /        \
                      SIM          NÃO
                       |             \
                   ❌ NÃO        [Temperatura > 28°C?]
                                      /           \
                                   SIM            NÃO
                                    |               \
                                ❌ NÃO          [Estou cansado?]
                                                   /         \
                                                SIM          NÃO
                                                 |            |
                                             ❌ NÃO        ✅ SIM
```

---

## 🎛️ Hiperparâmetros Explicados de Forma Lúdica

### 1️⃣ **max_depth** (Profundidade Máxima)

**Analogia:** Quantas perguntas você pode fazer antes de tomar uma decisão?

#### Exemplo: "Escolher um Filme"

**max_depth = 1** (Muito simples - UNDERFITTING)
```
        [É ação?]
         /     \
      SIM      NÃO
       |        |
   Vingadores Romance
```
❌ **Problema:** Muito genérico! E se eu gosto de comédia de ação?

---

**max_depth = 3** (Balanceado)
```
                [É ação?]
                 /     \
              SIM      NÃO
               |         \
        [Tem humor?]   [É romance?]
           /    \         /      \
        SIM    NÃO     SIM      NÃO
         |      |       |        |
      DeadPool Matrix  Titanic  Drama
```
✅ **Ideal:** Detalhado o suficiente, mas não exagerado!

---

**max_depth = 10** (Muito complexo - OVERFITTING)
```
[É ação?] → [Tem humor?] → [Ano > 2015?] → [Diretor é X?] 
  → [Ator principal é Y?] → [Orçamento > 100M?] → ...
```
❌ **Problema:** Tão específico que só funciona para os filmes que você JÁ viu! Não generaliza para filmes novos.

#### 📊 Comparação Visual:

```
max_depth = 1:  🌱 (plantinha)     → Simples demais
max_depth = 5:  🌳 (árvore)        → Equilibrado ✅
max_depth = 20: 🌴🌿🍃 (floresta) → Complexo demais
```

---

### 2️⃣ **min_samples_split** (Mínimo de Amostras para Dividir)

**Analogia:** Quantas pessoas devem votar antes de você fazer uma nova pergunta?

#### Exemplo: "Escolher Música na Festa"

Você tem 100 pessoas na festa e quer escolher música.

**min_samples_split = 2** (Divide muito!)
```
[Rock?] → [Hard Rock?] → [Metal progressivo?] → [Death Metal sueco?]
```
❌ **Problema:** Você faz perguntas tão específicas que cada pessoa tem seu próprio gênero! Festa vira um caos.

---

**min_samples_split = 20** (Balanceado)
```
[Rock?] → [Pesado ou Leve?]
          ✅ Para aqui se menos de 20 pessoas
```
✅ **Ideal:** Só divide em subgrupos se tiver gente suficiente para justificar.

---

**min_samples_split = 50** (Muito conservador)
```
[Rock ou Pop?]
  ✅ Não divide mais (menos de 50 por grupo)
```
⚠️ **Problema:** Às vezes, deixa grupos muito genéricos (underfitting).

#### 🎯 Regra de Ouro:
- Dataset pequeno (< 1000)? → Use 10-20
- Dataset grande (> 10k)? → Use 50-100

---

### 3️⃣ **min_samples_leaf** (Mínimo de Amostras por Folha)

**Analogia:** Quantas pessoas devem concordar com a decisão final?

#### Exemplo: "Classificar Frutas"

Você tem 1000 frutas para classificar.

**min_samples_leaf = 1** (Aceita qualquer decisão!)
```
Resultado: "Esta maçã é especial porque tem exatamente 3 manchas e 2cm!"
```
❌ **Problema:** Decisões baseadas em frutas individuais (overfitting!). Não generaliza.

---

**min_samples_leaf = 5** (Balanceado)
```
Resultado: "Maçãs são frutas vermelhas, médias, com casca lisa"
```
✅ **Ideal:** Decisão baseada em pelo menos 5 frutas similares.

---

**min_samples_leaf = 50** (Muito genérico)
```
Resultado: "Tudo é fruta redonda"
```
⚠️ **Problema:** Perde detalhes importantes (underfitting).

#### 📊 Impacto Visual:

```
min_samples_leaf = 1:  🍎 (cada fruta é única)      → Overfitting
min_samples_leaf = 5:  🍎🍎🍎🍎🍎 (grupo pequeno)  → Equilibrado ✅
min_samples_leaf = 50: 🍎x50 (grupo grande)         → Underfitting
```

---

### 4️⃣ **n_estimators** (Número de Árvores) - Para Random Forest

**Analogia:** Quantos especialistas você consulta antes de decidir?

#### Exemplo: "Diagnóstico Médico"

**n_estimators = 1** (Opinião de 1 médico)
```
Médico: "É gripe!"
```
⚠️ **Problema:** E se ele errou? Sem segunda opinião.

---

**n_estimators = 10** (Opinião de 10 médicos)
```
8 médicos: "Gripe"
2 médicos: "Resfriado"
Resultado: GRIPE (maioria vota)
```
✅ **Melhor:** Mais confiável, mas ainda pode melhorar.

---

**n_estimators = 100** (Opinião de 100 médicos)
```
85 médicos: "Gripe"
12 médicos: "Resfriado"
3 médicos: "Alergia"
Resultado: GRIPE (forte consenso)
```
✅ **Ideal:** Muito confiável! Mas leva mais tempo.

---

**n_estimators = 1000** (Opinião de 1000 médicos)
```
Resultado: Mesmo que 100, mas MUITO LENTO 🐌
```
⚠️ **Custo-benefício:** Ganho marginal não compensa o tempo.

#### 📊 Relação Performance vs Tempo:

```
n_estimators:   10    50    100   200   500   1000
Performance:    ★★☆   ★★★   ★★★★  ★★★★  ★★★★★ ★★★★★
Tempo:          ⚡    ⚡⚡   ⚡⚡⚡  ⚡⚡⚡⚡ 🐌    🐌🐌
```

**Sweet spot:** 100-300 (bom equilíbrio)

---

### 5️⃣ **max_features** (Máximo de Features por Split)

**Analogia:** Quantas características você considera em cada decisão?

#### Exemplo: "Escolher um Carro"

Você tem 10 características: cor, preço, marca, ano, potência, consumo, portas, ar-condicionado, direção, câmbio.

**max_features = None** (Considera TODAS)
```
Decisão: Considera todos os 10 fatores a cada pergunta
```
⚠️ **Problema:** Árvores muito similares em Random Forest (menos diversidade).

---

**max_features = 'sqrt'** (√10 ≈ 3 features)
```
Árvore 1: [Preço, Marca, Ano]
Árvore 2: [Consumo, Potência, Portas]
Árvore 3: [Cor, Ar-condicionado, Câmbio]
```
✅ **Ideal:** Cada árvore é diferente! Mais diversidade = melhor votação.

---

**max_features = 'log2'** (log₂(10) ≈ 3.3 features)
```
Similar ao sqrt, mas um pouco mais conservador
```
✅ **Bom para:** Datasets com muitas features correlacionadas.

#### 🎯 Quando usar cada um:

- **'sqrt'**: Classificação (padrão) ✅
- **'log2'**: Muitas features correlacionadas
- **None**: Quando você tem poucas features (<10)

---

## 🏗️ Como uma Árvore Aprende? (Passo a Passo)

### Exemplo: "Aprovar Empréstimo Bancário"

**Dataset:**
| Salário | Idade | Histórico | **Aprovado?** |
|---------|-------|-----------|--------------|
| Alto    | 35    | Bom       | ✅ SIM       |
| Baixo   | 25    | Ruim      | ❌ NÃO       |
| Médio   | 45    | Bom       | ✅ SIM       |
| Alto    | 22    | Ruim      | ❌ NÃO       |
| Baixo   | 55    | Bom       | ✅ SIM       |

### 🔍 Passo 1: Escolher a Melhor Pergunta

A árvore testa **todas** as possibilidades:
- "Salário > 50k?"
- "Idade > 30?"
- "Histórico = Bom?"

**Critério:** Qual pergunta **separa melhor** os dados?

#### Medindo "Separação" com Gini Impurity:

```python
# Antes de dividir:
Mistura: [✅✅✅ ❌❌] = 60% SIM, 40% NÃO
Gini = 0.48 (muito misturado! 🔀)

# Depois de perguntar "Histórico = Bom?":
Ramo SIM: [✅✅✅] = 100% SIM → Gini = 0.0 (perfeito! ✨)
Ramo NÃO: [❌❌] = 100% NÃO → Gini = 0.0 (perfeito! ✨)

🎯 Ganho = 0.48 - 0.0 = MÁXIMO! (melhor split possível)
```

### 🔍 Passo 2: Dividir os Dados

```
                [Histórico = Bom?]
                     /        \
                  SIM          NÃO
                   |            |
              ✅ APROVAR    ❌ NEGAR
```

### 🔍 Passo 3: Repetir nos Sub-ramos

Se ainda houver **mistura** (Gini > 0), continua dividindo:

```
                [Histórico = Bom?]
                     /        \
                  SIM          NÃO
                   |            |
            [Salário > 50k?]  ❌ NEGAR
               /        \
            SIM         NÃO
             |           |
        ✅ APROVAR   [Idade > 30?]
                        /      \
                     SIM       NÃO
                      |         |
                 ✅ APROVAR  ❌ NEGAR
```

### 🛑 Quando Parar?

A árvore para de crescer quando **qualquer um** acontece:

1. ✅ **Pureza total:** Todos são SIM ou NÃO (Gini = 0)
2. 🎛️ **max_depth:** Atingiu profundidade máxima
3. 🎛️ **min_samples_split:** Não há amostras suficientes para dividir
4. 🎛️ **min_samples_leaf:** Divisão criaria folhas muito pequenas

---

## 🎓 Relação entre Hiperparâmetros e Overfitting/Underfitting

### 🌡️ Termômetro do Modelo:

```
❄️ UNDERFITTING          🌡️ IDEAL          🔥 OVERFITTING
(Muito Simples)       (Balanceado)       (Muito Complexo)
     
     🌱                    🌳                  🌴🌿🍃
   1 folha             10 folhas            1000 folhas
   
Erro Alto             Erro Baixo           Train: Erro 0%
Treino: 70%           Treino: 85%          Test: 60% ⚠️
Teste: 65%            Teste: 83% ✅        
```

### 🎛️ Como Ajustar:

#### Se você tem UNDERFITTING (modelo simples demais):
```python
# ❌ Antes:
model = RandomForestClassifier(
    max_depth=3,          # Muito raso
    min_samples_leaf=20   # Muito conservador
)

# ✅ Depois:
model = RandomForestClassifier(
    max_depth=10,         # ↑ Mais profundo
    min_samples_leaf=5    # ↓ Menos restritivo
)
```

#### Se você tem OVERFITTING (modelo complexo demais):
```python
# ❌ Antes:
model = RandomForestClassifier(
    max_depth=None,       # Sem limite
    min_samples_leaf=1    # Aceita tudo
)

# ✅ Depois:
model = RandomForestClassifier(
    max_depth=15,         # ↓ Limitar profundidade
    min_samples_leaf=5,   # ↑ Mais amostras por folha
    min_samples_split=10  # ↑ Mais amostras para dividir
)
```

---

## 🎮 Exemplo Completo: "Prever se Aluno Passa de Ano"

### 📊 Dataset:

| Horas Estudo/dia | Faltas | Nota Anterior | **Passou?** |
|------------------|--------|---------------|-------------|
| 5                | 2      | 8.5           | ✅ SIM      |
| 1                | 10     | 5.0           | ❌ NÃO      |
| 3                | 5      | 7.0           | ✅ SIM      |
| 0.5              | 15     | 4.0           | ❌ NÃO      |
| 4                | 3      | 8.0           | ✅ SIM      |
| 2                | 8      | 6.0           | ❌ NÃO      |

### 🌳 Árvore Treinada (max_depth=2):

```
                    [Horas Estudo > 2.5?]
                         /            \
                      SIM              NÃO
                       |                 \
                  [Faltas < 6?]      [Nota Anterior > 5.5?]
                    /      \              /           \
                 SIM      NÃO          SIM           NÃO
                  |        |            |             |
              ✅ SIM    ❌ NÃO       ✅ SIM         ❌ NÃO
```

### 🎯 Interpretação:

1. **Primeira pergunta:** "Estuda mais de 2.5h/dia?"
   - Se SIM → Bom começo! Próxima pergunta...
   - Se NÃO → Depende da nota anterior

2. **Segunda pergunta (se estuda):** "Faltou menos de 6 vezes?"
   - Se SIM → ✅ PASSA (estudioso + presente)
   - Se NÃO → ❌ REPROVA (estuda mas falta muito)

3. **Segunda pergunta (se não estuda):** "Nota anterior > 5.5?"
   - Se SIM → ✅ PASSA (talvez seja inteligente)
   - Se NÃO → ❌ REPROVA (não estuda E vai mal)

### 📊 Performance:

```python
# Modelo com hiperparâmetros ruins:
model_ruim = RandomForestClassifier(max_depth=1, n_estimators=10)
# Resultado: 70% accuracy (UNDERFITTING)

# Modelo balanceado:
model_bom = RandomForestClassifier(max_depth=5, n_estimators=100)
# Resultado: 85% accuracy ✅

# Modelo overfitted:
model_complexo = RandomForestClassifier(max_depth=None, n_estimators=500)
# Resultado: Train 98%, Test 75% (OVERFITTING)
```

---

## 🎓 Resumo Final: Cheat Sheet

### 🎯 Valores Recomendados por Tamanho de Dataset:

| Dataset        | max_depth | min_samples_leaf | n_estimators |
|----------------|-----------|------------------|--------------|
| Pequeno (<1k)  | 5-10      | 5-10             | 100          |
| Médio (1k-10k) | 10-20     | 2-5              | 100-200      |
| Grande (>10k)  | 15-30     | 1-2              | 200-300      |

### 🎛️ Ajuste Rápido:

#### 📉 Seu modelo está RUIM no TREINO? (Underfitting)
```
✅ Aumentar: max_depth, n_estimators
❌ Diminuir: min_samples_leaf, min_samples_split
```

#### 📉 Seu modelo está BOM no TREINO mas RUIM no TESTE? (Overfitting)
```
❌ Diminuir: max_depth, n_estimators (ou parar de aumentar)
✅ Aumentar: min_samples_leaf, min_samples_split
✅ Adicionar: max_features='sqrt'
```

### 💡 Dica de Ouro:

> **"Comece simples, aumente aos poucos!"**
>
> 1. Inicie com valores padrão
> 2. Avalie train vs test accuracy
> 3. Se underfitting → ↑ complexidade
> 4. Se overfitting → ↓ complexidade
> 5. Use Grid Search para automatizar

---

## 🔗 Recursos Adicionais

- 📘 **Visualizar árvores:** Use `plot_tree()` do scikit-learn
- 🎮 **Interactive decision tree:** [R2D3 Visual Intro](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/)
- 📊 **Curso recomendado:** Veja notebook `01-ml-supervisionado-avancado.ipynb`

---

**Criado por:** GitHub Copilot  
**Data:** 11/11/2025  
**Projeto:** Aprendizado-IA-2025 - Semana 3
