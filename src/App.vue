<template>
  <div id="app">
    <AppHeader />
    <component :is="currentComponent" @file-selected="showFileDownload" @goBack="showFileUpload" />
  </div>
</template>

<script>
import AppHeader from '@/components/AppHeader.vue';
import FileUpload from '@/components/FileUpload.vue';
import FileDownload from '@/components/FileDownload.vue';

export default {
  name: 'App',
  components: {
    AppHeader,
    FileUpload,
    FileDownload,
  },
  data() {
    return {
      currentComponent: 'FileUpload',
    };
  },
  methods: {
    showFileDownload() {
      // Cambiar la vista solo si la vista actual es 'FileUpload'
      if (this.currentComponent === 'FileUpload') {
        this.currentComponent = 'FileDownload';
      }
    },
    showFileUpload() {
      this.currentComponent = 'FileUpload';
    },
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
