import { useEffect, useState } from 'react'
import axios from 'axios'

const API_URL = 'http://localhost:8000'

interface ModelMetadata {
  model_name: string
  model_type: string
  accuracy: number
  n_estimators: number
  max_depth: number
  features: string[]
  training_samples: number
  test_samples: number
}

function ModelInfo() {
  const [metadata, setMetadata] = useState<ModelMetadata | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    const fetchModelInfo = async () => {
      try {
        const response = await axios.get<ModelMetadata>(`${API_URL}/model/info`)
        setMetadata(response.data)
      } catch (err) {
        if (axios.isAxiosError(err)) {
          setError(err.response?.data?.detail || 'API offline ou modelo não carregado')
        } else {
          setError('Erro ao carregar informações do modelo')
        }
      } finally {
        setLoading(false)
      }
    }

    fetchModelInfo()
  }, [])

  if (loading) {
    return (
      <div className="loading">
        <div className="spinner"></div>
        <p>Carregando informações...</p>
      </div>
    )
  }

  if (error) {
    return (
      <div className="error">
        ⚠️ {error}
        <p style={{ fontSize: '0.9rem', marginTop: '0.5rem' }}>
          Certifique-se de que a API está rodando em http://localhost:8000
        </p>
      </div>
    )
  }

  if (!metadata) {
    return <div>Sem informações disponíveis</div>
  }

  return (
    <div className="info-grid">
      <div className="info-item">
        <span className="info-label">Modelo</span>
        <span className="info-value">{metadata.model_name}</span>
      </div>

      <div className="info-item">
        <span className="info-label">Accuracy</span>
        <span className="info-value" style={{ color: '#34d399' }}>
          {(metadata.accuracy * 100).toFixed(2)}%
        </span>
      </div>

      <div className="info-item">
        <span className="info-label">Tipo</span>
        <span className="info-value">{metadata.model_type}</span>
      </div>

      <div className="info-item">
        <span className="info-label">N° de Árvores</span>
        <span className="info-value">{metadata.n_estimators}</span>
      </div>

      <div className="info-item">
        <span className="info-label">Profundidade Máxima</span>
        <span className="info-value">{metadata.max_depth}</span>
      </div>

      <div className="info-item">
        <span className="info-label">Amostras de Treino</span>
        <span className="info-value">{metadata.training_samples}</span>
      </div>

      <div className="info-item">
        <span className="info-label">Amostras de Teste</span>
        <span className="info-value">{metadata.test_samples}</span>
      </div>

      <div className="info-item" style={{ gridColumn: '1 / -1' }}>
        <span className="info-label">Features</span>
        <span className="info-value" style={{ fontSize: '0.9rem' }}>
          {metadata.features.join(', ')}
        </span>
      </div>
    </div>
  )
}

export default ModelInfo
