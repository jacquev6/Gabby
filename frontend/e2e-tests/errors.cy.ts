import { loadFixtures, login, visit } from './utils'


describe("Gabby's error catcher", () => {
  before(() => {
    console.clear()
    loadFixtures('admin-user')
  })

  beforeEach(() => {
    login()
  })

  // @todo Find an error caught by 'window.onerror'

  it('catches dereferencing undefined', () => {
    visit('/errors')

    cy.get('button:contains("Dereference undefined")').click()

    cy.get('h1:contains("There was a bug")').should('exist')
    cy.get('pre')
      .should('contain', 'Caught by: Vue.config.errorHandler')
      .should('contain', 'Message: TypeError: Cannot read properties of undefined')
      .should('contain', 'End of details')
  })

  it('catches dereferencing null', () => {
    visit('/errors')

    cy.get('button:contains("Dereference null")').click()

    cy.get('h1:contains("There was a bug")').should('exist')
    cy.get('pre')
      .should('contain', 'Caught by: Vue.config.errorHandler')
      .should('contain', 'Message: TypeError: Cannot read properties of null')
      .should('contain', 'End of details')
  })

  it('catches unhandled rejection', () => {
    visit('/errors')

    cy.get('button:contains("Unhandled rejection")').click()

    cy.get('h1:contains("There was a bug")').should('exist')
    cy.get('pre')
      .should('contain', 'Caught by: Vue.config.errorHandler')
      .should('contain', 'Message: This is the reason')
      .should('contain', 'End of details')
  })

  it('catches unhandled rejection not caught by Vue.js', () => {
    cy.on('uncaught:exception', () => false)  // Don't fail the test, that's the whole point
    cy.visit('/errors?reject')
    cy.get('select').last().select('en', {force: true})

    cy.get('h1:contains("There was a bug")').should('exist')
    cy.get('pre')
      .should('contain', 'Caught by: window.onunhandledrejection')
      .should('contain', 'Message: This is the reason')
      .should('contain', 'End of details')
  })

  it('catches thrown exception', () => {
    visit('/errors')

    cy.get('button:contains("Throw exception")').click()

    cy.get('h1:contains("There was a bug")').should('exist')
    cy.get('pre')
      .should('contain', 'Caught by: Vue.config.errorHandler')
      .should('contain', 'Message: Error: This is the error')
      .should('contain', 'End of details')
  })

  it('catches 422', () => {
    visit('/errors')

    cy.get('button:contains("Generate a 422 response")').click()

    cy.get('h1:contains("There was a bug")').should('exist')
    cy.get('pre')
      .should('contain', 'Caught by: Vue.config.errorHandler')
      .should('contain', 'Message: Error: Failed to get syntheticError 422: 422')
      .should('contain', 'End of details')
  })

  it('catches 500', () => {
    visit('/errors')

    cy.get('button:contains("Generate a 500 response")').click()

    cy.get('h1:contains("There was a bug")').should('exist')
    cy.get('pre')
      .should('contain', 'Caught by: Vue.config.errorHandler')
      .should('contain', 'Message: Error: Failed to get syntheticError 500: 500')
      .should('contain', 'End of details')
  })
})
