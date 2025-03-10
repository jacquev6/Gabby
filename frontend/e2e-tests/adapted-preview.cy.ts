import { loadFixtures, login, notBusy, visit } from './utils'

describe('Gabby', () => {
  before(console.clear)

  beforeEach(() => {
    loadFixtures('more-test-exercises')
    login()
    cy.viewport(1000, 1000)
  })

  it('resets responses when changing adaptation type', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/exercise-dymwin')
    cy.get('label:contains("Number")').next().should('have.value', '11')

    cy.get('span[contenteditable]').first().type('Abcd')

    cy.get('label:contains("Adaptation type")').next().select('generic')
    cy.get('div:contains("Words") >input').check()
    cy.get('div:contains("Selectable") >input').check()
    notBusy()

    cy.get('span:contains("tracter")').first().click()
    cy.get('span:contains("tracter")').first().should('have.css', 'background-color', 'rgb(255, 255, 0)')

    cy.get('label:contains("Adaptation type")').next().select('fill-with-free-text')
    notBusy()

    cy.get('span[contenteditable]').first().should('have.value', '')

    cy.get('label:contains("Adaptation type")').next().select('generic')
    cy.get('div:contains("Selectable") >input').check()
    notBusy()

    cy.get('span:contains("tracter")').should('have.css', 'background-color', 'rgba(0, 0, 0, 0)')
  })
})
