import { createApp } from 'vue'
import App from './App.vue'

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faGoogleDrive, faDropbox } from '@fortawesome/free-brands-svg-icons'
import { faLink, faFilePdf } from '@fortawesome/free-solid-svg-icons'
import { library } from '@fortawesome/fontawesome-svg-core'

library.add(faGoogleDrive, faDropbox, faLink, faFilePdf);

createApp(App)
.component('font-awesome-icon', FontAwesomeIcon)
.mount('#app')


