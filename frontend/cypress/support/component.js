import { mount } from 'cypress/vue'

import './commands'
import { i18n } from '../../src/locales/for-tests'


Cypress.Commands.add('mount', (component, options) => {
  options = options || {}
  options.global = options.global || {}
  options.global.plugins = options.global.plugins || []
  options.global.plugins.push(i18n)

  return mount(component, options)
})
