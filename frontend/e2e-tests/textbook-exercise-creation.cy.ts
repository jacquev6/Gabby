import { visit, login, loadFixtures, notBusy } from './utils'


describe('Gabby', () => {
  before(console.clear)

  beforeEach(() => {
    loadFixtures('test-exercises')
    login()
  })

  it('enables the "Save exercise" button', () => {
    visit('/project-xkopqm/textbook-klxufv/page-6/new-exercise')

    cy.get('button:contains("Save then next")').should('be.disabled')

    cy.get('label:contains("Number")').next().type('1')
    cy.get('button:contains("Save then next")').should('be.enabled')

    cy.get('label:contains("Number")').next().clear()
    cy.get('button:contains("Save then next")').should('be.disabled')

    cy.get('label:contains("Number")').next().type('A')
    cy.get('button:contains("Save then next")').should('be.enabled')
  })

  it('creates a minimal exercise', () => {
    visit('/project-xkopqm/textbook-klxufv/page-6/new-exercise')

    cy.get('label:contains("Number")').next().type('1')
    cy.get('button:contains("Save then next")').click()
    notBusy()

    cy.get('label:contains("Number")').next().should('have.value', '2')

    cy.get('a:contains("Back to list (without saving)")').click()
    notBusy()
    cy.get('li:contains("1")').should('exist')
  })

  it('creates a full exercise', () => {
    visit('/project-xkopqm/textbook-klxufv/page-6/new-exercise')

    cy.get('label:contains("Number")').next().type('Défis')
    cy.get('label:contains("Instructions")').next().type('Do the smartest thing ever.')
    cy.get('label:contains("Wording")').next().type('The wording of this exercise is a bit longer in a quite artificial way.')
    cy.get('p:contains("Example")').click()
    cy.focused().type('The example')
    cy.get('p:contains("Clue")').click()
    cy.focused().type('The clue')

    cy.get('label:contains("Adaptation type") + select').select('generic')
    cy.get('div:contains("Words") >input').check()
    cy.get('div:contains("Selectable") >input').check()
    cy.get('span.maybe-usable-colors-container span.usable-colors-button[data-cy-colors="2"]').click()

    cy.get('span:contains("artificial")').first().click()
    cy.get('span:contains("artificial")').first().should('have.css', 'background-color', 'rgb(255, 255, 0)')
    cy.get('span:contains("artificial")').first().click()
    cy.get('span:contains("artificial")').first().should('have.css', 'background-color', 'rgb(255, 192, 203)')
    cy.get('span:contains("artificial")').first().click()
    cy.get('span:contains("artificial")').first().should('have.css', 'background-color', 'rgba(0, 0, 0, 0)')

    cy.get('button:contains("Save then next")').click()
    notBusy()

    cy.get('label:contains("Number")').next().should('have.value', '')

    cy.get('a:contains("Back to list (without saving)")').click()
    notBusy()
    cy.get('li:contains("Défis")').should('exist')
  })

  it('detects when an exercise already exists', () => {
    visit('/project-xkopqm/textbook-klxufv/page-6/new-exercise')

    cy.get('label:contains("Number")').next().type('2')
    cy.get('button:contains("Save then next")').click()
    notBusy()

    cy.get('label:contains("Number")').next().should('have.value', '3')
    cy.get('button:contains("Save then next")').should('be.disabled')
    cy.get('button:contains("Skip to next exercise")').click()
    cy.get('label:contains("Number")').next().should('have.value', '4')
    cy.get('button:contains("Save then next")').should('be.disabled')
    cy.get('button:contains("Skip to next exercise")').click()
    cy.get('label:contains("Number")').next().should('have.value', '5')
    cy.get('button:contains("Save then next")').should('be.enabled')

    cy.get('label:contains("Number")').next().type('{selectAll}3')
    cy.get('button:contains("Save then next")').should('be.disabled')
    cy.get('button:contains("Skip to next exercise")').should('be.enabled')
    cy.get('label:contains("Number")').next().type('0')
    cy.get('button:contains("Save then next")').should('be.enabled')
    cy.get('button:contains("Skip to next exercise")').should('not.exist')
  })
})
