import { visit, login, loadFixtures, notBusy } from './utils'


describe('Gabby', () => {
  before(console.clear)

  beforeEach(() => {
    loadFixtures('empty-project')
    login()
  })

  it('enables the "Create exercise" button', () => {
    visit('/project-xkopqm')

    cy.get('button:contains("Create exercise")').should('be.disabled')

    cy.get('label:contains("Number")').next().type('a')

    cy.get('button:contains("Create exercise")').should('be.enabled')

    cy.get('label:contains("Number")').next().clear()

    cy.get('button:contains("Create exercise")').should('be.disabled')
  })

  it('creates a minimal independent exercise', () => {
    visit('/project-xkopqm')

    cy.get('label:contains("Number")').next().type('10')
    cy.get('label:contains("Instructions")').next().type('Do something smart.')
    cy.get('button:contains("Create exercise")').click()

    notBusy()

    cy.get('label:contains("Number")').next().should('have.value', '11')

    cy.get('li:contains("10 Do something smart.")').should('exist')
  })

  it('creates a full independent exercise', () => {
    visit('/project-xkopqm')

    cy.get('label:contains("Number")').next().type('L10')
    cy.get('label:contains("Instructions")').next().type('Do the smartest thing ever.')
    cy.get('label:contains("Wording")').next().type('The wording')
    cy.get('p:contains("Example")').click()
    cy.focused().type('The example')
    cy.get('p:contains("Clue")').click()
    cy.focused().type('The clue')
    cy.get('button:contains("Create exercise")').click()

    notBusy()

    cy.get('label:contains("Number")').next().should('have.value', '')

    cy.get('li:contains("L10 Do the smartest thing eve…")').should('exist')
  })
})
