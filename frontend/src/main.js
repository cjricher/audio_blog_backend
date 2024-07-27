import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap'

// Import My CSS Here
import './assets/styles.less'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
