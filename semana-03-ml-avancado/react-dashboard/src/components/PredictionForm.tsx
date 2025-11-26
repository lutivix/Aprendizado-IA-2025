import { useState, FormEvent } from 'react'
import axios from 'axios'

const API_URL = 'http://localhost:8000'

interface PassengerData {
  pclass: number
  sex: string
  age: number
  sibsp: number
  parch: number
  fare: number
}

interface PredictionResponse {
  survived: number
  probability: number
  message: string
  model_name?: string
  model_accuracy?: number
}

interface Props {
  onPrediction: (result: PredictionResponse) => void
  onLoadingChange: (loading: boolean) => void
}

function PredictionForm({ onPrediction, onLoadingChange }: Props) {
  const [formData, setFormData] = useState<PassengerData>({
    pclass: 3,
    sex: 'male',
    age: 22,
    sibsp: 0,
    parch: 0,
    fare: 7.25
  })
  const [error, setError] = useState<string | null>(null)

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target
    setFormData(prev => ({
      ...prev,
      [name]: name === 'sex' ? value : Number(value)
    }))
  }

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault()
    setError(null)
    onLoadingChange(true)

    try {
      const response = await axios.post<PredictionResponse>(`${API_URL}/predict`, formData)
      onPrediction(response.data)
    } catch (err) {
      if (axios.isAxiosError(err)) {
        setError(err.response?.data?.detail || 'Erro ao conectar com a API')
      } else {
        setError('Erro desconhecido')
      }
    } finally {
      onLoadingChange(false)
    }
  }

  const loadExample = (example: 'survivor' | 'victim') => {
    if (example === 'survivor') {
      setFormData({
        pclass: 1,
        sex: 'female',
        age: 38,
        sibsp: 1,
        parch: 0,
        fare: 71.28
      })
    } else {
      setFormData({
        pclass: 3,
        sex: 'male',
        age: 22,
        sibsp: 1,
        parch: 0,
        fare: 7.25
      })
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <div style={{ display: 'flex', gap: '1rem', marginBottom: '1rem' }}>
        <button
          type="button"
          className="btn"
          style={{ background: 'rgba(52, 211, 153, 0.2)', color: '#34d399' }}
          onClick={() => loadExample('survivor')}
        >
          Exemplo: Sobrevivente
        </button>
        <button
          type="button"
          className="btn"
          style={{ background: 'rgba(248, 113, 113, 0.2)', color: '#f87171' }}
          onClick={() => loadExample('victim')}
        >
          Exemplo: Vítima
        </button>
      </div>

      <div className="form-group">
        <label htmlFor="pclass">Classe do Passageiro</label>
        <select
          id="pclass"
          name="pclass"
          value={formData.pclass}
          onChange={handleChange}
          required
        >
          <option value={1}>1ª Classe (Upper)</option>
          <option value={2}>2ª Classe (Middle)</option>
          <option value={3}>3ª Classe (Lower)</option>
        </select>
      </div>

      <div className="form-group">
        <label htmlFor="sex">Sexo</label>
        <select
          id="sex"
          name="sex"
          value={formData.sex}
          onChange={handleChange}
          required
        >
          <option value="male">Masculino</option>
          <option value="female">Feminino</option>
        </select>
      </div>

      <div className="form-group">
        <label htmlFor="age">Idade</label>
        <input
          type="number"
          id="age"
          name="age"
          value={formData.age}
          onChange={handleChange}
          min={0}
          max={100}
          step={0.1}
          required
        />
      </div>

      <div className="form-group">
        <label htmlFor="sibsp">Irmãos/Cônjuges a bordo</label>
        <input
          type="number"
          id="sibsp"
          name="sibsp"
          value={formData.sibsp}
          onChange={handleChange}
          min={0}
          required
        />
      </div>

      <div className="form-group">
        <label htmlFor="parch">Pais/Filhos a bordo</label>
        <input
          type="number"
          id="parch"
          name="parch"
          value={formData.parch}
          onChange={handleChange}
          min={0}
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
          onChange={handleChange}
          min={0}
          step={0.01}
          required
        />
      </div>

      <button type="submit" className="btn">
        🔮 Prever Sobrevivência
      </button>

      {error && (
        <div className="error">
          ⚠️ {error}
        </div>
      )}
    </form>
  )
}

export default PredictionForm
