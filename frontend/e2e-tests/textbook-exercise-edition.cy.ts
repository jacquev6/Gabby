import { visit, login, loadFixtures, notBusy } from './utils'


describe('Gabby', () => {
  before(console.clear)

  beforeEach(() => {
    loadFixtures('more-test-exercises')
    login()
  })

  it('saves an exercise after setting its adaptation', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/exercise-jkrudc', {wysiwyg: false})

    cy.get('label:contains("Adaptation type")').next().should('have.value', '-')

    cy.get('label:contains("Adaptation type")').next().select('selectThingsAdaptation')
    cy.get('label:contains("Instructions")').next().type('{selectAll}Instructions!')
    notBusy()
    // There was a bug with a 422 response from POST /api/fillWithFreeTextAdaptations
    cy.get('button:contains("Save then back to list")').click()
    notBusy()

    cy.get('li:contains("Instructions!"):contains("Select words")').should('exist')

    visit('/project-xkopqm/textbook-klxufv/page-7/exercise-jkrudc', {wysiwyg: false})
    cy.get('label:contains("Adaptation type")').next().should('have.value', 'selectThingsAdaptation')
    cy.get('label:contains("Instructions")').next().should('have.value', 'Instructions!')
  })

  it('saves an exercise after resetting its pre-existing adaptation', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/exercise-dymwin', {wysiwyg: false})

    cy.get('label:contains("Adaptation type")').next().should('have.value', 'fillWithFreeTextAdaptation')

    cy.get('label:contains("Adaptation type")').next().select('-')
    cy.get('label:contains("Instructions")').next().type('{selectAll}Instructions!')
    notBusy()
    cy.get('button:contains("Save then back to list")').click()
    notBusy()

    cy.get('li:contains("Instructions!")').should('exist').should('not.contain', 'Fill with free text')

    visit('/project-xkopqm/textbook-klxufv/page-7/exercise-dymwin', {wysiwyg: false})
    cy.get('label:contains("Adaptation type")').next().should('have.value', '-')
    cy.get('label:contains("Instructions")').next().should('have.value', 'Instructions!')
  })

  it('saves an exercise without changing its pre-existing adaptation', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/exercise-dymwin', {wysiwyg: false})

    cy.get('label:contains("Adaptation type")').next().should('have.value', 'fillWithFreeTextAdaptation')

    cy.get('label:contains("Instructions")').next().type('{selectAll}Instructions!')
    notBusy()
    // There was a bug with a 422 response from POST /api/fillWithFreeTextAdaptations
    cy.get('button:contains("Save then back to list")').click()
    notBusy()

    cy.get('li:contains("Instructions!"):contains("Fill with free text")').should('exist')

    visit('/project-xkopqm/textbook-klxufv/page-7/exercise-dymwin', {wysiwyg: false})
    cy.get('label:contains("Adaptation type")').next().should('have.value', 'fillWithFreeTextAdaptation')
    cy.get('label:contains("Instructions")').next().should('have.value', 'Instructions!')
  })

  it('saves an exercise after changing the type of its pre-existing adaptation', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/exercise-dymwin', {wysiwyg: false})

    cy.get('label:contains("Adaptation type")').next().should('have.value', 'fillWithFreeTextAdaptation')

    cy.get('label:contains("Adaptation type")').next().select('selectThingsAdaptation')
    cy.get('label:contains("Instructions")').next().type('{selectAll}Instructions!')
    notBusy()
    cy.get('button:contains("Save then back to list")').click()
    notBusy()

    cy.get('li:contains("Instructions!"):contains("Select words")').should('exist')

    visit('/project-xkopqm/textbook-klxufv/page-7/exercise-dymwin', {wysiwyg: false})
    cy.get('label:contains("Adaptation type")').next().should('have.value', 'selectThingsAdaptation')
    cy.get('label:contains("Instructions")').next().should('have.value', 'Instructions!')
  })
})
