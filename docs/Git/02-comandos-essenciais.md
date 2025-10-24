# 02. Comandos Essenciais

## 🏁 Configuração Inicial

```bash
# Configurar nome e email (uma vez só)
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"

# Ver configurações
git config --list
```

## 🆕 Iniciar Repositório

```bash
# Criar novo repositório
git init

# Clonar repositório existente
git clone https://github.com/usuario/projeto.git
```

## 📊 Status e Informações

```bash
# Ver status dos arquivos
git status

# Ver histórico de commits
git log
git log --oneline          # Versão compacta
git log --graph --oneline  # Com gráfico

# Ver diferenças
git diff                   # Working vs Staging
git diff --staged          # Staging vs Repository
```

## ➕ Adicionar Arquivos

```bash
# Adicionar arquivo específico
git add arquivo.txt

# Adicionar todos os arquivos
git add .

# Adicionar por extensão
git add *.py

# Adicionar pasta
git add pasta/
```

## 💾 Fazer Commits

```bash
# Commit básico
git commit -m "Mensagem do commit"

# Commit com descrição detalhada
git commit -m "Título" -m "Descrição detalhada"

# Adicionar e comitar de uma vez (só arquivos já rastreados)
git commit -am "Mensagem"
```

## 🌐 Trabalhar com Repositório Remoto

```bash
# Adicionar repositório remoto
git remote add origin https://github.com/usuario/repo.git

# Ver repositórios remotos
git remote -v

# Enviar mudanças
git push origin main

# Definir upstream (primeira vez)
git push -u origin main

# Baixar mudanças
git pull origin main
```

## 🔄 Comandos de Atualização

```bash
# Baixar sem fazer merge
git fetch origin

# Baixar e fazer merge
git pull origin main

# Push simples (depois do -u)
git push
```

## 📋 Exemplo de Fluxo Completo

```bash
# 1. Verificar status
git status

# 2. Adicionar arquivos modificados
git add .

# 3. Fazer commit
git commit -m "Adicionar nova funcionalidade"

# 4. Enviar para GitHub
git push

# 5. Verificar se tudo foi enviado
git status
```

## ⚡ Comandos Rápidos

```bash
# Ver último commit
git show

# Ver arquivos no último commit
git show --name-only

# Desfazer último commit (mantém arquivos)
git reset --soft HEAD~1

# Ver quem modificou cada linha
git blame arquivo.txt
```

---

**Anterior**: [01-conceitos-basicos.md](01-conceitos-basicos.md) | **Próximo**: [03-branches.md](03-branches.md)