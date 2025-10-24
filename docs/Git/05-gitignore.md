# 05. Configurando .gitignore

## 🎯 O que é .gitignore?

Arquivo que define quais arquivos/pastas o Git deve **ignorar**:
- Arquivos temporários
- Dependências baixadas
- Configurações locais
- Arquivos de build
- Dados sensíveis

## 📝 Estrutura Básica

```gitignore
# Comentários começam com #

# Ignorar arquivo específico
arquivo.txt

# Ignorar todos os arquivos com extensão
*.log
*.tmp

# Ignorar pasta
node_modules/
dist/

# Ignorar, exceto um arquivo específico
temp/*
!temp/importante.txt

# Padrões globais
**/*.cache
```

## 🌍 Templates por Linguagem

### Python
```gitignore
# Byte-compiled / optimized files
__pycache__/
*.py[cod]
*$py.class

# Virtual environments
venv/
env/
ENV/
.venv/

# Jupyter Notebooks
.ipynb_checkpoints

# PyInstaller
*.manifest
*.spec

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/

# pytest
.pytest_cache/
.coverage
htmlcov/

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Environment variables
.env
.env.local
.env.development.local
.env.test.local
.env.production.local
```

### Node.js / JavaScript
```gitignore
# Dependencies
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
package-lock.json  # (opcional)
yarn.lock         # (opcional)

# Build outputs
dist/
build/
out/

# Runtime data
pids
*.pid
*.seed
*.pid.lock

# Coverage directory used by tools like istanbul
coverage/
*.lcov

# nyc test coverage
.nyc_output

# ESLint cache
.eslintcache

# TypeScript cache
*.tsbuildinfo

# Optional npm cache directory
.npm

# Optional REPL history
.node_repl_history

# Output of 'npm pack'
*.tgz

# Yarn Integrity file
.yarn-integrity

# Environment variables
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# Next.js
.next/
out/

# Nuxt.js
.nuxt/
.output/

# Vite
.vite/
```

### Java
```gitignore
# Compiled class files
*.class

# Log files
*.log

# BlueJ files
*.ctxt

# Mobile Tools for Java (J2ME)
.mtj.tmp/

# Package Files
*.jar
*.war
*.nar
*.ear
*.zip
*.tar.gz
*.rar

# Virtual machine crash logs
hs_err_pid*

# Maven
target/
pom.xml.tag
pom.xml.releaseBackup
pom.xml.versionsBackup
pom.xml.next
release.properties
dependency-reduced-pom.xml
buildNumber.properties
.mvn/timing.properties
.mvn/wrapper/maven-wrapper.jar

# Gradle
.gradle/
build/
!gradle/wrapper/gradle-wrapper.jar
!**/src/main/**/build/
!**/src/test/**/build/

# IntelliJ IDEA
.idea/
*.iws
*.iml
*.ipr
out/
!**/src/main/**/out/
!**/src/test/**/out/

# Eclipse
.apt_generated
.classpath
.factorypath
.project
.settings
.springBeans
.sts4-cache
bin/
!**/src/main/**/bin/
!**/src/test/**/bin/

# NetBeans
/nbproject/private/
/nbbuild/
/dist/
/nbdist/
/.nb-gradle/

# VS Code
.vscode/
```

### C#/.NET
```gitignore
# Build results
[Dd]ebug/
[Dd]ebugPublic/
[Rr]elease/
[Rr]eleases/
x64/
x86/
[Ww][Ii][Nn]32/
[Aa][Rr][Mm]/
[Aa][Rr][Mm]64/
bld/
[Bb]in/
[Oo]bj/
[Ll]og/

# Visual Studio
.vs/
*.suo
*.user
*.sln.docstates
*.userprefs

# ReSharper
_ReSharper*/
*.[Rr]e[Ss]harper
*.DotSettings.user

# NuGet Packages
*.nupkg
**/[Pp]ackages/*
!**/[Pp]ackages/build/
!**/[Pp]ackages/repositories.config

# MSTest test Results
[Tt]est[Rr]esult*/
[Bb]uild[Ll]og.*

# NUNIT
*.VisualState.xml
TestResult.xml

# .NET Core
project.lock.json
project.fragment.lock.json
artifacts/

# Rider
.idea/
*.sln.iml

# User-specific files
*.rsuser
*.suo
*.user
*.userosscache
*.sln.docstates
```

## 🛠️ IDEs e Editores

```gitignore
# Visual Studio Code
.vscode/
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json

# IntelliJ IDEA
.idea/
*.iws
*.iml
*.ipr

# Sublime Text
*.sublime-workspace
*.sublime-project

# Vim
*.swp
*.swo
*~

# Emacs
*~
\#*\#
/.emacs.desktop
/.emacs.desktop.lock
*.elc
auto-save-list
tramp
.\#*
```

## 💻 Sistemas Operacionais

```gitignore
# Windows
Thumbs.db
ehthumbs.db
Desktop.ini
$RECYCLE.BIN/
*.cab
*.msi
*.msix
*.msm
*.msp
*.lnk

# macOS
.DS_Store
.AppleDouble
.LSOverride
Icon
._*
.DocumentRevisions-V100
.fseventsd
.Spotlight-V100
.TemporaryItems
.Trashes
.VolumeIcon.icns
.com.apple.timemachine.donotpresent
.AppleDB
.AppleDesktop
Network Trash Folder
Temporary Items
.apdisk

# Linux
*~
.fuse_hidden*
.directory
.Trash-*
.nfs*
```

## ⚡ Comandos Úteis

```bash
# Verificar arquivos ignorados
git status --ignored

# Ver o que seria ignorado
git check-ignore -v arquivo.txt

# Parar de rastrear arquivo já commitado
git rm --cached arquivo.txt
git commit -m "Stop tracking arquivo.txt"

# Atualizar .gitignore para arquivos já rastreados
git rm -r --cached .
git add .
git commit -m "Update .gitignore"
```

## 🌟 Boas Práticas

### ✅ FAZER
- Ignorar arquivos gerados automaticamente
- Ignorar dependências (node_modules, venv)
- Ignorar configurações locais/pessoais
- Ignorar arquivos temporários
- Ignorar dados sensíveis (.env)

### ❌ NÃO FAZER
- Ignorar código fonte
- Ignorar documentação importante
- Ignorar arquivos de configuração compartilhados
- Commitar .gitignore vazio
- Ignorar arquivos essenciais para build

## 🔧 Exemplo Completo (Projeto Full-Stack)

```gitignore
# Dependencies
node_modules/
__pycache__/
venv/
env/

# Build outputs
dist/
build/
*.pyc
*.pyo

# Environment variables
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# Logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Runtime data
pids
*.pid
*.seed
*.pid.lock

# Coverage directory
coverage/
.nyc_output

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS generated files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Database
*.db
*.sqlite
*.sqlite3

# Jupyter Notebooks
.ipynb_checkpoints

# Cache directories
.cache/
.parcel-cache/
.next/
.nuxt/
```

## 🌐 Recursos Online

- [gitignore.io](https://gitignore.io) - Gerador de .gitignore
- [GitHub Templates](https://github.com/github/gitignore) - Coleção oficial
- [Toptal Generator](https://www.toptal.com/developers/gitignore) - Gerador interativo

---

**Anterior**: [04-github-workflow.md](04-github-workflow.md) | **Próximo**: [06-comandos-avancados.md](06-comandos-avancados.md)