import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { PiniaSharedState } from 'pinia-shared-state'
import * as pdfjs from 'pdfjs-dist/build/pdf'

import App from './app.vue'
import router from './router'
import { i18n } from './locales'


pdfjs.GlobalWorkerOptions.workerSrc = '/pdf.worker.min.js'

createApp(App)
  .use(i18n)
  .use(createPinia().use(PiniaSharedState({enable: false})))
  .use(router)
  .mount('#app')
