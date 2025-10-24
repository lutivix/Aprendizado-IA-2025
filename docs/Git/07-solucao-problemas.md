# 07. Solução de Problemas Comuns

## ❌ Problemas e Soluções

### 🔐 Problemas de Autenticação

#### Erro: Permission denied (publickey)
```bash
# Verificar chaves SSH
ssh -T git@github.com

# Gerar nova chave SSH
ssh-keygen -t ed25519 -C "seu@email.com"

# Adicionar chave ao SSH agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Adicionar chave pública ao GitHub
cat ~/.ssh/id_ed25519.pub
# Copiar e colar em GitHub → Settings → SSH Keys
```

#### Token de Acesso Pessoal
```bash
# Para HTTPS, usar token ao invés de senha
git clone https://github.com/user/repo.git
# Username: seu-usuario
# Password: seu-token-pessoal

# Configurar credential helper
git config --global credential.helper store
```

### 🔀 Conflitos de Merge

#### Resolver Conflitos Manualmente
```bash
# Durante merge com conflito:
git status  # Ver arquivos conflitantes

# Editar arquivos com conflito:
<<<<<<< HEAD
Seu código
=======
Código da outra branch
>>>>>>> feature-branch

# Após resolver:
git add arquivo-resolvido.txt
git commit -m "Resolve merge conflict"
```

#### Ferramentas de Merge
```bash
# Configurar merge tool
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd 'code --wait $MERGED'

# Usar merge tool
git mergetool

# Abortar merge
git merge --abort
```

### 🔄 Desfazer Mudanças

#### Desfazer último commit
```bash
# Mantendo mudanças no working directory
git reset --soft HEAD~1

# Removendo mudanças
git reset --hard HEAD~1

# Criar commit que desfaz (recomendado para repos compartilhados)
git revert HEAD
```

#### Arquivo modificado por engano
```bash
# Descartar mudanças no working directory
git restore arquivo.txt
git checkout -- arquivo.txt  # Comando antigo

# Remover do staging
git restore --staged arquivo.txt
git reset HEAD arquivo.txt    # Comando antigo
```

#### Commit na branch errada
```bash
# Mover último commit para nova branch
git branch nova-branch
git reset --hard HEAD~1
git checkout nova-branch
```

### 🌿 Problemas com Branches

#### Branch divergiu do remoto
```bash
# Opção 1: Merge
git pull origin main

# Opção 2: Rebase (história mais limpa)
git pull --rebase origin main

# Se houver conflitos durante rebase:
# 1. Resolver conflitos
# 2. git add arquivo-resolvido
# 3. git rebase --continue

# Abortar rebase
git rebase --abort
```

#### Deletar branch local que não existe no remoto
```bash
# Limpar referências remotas
git remote prune origin

# Deletar branch local
git branch -d nome-branch

# Forçar deleção (se não foi merged)
git branch -D nome-branch
```

### 📦 Problemas com Repositório

#### Repositório muito grande
```bash
# Ver arquivos grandes
git rev-list --objects --all | git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | sed -n 's/^blob //p' | sort --numeric-sort --key=2 | tail -10

# Remover arquivo do histórico (CUIDADO!)
git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch arquivo-grande.zip' --prune-empty --tag-name-filter cat -- --all

# Alternativa moderna (Git 2.22+)
git filter-repo --strip-blobs-bigger-than 10M
```

#### Limpeza geral
```bash
# Limpar arquivos não rastreados
git clean -fd

# Limpar cache
git rm -r --cached .
git add .
git commit -m "Clean cache"

# Garbage collection
git gc --aggressive --prune=now
```

### 🔗 Problemas com Remote

#### URL remota incorreta
```bash
# Ver URL atual
git remote -v

# Alterar URL
git remote set-url origin https://github.com/user/repo.git

# Adicionar novo remote
git remote add upstream https://github.com/original/repo.git
```

#### Push rejeitado
```bash
# Erro: Updates were rejected
# Solução: Pull antes do push
git pull origin main
git push origin main

# Se histórico divergiu muito:
git pull --rebase origin main
git push origin main
```

### 📝 Problemas com Commits

#### Mensagem de commit errada
```bash
# Alterar último commit
git commit --amend -m "Nova mensagem"

# Alterar commit mais antigo (rebase interativo)
git rebase -i HEAD~3
# Trocar 'pick' por 'reword' no commit desejado
```

#### Arquivo esquecido no último commit
```bash
# Adicionar arquivo ao último commit
git add arquivo-esquecido.txt
git commit --amend --no-edit
```

#### Commit vazio por engano
```bash
# Remover commit vazio
git reset HEAD~1

# Ou usar rebase interativo
git rebase -i HEAD~2
# Trocar 'pick' por 'drop' no commit vazio
```

### 🏷️ Problemas com Tags

#### Tag na versão errada
```bash
# Deletar tag local
git tag -d v1.0.0

# Deletar tag remota
git push origin --delete v1.0.0

# Criar tag no commit correto
git tag -a v1.0.0 abc123 -m "Versão correta"
git push origin v1.0.0
```

## 🆘 Comandos de Emergência

### 🔍 Diagnóstico
```bash
# Verificar status geral
git status

# Ver histórico
git log --oneline -10

# Ver diferenças
git diff
git diff --staged

# Verificar integridade
git fsck

# Ver reflog (histórico de mudanças)
git reflog
```

### 🏥 Recuperação
```bash
# Recuperar arquivo deletado
git checkout HEAD~1 -- arquivo-deletado.txt

# Recuperar commit "perdido" via reflog
git reflog
git checkout abc123
git branch branch-recuperada

# Voltar estado anterior do repositório
git reset --hard HEAD~1

# Backup antes de operações perigosas
git branch backup-$(date +%Y%m%d-%H%M%S)
```

### 🧰 Kit de Sobrevivência

```bash
# 1. Sempre fazer backup antes de operações destrutivas
git branch backup

# 2. Verificar estado antes de fazer merge/rebase
git status
git log --oneline -5

# 3. Em caso de pânico, parar tudo
git merge --abort
git rebase --abort
git cherry-pick --abort

# 4. Recuperar via reflog
git reflog
git reset --hard HEAD@{5}

# 5. Último recurso: re-clonar
cd ..
git clone https://github.com/user/repo.git repo-novo
# Copiar mudanças locais manualmente
```

## 📚 Recursos para Ajuda

### 🔍 Comandos de Help
```bash
# Help geral
git help

# Help de comando específico
git help commit
git commit --help

# Versão resumida
git commit -h
```

### 🌐 Recursos Online
- [Git Documentation](https://git-scm.com/docs)
- [GitHub Docs](https://docs.github.com)
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)
- [Git Branching Game](https://learngitbranching.js.org)
- [Oh Shit, Git!?!](https://ohshitgit.com/) - Soluções rápidas

### 📱 Ferramentas Visuais
- **GitKraken** - Cliente visual
- **SourceTree** - Cliente Atlassian
- **GitHub Desktop** - Cliente oficial GitHub
- **VS Code** - Extensões Git integradas

---

**Anterior**: [06-comandos-avancados.md](06-comandos-avancados.md) | **Início**: [README.md](README.md)