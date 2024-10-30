### Contenido Completo del README.md en formato Markdown

```markdown
# Análisis de Sentimientos API

API de Análisis de Sentimientos en Español usando Machine Learning, diseñada para clasificar comentarios de usuarios en positivo, negativo y neutral.

## Descripción del Proyecto

Este proyecto es parte de una tesis cuyo objetivo es analizar comentarios en español para detectar el sentimiento que expresan. Utiliza técnicas de aprendizaje supervisado, empleando modelos de machine learning como SVM y Naive Bayes para clasificar los comentarios en tres categorías: positivo, negativo y neutral. 

La API está diseñada para desplegarse en una plataforma web, facilitando la clasificación de textos en tiempo real a través de una sencilla solicitud HTTP.

## Características

- **Clasificación de comentarios**: Los comentarios se clasifican en positivo, negativo o neutral.
- **API REST**: La API está implementada en Flask, lo que permite integrarla fácilmente en aplicaciones web.
- **Despliegue en la Web**: La API está preparada para su despliegue en servicios como Render o Heroku.
- **Modelo entrenado y optimizado**: Usa Support Vector Machines (SVM) y Naive Bayes, con técnicas de balanceo y validación cruzada para mejorar la precisión en la clasificación.

## Tecnologías Utilizadas

- **Python**: Lenguaje principal para el desarrollo del modelo y la API.
- **Flask**: Framework web para construir la API REST.
- **scikit-learn**: Librería de machine learning para el entrenamiento del modelo.
- **nltk**: Natural Language Toolkit para preprocesamiento de texto.
- **Render/Heroku**: Plataformas recomendadas para el despliegue.

## Requisitos Previos

Asegúrate de tener instaladas las siguientes dependencias. Puedes instalarlas ejecutando el siguiente comando:

```bash
pip install -r requirements.txt
```

El archivo `requirements.txt` incluye:
- Flask
- joblib
- numpy
- scikit-learn
- nltk
- gunicorn

## Instalación y Configuración

1. **Clona este repositorio** en tu máquina local:
   ```bash
   git clone https://github.com/tu-usuario/analisis-sentimientos-api.git
   ```

2. **Crea un entorno virtual** y actívalo:
   ```bash
   python3 -m venv venv
   # En Windows
   venv\\Scripts\\activate
   # En MacOS/Linux
   source venv/bin/activate
   ```

3. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecuta la API localmente**:
   ```bash
   python app.py
   ```
   La API estará disponible en `http://127.0.0.1:5000`.

## Uso de la API

Para clasificar un comentario, realiza una solicitud **POST** a la siguiente ruta:

**URL**: `http://127.0.0.1:5000/clasificar`

**Body (JSON)**:
```json
{
  "comentario": "Este lugar es increíble, me encantó el servicio."
}
```

**Respuesta**:
```json
{
  "sentimiento": "positivo"
}
```

### Ejemplo de Prueba con Postman

1. Abre Postman y configura una nueva solicitud **POST**.
2. Usa `http://127.0.0.1:5000/clasificar` como URL.
3. En el Body, selecciona **raw** y **JSON** para ingresar el comentario a clasificar.
4. Envía la solicitud y observa la respuesta.

## Despliegue en Render o Heroku

Para desplegar en Render o Heroku, sigue estos pasos:

1. **Sube el proyecto a un repositorio en GitHub**.
2. **Conéctate a Render o Heroku** y selecciona el repositorio.
3. **Configura el Comando de Inicio**:
   ```bash
   gunicorn app:app --bind 0.0.0.0:$PORT
   ```

Render o Heroku crearán la URL pública, que podrás utilizar para acceder a la API en cualquier lugar.

## Contribuciones

Si deseas contribuir a este proyecto, puedes:
1. Hacer un fork del repositorio.
2. Crear una nueva rama con la mejora o solución de problemas:
   ```bash
   git checkout -b nombre-de-la-rama
   ```
3. Hacer commit de tus cambios:
   ```bash
   git commit -m "Descripción de la mejora o arreglo"
   ```
4. Hacer push a tu rama:
   ```bash
   git push origin nombre-de-la-rama
   ```
5. Crear un Pull Request en este repositorio.

## Contacto

**David Casnanzuela** - Autor del Proyecto  
Correo: milton.casnanzuela@epn.edu.ec y personal: mdavidct17@gmail.com
