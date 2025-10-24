# 03. Trabalhando com Branches

## 🌿 O que são Branches?

**Branches** são linhas paralelas de desenvolvimento que permitem:
- Trabalhar em features sem afetar o código principal
- Colaborar sem conflitos
- Testar mudanças isoladamente
- Organizar o desenvolvimento

```
main:     A---B---C---F---G
              \         /
feature:       D---E---/
```

## 📋 Comandos Básicos

### Ver Branches
```bash
# Listar branches locais
git branch

# Listar todas as branches (local + remote)
git branch -a

# Ver branch atual
git branch --show-current
```

### Criar Branches
```bash
# Criar nova branch
git branch feature-login

# Criar e mudar para a branch
git checkout -b feature-login

# Comando mais moderno
git switch -c feature-login
```

### Mudar de Branch
```bash
# Mudar para branch existente
git checkout main
git switch main          # Comando mais moderno

# Voltar para branch anterior
git checkout -
git switch -
```

## 🔄 Fluxo de Trabalho com Branches

### 1. Criar Feature Branch
```bash
# Partir da main atualizada
git checkout main
git pull origin main

# Criar nova branch
git checkout -b feature-nova-funcao
```

### 2. Trabalhar na Branch
```bash
# Fazer mudanças
# ... editar arquivos ...

# Adicionar e comitar
git add .
git commit -m "Implementar nova funcionalidade"
```

### 3. Enviar Branch para GitHub
```bash
# Primeira vez
git push -u origin feature-nova-funcao

# Próximas vezes
git push
```

### 4. Fazer Merge
```bash
# Voltar para main
git checkout main

# Fazer merge
git merge feature-nova-funcao

# Enviar merge para GitHub
git push origin main
```

### 5. Limpar Branch
```bash
# Deletar branch local
git branch -d feature-nova-funcao

# Deletar branch remota
git push origin --delete feature-nova-funcao
```

## 🔀 Tipos de Merge

### Fast-Forward Merge
```bash
# Quando não há commits na main
git merge feature-branch
```

### Merge Commit
```bash
# Criar commit de merge
git merge --no-ff feature-branch
```

### Rebase (Alternativa ao Merge)
```bash
# Aplicar commits em cima da main
git checkout feature-branch
git rebase main
```

## 🌟 Estratégias de Branch

### Git Flow Simplificado
```
main        ← Produção
develop     ← Desenvolvimento
feature/*   ← Novas funcionalidades
hotfix/*    ← Correções urgentes
```

### GitHub Flow (Mais Simples)
```
main        ← Produção
feature/*   ← Tudo parte da main
```

## 📝 Convenções de Nomes

```bash
# Features
feature/login-system
feature/user-dashboard
feat/payment-integration

# Correções
fix/button-alignment
bugfix/login-error
hotfix/security-patch

# Melhorias
improve/performance
refactor/user-service
update/dependencies
```

## ⚡ Comandos Úteis

```bash
# Ver diferenças entre branches
git diff main feature-branch

# Ver commits únicos da branch
git log main..feature-branch

# Ver arquivos modificados na branch
git diff --name-only main

# Sincronizar com branch remota
git fetch origin
git checkout -b feature-branch origin/feature-branch
```

## 🔧 Cenários Práticos

### Começar nova feature
```bash
git checkout main
git pull origin main
git checkout -b feature/user-profile
# ... trabalhar ...
git add .
git commit -m "Add user profile page"
git push -u origin feature/user-profile
```

### Atualizar branch com main
```bash
git checkout feature/user-profile
git merge main
# ou
git rebase main
```

### Resolver conflitos
```bash
# Depois do merge com conflito
# ... editar arquivos conflitantes ...
git add .
git commit -m "Resolve merge conflicts"
```

---

**Anterior**: [02-comandos-essenciais.md](02-comandos-essenciais.md) | **Próximo**: [04-github-workflow.md](04-github-workflow.md)