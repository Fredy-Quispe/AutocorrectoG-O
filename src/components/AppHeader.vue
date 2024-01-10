<template>
  <header class="app-header">
    <div class="logo-container">
      <img src="@/assets/logo.svg" alt="Logo" class="logo" />
      <span class="logo-text">PDF Analyze</span>
    </div>
    <div class="title-container">
      <font-awesome-icon :icon="['fas', 'file-pdf']" class="title-ico"/>
      <h1 class="title-text">Analizar documento PDF</h1>
    </div>
    <div class="tools-container">
      <img src="@/assets/square.svg" alt="Square" class="square" />
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
  background-color: white;
  width: 100%;
  height: 85px;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1000;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
}
.logo-container {
  display: flex;
  align-items: center;
  margin: 0 20px;
}
.logo {
  width: 50px;
}
.logo-text {
  display: inline-block;
  vertical-align: middle;
  font-weight: 700;
  font-size: 22px;
  line-height: 29px;
  color: #313131;
}
.title-container {
  display: flex;
  align-items: center;
  gap: 12px;
}
.title-ico {
  color: #4caf50;
  font-size: 32px;
}
.title-text {
  margin: 0;
  font-size: 26px;
  line-height: 34px;
  color: #313131;
}
.tools-container {
  display: flex;
  align-items: center;
  width: 180px;
  overflow: hidden;
  margin: 0 20px;
  gap: 5px;
}
.square {
  width: 13px;
  height: 13px;
}
.tools-text {
  margin: 0;
  white-space: nowrap;
  font-size: 14px;
  line-height: 25px;
  color: #313131;
}
</style>
  