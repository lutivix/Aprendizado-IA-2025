"""
Script para treinar e salvar o modelo ML
Dia 3 - Semana 3: Dashboard React Interativo
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import joblib
import json
from pathlib import Path
import ssl
import urllib.request

# Configurar SSL para download
ssl._create_default_https_context = ssl._create_unverified_context

def download_data():
    """Baixar dataset Titanic"""
    # URL do Stanford (fonte confiável e estável)
    url = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
    data_path = Path(__file__).parent.parent / "titanic.csv"
    
    if not data_path.exists():
        print("⬇️ Baixando dataset Titanic...")
        try:
            urllib.request.urlretrieve(url, data_path)
            print(f"✅ Dataset salvo em: {data_path}")
        except Exception as e:
            print(f"❌ Erro ao baixar: {e}")
            raise
    else:
        print(f"✅ Dataset já existe: {data_path}")
    
    return data_path


def prepare_data(df):
    """Preparar e limpar dados"""
    print("\n📊 Preparando dados...")
    
    # Dataset Stanford tem nomes diferentes!
    # Renomear colunas para padronizar
    column_mapping = {
        'Siblings/Spouses Aboard': 'SibSp',
        'Parents/Children Aboard': 'Parch'
    }
    df = df.rename(columns=column_mapping)
    
    # Selecionar features importantes
    features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
    target = 'Survived'
    
    # Criar cópia
    df_processed = df[features + [target]].copy()
    
    # Tratar valores ausentes
    df_processed['Age'].fillna(df_processed['Age'].median(), inplace=True)
    df_processed['Fare'].fillna(df_processed['Fare'].median(), inplace=True)
    
    # Encodar variáveis categóricas
    le_sex = LabelEncoder()
    
    df_processed['Sex'] = le_sex.fit_transform(df_processed['Sex'])
    
    print(f"✅ Dados preparados: {df_processed.shape}")
    print(f"   Features: {features}")
    print(f"   Target: {target}")
    
    return df_processed, features, target, le_sex


def train_model(X_train, y_train):
    """Treinar modelo Random Forest"""
    print("\n🤖 Treinando modelo Random Forest...")
    
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1
    )
    
    model.fit(X_train, y_train)
    print("✅ Modelo treinado!")
    
    return model


def evaluate_model(model, X_test, y_test):
    """Avaliar modelo"""
    print("\n📊 Avaliando modelo...")
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\n✅ Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")
    print("\n📋 Classification Report:")
    print(classification_report(y_test, y_pred, target_names=['Não sobreviveu', 'Sobreviveu']))
    
    return accuracy, y_pred


def save_model(model, metadata, output_dir=None):
    """Salvar modelo e metadata"""
    if output_dir is None:
        output_dir = Path(__file__).parent
    
    model_path = output_dir / "model.pkl"
    metadata_path = output_dir / "model_metadata.json"
    
    # Salvar modelo
    joblib.dump(model, model_path)
    print(f"\n💾 Modelo salvo: {model_path}")
    
    # Salvar metadata
    with open(metadata_path, 'w') as f:
        json.dump(metadata, f, indent=2)
    print(f"💾 Metadata salva: {metadata_path}")
    
    return model_path, metadata_path


def main():
    """Função principal"""
    print("=" * 60)
    print("🚢 Titanic ML Model Training")
    print("=" * 60)
    
    # 1. Baixar e carregar dados
    data_path = download_data()
    df = pd.read_csv(data_path)
    print(f"\n✅ Dataset carregado: {df.shape}")
    
    # 2. Preparar dados
    df_processed, features, target, le_sex = prepare_data(df)
    
    # 3. Dividir dados
    X = df_processed[features]
    y = df_processed[target]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"\n📊 Split dos dados:")
    print(f"   Treino: {X_train.shape}")
    print(f"   Teste: {X_test.shape}")
    
    # 4. Treinar modelo
    model = train_model(X_train, y_train)
    
    # 5. Avaliar modelo
    accuracy, y_pred = evaluate_model(model, X_test, y_test)
    
    # 6. Feature importance
    feature_importance = pd.DataFrame({
        'feature': features,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    print("\n📊 Feature Importance:")
    print(feature_importance.to_string(index=False))
    
    # 7. Preparar metadata
    metadata = {
        "model_name": "Random Forest Classifier",
        "model_type": "RandomForestClassifier",
        "accuracy": float(accuracy),
        "n_estimators": model.n_estimators,
        "max_depth": model.max_depth,
        "features": features,
        "feature_importance": feature_importance.to_dict('records'),
        "training_samples": len(X_train),
        "test_samples": len(X_test),
        "target": target,
        "encodings": {
            "Sex": {"male": 1, "female": 0}
        }
    }
    
    # 8. Salvar modelo
    save_model(model, metadata)
    
    print("\n" + "=" * 60)
    print("✅ Processo completo!")
    print("=" * 60)
    print("\n💡 Próximos passos:")
    print("   1. Execute: python app.py")
    print("   2. Acesse: http://localhost:8000/docs")
    print("   3. Teste a API com predições!")


if __name__ == "__main__":
    main()
