<template>
  <header class="app-header">
    <div class="logo-container">
      <img src="@/assets/logo.png" alt="Logo" class="logo" />
    </div>
    <div class="title-container">
      <h1 class="title">Analizar documento PDF</h1>
    </div>
    <div class="tools-container">
      <p class="tools-text">Herramientas</p>
    </div>
  </header>
</template>
  
<script>
export default {
  name: 'AppHeader',
};
</script>
  
<style scoped>
.app-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  background-color: white;
  width: 100%;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1000;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1); 
}

.logo {
  max-width: 40px;
}

.title {
  margin: 0;
}

.tools-container {
  overflow: hidden;
  margin-right: 40px;
}

.tools-text {
  margin: 0;
  font-weight: italic;
  white-space: nowrap;
}
</style>
  