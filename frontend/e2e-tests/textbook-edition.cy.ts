import { visit, login, loadFixtures } from './utils'


describe('Gabby', () => {
  before(console.clear)

  beforeEach(() => {
    loadFixtures('test-exercises')
    login()
  })

  it('shows and hides the section editor dialog', () => {
    visit('/project-xkopqm/textbook-klxufv/page-6', {locale: 'fr'})

    cy.get('h1').contains('Lien entre PDF et manuel').should('not.exist')

    cy.get('button').contains('⚙').click()
    cy.get('h1').contains('Lien entre PDF et manuel').should('exist')

    cy.get('button').contains('Annuler').click()
    cy.get('h1').contains('Lien entre PDF et manuel').should('not.exist')
  })
})
