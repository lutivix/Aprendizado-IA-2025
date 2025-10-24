# 06. Comandos Avançados

## 🔄 Rebase Interativo

### O que é Rebase?
**Rebase** reorganiza commits, "re-aplicando" eles em uma nova base.

```bash
# Rebase interativo dos últimos 3 commits
git rebase -i HEAD~3

# Opções no editor:
# pick   = usar commit
# reword = usar commit, mas editar mensagem
# edit   = usar commit, mas parar para alterações
# squash = usar commit, mas juntar com anterior
# drop   = remover commit
```

### Exemplo Prático
```bash
# Histórico antes:
# A---B---C---D (main)

# Rebase últimos 2 commits
git rebase -i HEAD~2

# Editor abre:
pick abc123 Adicionar feature
squash def456 Corrigir typo

# Resultado:
# A---B---C' (commit combinado)
```

## 🕐 Desfazer Mudanças

### Reset
```bash
# Reset soft (mantém arquivos no staging)
git reset --soft HEAD~1

# Reset mixed (default - mantém arquivos no working dir)
git reset HEAD~1
git reset --mixed HEAD~1

# Reset hard (APAGA tudo)
git reset --hard HEAD~1

# Reset para commit específico
git reset --hard abc123
```

### Revert
```bash
# Criar commit que desfaz outro commit
git revert abc123

# Revert merge commit
git revert -m 1 abc123

# Revert sem commit automático
git revert --no-commit abc123
```

### Restore (Git 2.23+)
```bash
# Restaurar arquivo do working directory
git restore arquivo.txt

# Restaurar do staging
git restore --staged arquivo.txt

# Restaurar de commit específico
git restore --source=HEAD~1 arquivo.txt
```

## 🍒 Cherry Pick

```bash
# Aplicar commit específico de outra branch
git cherry-pick abc123

# Cherry pick múltiplos commits
git cherry-pick abc123 def456

# Cherry pick com edição
git cherry-pick --edit abc123

# Cherry pick sem commit automático
git cherry-pick --no-commit abc123
```

## 🔍 Stash (Armazenar Temporariamente)

```bash
# Guardar mudanças não commitadas
git stash

# Stash com mensagem
git stash push -m "WIP: nova feature"

# Incluir arquivos não rastreados
git stash -u

# Incluir arquivos ignorados
git stash -a

# Listar stashes
git stash list

# Aplicar último stash
git stash pop

# Aplicar stash específico
git stash apply stash@{2}

# Ver conteúdo do stash
git stash show -p stash@{0}

# Deletar stash
git stash drop stash@{0}

# Limpar todos os stashes
git stash clear
```

## 🔍 Bisect (Encontrar Bug)

```bash
# Iniciar bisect
git bisect start

# Marcar commit atual como ruim
git bisect bad

# Marcar commit conhecido como bom
git bisect good abc123

# Git vai sugerir commits para testar
# Testar e marcar:
git bisect good    # Se funcionou
git bisect bad     # Se não funcionou

# Finalizar
git bisect reset
```

## 🏷️ Tags Avançadas

```bash
# Listar tags
git tag
git tag -l "v1.8.5*"

# Tag anotada com informações
git tag -a v1.4 -m "Versão 1.4"

# Tag assinada (GPG)
git tag -s v1.5 -m "Versão assinada"

# Tag em commit específico
git tag -a v1.2 abc123

# Verificar tag assinada
git tag -v v1.4.2.1

# Deletar tag local
git tag -d v1.4

# Deletar tag remota
git push origin --delete v1.4

# Checkout para tag
git checkout v1.4
```

## 🔗 Submodules

```bash
# Adicionar submodule
git submodule add https://github.com/user/repo.git path/to/submodule

# Clonar repositório com submodules
git clone --recurse-submodules https://github.com/user/repo.git

# Inicializar submodules após clone
git submodule init
git submodule update

# Ou em um comando
git submodule update --init --recursive

# Atualizar submodules
git submodule update --remote

# Status dos submodules
git submodule status

# Remover submodule
git submodule deinit path/to/submodule
git rm path/to/submodule
rm -rf .git/modules/path/to/submodule
```

## 📊 Log Avançado

```bash
# Log formatado
git log --pretty=format:"%h %an %ar - %s"

# Log com estatísticas
git log --stat

# Log com patch
git log -p

# Log de arquivos específicos
git log -- arquivo.txt

# Log entre datas
git log --since="2023-01-01" --until="2023-12-31"

# Log por autor
git log --author="João"

# Log com grep na mensagem
git log --grep="fix"

# Log visual
git log --graph --pretty=oneline --abbrev-commit

# Log personalizado
git log --pretty=format:"%C(yellow)%h%C(reset) %C(blue)%an%C(reset) %C(green)%ar%C(reset) - %s"
```

## 🔧 Configurações Avançadas

```bash
# Aliases úteis
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
git config --global alias.visual '!gitk'

# Log bonito
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

# Editor padrão
git config --global core.editor "code --wait"

# Merge tool
git config --global merge.tool vimdiff

# Push padrão
git config --global push.default current

# Rebase ao invés de merge no pull
git config --global pull.rebase true

# Auto-setup remote tracking
git config --global push.autoSetupRemote true
```

## 🔍 Reflog (Histórico de Referências)

```bash
# Ver reflog
git reflog

# Reflog de branch específica
git reflog main

# Recuperar commit "perdido"
git checkout abc123

# Criar branch a partir de reflog
git branch feature-recuperada abc123

# Limpar reflog
git reflog expire --expire=now --all
git gc --prune=now
```

## 🧹 Limpeza e Manutenção

```bash
# Limpar arquivos não rastreados
git clean -f

# Limpar arquivos e diretórios
git clean -fd

# Ver o que seria removido
git clean -n

# Limpar também arquivos ignorados
git clean -fx

# Garbage collection
git gc

# Verificar integridade do repositório
git fsck

# Comprimir banco de dados
git gc --aggressive

# Ver tamanho do repositório
git count-objects -vH

# Remover branches remotas que não existem mais
git remote prune origin
```

---

**Anterior**: [05-gitignore.md](05-gitignore.md) | **Próximo**: [07-solucao-problemas.md](07-solucao-problemas.md)