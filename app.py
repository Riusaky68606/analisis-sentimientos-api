import re
import nltk
import joblib
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Configuración de Flask
app = Flask(__name__)
CORS(app)

# Descargar recursos de NLTK
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Cargar modelo y vectorizador previamente entrenados
model = joblib.load('random_forest_standard_model.pkl')  # Cambia aquí al modelo estándar
vectorizer = joblib.load('vectorizer.pkl')  # Cargar vectorizador guardado (TF-IDF)

# Inicializar stopwords y lematizador
stop_words = set(stopwords.words('spanish'))

# Lista ampliada de palabras relevantes
palabras_relevantes = {
    "pero", "aunque", "sin embargo", "no obstante", "mas", "empero",
    "a pesar de", "pese a", "al contrario", "por el contrario",
    "en cambio", "mientras que", "sino", "sino que", "con todo",
    "antes bien", "si bien", "no", "nunca", "no es como antes"
}

# Eliminar las palabras relevantes de las stopwords
stop_words -= palabras_relevantes

lemmatizer = WordNetLemmatizer()

# Función de preprocesamiento
def preprocess_text(text):
    """
    Limpia y preprocesa un texto:
    1. Elimina caracteres especiales, números y emojis.
    2. Convierte a minúsculas.
    3. Tokeniza.
    4. Elimina stopwords (sin eliminar palabras relevantes).
    5. Lematiza las palabras.
    """
    text = re.sub(r'[^\w\s]', '', text)  # Quitar signos de puntuación
    text = re.sub(r'\d+', '', text)      # Quitar números
    text = re.sub(r'[^\x00-\x7F]+', '', text)  # Quitar emojis y caracteres no ASCII
    text = text.lower()  # Convertir a minúsculas
    tokens = text.split()  # Tokenizar
    tokens = [word for word in tokens if word not in stop_words]  # Eliminar stopwords
    tokens = [lemmatizer.lemmatize(word) for word in tokens]  # Lematizar
    return ' '.join(tokens)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/clasificar", methods=["POST"])
def clasificar_sentimiento():
    """
    Clasifica un comentario enviado por el cliente.
    """
    try:
        # Obtener el comentario del cliente
        data = request.get_json()
        comentario = data.get("comentario", "")

        # Preprocesar el comentario
        comentario_preprocesado = preprocess_text(comentario)

        # Vectorizar el comentario
        comentario_vect = vectorizer.transform([comentario_preprocesado])

        # Clasificar con el modelo
        prediccion = model.predict(comentario_vect)

        # Mapear predicciones a texto (positivo, negativo o neutral)
        sentimiento = "positivo" if prediccion[0] == 1 else "negativo"

        # Respuesta JSON
        return jsonify({"sentimiento": sentimiento})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
