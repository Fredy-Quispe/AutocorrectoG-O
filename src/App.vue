<template>
  <div id="app">
    <AppHeader />
    <component :is="currentComponent" ref="dynamicComponent" @file-uploaded="showFileDownload"
      @go-Back="showFileUpload" />
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
      resultFilename: '',
      previewUrl: '',
    };
  },
  mounted() {
    this.$watch('currentComponent', this.onComponentChange);
  },
  methods: {
    onComponentChange() {
      this.$nextTick(() => {
        if (this.$refs.dynamicComponent && this.$refs.dynamicComponent.showFileDownload) {
          this.$refs.dynamicComponent.showFileDownload(this.resultFilename);
        }
      });
    },
    showFileDownload(result) {
      console.log('Contenido de resultFilename AVFT:', result);
      this.resultFilename = result;
      this.currentComponent = 'FileDownload';
    },
    showFileUpload() {
      console.log('Cambiando a vista FileUpload');
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
  font-family: ibm plex sans, sans-serif;
  background-color: #d9fadc;
  margin: 0;
}
</style>
