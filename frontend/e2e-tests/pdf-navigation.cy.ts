import { visit, login, loadFixtures, notBusy, loadPdf } from './utils'


describe('Gabby', () => {
  before(console.clear)

  beforeEach(() => {
    loadFixtures('more-test-exercises')
    login()
  })

  it('navigates the textbook', () => {
    visit('/project-xkopqm/textbook-klxufv/page-6')

    cy.get('p:contains("Page"):contains("(on 7)") input').should('have.value', '6')
    cy.get('p:contains("The PDF that contains this page (test.pdf) has not been loaded yet.")').should('exist')

    cy.get('p:contains("Page"):contains("(on 7)") :contains(">")').click()
    cy.get('p:contains("Page"):contains("(on 7)") input').should('have.value', '7')
    cy.url().should('eq', `${Cypress.config().baseUrl}project-xkopqm/textbook-klxufv/page-7`)
    cy.get('p:contains("Page"):contains("(on 7)") :contains(">")').should('be.disabled')
    cy.get('p:contains("The PDF that contains this page (test.pdf) has not been loaded yet.")').should('exist')

    cy.get('p:contains("Page"):contains("(on 7)") :contains("<")').click()
    cy.get('p:contains("Page"):contains("(on 7)") :contains(">")').should('be.enabled')

    cy.get('p:contains("Page"):contains("(on 7)") :contains("<")').click()
    cy.get('p:contains("Page"):contains("(on 7)") input').should('have.value', '5')
    cy.url().should('eq', `${Cypress.config().baseUrl}project-xkopqm/textbook-klxufv/page-5`)
    cy.get('p:contains("No known PDF contains this page.")').should('exist')
    cy.get('p:contains("The PDF that contains this page (test.pdf) has not been loaded yet.")').should('not.exist')

    cy.get('p:contains("Page"):contains("(on 7)") input').clear().type('1')
    cy.url().should('eq', `${Cypress.config().baseUrl}project-xkopqm/textbook-klxufv/page-1`)
    cy.get('p:contains("Page"):contains("(on 7)") :contains("<")').should('be.disabled')
    cy.get('p:contains("No known PDF contains this page.")').should('exist')

    cy.get('p:contains("Page"):contains("(on 7)") input').clear().type('100').blur()
    notBusy()
    cy.get('p:contains("Page"):contains("(on 7)") input').should('have.value', '1')
    cy.url().should('eq', `${Cypress.config().baseUrl}project-xkopqm/textbook-klxufv/page-1`)

    cy.get('p:contains("Page"):contains("(on 7)") input').clear().type('200').blur()
    notBusy()
    cy.get('p:contains("Page"):contains("(on 7)") input').should('have.value', '2')
    cy.url().should('eq', `${Cypress.config().baseUrl}project-xkopqm/textbook-klxufv/page-2`)
  })

  it('loads a PDF', () => {
    visit('/project-xkopqm/textbook-klxufv/page-6')

    notBusy()
    cy.get('p:contains("The PDF that contains this page (test.pdf) has not been loaded yet.")').should('exist')

    loadPdf('test')
    cy.get('p:contains("The PDF that contains this page (test.pdf) has not been loaded yet.")').should('not.exist')
    cy.get('input[type=file]').should('not.exist')
  })

  it('allows navigating the PDF when creating an exercise', () => {
    visit('/project-xkopqm/textbook-klxufv/page-6/new-exercise')

    loadPdf('test')

    cy.get('label:contains("Number")').next().type('5')

    cy.get('p:contains("Page"):contains("(on 7)") :contains(">")').click()
    cy.url().should('eq', `${Cypress.config().baseUrl}project-xkopqm/textbook-klxufv/page-7/new-exercise`)
    cy.get('label:contains("Number")').next().should('have.value', '5')

    cy.get('button:contains("Save then next")').click()
    notBusy()
    cy.get('a:contains("Back to list (without saving)")').click()

    notBusy()
    cy.url().should('eq', `${Cypress.config().baseUrl}project-xkopqm/textbook-klxufv/page-7`)
    cy.get('li:contains("5")').should('exist')
  })
})
