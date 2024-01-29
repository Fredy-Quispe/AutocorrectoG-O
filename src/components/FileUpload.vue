<template>
    <section class="main-content">
        <div v-if="errorMessage" class="modal-error">
            <div class="modal-content-error">
                <p>{{ errorMessage }}</p>
                <button @click="clearError">Cerrar</button>
            </div>
        </div>
        <div class="section-title">
            <span>Analize en segundos la gramatica y ortografia de su documento PDF.</span>
        </div>
        <button class="main-button" @click="selectFile">Seleccionar documento PDF</button>
        <input ref="fileInput" type="file" style="display: none" accept="application/pdf" @change="handleFileChange" />
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
                    <p>Se crea un documento PDF donde se resaltan los errores gramaticales y ortograficos y listo para
                        descargar.</p>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios'
export default {
    name: 'FileUpload',
    data() {
        return {
            resultFilename: '',
            previewUrl: '',
            errorMessage: '',
        };
    },
    methods: {
        selectFile() {
            this.$refs.fileInput.click();
        },

        toggleModal() {
            this.isOpen = !this.isOpen;
        },

        closeModal() {
            this.isOpen = false;
        },

        handleFileSelected(result) {
            console.log('Resultado recibido FSelected:', result);

            if (result.pdf_result_filepath && result.vista_previa_filepath) {
                const { pdf_result_filepath, vista_previa_filepath } = result;

                console.log('Ruta del archivo PDF resultante FSelected:', pdf_result_filepath);
                console.log('Ruta de la vista previa resultante FSelected:', vista_previa_filepath);

                if (typeof pdf_result_filepath === 'string' && typeof vista_previa_filepath === 'string') {
                    this.resultFilename = pdf_result_filepath;
                    this.previewUrl = vista_previa_filepath;
                    console.log('Nombre del archivo resultante FSelected:', this.resultFilename);
                    console.log('URL de vista previa FSelected:', this.previewUrl);
                    this.$emit('file-uploaded', {
                        pdf_result_filepath: result.pdf_result_filepath,
                        vista_previa_filepath: result.vista_previa_filepath
                    });
                } else {
                    console.error('Las rutas de archivos no son cadenas válidas.');
                }
            } else {
                console.error('Respuesta del servidor no tiene la estructura esperada.');
            }
        },

        showErrorNotification(message) {
            this.errorMessage = message;
        },

        clearError() {
            this.errorMessage = '';
        },

        handleFileChange(event) {
            console.log('Archivo seleccionado');
            const file = event.target.files[0];

            if (!file) {
                console.error('No se seleccionó ningún archivo.');
                return;
            }

            const formData = new FormData();
            formData.append('document', file);

            axios.post('http://localhost:5000/api/analyze', formData)
                .then(response => {
                    console.log('Respuesta desde el servidor FChange:', response.data);

                    if (response.data.error) {
                        console.error('Error en la respuesta del servidor:', response.data.error);
                        this.showErrorNotification('Hubo un error al procesar el documento. Por favor, inténtalo de nuevo.');
                    } else if (response.data.result_filename) {
                        const resultFilenames = response.data.result_filename;

                        if (Array.isArray(resultFilenames) && resultFilenames.length === 2) {
                            const [pdf_result_filepath, vista_previa_filepath] = resultFilenames;

                            console.log('Ruta del archivo PDF resultante Fchange:', pdf_result_filepath);
                            console.log('Ruta de la vista previa resultante Fchange:', vista_previa_filepath);

                            if (pdf_result_filepath == null && vista_previa_filepath == null) {
                                this.showErrorNotification('Hubo un error al procesar el documento. Por favor, inténtalo de nuevo.');
                            } else {
                                this.handleFileSelected({
                                    pdf_result_filepath,
                                    vista_previa_filepath
                                });
                            }
                        } else {
                            console.error('La respuesta del servidor no tiene la estructura esperada.');
                        }
                    } else {
                        console.error('Propiedad result_filename no encontrada en la respuesta del servidor.');
                    }
                })
                .catch(error => {
                    console.error('Error al enviar el archivo al servidor', error);
                    this.showErrorNotification('Hubo un error al enviar el archivo al servidor. Por favor, inténtalo de nuevo.');
                });
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
    margin-top: 60px;
    margin-bottom: 60px;
    height: 73px;
    width: 600px;
}

.main-button:hover {
    background-color: #45a049;
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
    font-family: ibm plex sans, sans-serif;
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

.modal-error {
    display: flex;
    align-items: center;
    justify-content: center;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 999;
}

.modal-content-error {
    background-color: #ffcccc;
    color: black;
    padding: 20px;
    border: 1px solid #990000;
    max-width: 400px;
    text-align: center;
    border-radius: 8px;
}

.modal-error button {
    background-color: #990000;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 3px;
    cursor: pointer;
    margin-top: 10px;
}

.modal-error button:hover {
    background-color: #770000;
}
</style>