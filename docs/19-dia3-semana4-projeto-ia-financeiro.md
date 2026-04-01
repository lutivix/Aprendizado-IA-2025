# 💰 Dia 3 - Semana 4: Projeto IA Financeiro

[← Semana 4](../semana-04-consolidacao/README.md)

**Data:** 1 Abril 2026  
**Foco:** Aplicar ML em projeto real com dados financeiros da família  
**Branch:** `IALearning` (fork do projeto Financeiro — main preservado)

---

## 📋 Índice

1. [Contexto e Decisão](#contexto-e-decisão)
2. [Exploração do Projeto Financeiro](#exploração-do-projeto-financeiro)
3. [Modelo de Dados](#modelo-de-dados)
4. [Problemas ML Identificados](#problemas-ml-identificados)
5. [Problema Selecionado: Previsão de Estouro de Orçamento](#problema-selecionado)
6. [Plano do Notebook](#plano-do-notebook)

---

## 🎯 Contexto e Decisão

### Por que usar o projeto real?

O projeto Financeiro familiar já existe, está em produção e tem dados reais acumulados ao longo de meses. Usar dados sintéticos ensinaria a mecânica do ML, mas perderia o contexto de negócio — que é onde mora o aprendizado mais rico.

**Abordagem adotada:**
- Branch `IALearning` criado a partir do `main` → projeto original **100% preservado**
- Symlink `ppiaFinanceiro` em `semana-04-consolidacao/` → acesso direto aos dados sem duplicação
- Notebooks ficam em `semana-04-consolidacao/notebooks/` → separação clara entre aprendizado e produção
- A integração do modelo na aplicação fica para a **Semana 11-12** (Agente IA Financeiro)

---

## 🔍 Exploração do Projeto Financeiro

### Stack Tecnológico

| Camada | Tecnologia |
|--------|-----------|
| Linguagem | Python 3.13+ |
| Banco de dados | SQLite 3 |
| Processamento | Pandas, NumPy |
| Dashboard | Plotly Dash |
| Integração Open Finance | Pluggy SDK (API bancária) |
| Testes | pytest |

### Estrutura Relevante para ML

```
Financeiro/
├── dados/
│   ├── db/
│   │   └── financeiro.db          ← banco principal (acessado para ML)
│   └── planilhas/
│       ├── consolidado_temp.xlsx  ← export consolidado
│       └── dadosMeuPluggy.csv     ← dados Open Finance
└── backend/
    └── src/
        ├── models/                ← Transaction, LearnedCategory, ProcessingStats
        ├── services/
        │   ├── categorization_service.py    ← ML de categorização (98.2% precisão)
        │   └── report_service.py            ← exports para análise
        └── budget_analysis/
            ├── weekly_budget_calculator.py  ← lógica de orçamento semanal
            └── recurring_analyzer.py        ← detecção de recorrências
```

---

## 🗄️ Modelo de Dados

### Tabela `lancamentos` (transações)

Tabela principal — cada linha é uma transação financeira.

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `id` | TEXT (UUID) | Identificador único |
| `Data` | TEXT | Data da transação (DD/MM/YYYY) |
| `Descricao` | TEXT | Descrição do lançamento |
| `Valor` | REAL | Valor (positivo = receita, negativo = despesa) |
| `Fonte` | TEXT | Origem (cartão/PIX) |
| `Categoria` | TEXT | Categoria atribuída |
| `MesComp` | TEXT | Mês de competência (YYYY-MM) |
| `raw_data` | TEXT | JSON com dados brutos da fonte |
| `created_at` | TEXT | Timestamp de criação |

### Fontes de Transação (`Fonte`)

| Fonte | Tipo |
|-------|------|
| `PIX` | Pagamentos instantâneos |
| `Master Físico` / `Virtual` / `Recorrente` | Itaú - Luciano |
| `Visa Físico` / `Virtual` / `Recorrente` | Latam - Luciano |
| `Visa Bia` | Latam - Beatriz |
| `Visa Mae` | Latam - Mãe |

> **Nota:** A coluna `Fonte` permite derivar a **pessoa** associada à transação: `Visa Bia` → Beatriz, `Visa Mae` → Mãe, demais → Luciano.

### Categorias (32 no total)

| Grupo | Categorias |
|-------|-----------|
| **Receita** | Salário, Investimentos |
| **Pessoal** | Betina, Nita, Esporte, Estetica, Hobby |
| **Casa/Carro** | Carro, Cartão, Combustível, Seguro, Casa, Utilidades, LF |
| **Compras** | Compras, Lanche, Mercado, Padaria, Roupa, Vestuário |
| **Saúde** | Farmácia, Pet, Saúde |
| **Estilo de Vida** | Datas, Eventos, Faculdade, Lazer, Stream, Transporte, Viagem |
| **Indefinido** | A definir |

### Tabela `weekly_budgets` (orçamentos semanais)

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `month_ref` | TEXT | Mês de referência |
| `week_number` | INTEGER | Semana do mês (1–5) |
| `category` | TEXT | Categoria |
| `source` | TEXT | Cartão/fonte |
| `person` | TEXT | "Luciano", "Bia" ou "Mãe" |
| `expected_amount` | REAL | Valor esperado no orçamento |
| `is_recurring` | BOOLEAN | Se é gasto recorrente |
| `confidence` | REAL | Confiança da previsão (0–1) |

### Tabela `categorias_aprendidas` (ML existente)

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `descricao` | TEXT (PK) | Padrão de descrição aprendido |
| `categoria` | TEXT | Categoria associada |
| `confidence` | REAL | Confiança (0–1) |
| `usage_count` | INTEGER | Quantas vezes foi utilizada |

> O projeto já possui um sistema de categorização automática com **98.2% de precisão**, baseado em matching de descrições com `confidence` score. Esse é um benchmark excelente para comparação futura.

---

## 🤖 Problemas ML Identificados

Foram identificados 4 problemas ML naturais com os dados disponíveis:

### A — Classificação de Categoria de Transação

| | |
|---|---|
| **Tipo** | Classificação multiclasse (32 classes) |
| **Input** | `Descricao`, `Valor`, `Fonte`, `Data` |
| **Output** | `Categoria` |
| **Valor prático** | ⭐⭐⭐ |
| **Decisão** | Não selecionado — já existe com 98.2% de precisão no projeto |

### B — Previsão de Gasto Mensal Total

| | |
|---|---|
| **Tipo** | Regressão |
| **Input** | Gastos dos primeiros N dias do mês por categoria |
| **Output** | Total estimado ao final do mês |
| **Valor prático** | ⭐⭐⭐⭐ |
| **Decisão** | Reservado para Semana 7-8 (Séries Temporais) |

### C — Detecção de Transações Atípicas (Anomalias)

| | |
|---|---|
| **Tipo** | Não supervisionado (Anomaly Detection) |
| **Input** | `Valor`, `Categoria`, `Fonte`, `Data`, padrão histórico |
| **Output** | Score de anomalia / flag de transação suspeita |
| **Valor prático** | ⭐⭐⭐⭐ |
| **Decisão** | Reservado para Semana 5-6 (ML Não Supervisionado) |

### D — Previsão de Estouro de Orçamento Semanal ✅ SELECIONADO

| | |
|---|---|
| **Tipo** | Classificação binária |
| **Input** | Gastos acumulados na semana + orçamento previsto + histórico |
| **Output** | `estourou` (1) ou `dentro do orçamento` (0) |
| **Valor prático** | ⭐⭐⭐⭐⭐ |
| **Decisão** | **Selecionado para este notebook** |

---

## 🎯 Problema Selecionado

### Previsão de Estouro de Orçamento Semanal

**Pergunta de negócio:**  
> *"Dado o histórico de gastos de uma semana, qual a probabilidade de o orçamento daquela categoria/pessoa ser ultrapassado?"*

**Por que este é o mais valioso:**
- Resultado **imediatamente acionável**: alertas no dashboard
- Dados suficientes: vários meses × 4 semanas × 32 categorias × 3 pessoas
- Exercita **feature engineering temporal** (dia da semana, semana do mês, acúmulo)
- Usa **join entre tabelas** (`lancamentos` + `weekly_budgets`) — realista
- Abrange EDA, FE, treino, avaliação e interpretação — pipeline completo

### Features Planejadas

**Features diretas (das tabelas):**
- `week_number` — semana do mês (1–5)
- `category` — categoria do gasto
- `person` — Luciano / Bia / Mãe
- `expected_amount` — orçamento previsto
- `is_recurring` — se é recorrente

**Features de engenharia:**
- `gasto_acumulado_semana` — soma dos gastos até aquele ponto da semana
- `percentual_consumido` — `gasto_acumulado / expected_amount`
- `dias_restantes_semana` — quantos dias faltam para o fim da semana
- `media_historica_categoria_semana` — média histórica de semanas anteriores iguais
- `desvio_vs_historico` — diferença percentual do acumulado vs média histórica
- `num_transacoes_semana` — volume de transações na semana
- `maior_transacao_semana` — valor do maior lançamento da semana

**Target:**
- `estourou`: 1 se gasto real > expected_amount × 1.05 (5% de tolerância), 0 caso contrário

### Algoritmos a Testar

| Algoritmo | Justificativa |
|-----------|--------------|
| Logistic Regression | Baseline + interpretabilidade |
| Random Forest | Robusto, feature importance |
| XGBoost | Performance, lida bem com dados tabulares |

---

## 📓 Plano do Notebook

**Arquivo:** `semana-04-consolidacao/notebooks/03-projeto-financeiro.ipynb`

| Seção | Conteúdo |
|-------|---------|
| **1. Setup** | Imports, conexão SQLite, configurações |
| **2. Carregamento** | Leitura das tabelas `lancamentos` + `weekly_budgets` |
| **3. EDA** | Distribuição por categoria, pessoa, semana; valores missing; outliers |
| **4. Construção do Dataset** | Join das tabelas, criação do target `estourou` |
| **5. Feature Engineering** | Agregações semanais, features temporais, encoding |
| **6. Pipeline ML** | train/test split, ColumnTransformer, 3 modelos |
| **7. Avaliação** | Accuracy, Precision, Recall, F1, matriz de confusão |
| **8. Interpretação** | Feature importance, exemplos concretos |
| **9. Conclusões** | Aprendizados, limitações, próximos passos |

---

## 📚 Recursos e Links

- [Semana 4 README](../semana-04-consolidacao/README.md)
- [Projeto Financeiro](../semana-04-consolidacao/ppiaFinanceiro/)
- [Feature Engineering (ref)](./18-dia2-semana4-feature-engineering.md)
- [Revisão de Algoritmos (ref)](./17-dia1-semana4-revisao-ml.md)

---

*Próximo passo: executar o notebook `03-projeto-financeiro.ipynb`* 🚀
