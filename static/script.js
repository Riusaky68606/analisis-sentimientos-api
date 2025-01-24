document.getElementById('analizar-btn').addEventListener('click', async () => {
    const comentario = document.getElementById('comentario').value.trim();
    const resultadoDiv = document.getElementById('resultado');
    const loadingDiv = document.getElementById('loading');
  
    // Limpiar el resultado anterior
    resultadoDiv.innerHTML = '';
    resultadoDiv.classList.remove('fade-in');
  
    if (!comentario) {
      resultadoDiv.innerHTML = 'Por favor, escribe un comentario antes de analizar.';
      return;
    }
  
    // Mostrar indicador de carga
    loadingDiv.style.display = 'block';
  
    try {
      const resp = await fetch('/clasificar', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ comentario }),
      });
      const data = await resp.json();
  
      // Depuración
      console.log('Sentimiento detectado:', data.sentimiento);
  
      // Ocultar indicador de carga
      loadingDiv.style.display = 'none';
  
      // Mostrar el resultado con íconos emocionales
      let icon;
      if (data.sentimiento === 'positivo') {
        icon = '😊'; // Cara feliz
      } else if (data.sentimiento === 'negativo') {
        icon = '😢'; // Cara triste
      } else if (data.sentimiento === 'neutral') {
        icon = '😐'; // Cara neutral
      } else {
        icon = '❓'; // Icono de pregunta si hay error
      }
  
      // Construir el resultado
      let iconSpan = document.createElement('span');
      iconSpan.className = 'icon';
      iconSpan.textContent = icon; // Añadir emoji como texto
  
      resultadoDiv.innerHTML = ''; // Limpiar contenido previo
      resultadoDiv.appendChild(iconSpan);
      resultadoDiv.appendChild(
        document.createTextNode(` Sentimiento detectado: ${data.sentimiento || data.error}`)
      );
      resultadoDiv.classList.add('fade-in');
    } catch (err) {
      loadingDiv.style.display = 'none';
      resultadoDiv.innerHTML = `Error en la comunicación con el servidor: ${err}`;
    }
  
    // Limpiar el campo de texto
    document.getElementById('comentario').value = '';
  });
  