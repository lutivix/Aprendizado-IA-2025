@echo off
echo 🔧 Configurando PATH do Anaconda para VS Code...

REM Adicionar Anaconda ao PATH da sessão atual
set PATH=C:\ProgramData\anaconda3;C:\ProgramData\anaconda3\Scripts;C:\ProgramData\anaconda3\condabin;%PATH%

echo ✅ PATH configurado com sucesso!
echo 🐍 Testando Python do Anaconda...

python --version
echo.

echo 🔧 Testando conda...
conda --version
echo.

echo 🎯 Para usar este PATH permanentemente:
echo 1. Abra as Configurações do Sistema
echo 2. Vá em Variáveis de Ambiente
echo 3. Adicione ao PATH do sistema:
echo    - C:\ProgramData\anaconda3
echo    - C:\ProgramData\anaconda3\Scripts  
echo    - C:\ProgramData\anaconda3\condabin
echo.

echo 💡 Ou execute este script sempre antes de usar o VS Code
pause