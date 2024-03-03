import LanguageSelector from './language-selector.vue'
import { i18n } from '../../locales/for-tests'


describe('LanguageSelector', () => {
  it('changes locale', () => {
    cy.mount(LanguageSelector)
    cy.get('select').should('have.value', 'en')
    cy.wrap(i18n).then(p => p.global.t('test')).should('eq', 'test in English')

    cy.get('select').select('fr')
    cy.get('select').should('have.value', 'fr')
    cy.wrap(i18n).then(p => p.global.t('test')).should('eq', 'test en français')

    cy.get('select').select('en')
  })
})
