#!/usr/bin/env python3
"""
🐍 Script de Verificação - Setup Python + Anaconda
Semana 1 - Fundamentos IA
"""

import sys
import platform
from datetime import datetime

def verificar_python():
    """Verifica a versão do Python"""
    print("=" * 50)
    print("🐍 VERIFICAÇÃO PYTHON")
    print("=" * 50)
    print(f"Versão Python: {sys.version}")
    print(f"Executável: {sys.executable}")
    print(f"Plataforma: {platform.platform()}")
    print()

def verificar_bibliotecas():
    """Verifica se as principais bibliotecas estão instaladas"""
    print("=" * 50)
    print("📚 VERIFICAÇÃO BIBLIOTECAS")
    print("=" * 50)
    
    bibliotecas = [
        ('numpy', 'NumPy'),
        ('pandas', 'Pandas'),
        ('matplotlib', 'Matplotlib'),
        ('seaborn', 'Seaborn'),
        ('sklearn', 'Scikit-learn'),
        ('jupyter', 'Jupyter'),
        ('ipython', 'IPython')
    ]
    
    instaladas = []
    nao_instaladas = []
    
    for modulo, nome in bibliotecas:
        try:
            __import__(modulo)
            versao = __import__(modulo).__version__ if hasattr(__import__(modulo), '__version__') else 'N/A'
            print(f"✅ {nome}: {versao}")
            instaladas.append(nome)
        except ImportError:
            print(f"❌ {nome}: Não instalada")
            nao_instaladas.append(nome)
    
    print(f"\n📊 Resumo: {len(instaladas)}/{len(bibliotecas)} bibliotecas instaladas")
    return len(nao_instaladas) == 0

def verificar_conda():
    """Verifica se conda está disponível"""
    print("=" * 50)
    print("🔧 VERIFICAÇÃO CONDA")
    print("=" * 50)
    
    try:
        import subprocess
        result = subprocess.run(['conda', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Conda: {result.stdout.strip()}")
            
            # Listar ambientes
            env_result = subprocess.run(['conda', 'env', 'list'], capture_output=True, text=True)
            print(f"🌍 Ambientes disponíveis:")
            for line in env_result.stdout.split('\n')[2:]:  # Skip header
                if line.strip():
                    print(f"   {line}")
            return True
        else:
            print("❌ Conda não encontrado")
            return False
    except Exception as e:
        print(f"❌ Erro ao verificar conda: {e}")
        return False

def main():
    """Função principal"""
    print("🚀 VERIFICAÇÃO COMPLETA DO AMBIENTE PYTHON")
    print(f"⏰ Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print()
    
    verificar_python()
    bibliotecas_ok = verificar_bibliotecas()
    conda_ok = verificar_conda()
    
    print("=" * 50)
    print("📋 RESULTADO FINAL")
    print("=" * 50)
    
    if bibliotecas_ok and conda_ok:
        print("🎉 PARABÉNS! Seu ambiente está completamente configurado!")
        print("✅ Pronto para começar com IA e Data Science!")
    elif conda_ok:
        print("⚠️  Conda instalado, mas algumas bibliotecas podem estar faltando")
        print("💡 Execute: conda install numpy pandas matplotlib seaborn scikit-learn jupyter")
    else:
        print("❌ Ambiente incompleto")
        print("💡 Verifique se o Anaconda foi instalado corretamente")
    
    print("\n🔄 Execute este script novamente após qualquer instalação/correção")

if __name__ == "__main__":
    main()