"""
Script para treinar e salvar o modelo de ML do Titanic
Usa os mesmos dados e features do notebook de EDA
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib
import json
import warnings
warnings.filterwarnings('ignore')

def load_data():
    """Carrega o dataset do Titanic"""
    print("📊 Carregando dataset do Titanic...")
    
    # URL do Stanford (fonte confiável)
    url = 'https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv'
    
    try:
        df = pd.read_csv(url)
        print(f"✅ Dataset carregado da web: {len(df)} registros")
        
        # Verificar se tem as colunas necessárias
        required_cols = ['Survived', 'Pclass', 'Sex', 'Age', 'Siblings/Spouses Aboard', 
                        'Parents/Children Aboard', 'Fare']
        
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Colunas faltando no dataset: {missing_cols}")
            
        return df
        
    except Exception as e:
        print(f"❌ Erro ao carregar dataset: {e}")
        raise

def feature_engineering(df):
    """Aplica feature engineering no dataset"""
    print("\n🔧 Aplicando Feature Engineering...")
    
    # Criar cópia para não modificar original
    df_processed = df.copy()
    
    # 1. Converter Sex para numérico
    df_processed['sex_numeric'] = (df_processed['Sex'] == 'male').astype(int)
    
    # 2. Criar family_size
    df_processed['family_size'] = df_processed['Siblings/Spouses Aboard'] + \
                                   df_processed['Parents/Children Aboard'] + 1
    
    # 3. Criar is_alone
    df_processed['is_alone'] = (df_processed['family_size'] == 1).astype(int)
    
    # 4. Tratar valores ausentes em Age
    df_processed['Age'].fillna(df_processed['Age'].median(), inplace=True)
    
    # 5. Tratar valores ausentes em Fare
    df_processed['Fare'].fillna(df_processed['Fare'].median(), inplace=True)
    
    print("✅ Features criadas:")
    print("   - sex_numeric (0=female, 1=male)")
    print("   - family_size (total de familiares)")
    print("   - is_alone (1=viajando sozinho)")
    print("   - Age e Fare (valores ausentes preenchidos)")
    
    return df_processed

def prepare_data(df):
    """Prepara os dados para treinamento"""
    print("\n📦 Preparando dados para treinamento...")
    
    # Selecionar features
    features = ['Pclass', 'sex_numeric', 'Age', 'family_size', 'is_alone', 'Fare']
    X = df[features]
    y = df['Survived']
    
    # Split train/test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print(f"✅ Dados divididos:")
    print(f"   - Treino: {len(X_train)} registros")
    print(f"   - Teste: {len(X_test)} registros")
    
    return X_train, X_test, y_train, y_test, features

def train_model(X_train, y_train):
    """Treina o modelo de Logistic Regression"""
    print("\n🤖 Treinando modelo Logistic Regression...")
    
    model = LogisticRegression(random_state=42, max_iter=1000)
    model.fit(X_train, y_train)
    
    print("✅ Modelo treinado com sucesso!")
    
    return model

def evaluate_model(model, X_test, y_test):
    """Avalia o modelo"""
    print("\n📈 Avaliando modelo...")
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\n✅ Acurácia: {accuracy:.2%}")
    print("\n📊 Relatório de Classificação:")
    print(classification_report(y_test, y_pred, 
                                target_names=['Não Sobreviveu', 'Sobreviveu']))
    
    return accuracy

def save_model(model, features, accuracy):
    """Salva o modelo e metadados"""
    print("\n💾 Salvando modelo...")
    
    # Salvar modelo
    joblib.dump(model, 'model.pkl')
    print("✅ Modelo salvo: model.pkl")
    
    # Salvar metadados
    metadata = {
        'model_type': 'LogisticRegression',
        'features': features,
        'accuracy': float(accuracy),
        'feature_descriptions': {
            'Pclass': 'Classe do passageiro (1, 2 ou 3)',
            'sex_numeric': 'Gênero (0=feminino, 1=masculino)',
            'Age': 'Idade em anos',
            'family_size': 'Tamanho da família (incluindo passageiro)',
            'is_alone': 'Viajando sozinho (0=não, 1=sim)',
            'Fare': 'Tarifa paga'
        },
        'training_date': '2025-10-29'
    }
    
    with open('model_metadata.json', 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    
    print("✅ Metadados salvos: model_metadata.json")

def main():
    """Função principal"""
    print("=" * 60)
    print("🚀 TREINAMENTO DO MODELO TITANIC")
    print("=" * 60)
    
    # 1. Carregar dados
    df = load_data()
    
    # 2. Feature engineering
    df_processed = feature_engineering(df)
    
    # 3. Preparar dados
    X_train, X_test, y_train, y_test, features = prepare_data(df_processed)
    
    # 4. Treinar modelo
    model = train_model(X_train, y_train)
    
    # 5. Avaliar modelo
    accuracy = evaluate_model(model, X_test, y_test)
    
    # 6. Salvar modelo
    save_model(model, features, accuracy)
    
    print("\n" + "=" * 60)
    print("✅ PROCESSO CONCLUÍDO COM SUCESSO!")
    print("=" * 60)
    print("\n📦 Arquivos gerados:")
    print("   - model.pkl (modelo treinado)")
    print("   - model_metadata.json (informações do modelo)")
    print("\n🚀 Pronto para usar na API!")

if __name__ == "__main__":
    main()
