import { createApp } from 'vue'
import { createI18n } from 'vue-i18n'

import App from './App.vue'
import router from './router'
import en from './locales/en.json'
import fr from './locales/fr.json'

import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'


createApp(App)
  .use(createI18n({
    legacy: false,
    locale: 'fr',
    fallbackLocale: 'fr',
    messages: {en, fr},
  }))
  .use(router)
  .mount('#app')
