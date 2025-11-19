# 🧪 Teste de Validação - Semana 1: Fundamentos de IA/ML

## ⏱️ Tempo estimado: 15 minutos

---

## 📋 Parte 1: Conceitos Fundamentais (múltipla escolha)

### Questão 1: Tipos de Machine Learning
Você precisa criar um sistema que identifica se um e-mail é spam ou não spam. Qual tipo de ML você usaria?

**A)** Aprendizado Não-Supervisionado  
**B)** Aprendizado Supervisionado  
**C)** Aprendizado por Reforço  
**D)** Não é possível com ML  

<details>
<summary>💡 Ver resposta</summary>

**Resposta: B) Aprendizado Supervisionado**

**Por quê:**
- O problema tem **labels claros** (spam ou não-spam)
- Você tem **exemplos rotulados** para treinar
- O objetivo é **classificar** novos e-mails

**Aprendizado Supervisionado:**
- Requer dados rotulados (X → y)
- Usado para classificação e regressão
- Exemplos: spam detection, previsão de preços, diagnóstico médico

**Quando usar cada tipo:**
- **Supervisionado:** Tenho labels (spam/não-spam, preço, doença/saudável)
- **Não-Supervisionado:** Não tenho labels (agrupar clientes similares)
- **Reforço:** Decisões sequenciais (jogo, robótica, trading)

**Conceito-chave:** Se você tem a "resposta certa" nos dados de treino, é supervisionado!
</details>

---

### Questão 2: Features e Target
Você tem este dataset de casas:

```python
import pandas as pd

df = pd.DataFrame({
    'area': [100, 150, 80, 200],
    'quartos': [2, 3, 2, 4],
    'idade': [5, 10, 2, 15],
    'preco': [300000, 450000, 250000, 600000]
})
```

Se você quer **prever o preço**, o que são as **features** e o que é o **target**?

**A)** Features: preco | Target: area, quartos, idade  
**B)** Features: area, quartos, idade | Target: preco  
**C)** Features: area, quartos | Target: idade, preco  
**D)** Todas são features  

<details>
<summary>💡 Ver resposta</summary>

**Resposta: B) Features: area, quartos, idade | Target: preco**

**Por quê:**

**Features (X):**
- São as **variáveis independentes**
- Informações que você **TEM** sobre o problema
- Usadas para **fazer a previsão**
- No exemplo: `area`, `quartos`, `idade`

**Target (y):**
- É a **variável dependente**
- O que você **QUER PREVER**
- No exemplo: `preco`

**Código correto:**
```python
# Separar features e target
X = df[['area', 'quartos', 'idade']]  # Features
y = df['preco']                        # Target

# Ou usando drop:
X = df.drop('preco', axis=1)  # Remove o target
y = df['preco']                # Pega apenas o target
```

**Conceito-chave:** 
- **Features = O que você usa para prever**
- **Target = O que você quer prever**

**Analogia:**
```
Previsão do tempo:
Features: temperatura de ontem, umidade, pressão
Target: vai chover hoje? (sim/não)
```
</details>

---

### Questão 3: Train/Test Split
Por que dividimos os dados em treino e teste?

**A)** Para o modelo treinar mais rápido  
**B)** Para economizar memória  
**C)** Para avaliar se o modelo generaliza para dados novos  
**D)** Para visualizar os dados melhor  

<details>
<summary>💡 Ver resposta</summary>

**Resposta: C) Para avaliar se o modelo generaliza para dados novos**

**Por quê:**

**O Problema:**
```python
# Se treinar e testar nos MESMOS dados:
model.fit(X, y)           # Treina com todos os dados
score = model.score(X, y) # Testa nos mesmos dados = 100%! 😱

# Mas o modelo pode ter DECORADO, não APRENDIDO!
```

**A Solução:**
```python
# Dividir em treino e teste:
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model.fit(X_train, y_train)        # Treina com 80%
score = model.score(X_test, y_test) # Testa com 20% nunca vistos
```

**Analogia:**
```
❌ Estudar as respostas da prova antes de fazer
   = 100% de nota, mas não aprendeu!

✅ Estudar com exercícios A, fazer prova com exercícios B
   = Nota real mostra se realmente aprendeu
```

**Proporções comuns:**
- **80-20:** Padrão (80% treino, 20% teste)
- **70-30:** Dataset médio
- **90-10:** Dataset muito pequeno

**Conceito-chave:** Test set simula dados do "mundo real" que o modelo nunca viu!
</details>

---

### Questão 4: Overfitting vs Underfitting
Observe estes resultados:

**Modelo A:**
- Train accuracy: 99%
- Test accuracy: 60%

**Modelo B:**
- Train accuracy: 65%
- Test accuracy: 63%

**Modelo C:**
- Train accuracy: 85%
- Test accuracy: 82%

Qual modelo está em overfitting? Qual em underfitting? Qual está bom?

**A)** Overfitting: A | Underfitting: B | Bom: C  
**B)** Overfitting: B | Underfitting: A | Bom: C  
**C)** Overfitting: C | Underfitting: A | Bom: B  
**D)** Todos estão em overfitting  

<details>
<summary>💡 Ver resposta</summary>

**Resposta: A) Overfitting: A | Underfitting: B | Bom: C**

**Análise Detalhada:**

### 🔴 Modelo A - OVERFITTING
```
Train: 99% | Test: 60%
Diferença: 39% ← MUITO ALTO!
```
**Problema:** Modelo **decorou** os dados de treino, não generalizou.

**Sintomas:**
- Train accuracy muito alta
- Test accuracy muito baixa
- Grande diferença entre train e test (>15%)

**Causa:**
- Modelo muito complexo
- Muitas features irrelevantes
- Poucos dados de treino

**Solução:**
```python
# Simplificar o modelo
RandomForestClassifier(
    max_depth=5,           # Limita profundidade
    min_samples_split=20   # Exige mais dados para dividir
)

# Ou adicionar mais dados de treino
```

---

### 🟡 Modelo B - UNDERFITTING
```
Train: 65% | Test: 63%
Ambos baixos!
```
**Problema:** Modelo muito **simples**, não captura padrões.

**Sintomas:**
- Train accuracy baixa
- Test accuracy baixa
- Diferença pequena (modelo consistente, mas ruim)

**Causa:**
- Modelo muito simples
- Poucas features
- Features não informativas

**Solução:**
```python
# Aumentar complexidade
RandomForestClassifier(
    max_depth=15,          # Permite mais profundidade
    n_estimators=200       # Mais árvores
)

# Ou adicionar mais features relevantes
```

---

### 🟢 Modelo C - BOM (IDEAL)
```
Train: 85% | Test: 82%
Diferença: 3% ← BOM!
```
**Resultado:** Modelo generaliza bem!

**Características:**
- Train e Test próximos (diferença <5-10%)
- Accuracies razoáveis (>80% depende do problema)
- Modelo equilibrado

---

### 📊 Resumo Visual:

```
                 Train  Test  Diferença  Diagnóstico
Modelo A (❌)    99%    60%   39%        Overfitting
Modelo B (⚠️)    65%    63%   2%         Underfitting
Modelo C (✅)    85%    82%   3%         Bom!
```

**Conceito-chave:** Busque **equilíbrio** entre train e test!
</details>

---

## 🖥️ Parte 2: Prática (código)

### Desafio: Primeiro Pipeline ML

Complete o código abaixo com as partes que faltam:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Carregar dados
df = pd.read_csv('titanic.csv')

# Selecionar apenas colunas numéricas para simplificar
X = df[['age', 'fare', 'pclass']].fillna(0)
y = df['survived']

# PREENCHA: Dividir em treino e teste (80-20)
X_train, X_test, y_train, y_test = ________________

# PREENCHA: Criar modelo Random Forest
model = ________________

# PREENCHA: Treinar o modelo
________________

# PREENCHA: Fazer previsões
y_pred = ________________

# Avaliar
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia: {accuracy:.2%}")
```

<details>
<summary>💡 Ver resposta completa</summary>

### ✅ Código Completo e Correto:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Carregar dados
df = pd.read_csv('titanic.csv')

# Selecionar apenas colunas numéricas para simplificar
X = df[['age', 'fare', 'pclass']].fillna(0)
y = df['survived']

# 1️⃣ Dividir em treino e teste (80-20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2,      # 20% para teste
    random_state=42     # Reprodutibilidade
)

# 2️⃣ Criar modelo Random Forest
model = RandomForestClassifier(
    n_estimators=100,   # 100 árvores
    random_state=42     # Reprodutibilidade
)

# 3️⃣ Treinar o modelo
model.fit(X_train, y_train)

# 4️⃣ Fazer previsões
y_pred = model.predict(X_test)

# Avaliar
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia: {accuracy:.2%}")
```

---

### 📝 Explicação Linha por Linha:

#### 1️⃣ Train/Test Split
```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y,              # Features e target
    test_size=0.2,     # 20% teste, 80% treino
    random_state=42    # Seed para reproduzir resultados
)
```
**Por quê `random_state=42`?**
- Garante que a divisão seja sempre igual
- Facilita comparar resultados
- Qualquer número serve (42 é tradicional)

---

#### 2️⃣ Criar Modelo
```python
model = RandomForestClassifier(
    n_estimators=100,   # Quantas árvores criar
    random_state=42     # Reprodutibilidade
)
```
**Alternativas:**
```python
# Outros modelos comuns:
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

model = LogisticRegression(random_state=42)
model = DecisionTreeClassifier(random_state=42)
```

---

#### 3️⃣ Treinar
```python
model.fit(X_train, y_train)
```
**O que acontece:**
- Modelo analisa `X_train` (features)
- Aprende padrões que levam a `y_train` (target)
- Ajusta parâmetros internos

**⚠️ NUNCA use X_test aqui!**

---

#### 4️⃣ Prever
```python
y_pred = model.predict(X_test)
```
**O que retorna:**
- Array com previsões: `[0, 1, 1, 0, ...]`
- Um valor para cada linha de `X_test`
- 0 = não sobreviveu, 1 = sobreviveu

**Verificar:**
```python
print(f"Previsões: {y_pred[:5]}")        # [0 1 1 0 1]
print(f"Valores reais: {y_test[:5]}")    # [0 1 0 0 1]
```

---

### 🎯 Checklist de Validação:

| Passo | Descrição | Dados Usados |
|-------|-----------|--------------|
| 1. Split | Dividir dados | X, y → train/test |
| 2. Create | Criar modelo | - |
| 3. Fit | Treinar | X_train, y_train |
| 4. Predict | Prever | X_test |
| 5. Evaluate | Avaliar | y_test vs y_pred |

**⚠️ Regra de Ouro:**
```
Treino: usa apenas _train
Teste: usa apenas _test
NUNCA misture!
```

</details>

---

## 📊 Parte 3: Análise de Dados

Você tem este resultado de `.describe()`:

```python
df[['age', 'fare']].describe()
```

```
              age        fare
count    891.00     891.00
mean      29.70      32.20
std       14.53      49.69
min        0.42       0.00
25%       20.12       7.91
50%       28.00      14.45
75%       38.00      31.00
max       80.00     512.33
```

### Questão: O que você pode concluir sobre `age` e `fare`?

<details>
<summary>💡 Ver resposta e análise</summary>

### 📊 Análise Detalhada:

#### 🔍 Coluna `age` (Idade):

**Observações:**
- **Média:** 29.7 anos (população jovem/adulta)
- **Mediana (50%):** 28 anos (similar à média = distribuição simétrica)
- **Desvio padrão:** 14.5 anos (variação moderada)
- **Range:** 0.42 a 80 anos (bebês a idosos)

**Interpretação:**
```
✅ Distribuição relativamente normal
✅ Sem outliers extremos
✅ Idade variada (boa diversidade)
```

**Visualização mental:**
```
   |
   |    *****
   |   *******
   |  *********
   | ***********
   |_____________
   0  20  40  60  80
      (distribuição normal)
```

---

#### 🔍 Coluna `fare` (Tarifa):

**Observações:**
- **Média:** 32.2
- **Mediana (50%):** 14.45 (MUITO MENOR que média!)
- **Desvio padrão:** 49.7 (MAIOR que a média! 😱)
- **Max:** 512.33 (16x a média!)

**Interpretação:**
```
⚠️ Distribuição ASSIMÉTRICA (skewed)
⚠️ Presença de OUTLIERS (valores muito altos)
⚠️ Mediana << Média indica assimetria à direita
```

**Visualização mental:**
```
   |*
   |**
   |***
   |****
   |*****
   |********          *
   |__________________|_____
   0    50   100  200  512
   (muitos valores baixos, poucos muito altos)
```

---

### 🎯 Conclusões Práticas:

#### 1. **Mediana vs Média**
```python
# Quando usar cada uma:

# age: média ≈ mediana (29.7 vs 28)
# → Usar MÉDIA para análises

# fare: média >> mediana (32.2 vs 14.45)
# → Usar MEDIANA (mais representativa!)
```

**Por quê fare tem essa diferença?**
- Maioria pagou tarifas baixas (classes 2 e 3)
- Poucos pagaram tarifas muito altas (classe 1, suítes)
- Outliers "puxam" a média para cima

---

#### 2. **Outliers**
```python
# Detectar outliers em fare:
Q1 = 7.91    # 25%
Q3 = 31.00   # 75%
IQR = Q3 - Q1 = 23.09

upper_bound = Q3 + 1.5 * IQR = 31 + 34.6 = 65.6

# Valores > 65.6 são outliers
# Max = 512.33 → Definitivamente outlier!
```

---

#### 3. **Normalização**
```python
# fare precisa de normalização para alguns modelos:
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df['fare_scaled'] = scaler.fit_transform(df[['fare']])

# age pode não precisar (distribuição mais normal)
```

---

### 📋 Checklist de Análise `.describe()`:

Ao analisar `.describe()`, observe:

- [ ] **Count:** Tem dados faltantes? (count < total de linhas)
- [ ] **Mean vs Median:** São próximos? (normal) ou distantes? (assimétrico)
- [ ] **Std:** É alto? (muita variação) ou baixo? (dados homogêneos)
- [ ] **Min/Max:** Tem valores impossíveis? (idade negativa, salário 0)
- [ ] **Quartis:** Distribuição uniforme ou concentrada?

---

### 🎨 Visualizações Úteis:

```python
import matplotlib.pyplot as plt

# Comparar age vs fare
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Age: distribuição normal
axes[0].hist(df['age'], bins=30, edgecolor='black')
axes[0].set_title('Age (Distribuição Normal)')

# Fare: assimétrica com outliers
axes[1].hist(df['fare'], bins=30, edgecolor='black')
axes[1].set_title('Fare (Assimétrica com Outliers)')

plt.tight_layout()
plt.show()
```

**Conceito-chave:** `.describe()` revela problemas antes do modelo!

</details>

---

## 🎓 Gabarito de Auto-Avaliação

### Pontuação:

- **Parte 1 (Conceitos):** 4 questões × 2.5 pontos = **10 pontos**
- **Parte 2 (Código):** 1 exercício × 5 pontos = **5 pontos**  
- **Parte 3 (Análise):** 1 questão × 5 pontos = **5 pontos**

**TOTAL:** 20 pontos

---

### 📊 Interpretação da sua nota:

#### 🏆 17-20 pontos: EXCELENTE!
**Você dominou os fundamentos!**

✅ Entende tipos de ML  
✅ Sabe separar features e target  
✅ Compreende train/test split  
✅ Identifica overfitting/underfitting  

**Próximos passos:**
- ✅ AVANÇAR para Semana 2 com confiança!
- Considere revisar rapidamente os pontos que errou

---

#### 💪 13-16 pontos: BOM!
**Você entende o básico, mas pode reforçar alguns conceitos.**

✅ Conceitos principais estão claros  
⚠️ Alguns detalhes precisam de atenção  

**Próximos passos:**
- Revise as questões que errou
- Execute novamente o notebook da Semana 1
- Pode avançar para Semana 2, mas consulte o material S1 quando necessário

---

#### 🔄 9-12 pontos: PARCIAL
**Recomendado revisar alguns conceitos antes de avançar.**

⚠️ Conceitos fundamentais não estão totalmente claros  
⚠️ Pode ter dificuldade na Semana 2  

**Próximos passos:**
- Refaça os notebooks da Semana 1
- Foque nos conceitos que errou aqui
- Faça o teste novamente após 2 dias
- Avance quando se sentir mais confiante

---

#### 📚 0-8 pontos: REVISAR
**É importante reforçar os fundamentos da Semana 1.**

❌ Conceitos base precisam de mais atenção  

**Próximos passos:**
1. **Não desanime!** ML é complexo no início
2. Releia a documentação da Semana 1
3. Execute cada célula do notebook com atenção
4. Anote os conceitos principais com suas palavras
5. Retome este teste em 1 semana

**Lembre-se:** Fundamentos sólidos = sucesso no futuro!

---

## 🎯 Reflexão Final

Responda honestamente (só para você):

1. **Sei diferenciar Supervisionado de Não-Supervisionado?**  
   [ ] Sim [ ] Mais ou menos [ ] Preciso revisar  

2. **Entendo por que dividir em train/test?**  
   [ ] Sim [ ] Mais ou menos [ ] Preciso revisar  

3. **Consigo identificar overfitting?**  
   [ ] Sim [ ] Mais ou menos [ ] Preciso revisar  

4. **Me sinto confortável para fazer um pipeline básico?**  
   [ ] Sim [ ] Com ajuda [ ] Ainda não  

---

## ✅ Decisão Final

### ➡️ AVANCE para Semana 2 se:
- Acertou 13+ pontos
- Respondeu "Sim" ou "Mais ou menos" na maioria das reflexões
- Sente que entende os conceitos principais

### 🔄 REVISE Semana 1 se:
- Acertou <9 pontos
- Respondeu "Preciso revisar" em 3+ reflexões
- Sente que os conceitos ainda estão confusos

---

## 💡 Dica Final

Os fundamentos da Semana 1 são a **BASE de tudo** que vem depois:

```
Semana 1: Fundamentos
    ↓
Semana 2: Data Science (usa train/test, features)
    ↓
Semana 3: ML Avançado (usa overfitting, modelos)
    ↓
...
```

**Invista tempo aqui = Facilita TUDO que vem depois!** 🎯

---

**Sucesso! Você está construindo uma base sólida! 🚀**

_Este teste pode ser refeito sempre que quiser. Use-o como ferramenta de aprendizado!_
