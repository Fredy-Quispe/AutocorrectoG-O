<template>
    <section class="main-content">
      <div class="section-title">
        <span>Analize en segundos la gramatica y ortografia de su documento PDF.</span>
      </div>
      <button class="main-button">Seleccionar documento PDF</button>
      <div class="alternative-buttons">
        <div class="circular-buttons">
          <button class="alternative-button circular" title="Seleccionar un archivo de Google Drive"><font-awesome-icon :icon="['fab', 'google-drive']" /></button>
          <button class="alternative-button circular" title="Seleccione el archivo de Dropbox"><font-awesome-icon :icon="['fab', 'dropbox']" /></button>
          <button class="alternative-button circular" title="Cargar el archivo desde la URL"><font-awesome-icon :icon="['fas', 'link']" /></button>
        </div>
      </div>
      <div class="how-to-use">
        <h2>Cómo analizar un documento PDF</h2>
        <div class="step-cards">
          <div class="step-card">Paso 1: Elija el PDF que desea analizar desde su ordenador.</div>
          <div class="step-card">Paso 2: Nuestro analizador de ortografia y gramatica comenzará a extraer el texto de su PDF.</div>
          <div class="step-card">Paso 3: En segundos se crea un documento PDF donde se resaltan los errores gramaticales y ortograficos y listo para descargar.</div>
        </div>
      </div>
    </section>
</template>

<script>
export default {
  name: 'FileUpload',
};
</script>

<style scoped>
.main-content {
  margin-top: 170px;
}
.main-button {
  background-color: #4caf50;
  color: white;
  padding: 15px 30px;
  font-size: 18px;
  border: none;
  border-radius: 50px;
  cursor: pointer;
  margin-top: 50px;
  height: 73px;
  width: 600px;
}
.main-button:hover {
  background-color: #45a049;
}
.alternative-buttons {
  margin-top: 30px;
  text-align: center;
}
.alternative-button {
  background-color: white;
  border: 1px solid rgb(151, 151, 151);
  outline: 2px solid transparent; 
  color: black;
  padding: 10px 20px;
  font-size: 20px;
  cursor: pointer;
  margin-right: 16px;
}
.alternative-button:hover {
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
.how-to-use {
  margin-top: 80px;
}
.step-cards {
  display: flex;
}
.step-card {
  background-color: white;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
  margin: 10px 10px 10px 10px;
  display: inline-block;
}
</style>