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

  it('saves an exercise after deleting its adaptation', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7')
    cy.get('a[href*="exercise-dymwin"]').click()
    notBusy()

    cy.get('label:contains("Adaptation type")').next().should('have.value', 'fillWithFreeTextAdaptation')

    cy.get('label:contains("Adaptation type")').next().select('-')
    notBusy()
    cy.get('button:contains("Save then back to list")').click()
    notBusy()

    cy.get('a[href*="exercise-dymwin"]').click()
    notBusy()
    cy.get('label:contains("Adaptation type")').next().should('have.value', '-')
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

  it('saves an exercise after changing details of its adaptation', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7')  // Trigger a bug where the exercise's cached adaptation was not updated. Did not happen when going directly to the exercise page.
    cy.get('li:contains("Select words") a:contains("Edit")').click()
    notBusy()

    cy.get('span.maybe-usable-colors-container span.usable-colors-button[data-cy-colors="4"]').should('have.css', 'background-color', 'rgb(187, 255, 187)')

    cy.get('span.maybe-usable-colors-container span.usable-colors-button[data-cy-colors="4"]').rightclick()
    cy.get('.colour-area-mask').click(100, 100)
    notBusy()
    cy.get('sel-blot[data-sel="4"]').should('have.css', 'background-color', 'rgb(45, 75, 45)')
    cy.get('span.maybe-usable-colors-container span.usable-colors-button[data-cy-colors="4"]').should('have.css', 'background-color', 'rgb(45, 75, 45)')
    cy.get('button[data-cy="format-color-4"] > span').should('have.css', 'background-color', 'rgb(45, 75, 45)')
    cy.get('span:contains("verbes")').last().should('have.css', 'background-color', 'rgb(45, 75, 45)')
    cy.get('span:contains("4 clicks")').last().should('have.css', 'background-color', 'rgb(45, 75, 45)')
    cy.get('button:contains("OK")').click()
    cy.get('span:contains("Afrique")').last().click()
    cy.get('span:contains("Afrique")').last().click()
    cy.get('span:contains("Afrique")').last().click()
    cy.get('span:contains("Afrique")').last().click()
    cy.get('span:contains("Afrique")').last().should('have.css', 'background-color', 'rgb(45, 75, 45)')

    cy.get('button:contains("Save then back to list")').click()
    notBusy()

    cy.get('li:contains("Select words") a:contains("Edit")').click()
    notBusy()

    cy.get('sel-blot[data-sel="4"]').should('have.css', 'background-color', 'rgb(45, 75, 45)')
    cy.get('span.maybe-usable-colors-container span.usable-colors-button[data-cy-colors="4"]').should('have.css', 'background-color', 'rgb(45, 75, 45)')
    cy.get('button[data-cy="format-color-4"] > span').should('have.css', 'background-color', 'rgb(45, 75, 45)')
    cy.get('span:contains("verbes")').last().should('have.css', 'background-color', 'rgb(45, 75, 45)')
    cy.get('span:contains("4 clicks")').last().should('have.css', 'background-color', 'rgb(45, 75, 45)')
    cy.get('span:contains("Afrique")').last().click()
    cy.get('span:contains("Afrique")').last().click()
    cy.get('span:contains("Afrique")').last().click()
    cy.get('span:contains("Afrique")').last().click()
    cy.get('span:contains("Afrique")').last().should('have.css', 'background-color', 'rgb(45, 75, 45)')
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

  it('throttles updates of the preview', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/exercise-vodhqn', {wysiwyg: false})

    cy.get('label:contains("Wording")').next().type('{selectAll}{del}', {delay: 0})
    notBusy()

    cy.intercept('POST', '/api/parsedExercises').as('parsedExercises')
    for (let i = 0; i !== 20; i += 1) {
      cy.get('label:contains("Wording")').next().type(' a', {delay: 0})
    }
    notBusy()

    cy.get('@parsedExercises.all').its('length').should('be.lessThan', 19)
  })
})
