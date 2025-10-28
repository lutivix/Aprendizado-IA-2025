# 📊 Métricas de ML e Confiabilidade de Modelos

**Data:** 28 Outubro 2025  
**Contexto:** Semana 2 - Dia 1 (Análise do modelo Titanic)

---

## 🎯 **As 4 Métricas Essenciais**

### **Visão Geral:**

| Métrica | Pergunta que Responde | Fórmula | Quando Usar |
|---------|----------------------|---------|-------------|
| **Accuracy** | Quantos % acertei no total? | (TP+TN) / Total | Dados balanceados |
| **Precision** | Quando digo SIM, acerto quantos %? | TP / (TP+FP) | Custo FP alto |
| **Recall** | De todos os SIM reais, pego quantos %? | TP / (TP+FN) | Custo FN alto |
| **F1-Score** | Qual equilíbrio entre Precision e Recall? | 2×(P×R)/(P+R) | Comparar modelos |

---

## 📐 **Matriz de Confusão**

```
                  PREDITO
                Não  |  Sim
              ─────────────────
        Não │  TN  │  FP  │
REAL        │      │      │
        Sim │  FN  │  TP  │
              ─────────────────
```

### **Legenda:**
- **TP (True Positive):** Acertou o SIM ✅
- **TN (True Negative):** Acertou o NÃO ✅
- **FP (False Positive):** Erro - Disse SIM (era NÃO) ❌ *Alarme Falso*
- **FN (False Negative):** Erro - Disse NÃO (era SIM) ❌ *Perdeu o alvo*

---

## 🧮 **Cálculo das Métricas (Exemplo Titanic)**

### **Matriz de Confusão Real:**

```
           PREDITO
         Morreu | Sobreviveu
       ──────────────────────
Morreu │   95   │    10     │ = 105 mortos
       │  (TN)  │   (FP)    │
       ──────────────────────
Sobre- │   26   │    47     │ = 73 sobreviventes
viveu  │  (FN)  │   (TP)    │
       ──────────────────────
         121       57
```

### **Resultados:**

```python
TP = 47  # Acertou: Sobreviveu
TN = 95  # Acertou: Morreu
FP = 10  # Erro: Disse sobreviveu (mas morreu)
FN = 26  # Erro: Disse morreu (mas sobreviveu)

# ACCURACY = 80%
(47 + 95) / 178 = 142 / 178 = 0.798
"8 em cada 10 predições corretas"

# PRECISION = 82.5%
47 / (47 + 10) = 47 / 57 = 0.825
"Quando disse 'sobreviveu', acertou 82.5%"

# RECALL = 64.4%
47 / (47 + 26) = 47 / 73 = 0.644
"Encontrou 64% dos sobreviventes reais"

# F1-SCORE = 72.4%
2 × (0.825 × 0.644) / (0.825 + 0.644) = 0.724
"Equilíbrio razoável entre Precision e Recall"
```

---

## 📊 **Quando Usar Cada Métrica?**

### **1. ACCURACY - Acurácia**

**Quando usar:**
✅ Dados balanceados (50% sim, 50% não)
✅ Visão geral de performance

**Quando NÃO usar:**
❌ Dados desbalanceados (90% sim, 10% não)

**Exemplo de problema:**
```python
# Dataset: 95 pessoas saudáveis, 5 doentes
# Modelo preguiçoso: "Todo mundo é saudável"

Accuracy = 95/100 = 95%  # Parece ótimo!
# Mas errou TODAS as 5 pessoas doentes! ❌
```

---

### **2. PRECISION - Precisão**

**Quando usar:**
✅ **Custo de FALSO POSITIVO é alto**

**Exemplos práticos:**

```
📧 Filtro de SPAM:
- Falso Positivo = Email importante vai pro spam
- Precision alta = Confio que spam é realmente spam

🏥 Diagnóstico de doença grave:
- Falso Positivo = Pessoa saudável recebe tratamento pesado
- Precision alta = Evita tratamentos desnecessários

⚖️ Sistema judicial:
- Falso Positivo = Inocente condenado
- Precision alta = "Melhor 10 culpados soltos que 1 inocente preso"
```

---

### **3. RECALL - Revocação**

**Quando usar:**
✅ **Custo de FALSO NEGATIVO é alto**

**Exemplos práticos:**

```
🏥 Diagnóstico de câncer:
- Falso Negativo = Doente não é identificado
- Recall alto = CRUCIAL! Não podemos perder ninguém

🔍 Detector de fraude:
- Falso Negativo = Fraude passa despercebida
- Recall alto = Pegar todas as fraudes possíveis

🚨 Sistema de segurança:
- Falso Negativo = Intruso não detectado
- Recall alto = Detectar todas as ameaças
```

---

### **4. F1-SCORE**

**Quando usar:**
✅ Comparar múltiplos modelos
✅ Dados desbalanceados
✅ Não sabe qual é mais importante (Precision ou Recall)

**Interpretação:**

```
Modelo A: Precision=90%, Recall=50% → F1=64%
Modelo B: Precision=70%, Recall=70% → F1=70% ✅ Melhor!
Modelo C: Precision=50%, Recall=90% → F1=64%
```

---

## ⚖️ **Trade-off: Precision vs Recall**

### **Cenário 1: Modelo Conservador**
```python
# Só diz "SIM" quando TEM CERTEZA

Precision: ↑ 95% (quase sempre acerta)
Recall:    ↓ 40% (perde muitos casos)
F1:        ↓ 56% (desbalanceado)
```

### **Cenário 2: Modelo Agressivo**
```python
# Diz "SIM" na dúvida

Recall:    ↑ 90% (encontra quase todos)
Precision: ↓ 60% (muitos falsos alarmes)
F1:        ↓ 72% (desbalanceado)
```

### **Cenário 3: Modelo Equilibrado**
```python
# Balanceado

Precision: 75%
Recall:    75%
F1:        75% ✅ Melhor equilíbrio!
```

---

## 🎯 **Confiabilidade de Modelos**

### **Escala de Accuracy:**

| Accuracy | Avaliação | Contexto |
|----------|-----------|----------|
| **< 60%** | ❌ **Ruim** | Pior que "chutar" |
| **60-70%** | 😐 **Mediano** | Aprendeu algo, mas fraco |
| **70-80%** | ✅ **Bom** | Útil para produção |
| **80-90%** | 🔥 **Muito Bom** | Alta confiabilidade |
| **90-95%** | 🏆 **Excelente** | Estado da arte |
| **> 95%** | ⚠️ **Suspeito** | Pode ser overfitting |

---

## 🚢 **Análise: Modelo Titanic (79% Accuracy)**

### **Baseline de Comparação:**

```python
# Estratégia 1: Sempre diz "morreu"
baseline_1 = 61.6% accuracy
# Seu modelo: +17.4% melhor! ✅

# Estratégia 2: Chute aleatório (50/50)
baseline_2 = 50% accuracy
# Seu modelo: +29% melhor! ✅
```

### **Comparação Kaggle:**

```
🏆 1º lugar:  85.0% accuracy
🥈 Top 100:   83-84%
🥉 Top 500:   81-82%
📊 Média:     79-80% ← VOCÊ ESTÁ AQUI! ✅
😐 Básico:    75-78%
❌ Fraco:     < 75%
```

### **Limite Teórico:**

```
⚠️ Limite prático: ~85-86%
   (Dados incompletos, sorte/acaso, info perdida)

🏆 Recorde Kaggle: ~85%

📊 Seu modelo: 79% → 93% do limite teórico! ✅
```

### **Avaliação Final:**

```
Accuracy:  79%  ✅ BOM (acima da média)
Precision: 82%  ✅ BOM (confiável quando diz "sim")
Recall:    64%  😐 MÉDIO (perde alguns sobreviventes)
F1-Score:  72%  ✅ RAZOÁVEL (equilíbrio OK)

Classificação: MODELO CONSERVADOR
- Prefere não arriscar
- Alta Precision (82%) > Recall (64%)
- Só diz "sobreviveu" com certeza
```

---

## 🔍 **Confiabilidade de Features**

### **Caso: `sex` no Titanic**

**Por que `sex` foi a feature mais importante (45% importance)?**

✅ **Política real:** "Mulheres e crianças primeiro"
✅ **Diferença massiva:** 74% mulheres vs 19% homens sobreviveram (55% gap!)
✅ **Documentado:** Registros históricos
✅ **Consistente:** Vale em todas as classes

**Estatísticas:**
```
Mulheres:  74% sobreviveram (233 de 314)
Homens:    19% sobreviveram (109 de 577)

Diferença: 55 pontos percentuais! 🔥

Comparação:
sex_numeric × survived:  -0.54  (FORTE)
pclass × survived:       -0.34  (MODERADA)
fare × survived:         +0.26  (FRACA)
```

### **Checklist de Confiabilidade de Features:**

```
✅ Faz sentido causal? (não é só correlação)
✅ Documentado/explicável? (tem evidência)
✅ Consistente em subgrupos? (não é flutuação)
✅ Magnitude forte? (diferença significativa)
✅ Ético usar? (não perpetua discriminação)
```

### **Quando Desconfiar:**

❌ **Correlação espúria** (causa comum escondida)
❌ **Discriminação histórica** (bias nos dados)
❌ **Causalidade inversa** (direção errada)
❌ **Não generalizável** (contexto específico)

---

## 📋 **Benchmarks por Contexto**

### **Quando 79% é BOM:**

```
✅ Análises históricas (Titanic)
✅ Recomendações (Netflix, Spotify)
✅ Filtros de spam (não crítico)
✅ Segmentação de clientes
✅ Previsão de churn (não urgente)
```

### **Quando 79% é INSUFICIENTE:**

```
❌ Diagnóstico médico crítico (mínimo: 95-98%)
❌ Carros autônomos (mínimo: 99.9%)
❌ Detecção de fraude (mínimo: 98-99%)
❌ Reconhecimento facial segurança (mínimo: 99%)
```

---

## 🚀 **Como Melhorar Accuracy**

### **Estratégias Testadas (Kaggle):**

```python
# 1. Feature Engineering avançado (+3-4%)
- Extrair título do nome (Mr, Mrs, Miss)
- Agrupar cabines por deck
- Criar "família grande" (>4 pessoas)

# 2. Modelos mais complexos (+2-3%)
- Random Forest (ensemble)
- XGBoost (gradient boosting)
- Voting Classifier

# 3. Hyperparameter Tuning (+1-2%)
- GridSearchCV
- RandomizedSearchCV

# 4. Tratamento de outliers (+1%)
- Remover extremos de fare
- Normalizar idade

# 5. Ensemble (+2%)
- Combinar previsões de múltiplos modelos
```

**Ganho esperado total:** 79% → 82-85% (+3-6%)

---

## 💡 **Decisões Práticas**

### **Modelo Titanic (79%) é confiável para:**

✅ **Análise histórica:**
- Entender padrões de sobrevivência
- Identificar fatores importantes
- Gerar insights (classe social > idade)
- Validar hipóteses históricas

❌ **Decisões reais (resgate moderno):**
- 21% de erro é inaceitável
- Protocolos mudaram (igualdade)
- Contexto diferente (tecnologia)

---

## 📊 **Comparação com Outros Datasets**

| Dataset | Problema | Accuracy Típica | Dificuldade |
|---------|----------|-----------------|-------------|
| **Iris** | 3 espécies flores | 95-98% | Fácil |
| **Titanic** | Sobrevivência | **75-85%** | **Médio** |
| **Wine** | Qualidade vinho | 85-90% | Médio |
| **Breast Cancer** | Diagnóstico | 95-98% | Médio-Difícil |
| **MNIST** | Dígitos escritos | 98-99% | Médio |
| **ImageNet** | 1000 objetos | 70-80% | Difícil |

**Titanic é considerado INTERMEDIÁRIO.**

---

## 🎓 **Resumo Executivo**

### **Seu Modelo Titanic:**

```
✅ Accuracy: 79% (BOM - acima da média)
✅ Na média Kaggle (79-80%)
✅ 93% do limite teórico (~85%)
✅ Confiável para análise histórica
✅ Feature principal (`sex`) é legítima e documentada
❌ Insuficiente para decisões críticas
```

### **Aprendizados Principais:**

1. **Métricas diferentes para contextos diferentes**
   - Accuracy ≠ Precision ≠ Recall
   - F1-Score balanceia ambos

2. **Confiabilidade é contextual**
   - 79% pode ser ótimo ou péssimo
   - Depende do problema e consequências

3. **Questionar features é fundamental**
   - Correlação ≠ Causação
   - Buscar evidências e contexto

4. **Trade-offs são inevitáveis**
   - Precision ↑ → Recall ↓
   - Escolher baseado no custo de erros

---

## ✅ **Checklist de Avaliação de Modelo**

### **Performance:**
- [ ] Accuracy > baseline (estratégias simples)
- [ ] Comparou com benchmarks do problema
- [ ] F1-Score balanceado (se dados desbalanceados)
- [ ] Testou em dados separados (não treino)

### **Confiabilidade:**
- [ ] Features fazem sentido causal
- [ ] Magnitude de diferença é significativa
- [ ] Consistente em subgrupos
- [ ] Não perpetua discriminação

### **Interpretação:**
- [ ] Entende o que modelo está aprendendo
- [ ] Sabe limitações e contexto
- [ ] Identifica possíveis vieses
- [ ] Documenta decisões

---

**🎉 Parabéns! Você dominou:**
- ✅ As 4 métricas essenciais
- ✅ Interpretação de resultados
- ✅ Avaliação crítica de modelos
- ✅ Pensamento contextual

**🚀 Próximo passo: Dia 2 - API REST com esse modelo!**
