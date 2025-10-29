"""
Script para testar a API de predição do Titanic
"""

import requests
import json
from time import sleep

API_URL = "http://localhost:8000"

def print_section(title):
    """Imprime uma seção formatada"""
    print("\n" + "="*60)
    print(f"🧪 {title}")
    print("="*60)

def test_health_check():
    """Testa o endpoint raiz"""
    print_section("TEST 1: Health Check")
    
    response = requests.get(f"{API_URL}/")
    print(f"Status: {response.status_code}")
    print(f"Response:")
    print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    
    return response.status_code == 200

def test_model_info():
    """Testa o endpoint de informações do modelo"""
    print_section("TEST 2: Model Info")
    
    response = requests.get(f"{API_URL}/model/info")
    print(f"Status: {response.status_code}")
    print(f"Response:")
    print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    
    return response.status_code == 200

def test_prediction_high_survival():
    """Testa predição com alta chance de sobrevivência"""
    print_section("TEST 3: Predição - Alta Chance (1ª classe, mulher)")
    
    passenger = {
        "pclass": 1,
        "sex": "female",
        "age": 29.0,
        "siblings_spouses": 0,
        "parents_children": 0,
        "fare": 211.5
    }
    
    print("Passageiro:")
    print(json.dumps(passenger, indent=2, ensure_ascii=False))
    
    response = requests.post(f"{API_URL}/predict", json=passenger)
    print(f"\nStatus: {response.status_code}")
    print(f"Predição:")
    result = response.json()
    print(json.dumps(result, indent=2, ensure_ascii=False))
    
    print(f"\n{'='*40}")
    print(f"🎯 Resultado: {'SOBREVIVEU ✅' if result['survived'] == 1 else 'NÃO SOBREVIVEU ❌'}")
    print(f"📊 Probabilidade: {result['probability']*100:.2f}%")
    print(f"📈 Avaliação: {result['survival_chance']}")
    
    return response.status_code == 200

def test_prediction_low_survival():
    """Testa predição com baixa chance de sobrevivência"""
    print_section("TEST 4: Predição - Baixa Chance (3ª classe, homem)")
    
    passenger = {
        "pclass": 3,
        "sex": "male",
        "age": 22.0,
        "siblings_spouses": 1,
        "parents_children": 0,
        "fare": 7.25
    }
    
    print("Passageiro:")
    print(json.dumps(passenger, indent=2, ensure_ascii=False))
    
    response = requests.post(f"{API_URL}/predict", json=passenger)
    print(f"\nStatus: {response.status_code}")
    print(f"Predição:")
    result = response.json()
    print(json.dumps(result, indent=2, ensure_ascii=False))
    
    print(f"\n{'='*40}")
    print(f"🎯 Resultado: {'SOBREVIVEU ✅' if result['survived'] == 1 else 'NÃO SOBREVIVEU ❌'}")
    print(f"📊 Probabilidade: {result['probability']*100:.2f}%")
    print(f"📈 Avaliação: {result['survival_chance']}")
    
    return response.status_code == 200

def test_batch_prediction():
    """Testa predição em lote"""
    print_section("TEST 5: Predição em Lote")
    
    passengers = [
        {
            "pclass": 1,
            "sex": "female",
            "age": 25.0,
            "siblings_spouses": 0,
            "parents_children": 0,
            "fare": 100.0
        },
        {
            "pclass": 2,
            "sex": "male",
            "age": 30.0,
            "siblings_spouses": 1,
            "parents_children": 0,
            "fare": 20.0
        },
        {
            "pclass": 3,
            "sex": "female",
            "age": 18.0,
            "siblings_spouses": 0,
            "parents_children": 2,
            "fare": 15.0
        }
    ]
    
    print(f"Testando {len(passengers)} passageiros...")
    
    response = requests.post(f"{API_URL}/predict/batch", json=passengers)
    print(f"\nStatus: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        print(f"\n📊 Total de predições: {result['total']}")
        
        for i, prediction in enumerate(result['predictions'], 1):
            passenger = prediction['input']
            print(f"\n{'─'*40}")
            print(f"Passageiro #{i}:")
            print(f"  Classe: {passenger['pclass']}, Sexo: {passenger['sex']}, Idade: {passenger['age']}")
            print(f"  🎯 {'SOBREVIVEU ✅' if prediction['survived'] == 1 else 'NÃO SOBREVIVEU ❌'}")
            print(f"  📊 Probabilidade: {prediction['probability']*100:.2f}%")
            print(f"  📈 Chance: {prediction['survival_chance']}")
    
    return response.status_code == 200

def test_invalid_input():
    """Testa validação de entrada inválida"""
    print_section("TEST 6: Validação - Entrada Inválida")
    
    # Classe inválida (deve ser 1, 2 ou 3)
    invalid_passenger = {
        "pclass": 5,  # ❌ Inválido
        "sex": "female",
        "age": 25.0,
        "siblings_spouses": 0,
        "parents_children": 0,
        "fare": 100.0
    }
    
    print("Tentando enviar passageiro com classe inválida (pclass=5)...")
    
    response = requests.post(f"{API_URL}/predict", json=invalid_passenger)
    print(f"Status: {response.status_code}")
    
    if response.status_code != 200:
        print(f"✅ Validação funcionou! Erro detectado:")
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
        return True
    else:
        print(f"❌ Validação não funcionou!")
        return False

def main():
    """Executa todos os testes"""
    print("\n" + "🚀"*30)
    print("TESTE COMPLETO DA API TITANIC")
    print("🚀"*30)
    
    # Aguardar API iniciar
    print("\n⏳ Aguardando API iniciar...")
    sleep(3)
    
    tests = [
        ("Health Check", test_health_check),
        ("Model Info", test_model_info),
        ("Predição Alta Chance", test_prediction_high_survival),
        ("Predição Baixa Chance", test_prediction_low_survival),
        ("Predição em Lote", test_batch_prediction),
        ("Validação de Entrada", test_invalid_input),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n❌ Erro no teste '{test_name}': {e}")
            results.append((test_name, False))
    
    # Resumo
    print_section("RESUMO DOS TESTES")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASSOU" if result else "❌ FALHOU"
        print(f"{status} - {test_name}")
    
    print(f"\n{'='*60}")
    print(f"📊 Total: {passed}/{total} testes passaram")
    print(f"📈 Taxa de sucesso: {passed/total*100:.1f}%")
    print(f"{'='*60}")
    
    if passed == total:
        print("\n🎉 TODOS OS TESTES PASSARAM! API FUNCIONANDO PERFEITAMENTE!")
    else:
        print(f"\n⚠️  {total-passed} teste(s) falharam. Verifique os logs acima.")

if __name__ == "__main__":
    main()
