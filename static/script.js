document.getElementById('analizar-btn').addEventListener('click', async () => {
  const comentario = document.getElementById('comentario').value.trim();
  const resultadoDiv = document.getElementById('resultado');
  const loadingDiv = document.getElementById('loading');

  resultadoDiv.innerHTML = '';
  resultadoDiv.classList.remove('fade-in');

  if (!comentario) {
      resultadoDiv.innerHTML = 'Por favor, ingresa un comentario.';
      return;
  }

  loadingDiv.style.display = 'block';

  try {
      const resp = await fetch('/clasificar', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ comentario }),
      });
      const data = await resp.json();

      loadingDiv.style.display = 'none';

      let icon;
      if (data.sentimiento === 'positivo') {
          icon = '😊';
      } else if (data.sentimiento === 'negativo') {
          icon = '😢';
      } else {
          icon = '❓';
      }

      resultadoDiv.innerHTML = `<span class="icon">${icon}</span> Sentimiento detectado: ${data.sentimiento || data.error}`;
      resultadoDiv.classList.add('fade-in');
  } catch (err) {
      loadingDiv.style.display = 'none';
      resultadoDiv.innerHTML = `Error en la comunicación con el servidor: ${err}`;
  }

  document.getElementById('comentario').value = '';
});
