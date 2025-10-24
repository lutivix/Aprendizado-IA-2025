# 04. GitHub Workflow

## 🌍 Git vs GitHub

| Git | GitHub |
|-----|--------|
| Sistema de controle de versão | Plataforma de hospedagem |
| Local | Remoto |
| Comandos de terminal | Interface web + comandos |
| Repositórios | Repositórios + Issues + PRs |

## 🔄 Fluxo Completo GitHub

### 1. Fork & Clone
```bash
# No GitHub: Fork do repositório
# Depois clonar seu fork
git clone https://github.com/SEU-USUARIO/projeto.git
cd projeto

# Adicionar repositório original como upstream
git remote add upstream https://github.com/USUARIO-ORIGINAL/projeto.git
```

### 2. Criar Feature Branch
```bash
# Sincronizar com upstream
git fetch upstream
git checkout main
git merge upstream/main

# Criar branch para feature
git checkout -b feature/nova-funcionalidade
```

### 3. Desenvolver
```bash
# Fazer mudanças
# ... editar arquivos ...

# Commits incrementais
git add .
git commit -m "feat: adicionar validação de email"

git add .
git commit -m "test: adicionar testes para validação"

git add .
git commit -m "docs: atualizar README com nova feature"
```

### 4. Push da Branch
```bash
# Enviar branch para seu fork
git push -u origin feature/nova-funcionalidade
```

### 5. Pull Request
```bash
# No GitHub:
# 1. Ir para seu fork
# 2. Clicar "Compare & pull request"
# 3. Preencher título e descrição
# 4. Criar Pull Request
```

## 🎯 Pull Requests (PRs)

### Anatomia de um PR
```markdown
## 📋 Descrição
Breve descrição da mudança

## 🔧 Mudanças
- [ ] Adicionar validação de email
- [ ] Criar testes unitários
- [ ] Atualizar documentação

## 🧪 Como testar
1. Fazer checkout da branch
2. Executar `npm test`
3. Verificar funcionalidade

## 📸 Screenshots
(se aplicável)
```

### Template de PR
```markdown
<!-- .github/pull_request_template.md -->
## Tipo de mudança
- [ ] Bug fix
- [ ] Nova feature
- [ ] Breaking change
- [ ] Documentação

## Checklist
- [ ] Código testado localmente
- [ ] Testes passando
- [ ] Documentação atualizada
- [ ] Sem conflitos com main
```

## 📝 Convenções de Commit

### Conventional Commits
```bash
# Formato: tipo(escopo): descrição

# Tipos:
feat:     # Nova funcionalidade
fix:      # Correção de bug
docs:     # Documentação
style:    # Formatação (não afeta lógica)
refactor: # Refatoração
test:     # Testes
chore:    # Tarefas de build, CI, etc.

# Exemplos:
git commit -m "feat(auth): adicionar login com Google"
git commit -m "fix(ui): corrigir alinhamento do botão"
git commit -m "docs: atualizar guia de instalação"
```

## 🏷️ Releases e Tags

### Criar Tag
```bash
# Tag simples
git tag v1.0.0

# Tag com mensagem
git tag -a v1.0.0 -m "Primeira versão estável"

# Enviar tags
git push origin v1.0.0
git push origin --tags
```

### Semantic Versioning
```
v1.2.3
│ │ │
│ │ └── PATCH: correções de bugs
│ └──── MINOR: novas features (compatível)
└────── MAJOR: mudanças quebram compatibilidade
```

## 🔧 Issues e Project Management

### Template de Issue
```markdown
<!-- .github/ISSUE_TEMPLATE/bug_report.md -->
## 🐛 Descrição do Bug
Descrição clara do problema

## 🔄 Passos para Reproduzir
1. Ir para '...'
2. Clicar em '....'
3. Scroll down to '....'
4. Ver erro

## ✅ Comportamento Esperado
O que deveria acontecer

## 📷 Screenshots
Se aplicável

## 🌍 Ambiente
- OS: [Windows/Mac/Linux]
- Browser: [Chrome/Firefox/Safari]
- Versão: [v1.0.0]
```

### Linking Issues e PRs
```bash
# No commit ou PR:
"fix: corrigir bug do login (closes #123)"
"feat: adicionar dashboard (refs #456)"

# Palavras-chave que fecham issues:
# closes, fixes, resolves
```

## 🤖 GitHub Actions (CI/CD)

### Workflow Básico
```yaml
# .github/workflows/ci.yml
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: npm install
      - run: npm test
```

## 🛡️ Proteção de Branches

### Configurar Branch Protection
```
Settings → Branches → Add rule

✅ Require pull request reviews
✅ Require status checks to pass
✅ Require branches to be up to date
✅ Include administrators
```

## 📚 Comandos GitHub CLI

```bash
# Instalar: https://cli.github.com/

# Login
gh auth login

# Criar repo
gh repo create meu-projeto --public

# Criar PR
gh pr create --title "Nova feature" --body "Descrição"

# Ver PRs
gh pr list

# Fazer checkout de PR
gh pr checkout 123
```

---

**Anterior**: [03-branches.md](03-branches.md) | **Próximo**: [05-gitignore.md](05-gitignore.md)