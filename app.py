import re
import os
import nltk
import joblib
import numpy as np

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  
from nltk.corpus import stopwords

# Crear la aplicación Flask
app = Flask(__name__)
CORS(app) 

# Descargar las stopwords en español
nltk.download('stopwords')
stop_words = set(stopwords.words('spanish'))

# Cargar el modelo entrenado y el vectorizador
model = joblib.load('svm_model_optimized.pkl')  # Cargar tu modelo optimizado SVM
vectorizer = joblib.load('vectorizer.pkl')  # Cargar el vectorizador


@app.route("/")
def home():
    # Renderizamos el index.html que estará en /templates/index.html
    return render_template("index.html")

@app.route('/clasificar', methods=['POST'])
def clasificar_sentimiento():
    try:
        # Obtener el comentario enviado en la petición
        data = request.get_json()
        comentario = data['comentario']

        # Preprocesar el comentario
        comentario_preprocesado = preprocess_text(comentario)

        # Vectorizar el comentario preprocesado
        comentario_vect = vectorizer.transform([comentario_preprocesado])

        # Clasificar el comentario con el modelo
        prediccion = model.predict(comentario_vect)

        # Devolver la predicción como respuesta JSON
        return jsonify({'sentimiento': prediccion[0]})

    except Exception as e:
        return jsonify({'error': str(e)})

# Función de preprocesamiento (replica tu preprocesamiento en Colab)
def preprocess_text(text):
    # Eliminar signos de puntuación y números
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    # Convertir a minúsculas
    text = text.lower()
    # Tokenización y eliminación de stopwords
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
