import { createApp } from 'vue'
import { createI18n } from 'vue-i18n'
import { createPinia } from 'pinia'
import * as pdfjs from 'pdfjs-dist/build/pdf'

import App from './App.vue'
import router from './router'
import en from './locales/en.json'
import fr from './locales/fr.json'

import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'


pdfjs.GlobalWorkerOptions.workerSrc = '/pdf.worker.min.js'

createApp(App)
  .use(createI18n({
    legacy: false,
    locale: 'fr',
    fallbackLocale: 'fr',
    messages: {en, fr},
  }))
  .use(createPinia())
  .use(router)
  .mount('#app')
