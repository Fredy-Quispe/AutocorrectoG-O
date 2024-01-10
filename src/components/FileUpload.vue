<template>
    <section class="main-content">
        <div class="section-title">
            <span>Analize en segundos la gramatica y ortografia de su documento PDF.</span>
        </div>
        <button @click="openFileInput" class="main-button">Seleccionar documento PDF</button>
        <input ref="fileInput" type="file" @change="handleFileSelect" style="display: none" accept="application/pdf" />
        <div class="alternative-buttons">
            <div class="circular-buttons">
                <button class="alternative-button circular" @click="openGoogleDrivePicker" title="Seleccionar un archivo de Google Drive"><font-awesome-icon :icon="['fab', 'google-drive']" /></button>
                <button class="alternative-button circular" title="Seleccione el archivo de Dropbox"><font-awesome-icon :icon="['fab', 'dropbox']" /></button>
                <button class="alternative-button circular" title="Cargar el archivo desde la URL"><font-awesome-icon :icon="['fas', 'link']" /></button>
            </div>
        </div>
        <div class="how-to-use">
            <h2>Cómo analizar un documento PDF</h2>
            <div class="step-cards">
                <div class="step-card">
                    <font-awesome-icon :icon="['fas', '1']" class="card-number circular2" />
                    <p>Elija el PDF que desea analizar desde su ordenador.</p>
                </div>
                <div class="step-card">
                    <font-awesome-icon :icon="['fas', '2']" class="card-number circular2" />
                    <p>Nuestro analizador de ortografia y gramatica comenzará a extraer el texto de su PDF.</p>
                </div>
                <div class="step-card">
                    <font-awesome-icon :icon="['fas', '3']" class="card-number circular2" />
                    <p>Se crea un documento PDF donde se resaltan los errores gramaticales y ortograficos y listo para descargar.</p>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import gapi from 'gapi-client';
const google = window.google;

export default {
    methods: {
        async mounted() {
            await new Promise((resolve) => {
                if (window.gapi && window.gapi.load) {
                    resolve();
                } else {
                    window.__gapiPromiseResolve = resolve;
                }
            });

            gapi.load('client:auth2', () => {
                this.initGoogleDriveClient();
                this.openGoogleDrivePicker();
            });
            },

            openFileInput() {
                this.$refs.fileInput.click();
            },

            handleFileSelect(event) {
                const selectedFile = event.target.files[0];
                if (selectedFile) {
                    console.log('Archivo seleccionado:', selectedFile);
                    this.$emit('file-selected', selectedFile);
                }
            },

            initGoogleDriveClient() {
                gapi.client.init({
                    apiKey: 'AIzaSyBB4mhQRIuMpY-fZhTIA9bJMdIAL81Ctl4',
                    clientId: '196805263513-k6a8gp4h6sg3tfs4p93v9htjb5gti9ge.apps.googleusercontent.com',
                    discoveryDocs: ['https://www.googleapis.com/discovery/v1/apis/drive/v3/rest'],
                    scope: 'https://www.googleapis.com/auth/drive.file',
                }).then(() => {});
            },

            openGoogleDrivePicker() {
                if (gapi.auth2) {
                    gapi.auth2.getAuthInstance().signIn().then(() => {
                    const picker = new google.picker.PickerBuilder()
                        .addView(new google.picker.DocsView())
                        .setOAuthToken(gapi.auth2.getAuthInstance().currentUser.get().getAuthResponse().access_token)
                        .setCallback(this.handleGoogleDrivePicker)
                        .build();
                    picker.setVisible(true);
                    });
                } else {
                    console.error('gapi.auth2 no está definido');
                }
            },

            handleGoogleDrivePicker() {
                // Maneja la lógica después de que el usuario selecciona un archivo en Google Drive
            },
    },
};
</script>

<style scoped>
.main-content {
    margin-top: 150px;
}

.section-title {
    font-size: 20px;
    margin-bottom: 30px;
}

.main-button {
    background-color: #4caf50;
    color: white;
    padding: 15px 30px;
    font-weight: 700;
    font-size: 20px;
    line-height: 26px;
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
    margin-top: 60px;
}

.how-to-use h2 {
    font-weight: 700;
    font-size: 20px;
    line-height: 26px;
    text-align: center;
    color: #313131;
}

.step-cards {
    display: flex;
    align-items: center;
    justify-content: center;
}

.step-card {
    padding: 10px;
    margin: 20px;
    display: flex;
    gap: 32px;
    text-align: left;
    flex-direction: row;
    align-items: center;
    max-width: 450px;
    font-family: ibm plex sans,sans-serif;
}
.card-number {
    background-color: white;
    border: 1px solid rgb(151, 151, 151);
    outline: 2px solid transparent;
    color: #45a049;
    padding: 7px 10px;
    font-weight: 700;
    margin-right: 20px;
}
.circular2 {
    border-radius: 50%;
    width: 15px;
    height: 15px;
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>