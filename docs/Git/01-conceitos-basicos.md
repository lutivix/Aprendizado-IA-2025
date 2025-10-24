# 01. Conceitos Básicos do Git

## 🤔 O que é Git?

**Git** é um sistema de controle de versão distribuído que ajuda a:
- **Rastrear** mudanças no código
- **Colaborar** com outros desenvolvedores
- **Voltar** a versões anteriores
- **Gerenciar** diferentes versões do projeto

## 📂 Estrutura Básica

```
projeto/
├── .git/           # Pasta oculta com histórico
├── arquivo1.py     # Seus arquivos
├── arquivo2.js
└── .gitignore      # Arquivos a ignorar
```

## 🔄 Estados dos Arquivos

### 1. **Working Directory** (Diretório de Trabalho)
- Onde você edita os arquivos
- Mudanças ainda não rastreadas

### 2. **Staging Area** (Área de Preparação)
- Arquivos prontos para commit
- Use `git add` para colocar aqui

### 3. **Repository** (Repositório)
- Histórico permanente
- Use `git commit` para salvar aqui

```
Working Dir → [git add] → Staging → [git commit] → Repository
```

## 🏷️ Principais Termos

| Termo | Significado |
|-------|-------------|
| **Repository (Repo)** | Pasta com controle de versão |
| **Commit** | Snapshot das mudanças |
| **Branch** | Linha de desenvolvimento |
| **Clone** | Copiar repositório remoto |
| **Fork** | Copiar repo para sua conta |
| **Pull Request (PR)** | Proposta de mudança |
| **Merge** | Juntar branches |
| **Push** | Enviar para repositório remoto |
| **Pull** | Baixar do repositório remoto |

## 🎯 Fluxo Básico

1. **Modificar** arquivos
2. **Adicionar** ao staging (`git add`)
3. **Comitar** mudanças (`git commit`)
4. **Enviar** para repositório remoto (`git push`)

---

**Próximo**: [02-comandos-essenciais.md](02-comandos-essenciais.md)