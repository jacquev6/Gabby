import { loadFixtures, login, visit } from './utils'


describe('Not found message', () => {
  before(() => {
    console.clear()
    loadFixtures('more-test-exercises')
  })

  beforeEach(() => {
    login()
  })

  it('on the project view when the project does not exist', () => {
    visit('/project-nope')

    cy.get('h1:contains("Project not found")').should('exist')
    cy.title().should('eq', 'MALIN - Project not found')
  })

  it('on the textbook page view when the project does not exist', () => {
    visit('/project-nope/textbook-klxufv/page-6')

    cy.get('h1:contains("Project not found")').should('exist')
    cy.title().should('eq', 'MALIN - Project not found')
  })

  it('on the textbook page view when the textbook does not exist', () => {
    visit('/project-xkopqm/textbook-nope/page-6')

    cy.get('h1:contains("Textbook not found")').should('exist')
    cy.title().should('eq', 'MALIN - Premier projet de test - Textbook not found')
  })

  it('on the textbook page view when the textbook does not belong to this project', () => {
    visit('/project-fryrbl/textbook-klxufv/page-6')

    cy.get('h1:contains("Textbook not found")').should('exist')
    cy.title().should('eq', 'MALIN - Deuxième projet de test - Textbook not found')
  })

  it('on the exercise creation view when the project does not exist', () => {
    visit('/project-nope/textbook-klxufv/page-6/new-exercise')

    cy.get('h1:contains("Project not found")').should('exist')
    cy.title().should('eq', 'MALIN - Project not found')
  })

  it('on the exercise creation view when the textbook does not exist', () => {
    visit('/project-xkopqm/textbook-nope/page-6/new-exercise')

    cy.get('h1:contains("Textbook not found")').should('exist')
    cy.title().should('eq', 'MALIN - Premier projet de test - Textbook not found')
  })

  it('on the exercise creation view when the textbook does not belong to this project', () => {
    visit('/project-fryrbl/textbook-klxufv/page-6/new-exercise')

    cy.get('h1:contains("Textbook not found")').should('exist')
    cy.title().should('eq', 'MALIN - Deuxième projet de test - Textbook not found')
  })
})
