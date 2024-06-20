import { createI18n } from 'vue-i18n'

import opinionEn from './opinion/en.json'
import opinionFr from './opinion/fr.json'
import appEn from './en.json'
import appFr from './fr.json'


const defaultLocale = import.meta.env.VITE_OPINION_APP_DEFAULT_LOCALE ?? 'en'

const long = {
  year: 'numeric', month: 'long', day: 'numeric',
  weekday: 'long', hour: 'numeric', minute: 'numeric',
  timeZoneName: 'short',
}

export const i18n = createI18n({
  legacy: false,
  locale: defaultLocale,
  fallbackLocale: defaultLocale,
  datetimeFormats: {
    en: {
      long,
    },
    fr: {
      long,
    },
  },
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
