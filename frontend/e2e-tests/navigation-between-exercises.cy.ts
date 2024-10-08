import { loadFixtures, login, visit } from './utils'


describe('Gabby\'s new exercise view', () => {
  before(console.clear)

  beforeEach(() => {
    loadFixtures('more-test-exercises')
    login()
  })

  it('navigates using "Save then next" and "Previous" buttons', () => {
    visit('/project-xkopqm/textbook-klxufv/page-1/new-exercise')

    cy.get('label:contains("Number")').next().type('1')

    cy.get('button:contains("Previous (without saving)")').should('be.disabled')

    cy.get('button:contains("Save then next")').click()

    cy.get('label:contains("Number")').next().should('have.value', '2')
    cy.get('button:contains("Previous (without saving)")').should('be.enabled')
    cy.get('button:contains("Save then next")').click()

    cy.get('label:contains("Number")').next().should('have.value', '3')

    cy.get('button:contains("Previous (without saving)")').click()

    cy.location('pathname').should('equal', '/project-xkopqm/textbook-klxufv/page-1/exercise-fxcuac')
    cy.get('label:contains("Number")').next().should('have.value', '2')

    cy.get('button:contains("Save then next")').click()

    cy.location('pathname').should('equal', '/project-xkopqm/textbook-klxufv/page-1/new-exercise')
    cy.get('label:contains("Number")').next().should('have.value', '3')

    cy.get('button:contains("Previous (without saving)")').click()

    cy.location('pathname').should('equal', '/project-xkopqm/textbook-klxufv/page-1/exercise-fxcuac')
    cy.get('label:contains("Number")').next().should('have.value', '2')

    cy.get('button:contains("Previous (without saving)")').click()

    cy.location('pathname').should('equal', '/project-xkopqm/textbook-klxufv/page-1/exercise-pghtfo')
    cy.get('label:contains("Number")').next().should('have.value', '1')

    cy.get('button:contains("Save then next")').click()

    cy.location('pathname').should('equal', '/project-xkopqm/textbook-klxufv/page-1/exercise-fxcuac')
    cy.get('label:contains("Number")').next().should('have.value', '2')

    cy.get('button:contains("Save then next")').click()

    cy.location('pathname').should('equal', '/project-xkopqm/textbook-klxufv/page-1/new-exercise')
    cy.get('label:contains("Number")').next().should('have.value', '3')
  })

  it('resets history when going back to list', () => {
    visit('/project-xkopqm/textbook-klxufv/page-1/new-exercise')

    cy.get('label:contains("Number")').next().type('1')

    cy.get('button:contains("Save then next")').click()

    cy.get('label:contains("Number")').next().should('have.value', '2')
    cy.get('button:contains("Previous (without saving)")').should('be.enabled')

    cy.get('a:contains("Back to list (without saving)")').click()

    cy.get('a:contains("New exercise")').click()

    cy.get('label:contains("Number")').next().should('have.value', '')
    cy.get('button:contains("Previous (without saving)")').should('be.disabled')
  })
})
