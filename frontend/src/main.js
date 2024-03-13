import { createApp } from 'vue'
import { RouterView } from 'vue-router'
import { createPinia } from 'pinia'
import { createHead } from '@unhead/vue'
import { PiniaSharedState } from 'pinia-shared-state'
import * as pdfjs from 'pdfjs-dist/build/pdf'

import router from './router'
import { i18n } from './locales'


pdfjs.GlobalWorkerOptions.workerSrc = '/pdf.worker.min.js'

createApp(RouterView)
  .use(i18n)
  .use(createHead())
  .use(createPinia().use(PiniaSharedState({enable: false})))
  .use(router)
  .mount('#app')
