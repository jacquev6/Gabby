import LanguageSelector from './language-selector.vue'
import { i18n } from '../../locales/for-tests'


// @todo Access the https://test-utils.vuejs.org/api/#config wrapped by Cypress, to avoid repeating '{global}' on each 'mount'
const global = {
  plugins: [i18n],
}

describe('LanguageSelector', () => {
  afterEach(() => {
    cy.wrap(i18n).then(p => p.global.locale.value = 'en')
  })

  it('changes locale', () => {
    cy.mount(LanguageSelector, {global})
    cy.get('select').should('have.value', 'en')
    cy.wrap(i18n).then(p => p.global.t('test')).should('eq', 'test in English')

    cy.get('select').select('fr')
    cy.get('select').should('have.value', 'fr')
    cy.wrap(i18n).then(p => p.global.t('test')).should('eq', 'test en français')
  })
})
