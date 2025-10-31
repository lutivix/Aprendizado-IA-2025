import { useState } from 'react';
import './TitanicPredictor.css';

interface PassengerData {
  pclass: number;
  sex: string;
  age: number;
  siblings_spouses: number;
  parents_children: number;
  fare: number;
}

interface PredictionResult {
  survived: number;
  probability: number;
  survival_chance: string;
  features_used: {
    Pclass: number;
    sex_numeric: number;
    Age: number;
    family_size: number;
    is_alone: number;
    Fare: number;
  };
}

const PYTHON_API_URL = 'http://localhost:8000';
const NESTJS_API_URL = 'http://localhost:3001';

export function TitanicPredictor() {
  const [useNestJS, setUseNestJS] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<PredictionResult | null>(null);

  const [formData, setFormData] = useState<PassengerData>({
    pclass: 3,
    sex: 'male',
    age: 22,
    siblings_spouses: 0,
    parents_children: 0,
    fare: 7.25,
  });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const apiUrl = useNestJS 
        ? `${NESTJS_API_URL}/titanic/predict`
        : `${PYTHON_API_URL}/predict`;

      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error(`Erro ${response.status}: ${response.statusText}`);
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Erro desconhecido');
    } finally {
      setLoading(false);
    }
  };

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: name === 'sex' ? value : Number(value),
    }));
  };

  const loadExample = (type: 'high' | 'low') => {
    if (type === 'high') {
      setFormData({
        pclass: 1,
        sex: 'female',
        age: 29,
        siblings_spouses: 0,
        parents_children: 0,
        fare: 211.5,
      });
    } else {
      setFormData({
        pclass: 3,
        sex: 'male',
        age: 22,
        siblings_spouses: 1,
        parents_children: 0,
        fare: 7.25,
      });
    }
  };

  return (
    <div className="predictor-container">
      <div className="header">
        <h1>🚢 Titanic Survival Predictor</h1>
        <p>Predição de sobrevivência usando Machine Learning</p>
      </div>

      <div className="api-toggle">
        <label className="toggle-label">
          <input
            type="checkbox"
            checked={useNestJS}
            onChange={(e) => setUseNestJS(e.target.checked)}
          />
          <span className="toggle-text">
            {useNestJS ? '🟢 NestJS (Proxy)' : '🐍 Python (Direto)'}
          </span>
        </label>
        <small className="api-info">
          {useNestJS 
            ? 'React → NestJS → Python API' 
            : 'React → Python API'}
        </small>
      </div>

      <div className="example-buttons">
        <button 
          type="button" 
          onClick={() => loadExample('high')}
          className="btn-example btn-high"
        >
          👩 Exemplo Alta Chance
        </button>
        <button 
          type="button" 
          onClick={() => loadExample('low')}
          className="btn-example btn-low"
        >
          👨 Exemplo Baixa Chance
        </button>
      </div>

      <form onSubmit={handleSubmit} className="form">
        <div className="form-grid">
          <div className="form-group">
            <label htmlFor="pclass">Classe do Bilhete</label>
            <select
              id="pclass"
              name="pclass"
              value={formData.pclass}
              onChange={handleInputChange}
              required
            >
              <option value={1}>1ª Classe (Luxo)</option>
              <option value={2}>2ª Classe (Média)</option>
              <option value={3}>3ª Classe (Econômica)</option>
            </select>
          </div>

          <div className="form-group">
            <label htmlFor="sex">Gênero</label>
            <select
              id="sex"
              name="sex"
              value={formData.sex}
              onChange={handleInputChange}
              required
            >
              <option value="male">Masculino</option>
              <option value="female">Feminino</option>
            </select>
          </div>

          <div className="form-group">
            <label htmlFor="age">Idade (anos)</label>
            <input
              type="number"
              id="age"
              name="age"
              value={formData.age}
              onChange={handleInputChange}
              min={0}
              max={120}
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="fare">Tarifa (£)</label>
            <input
              type="number"
              id="fare"
              name="fare"
              value={formData.fare}
              onChange={handleInputChange}
              min={0}
              step={0.01}
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="siblings_spouses">Irmãos/Cônjuges a bordo</label>
            <input
              type="number"
              id="siblings_spouses"
              name="siblings_spouses"
              value={formData.siblings_spouses}
              onChange={handleInputChange}
              min={0}
              max={10}
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="parents_children">Pais/Filhos a bordo</label>
            <input
              type="number"
              id="parents_children"
              name="parents_children"
              value={formData.parents_children}
              onChange={handleInputChange}
              min={0}
              max={10}
              required
            />
          </div>
        </div>

        <button 
          type="submit" 
          className="btn-submit"
          disabled={loading}
        >
          {loading ? '🔄 Processando...' : '🎯 Fazer Predição'}
        </button>
      </form>

      {error && (
        <div className="error-box">
          <h3>❌ Erro</h3>
          <p>{error}</p>
          <small>Certifique-se que a API está rodando</small>
        </div>
      )}

      {result && (
        <div className={`result-box ${result.survived === 1 ? 'survived' : 'not-survived'}`}>
          <div className="result-header">
            <h2>
              {result.survived === 1 ? '✅ SOBREVIVEU' : '❌ NÃO SOBREVIVEU'}
            </h2>
            <span className="probability">
              {(result.probability * 100).toFixed(2)}%
            </span>
          </div>

          <div className="result-details">
            <div className="detail-item">
              <span className="label">Chance:</span>
              <span className="value">{result.survival_chance}</span>
            </div>
            <div className="detail-item">
              <span className="label">Probabilidade:</span>
              <span className="value">{(result.probability * 100).toFixed(2)}%</span>
            </div>
          </div>

          <div className="features-used">
            <h3>Features Utilizadas</h3>
            <div className="features-grid">
              <div className="feature">
                <span>Classe:</span>
                <strong>{result.features_used.Pclass}</strong>
              </div>
              <div className="feature">
                <span>Gênero:</span>
                <strong>{result.features_used.sex_numeric === 0 ? 'F' : 'M'}</strong>
              </div>
              <div className="feature">
                <span>Idade:</span>
                <strong>{result.features_used.Age}</strong>
              </div>
              <div className="feature">
                <span>Tarifa:</span>
                <strong>£{result.features_used.Fare.toFixed(2)}</strong>
              </div>
              <div className="feature">
                <span>Família:</span>
                <strong>{result.features_used.family_size}</strong>
              </div>
              <div className="feature">
                <span>Sozinho:</span>
                <strong>{result.features_used.is_alone ? 'Sim' : 'Não'}</strong>
              </div>
            </div>
          </div>
        </div>
      )}

      <div className="info-box">
        <h3>ℹ️ Como funciona</h3>
        <p>
          Este aplicativo usa um modelo de <strong>Machine Learning</strong> (Logistic Regression) 
          treinado com dados reais do Titanic para prever a probabilidade de sobrevivência.
        </p>
        <ul>
          <li>🎯 <strong>Acurácia:</strong> 75.28%</li>
          <li>🧠 <strong>Features:</strong> 6 variáveis analisadas</li>
          <li>📊 <strong>Dataset:</strong> 887 passageiros do Titanic</li>
          <li>🔗 <strong>Stack:</strong> React + TypeScript + FastAPI + scikit-learn</li>
        </ul>
      </div>
    </div>
  );
}
