# 📋 01 - Relatório Dia 1 - Setup Python/Anaconda

**Data:** 21/10/2025 (Segunda-feira)  
**Horário:** 17:00-19:20 (Buffer Dinâmico)  
**Duração:** 2h20min  
**Status:** ✅ Concluído com sucesso  

## 🎯 Objetivos Planejados

- [x] Setup Python + Anaconda
- [x] Configuração Jupyter Notebook
- [x] Primeiro notebook funcional
- [x] Teste das bibliotecas essenciais

## ✅ Conquistas do Dia

### 🐍 **Ambiente Python Configurado**
- **Anaconda 25.5.1** instalado em `C:\ProgramData\anaconda3`
- **Python 3.13.5** (versão Anaconda) funcionando
- PATH configurado corretamente
- Todas as bibliotecas de Data Science instaladas

### 📚 **Bibliotecas Verificadas**
- ✅ **NumPy 2.1.3** - Computação numérica
- ✅ **Pandas 2.2.3** - Manipulação de dados
- ✅ **Matplotlib 3.10.0** - Visualização básica
- ✅ **Seaborn 0.13.2** - Visualização avançada
- ✅ **Scikit-learn 1.6.1** - Machine Learning
- ✅ **IPython 8.30.0** - Interface interativa

### 📓 **Jupyter Configurado**
- **Jupyter Lab 4.3.4** funcionando
- **VS Code** com extensão Jupyter instalada
- **Browser** rodando em `localhost:8888`
- Kernel Python (Anaconda) selecionado corretamente

### 📊 **Primeiro Notebook Criado**
- Arquivo: `01-primeiro-teste-v2.ipynb`
- **4 células executadas** com sucesso:
  1. Verificação do ambiente Python
  2. Importação das bibliotecas
  3. Criação do primeiro dataset
  4. Visualização dos dados

## 🛠️ Ferramentas Criadas

### 📄 **Scripts de Verificação**
- `verificar-instalacao.py` - Diagnóstico completo do ambiente
- `COMANDOS-VERIFICACAO.md` - Guia de comandos úteis

### 📓 **Notebooks**
- `01-primeiro-teste-v2.ipynb` - Notebook principal (VS Code)
- `01-fundamentos-browser.ipynb` - Versão para browser

## 📈 **Dados de Teste**

Criamos um dataset simples para aprendizado:

| Nome    | Idade | Salário | Experiência |
|---------|-------|---------|-------------|
| Alice   | 25    | 50000   | 2 anos      |
| Bob     | 30    | 60000   | 5 anos      |
| Charlie | 35    | 70000   | 8 anos      |
| Diana   | 28    | 55000   | 3 anos      |
| Eve     | 32    | 65000   | 6 anos      |

**Correlação experiência vs salário:** 0.965 (forte correlação positiva)

## 🚧 Desafios Enfrentados

### 🔧 **Problema 1: PATH do Anaconda**
- **Situação:** Conda não reconhecido após instalação
- **Solução:** Configuração manual do PATH e uso do caminho completo
- **Aprendizado:** Instalações corporativas podem precisar configuração manual

### 📋 **Problema 2: Formato JSON do Notebook**
- **Situação:** Jupyter browser não conseguia ler os arquivos iniciais
- **Solução:** Criação de arquivos com formato JSON correto
- **Aprendizado:** VS Code e Jupyter browser têm pequenas diferenças de formato

### 🔑 **Problema 3: Seleção de Kernel**
- **Situação:** VS Code não detectava automaticamente o Python do Anaconda
- **Solução:** Configuração manual do interpretador Python
- **Aprendizado:** Sempre verificar qual Python/ambiente está sendo usado

## 💡 Conceitos Introduzidos

### 🧠 **IA vs ML vs DL**
- **IA:** Campo mais amplo, inclui qualquer simulação de inteligência
- **ML:** Subconjunto da IA que aprende com dados
- **DL:** Subconjunto do ML usando redes neurais profundas

### 📊 **Análise Exploratória**
- Uso do `pandas.DataFrame` para estruturar dados
- Métodos `.describe()` e `.info()` para estatísticas
- Conceito de correlação entre variáveis

## 🎯 Próximos Passos (Dia 2)

### 📚 **Teoria Fundamental**
- Aprofundar IA vs ML vs DL
- Tipos de aprendizado (supervisionado, não-supervisionado, reforço)
- Ética em IA

### 🤖 **Primeiro Modelo ML**
- Algoritmo de regressão linear simples
- Predição de salário baseado em experiência
- Métricas de avaliação

### 🔧 **Setup Web (se der tempo)**
- Node.js + TypeScript
- Primeiro Hello World

## 📊 Métricas do Dia

- **⏰ Tempo investido:** 2h20min
- **🎯 Objetivos cumpridos:** 4/4 (100%)
- **🚧 Problemas encontrados:** 3
- **✅ Problemas resolvidos:** 3/3 (100%)
- **📓 Notebooks funcionais:** 2
- **🔧 Scripts criados:** 2

## 💭 Reflexões

### ✅ **Pontos Positivos**
- Setup mais complexo que esperado, mas resultado robusto
- Ambiente completamente funcional para aprendizado
- Base sólida para os próximos dias
- Jupyter funcionando em duas interfaces (VS Code + Browser)

### 🔄 **Melhorias para Próximos Setups**
- Verificar PATH automaticamente após instalações
- Criar scripts de verificação antes de começar
- Testar formato de arquivo antes de criar notebooks

### 🎓 **Aprendizados**
- Anaconda é mais poderoso que Python standalone para Data Science
- Jupyter Notebook é realmente ideal para aprendizado iterativo
- VS Code + Jupyter oferece melhor experiência de desenvolvimento
- Correlações simples já mostram insights valiosos nos dados

---

**📅 Próximo relatório:** `02-dia2-conceitos-ml.md`  
**🚀 Status geral:** No cronograma, base sólida estabelecida