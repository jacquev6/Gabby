import { createI18n } from 'vue-i18n'

import opinionEn from './opinion/en.json'
import opinionFr from './opinion/fr.json'
import appEn from './en.json'
import appFr from './fr.json'


export const i18n = createI18n({
  legacy: false,
  locale: 'en',
  fallbackLocale: 'en',
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
