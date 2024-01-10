import { createApp } from 'vue'
import App from './App.vue'

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faGoogleDrive, faDropbox } from '@fortawesome/free-brands-svg-icons'
import { faLink, faFilePdf, fa1, fa2, fa3, faLeftLong, faFileArrowDown, faTrash} from '@fortawesome/free-solid-svg-icons'
import { library } from '@fortawesome/fontawesome-svg-core'

library.add(faGoogleDrive, faDropbox, faLink, faFilePdf, fa1, fa2, fa3, faLeftLong, faFileArrowDown, faTrash);

createApp(App)
.component('font-awesome-icon', FontAwesomeIcon)
.mount('#app')


