# Main - feat(week2-day1): Complete EDA with Titanic dataset

## 📊 Análise Exploratória de Dados Completa

### Implementações Principais
- **Dataset**: 887 passageiros do Titanic (Stanford repository)
- **Visualizações**: 5 gráficos profissionais criados
  - Taxa de sobrevivência geral
  - Correlações entre features
  - Distribuições por classe e gênero
  - Boxplots de idade e tarifa
  - Heatmap de correlação

### 🔧 Feature Engineering
- `family_size`: Tamanho da família (SibSp + Parch + 1)
- `is_alone`: Indicador binário de viajante solo
- `sex_numeric`: Conversão de gênero para valores numéricos

### 🤖 Modelos de Machine Learning
- **LogisticRegression**: 79% de acurácia
- **DecisionTreeClassifier**: Modelo comparativo
- **Métricas Calculadas**:
  - Accuracy: 79%
  - Precision: 82%
  - Recall: 64%
  - F1-Score: 72%

### 📚 Documentação Criada (~15,000 palavras)
1. **05-referencia-visualizacoes.md**
   - Guia completo de visualizações
   - Matplotlib e Seaborn
   - Quando usar cada tipo de gráfico

2. **06-correlacao-e-pipeline-ml.md**
   - Pipeline de ML em 11 etapas
   - Interpretação de correlações
   - Seleção de features

3. **07-metricas-ml-e-confiabilidade.md**
   - Explicação detalhada de métricas
   - Matriz de confusão
   - Análise de confiabilidade do modelo

4. **04-dia1-semana2-eda.md**
   - Guia do Dia 1
   - Conceitos fundamentais
   - Exercícios práticos

### 📈 Progresso do Projeto
- Semana 2: 33% completa (Dia 1/3)
- Performance do modelo acima da média Kaggle
- Feature importance: sex_numeric (45%) > pclass (25%) > fare (15%)

### ✅ Resultados Validados
- Modelo atingiu 79% de acurácia (93% do limite teórico de ~85%)
- Todas as células do notebook executadas com sucesso
- Código modernizado (sem `inplace=True`)
- Tratamento de erros implementado (fallback URLs)
