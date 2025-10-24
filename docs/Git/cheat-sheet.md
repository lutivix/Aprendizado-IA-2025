# 🚀 Cheat Sheet - Comandos Git

## ⚡ Comandos Essenciais

### Configuração Inicial
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

### Iniciar/Clonar
```bash
git init                                          # Novo repo
git clone https://github.com/user/repo.git       # Clonar repo
```

### Status e Info
```bash
git status                    # Status dos arquivos
git log --oneline            # Histórico resumido
git diff                     # Mudanças não adicionadas
git diff --staged            # Mudanças no staging
```

### Adicionar e Commitar
```bash
git add arquivo.txt          # Adicionar arquivo específico
git add .                    # Adicionar todos
git commit -m "mensagem"     # Commit com mensagem
git commit -am "mensagem"    # Add + commit (só tracked files)
```

### Push/Pull
```bash
git push origin main         # Enviar mudanças
git pull origin main         # Baixar mudanças
git push -u origin main      # Primeira vez (set upstream)
```

## 🌿 Branches

```bash
git branch                   # Listar branches
git branch feature          # Criar branch
git checkout feature        # Mudar para branch
git checkout -b feature     # Criar e mudar
git switch feature          # Mudar (comando novo)
git switch -c feature       # Criar e mudar (novo)

git merge feature           # Merge branch
git branch -d feature       # Deletar branch
git push origin --delete feature  # Deletar branch remota
```

## 🔄 Desfazer Mudanças

```bash
# Desfazer mudanças no working directory
git restore arquivo.txt
git checkout -- arquivo.txt

# Remover do staging
git restore --staged arquivo.txt
git reset HEAD arquivo.txt

# Desfazer último commit (mantém arquivos)
git reset --soft HEAD~1

# Desfazer último commit (remove arquivos)
git reset --hard HEAD~1

# Criar commit que desfaz outro commit
git revert abc123
```

## 🏷️ Tags

```bash
git tag v1.0.0              # Tag simples
git tag -a v1.0.0 -m "msg"  # Tag anotada
git push origin v1.0.0      # Enviar tag
git push origin --tags      # Enviar todas as tags
```

## 🔍 Stash

```bash
git stash                   # Guardar mudanças
git stash pop               # Aplicar último stash
git stash list              # Listar stashes
git stash apply stash@{0}   # Aplicar stash específico
git stash drop stash@{0}    # Deletar stash
```

## 📊 Log Avançado

```bash
git log --oneline           # Uma linha por commit
git log --graph             # Com gráfico
git log --stat              # Com estatísticas
git log -p                  # Com diff
git log --author="Nome"     # Por autor
git log --since="2023-01-01"  # Por data
```

## 🔧 Comandos Úteis

```bash
# Ver configurações
git config --list

# Ver repositórios remotos
git remote -v

# Adicionar repositório remoto
git remote add origin https://github.com/user/repo.git

# Alterar URL remota
git remote set-url origin https://github.com/user/novo-repo.git

# Limpar arquivos não rastreados
git clean -fd

# Verificar arquivos ignorados
git status --ignored

# Ver quem modificou cada linha
git blame arquivo.txt
```

## 🌐 GitHub CLI

```bash
gh auth login               # Login
gh repo create nome         # Criar repositório
gh pr create               # Criar pull request
gh pr list                 # Listar PRs
gh issue create            # Criar issue
```

## 🆘 Emergência

```bash
# Parar merge/rebase
git merge --abort
git rebase --abort

# Ver histórico de operações
git reflog

# Voltar a estado anterior
git reset --hard HEAD@{5}

# Backup antes de operação perigosa
git branch backup
```

## 📝 Convenções de Commit

```bash
feat: nova funcionalidade
fix: correção de bug
docs: documentação
style: formatação
refactor: refatoração
test: testes
chore: tarefas auxiliares

# Exemplo:
git commit -m "feat(auth): adicionar login com Google"
```

## 🔀 Fluxo de Trabalho

```bash
# 1. Atualizar main
git checkout main
git pull origin main

# 2. Criar feature branch
git checkout -b feature/nova-funcao

# 3. Trabalhar e commitar
git add .
git commit -m "feat: implementar nova função"

# 4. Enviar branch
git push -u origin feature/nova-funcao

# 5. Criar PR no GitHub

# 6. Após merge, limpar
git checkout main
git pull origin main
git branch -d feature/nova-funcao
```

---

📚 **Documentação Completa**: [README.md](README.md)