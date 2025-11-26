"""
Script para testar a API
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def test_root():
    """Testar endpoint raiz"""
    print("🧪 Testando endpoint raiz...")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
    print()


def test_health():
    """Testar health check"""
    print("🧪 Testando health check...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
    print()


def test_model_info():
    """Testar informações do modelo"""
    print("🧪 Testando model info...")
    response = requests.get(f"{BASE_URL}/model/info")
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"Modelo: {data.get('model_name')}")
        print(f"Accuracy: {data.get('accuracy'):.4f}")
    print()


def test_single_prediction():
    """Testar predição única"""
    print("🧪 Testando predição única...")
    
    # Exemplo 1: Passageiro de 3ª classe (baixa chance)
    passenger1 = {
        "pclass": 3,
        "sex": "male",
        "age": 22.0,
        "sibsp": 1,
        "parch": 0,
        "fare": 7.25,
        "embarked": "S"
    }
    
    response = requests.post(f"{BASE_URL}/predict", json=passenger1)
    print(f"Status: {response.status_code}")
    print("Passageiro 1 (3ª classe, homem):")
    print(json.dumps(response.json(), indent=2))
    print()
    
    # Exemplo 2: Passageira de 1ª classe (alta chance)
    passenger2 = {
        "pclass": 1,
        "sex": "female",
        "age": 38.0,
        "sibsp": 1,
        "parch": 0,
        "fare": 71.2833,
        "embarked": "C"
    }
    
    response = requests.post(f"{BASE_URL}/predict", json=passenger2)
    print("Passageiro 2 (1ª classe, mulher):")
    print(json.dumps(response.json(), indent=2))
    print()


def test_batch_prediction():
    """Testar predição em lote"""
    print("🧪 Testando predição em lote...")
    
    passengers = [
        {
            "pclass": 3,
            "sex": "male",
            "age": 22.0,
            "sibsp": 1,
            "parch": 0,
            "fare": 7.25,
            "embarked": "S"
        },
        {
            "pclass": 1,
            "sex": "female",
            "age": 38.0,
            "sibsp": 1,
            "parch": 0,
            "fare": 71.2833,
            "embarked": "C"
        },
        {
            "pclass": 2,
            "sex": "female",
            "age": 26.0,
            "sibsp": 0,
            "parch": 0,
            "fare": 13.0,
            "embarked": "S"
        }
    ]
    
    response = requests.post(f"{BASE_URL}/predict/batch", json=passengers)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"Total: {data['total']}")
        print(f"Sobreviventes: {data['survived_count']}")
        print(f"Taxa de sobrevivência: {data['survival_rate']:.2%}")
    print()


def main():
    """Função principal"""
    print("=" * 60)
    print("🧪 Testando Titanic ML API")
    print("=" * 60)
    print()
    
    try:
        test_root()
        test_health()
        test_model_info()
        test_single_prediction()
        test_batch_prediction()
        
        print("=" * 60)
        print("✅ Todos os testes concluídos!")
        print("=" * 60)
        
    except requests.exceptions.ConnectionError:
        print("❌ Erro: API não está rodando!")
        print("💡 Execute: python app.py")
    except Exception as e:
        print(f"❌ Erro: {e}")


if __name__ == "__main__":
    main()
