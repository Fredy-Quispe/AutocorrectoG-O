<template>
    <section class="file-download">

        <div class="document-preview">
            <!-- Aquí mostrar el documento reducido -->
        </div>

        <button class="download-button">Descargar Documento</button>

        <div class="options">
            <div class="circular-buttons">
                <button class="option-button circular" title="Guardar en Google Drive"><font-awesome-icon :icon="['fab', 'google-drive']" /></button>
                <button class="option-button circular" title="Guardar en Dropbox"><font-awesome-icon :icon="['fab', 'dropbox']" /></button>
                <button class="option-button circular" title="Eliminar"><font-awesome-icon :icon="['fas', 'trash']" /></button>
            </div>
        </div>

        <footer class="footer">
            <button class="return-button" @click="goBack"> <font-awesome-icon :icon="['fas', 'left-long']" class="return-ico"/> Volver a empezar</button>
        </footer>
    </section>
</template>
  
<script>
import axios from 'axios'
export default {
  name: 'FileDownload',
  methods: {
    goBack() {
      this.$emit('goBack');
    },
    downloadResult() {
      // Hacer una solicitud para obtener el nombre del archivo resultante
      // Esto asume que tienes acceso a un servicio que proporciona la ruta del archivo resultante
      // Puedes usar axios u otra librería para hacer la solicitud
      // Reemplaza la URL con la correcta según tu configuración del servidor Flask
      axios
        .post('http://tu_servidor/api/analyze', { document: 'ruta_de_tu_archivo.pdf' })
        .then(response => {
          const resultFilename = response.data.result_filename;

          // Crear un enlace temporal y simular un clic para descargar el archivo
          const link = document.createElement('a');
          link.href = `http://tu_servidor/api/download/${resultFilename}`;
          link.download = 'resultado.pdf';
          document.body.appendChild(link);
          link.click();
          document.body.removeChild(link);
        })
        .catch(error => {
          console.error('Error al descargar el resultado', error);
        });
    },
  },
};

</script>
  
<style scoped>
.file-download {
    margin-top: 104px;
}

.document-preview {
    width: 236px;
    height: 305px;
    border-radius: 5px;
    background-color: white;
    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
    margin: 10px auto;
    display: flex;
    align-items: center;
    justify-content: center;
}

.download-button {
    width: 450px;
    height: 73px;
    border: none;
    border-radius: 50px;
    color: white;
    cursor: pointer;
    background-color: #4caf50;
    margin: 20px auto;
    display: flex;
    gap: 50px;
    align-items: center;
    justify-content: center;
    flex-direction: row;
    font-size: 20px;
    font-weight: 700;
    line-height: 26px;
    text-align: center;
}

.options {
    margin-top: 25px;
    text-align: center;
}

.option-button {
    background-color: white;
    border: 1px solid rgb(151, 151, 151);
    outline: 2px solid transparent;
    color: black;
    padding: 10px 20px;
    font-size: 20px;
    cursor: pointer;
    margin-right: 16px;
}

.option-button:hover {
    border-color: #45a049;
}

.circular-buttons {
    display: flex;
    justify-content: center;
}

.circular {
    border-radius: 50%;
    width: 45px;
    height: 45px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-right: 14px;
}

.footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: white;
  width: 100%;
  height: 65px;
  position: fixed;
  bottom: 0;
  left: 0;
  z-index: 1000;
  box-shadow: 0px -2px 5px rgba(0, 0, 0, 0.1);
}

.return-button {
    width: 190px;
    background: transparent;
    border:none;
    margin-left: 20px;
    font-weight: 700;
    font-size: 16px;
    line-height: 19px;
    text-align: center;
    color: #313131;
    cursor: pointer;
}

.return-ico {
    margin-right: 20px;
    color: magenta;
}
</style>
  