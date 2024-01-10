<template>
  <div id="app">
    <AppHeader />
    <FileDownload />
  </div>
</template>

<script>
import AppHeader from '@/components/AppHeader.vue';
import FileDownload from '@/components/FileDownload.vue';

export default {
  name: 'App',
  components: {
    AppHeader,
    FileDownload,
  },
};
</script>

<style>
#app {
  text-align: center;
  color: #2c3e50;
}

body {
  font-family: ibm plex sans,sans-serif;
  background-color: #d9fadc;
  margin: 0;
}
</style>
