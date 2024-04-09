import { createI18n } from 'vue-i18n'

import opinionEn from './opinion/en.json'
import opinionFr from './opinion/fr.json'
import appEn from './en.json'
import appFr from './fr.json'


export const i18n = createI18n({
  legacy: false,
  locale: import.meta.env.VITE_OPINION_APP_DEFAULT_LOCALE ?? 'en',
  fallbackLocale: import.meta.env.VITE_OPINION_APP_DEFAULT_LOCALE ?? 'en',
  messages: {
    en: {
      ...appEn,
      opinion: opinionEn,
    },
    fr: {
      ...appFr,
      opinion: opinionFr,
    },
  },
})
