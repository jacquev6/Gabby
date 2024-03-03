import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createI18n } from 'vue-i18n'

import App from './App.vue'
import router from './router'

import opinionEn from './locales/opinion/en.json'
import opinionFr from './locales/opinion/fr.json'

const messages = {
  en: {
    opinion: opinionEn,
  },
  fr: {
    opinion: opinionFr,
  },
}


createApp(App)
  .use(createPinia())
  .use(router)
  .use(createI18n({
    legacy: false,
    locale: 'en',
    fallbackLocale: 'en',
    messages,
  }))
  .mount('#app')
