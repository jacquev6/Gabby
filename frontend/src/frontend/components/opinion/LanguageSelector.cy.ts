import LanguageSelector from './LanguageSelector.vue'
import { i18n } from '$/locales'


describe('LanguageSelector', () => {
  it('changes locale', () => {
    cy.mount(LanguageSelector)
    cy.get('select[data-cy="language"]').should('have.value', 'en')
    cy.wrap(i18n).then(p => (p as any/* Work around Cypress typing limitations */).global.t('opinion.ping')).should('eq', 'Ping (in English)')

    cy.get('select[data-cy="language"]').select('fr')
    cy.get('select[data-cy="language"]').should('have.value', 'fr')
    cy.wrap(i18n).then(p => (p as any/* Work around Cypress typing limitations */).global.t('opinion.ping')).should('eq', 'Ping (en français)')

    cy.get('select[data-cy="language"]').select('en')
  })
})
