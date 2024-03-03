import { createI18n } from 'vue-i18n'

import opinionEn from './opinion/en.json'
import opinionFr from './opinion/fr.json'


export const i18n = createI18n({
  legacy: false,
  locale: 'en',
  fallbackLocale: 'en',
  messages: {
    en: {
      opinion: opinionEn,
      test: 'test in English',
    },
    fr: {
      opinion: opinionFr,
      test: 'test en français',
    },
  },
})
