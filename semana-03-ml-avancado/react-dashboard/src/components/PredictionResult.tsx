interface PredictionResponse {
  survived: number
  probability: number
  message: string
  model_name?: string
  model_accuracy?: number
}

interface Props {
  prediction: PredictionResponse | null
  loading: boolean
}

function PredictionResult({ prediction, loading }: Props) {
  if (loading) {
    return (
      <div className="loading">
        <div className="spinner"></div>
        <p>Analisando dados...</p>
      </div>
    )
  }

  if (!prediction) {
    return null
  }

  const survived = prediction.survived === 1
  const probabilityPercent = (prediction.probability * 100).toFixed(1)

  return (
    <div className="prediction-result">
      <div className="prediction-icon">
        {survived ? '🎉' : '😢'}
      </div>
      
      <div className={`prediction-message ${survived ? 'survived' : 'not-survived'}`}>
        {prediction.message}
      </div>
      
      <div className="prediction-probability">
        Probabilidade de sobrevivência: <strong>{probabilityPercent}%</strong>
      </div>

      {prediction.model_name && (
        <div style={{ marginTop: '2rem', fontSize: '0.9rem', color: 'rgba(255, 255, 255, 0.6)' }}>
          Modelo: {prediction.model_name}
          {prediction.model_accuracy && (
            <> | Accuracy: {(prediction.model_accuracy * 100).toFixed(2)}%</>
          )}
        </div>
      )}

      <div style={{ 
        marginTop: '2rem', 
        padding: '1rem', 
        background: 'rgba(255, 255, 255, 0.05)', 
        borderRadius: '8px',
        textAlign: 'left'
      }}>
        <h4 style={{ marginBottom: '1rem', color: '#60a5fa' }}>💡 Interpretação:</h4>
        <p style={{ fontSize: '0.95rem', lineHeight: '1.6', color: 'rgba(255, 255, 255, 0.8)' }}>
          {survived ? (
            <>
              Com uma probabilidade de <strong>{probabilityPercent}%</strong>, o modelo prevê que 
              este passageiro <span style={{ color: '#34d399' }}>teria sobrevivido</span> ao desastre 
              do Titanic. Fatores como classe, sexo e idade influenciaram positivamente esta predição.
            </>
          ) : (
            <>
              Com uma probabilidade de <strong>{(100 - Number(probabilityPercent)).toFixed(1)}%</strong> de 
              não sobrevivência, o modelo prevê que este passageiro <span style={{ color: '#f87171' }}>não 
              teria sobrevivido</span> ao desastre. Infelizmente, as circunstâncias e características 
              indicam baixas chances de sobrevivência.
            </>
          )}
        </p>
      </div>
    </div>
  )
}

export default PredictionResult
