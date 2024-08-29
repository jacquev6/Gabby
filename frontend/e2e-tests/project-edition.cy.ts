import { visit, login, loadFixtures } from './utils'


describe('Gabby', () => {
  before(console.clear)

  beforeEach(() => {
    loadFixtures('empty-project')
    login()
  })

  it('lands', () => {
    visit('/project-xkopqm')

    cy.get('h1:contains("Test project")').should('exist')
    cy.title().should('eq', 'MALIN - Test project')
    cy.get('p:contains("This is a test project, created empty in a fixture.")').should('exist')
    cy.get('.navbar').should('contain', 'Test project')
    cy.get('h2:contains("New textbook")').should('exist')
    cy.get('h2:contains("New independent exercise")').should('exist')
    cy.get('h2:contains("Existing textbooks and exercises")').should('exist')
  })

  it('edits title and description', () => {
    visit('/project-xkopqm')

    cy.get('h1:contains("Test project") button:contains("Edit")').click()
    cy.get('label:contains("Title")').first().next().clear().type('New title')
    cy.get('label:contains("Description")').next().clear().type('New description.')
    cy.get('button:contains("Save")').click()

    cy.get('h1:contains("New title")').should('exist')
    cy.title().should('eq', 'MALIN - New title')
    cy.get('p:contains("New description.")').should('exist')

    visit('/project-xkopqm')
    cy.get('h1:contains("New title")').should('exist')
    cy.title().should('eq', 'MALIN - New title')
    cy.get('p:contains("New description.")').should('exist')
  })

  it('refuses to empty title', () => {
    visit('/project-xkopqm')

    cy.get('h1:contains("Test project") button:contains("Edit")').click()
    cy.get('label:contains("Title")').first().next().clear()
    cy.get('button:contains("Save")').should('be.disabled')
  })
})
