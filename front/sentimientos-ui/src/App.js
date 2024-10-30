import React, { useState } from 'react';
import './App.css';

function App() {
  const [comentario, setComentario] = useState('');
  const [resultado, setResultado] = useState(null);

  const analizarSentimiento = async () => {
    try {
      const respuesta = await fetch('http://localhost:5000/clasificar', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ comentario }),
      });
      const data = await respuesta.json();
      setResultado(data.sentimiento);
    } catch (error) {
      console.error('Error al analizar el sentimiento:', error);
    }
  };

  return (
    <div className="App">
      <h1 className="title">Análisis de Sentimientos</h1>
      <textarea
        className="input-text"
        value={comentario}
        onChange={(e) => setComentario(e.target.value)}
        placeholder="Escribe un comentario..."
      />
      <button className="analyze-button" onClick={analizarSentimiento}>
        Analizar Sentimiento
      </button>
      {resultado && (
        <div className="result-container">
          <h2>Resultado del Análisis:</h2>
          <p className="result">{resultado}</p>
        </div>
      )}
    </div>
  );
}

export default App;
