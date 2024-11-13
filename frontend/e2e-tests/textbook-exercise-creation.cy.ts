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

  it('adjusts textarea heights', () => {
    visit('/project-xkopqm/textbook-klxufv/page-6/new-exercise', {wysiwyg: false})

    for (const label of ['Instructions', 'Wording']) {
      cy.get(`label:contains("${label}")`).next().should('have.attr', 'rows', '2')
      cy.get(`label:contains("${label}")`).next().type('a\nb\nc\nd')
      cy.get(`label:contains("${label}")`).next().should('have.attr', 'rows', '5')
    }

    for (const label of ['Example', 'Clue']) {
      cy.get(`p:contains("${label}")`).click()
      cy.get(`label:contains("${label}")`).next().should('have.attr', 'rows', '2')
      cy.get(`label:contains("${label}")`).next().type('a\nb\nc')
      cy.get(`label:contains("${label}")`).next().should('have.attr', 'rows', '4')
    }
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
    visit('/project-xkopqm/textbook-klxufv/page-6/new-exercise', {wysiwyg: false})

    cy.get('label:contains("Number")').next().type('Défis')
    cy.get('label:contains("Instructions")').next().type('Do the smartest thing ever.')
    cy.get('label:contains("Wording")').next().type('The wording of this exercise is a bit longer in a quite artificial way.')
    cy.get('p:contains("Example")').click()
    cy.focused().type('The example')
    cy.get('p:contains("Clue")').click()
    cy.focused().type('The clue')

    cy.get('label:contains("Adaptation type") + select').select('items-and-effects-attempt-1')
    cy.get('div:contains("Selectable") >input').check()
    cy.get('span.maybe-usable-colors-container span.usable-colors-button[data-cy-colors="2"]').click()

    cy.get('span:contains("artificial")').last().click()
    cy.get('span:contains("artificial")').last().should('have.css', 'background-color', 'rgb(255, 255, 0)')
    cy.get('span:contains("artificial")').last().click()
    cy.get('span:contains("artificial")').last().should('have.css', 'background-color', 'rgb(255, 192, 203)')
    cy.get('span:contains("artificial")').last().click()
    cy.get('span:contains("artificial")').last().should('have.css', 'background-color', 'rgba(0, 0, 0, 0)')

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
