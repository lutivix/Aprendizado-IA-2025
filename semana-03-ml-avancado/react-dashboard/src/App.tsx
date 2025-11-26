import { useState } from 'react'
import './App.css'
import PredictionForm from './components/PredictionForm'
import PredictionResult from './components/PredictionResult'
import ModelInfo from './components/ModelInfo'

interface PredictionResponse {
  survived: number
  probability: number
  message: string
  model_name?: string
  model_accuracy?: number
}

function App() {
  const [prediction, setPrediction] = useState<PredictionResponse | null>(null)
  const [loading, setLoading] = useState(false)

  const handlePrediction = (result: PredictionResponse) => {
    setPrediction(result)
  }

  const handleLoadingChange = (isLoading: boolean) => {
    setLoading(isLoading)
  }

  return (
    <div className="App">
      <header className="app-header">
        <h1>🚢 Titanic Survival Predictor</h1>
        <p>Predição de sobrevivência usando Machine Learning</p>
      </header>

      <div className="container">
        <div className="grid">
          <div className="card">
            <h2>📊 Informações do Modelo</h2>
            <ModelInfo />
          </div>

          <div className="card">
            <h2>📝 Fazer Predição</h2>
            <PredictionForm 
              onPrediction={handlePrediction}
              onLoadingChange={handleLoadingChange}
            />
          </div>

          {(prediction || loading) && (
            <div className="card result-card">
              <h2>🎯 Resultado</h2>
              <PredictionResult 
                prediction={prediction}
                loading={loading}
              />
            </div>
          )}
        </div>
      </div>

      <footer className="app-footer">
        <p>Semana 3 - Dia 3 | ML Avançado + Dashboard React</p>
      </footer>
    </div>
  )
}

export default App
