<template>
  <div id="app">
    <AppHeader />
    <FileUpload />
  </div>
</template>

<script>
import AppHeader from '@/components/AppHeader.vue';
import FileUpload from '@/components/FileUpload.vue';

export default {
  name: 'App',
  components: {
    AppHeader,
    FileUpload,
  },
};
</script>

<style>
#app {
  font-family: ibm plex sans,sans-serif;
  text-align: center;
  color: #2c3e50;
}

body {
  font-family: ibm plex sans,sans-serif;
  background-color: #d9fadc;
  margin: 0;
}
</style>
