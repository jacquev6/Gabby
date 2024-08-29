import { visit, login, loadFixtures, loadPdf } from './utils'


describe('Gabby', () => {
  before(console.clear)

  beforeEach(() => {
    loadFixtures('empty-project')
    login()
  })

  it('enables the "Create textbook" button', () => {
    visit('/project-xkopqm')

    cy.get('button:contains("Create textbook")').should('be.disabled')

    cy.get('label:contains("Title")').next().type('Test textbook')
    cy.get('button:contains("Create textbook")').should('be.disabled')

    loadPdf('test')
    cy.get('button:contains("Create textbook")').should('be.enabled')

    cy.get('label:contains("Title")').next().clear()
    cy.get('button:contains("Create textbook")').should('be.disabled')
  })

  it('previews the pdf', () => {
    visit('/project-xkopqm')

    loadPdf('test')

    cy.get('p:contains("Page"):contains("(on 2)") input').should('have.value', '1')
    cy.get('p:contains("Page"):contains("(on 2)") button:contains("<")').should('be.disabled')
    cy.get('p:contains("Page"):contains("(on 2)") button:contains(">")').click()
    cy.get('p:contains("Page"):contains("(on 2)") input').should('have.value', '2')
    cy.get('p:contains("Page"):contains("(on 2)") button:contains(">")').should('be.disabled')

    cy.get('p:contains("Page"):contains("(on 2)") input').clear().type('37').blur()
    cy.get('p:contains("Page"):contains("(on 2)") input').should('have.value', '2')

    cy.get('p:contains("Page"):contains("(on 2)") input').clear().type('137').blur()
    cy.get('p:contains("Page"):contains("(on 2)") input').should('have.value', '1')

    cy.get('button:contains("Cancel")').click()
    cy.get('p:contains("Page"):contains("(on 2)")').should('not.exist')

    loadPdf('test')

    cy.get('p:contains("Page"):contains("(on 2)")').should('exist')
  })

  it('creates a minimal textbook', () => {
    visit('/project-xkopqm')

    loadPdf('test')
    cy.get('label:contains("Title")').next().type('Test textbook')
    cy.get('button:contains("Create textbook")').click()

    cy.get('p:contains("No exercises yet")').should('exist')

    visit('/project-xkopqm')

    cy.get('h3:contains("Test textbook")').should('exist')
  })

  it('creates a full textbook', () => {
    visit('/project-xkopqm')

    loadPdf('test')
    cy.get('label:contains("Title")').next().type('Test textbook')
    cy.get('label:contains("Publisher")').next().type('Test publisher')
    cy.get('label:contains("Year")').next().type('2024')
    cy.get('label:contains("ISBN")').next().type('1234567890123')
    cy.get('button:contains("Create textbook")').click()

    cy.get('p:contains("No exercises yet")').should('exist')

    visit('/project-xkopqm')

    cy.get('h3:contains("Test textbook, Test publisher (2024)")').should('exist')
  })

  it('creates two textbooks from the same PDF', () => {
    visit('/project-xkopqm')
    loadPdf('test')
    cy.get('label:contains("Title")').next().type('First textbook')
    cy.get('button:contains("Create textbook")').click()
    cy.get('p:contains("No exercises yet")').should('exist')

    visit('/project-xkopqm')
    loadPdf('test')
    cy.get('label:contains("Title")').next().type('Second textbook')
    cy.get('button:contains("Create textbook")').click()
    cy.get('p:contains("No exercises yet")').should('exist')

    visit('/project-xkopqm')
    cy.get('h3:contains("First textbook")').should('exist')
    cy.get('h3:contains("Second textbook")').should('exist')
  })
})
