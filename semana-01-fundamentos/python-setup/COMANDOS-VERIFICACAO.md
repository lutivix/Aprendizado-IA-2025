# 🚀 Comandos de Verificação - Setup Anaconda

## 📋 Após Instalação do Anaconda

### 1️⃣ Feche todos os terminais e abra um novo

### 2️⃣ Teste os comandos básicos:

```bash
# Verificar Python
python --version

# Verificar Conda
conda --version

# Verificar Jupyter
jupyter --version

# Listar ambientes Conda
conda env list
```

### 3️⃣ Execute o script de verificação:

```bash
# Navegar para a pasta
cd "D:\Professional\Projetos\Github\Aprendizado-IA-2025\semana-01-fundamentos\python-setup"

# Executar verificação
python verificar-instalacao.py
```

### 4️⃣ Abrir Jupyter Notebook:

```bash
# Navegar para notebooks
cd "D:\Professional\Projetos\Github\Aprendizado-IA-2025\semana-01-fundamentos\notebooks"

# Iniciar Jupyter
jupyter notebook
```

### 5️⃣ Abrir nosso primeiro notebook:
- No navegador que abrir, clique em `01-primeiro-teste.ipynb`
- Execute as células com `Shift + Enter`

## 🛠️ Se algo der errado:

### Python não reconhecido:
```bash
# Verificar se está no PATH
where python
where conda
```

### Bibliotecas faltando:
```bash
# Instalar pacotes essenciais
conda install numpy pandas matplotlib seaborn scikit-learn jupyter
```

### Problemas com Jupyter:
```bash
# Reinstalar Jupyter
conda install jupyter
```

## 📞 Próximos Passos:
1. ✅ Executar verificação
2. 📓 Testar primeiro notebook  
3. 🎯 Partir para conceitos de IA/ML
4. 🔧 Setup Node.js/TypeScript