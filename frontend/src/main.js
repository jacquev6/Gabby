import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './app.vue'
import router from './router'
import { i18n } from './locales'


createApp(App)
  .use(i18n)
  .use(createPinia())
  .use(router)
  .mount('#app')
