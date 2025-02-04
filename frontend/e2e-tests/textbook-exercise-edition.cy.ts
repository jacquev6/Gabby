import { visit, login, loadFixtures, notBusy } from './utils'


describe('Gabby', () => {
  before(console.clear)

  beforeEach(() => {
    loadFixtures('more-test-exercises')
    login()
  })

  it('saves an exercise after setting its adaptation', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/exercise-jkrudc')

    cy.get('label:contains("Adaptation type")').next().should('have.value', 'generic')

    cy.get('label:contains("Adaptation type")').next().select('multiple-choices')
    cy.get('label:contains("Instructions")').next().type('{selectAll}Instructions!')
    notBusy()
    // There was a bug with a 422 response from POST /api/fill-with-free-texts
    cy.get('button:contains("Save then back to list")').click()
    notBusy()

    cy.get('li:contains("Instructions!"):contains("Multiple choices")').should('exist')

    visit('/project-xkopqm/textbook-klxufv/page-7/exercise-jkrudc')
    cy.get('label:contains("Adaptation type")').next().should('have.value', 'multiple-choices')
    cy.get('label:contains("Instructions")').next().should('have.text', 'Instructions!')
  })

  it('saves an exercise after resetting its pre-existing adaptation', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/exercise-dymwin')

    cy.get('label:contains("Adaptation type")').next().should('have.value', 'fill-with-free-text')

    cy.get('label:contains("Adaptation type")').next().select('generic')
    cy.get('label:contains("Instructions")').next().type('{selectAll}Instructions!')
    notBusy()
    cy.get('button:contains("Save then back to list")').click()
    notBusy()

    cy.get('li:contains("Instructions!")').should('exist').should('not.contain', 'Fill with free text')

    visit('/project-xkopqm/textbook-klxufv/page-7/exercise-dymwin')
    cy.get('label:contains("Adaptation type")').next().should('have.value', 'generic')
    cy.get('label:contains("Instructions")').next().should('have.text', 'Instructions!')
  })

  it('saves an exercise after deleting its adaptation', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7')
    cy.get('a[href*="exercise-dymwin"]').click()
    notBusy()

    cy.get('label:contains("Adaptation type")').next().should('have.value', 'fill-with-free-text')

    cy.get('label:contains("Adaptation type")').next().select('generic')
    notBusy()
    cy.get('button:contains("Save then back to list")').click()
    notBusy()

    cy.get('a[href*="exercise-dymwin"]').click()
    notBusy()
    cy.get('label:contains("Adaptation type")').next().should('have.value', 'generic')
  })

  it('saves an exercise without changing its pre-existing adaptation', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/exercise-dymwin')

    cy.get('label:contains("Adaptation type")').next().should('have.value', 'fill-with-free-text')

    cy.get('label:contains("Instructions")').next().type('{selectAll}Instructions!')
    notBusy()
    // There was a bug with a 422 response from POST /api/fill-with-free-texts
    cy.get('button:contains("Save then back to list")').click()
    notBusy()

    cy.get('li:contains("Instructions!"):contains("Fill with free text")').should('exist')

    visit('/project-xkopqm/textbook-klxufv/page-7/exercise-dymwin')
    cy.get('label:contains("Adaptation type")').next().should('have.value', 'fill-with-free-text')
    cy.get('label:contains("Instructions")').next().should('have.text', 'Instructions!')
  })

  it('saves an exercise after changing details of its adaptation', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7')  // Trigger a bug where the exercise's cached adaptation was not updated. Did not happen when going directly to the exercise page.
    cy.get('li:contains("7 Relève") a:contains("Edit")').click()
    notBusy()

    cy.get('span.maybe-usable-colors-container span.usable-colors-button[data-cy-colors="4"]').should('have.css', 'background-color', 'rgb(187, 255, 187)')

    cy.get('span.maybe-usable-colors-container span.usable-colors-button[data-cy-colors="4"]').rightclick()
    cy.get('.color').eq(9).click()
    notBusy()
    cy.get('sel-blot[data-sel="4"]').should('have.css', 'background-color', 'rgb(99, 47, 43)')
    cy.get('span.maybe-usable-colors-container span.usable-colors-button[data-cy-colors="4"]').should('have.css', 'background-color', 'rgb(99, 47, 43)')
    cy.get('button[data-cy="format-color-4"] > span').should('have.css', 'background-color', 'rgb(99, 47, 43)')
    cy.get('span:contains("verbes")').last().should('have.css', 'background-color', 'rgb(99, 47, 43)')
    cy.get('span:contains("Afrique")').first().click()
    cy.get('span:contains("Afrique")').first().click()
    cy.get('span:contains("Afrique")').first().click()
    cy.get('span:contains("Afrique")').first().click()
    cy.get('span:contains("Afrique")').first().should('have.css', 'background-color', 'rgb(99, 47, 43)')

    cy.get('button:contains("Save then back to list")').click()
    notBusy()

    cy.get('li:contains("7 Relève") a:contains("Edit")').click()
    notBusy()

    cy.get('sel-blot[data-sel="4"]').should('have.css', 'background-color', 'rgb(99, 47, 43)')
    cy.get('span.maybe-usable-colors-container span.usable-colors-button[data-cy-colors="4"]').should('have.css', 'background-color', 'rgb(99, 47, 43)')
    cy.get('button[data-cy="format-color-4"] > span').should('have.css', 'background-color', 'rgb(99, 47, 43)')
    cy.get('span:contains("verbes")').last().should('have.css', 'background-color', 'rgb(99, 47, 43)')
    cy.get('span:contains("Afrique")').first().click()
    cy.get('span:contains("Afrique")').first().click()
    cy.get('span:contains("Afrique")').first().click()
    cy.get('span:contains("Afrique")').first().click()
    cy.get('span:contains("Afrique")').first().should('have.css', 'background-color', 'rgb(99, 47, 43)')
  })

  it('saves an exercise after changing the type of its pre-existing adaptation', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/exercise-dymwin')

    cy.get('label:contains("Adaptation type")').next().should('have.value', 'fill-with-free-text')

    cy.get('label:contains("Adaptation type")').next().select('multiple-choices')
    cy.get('label:contains("Instructions")').next().type('{selectAll}Instructions!')
    notBusy()
    cy.get('button:contains("Save then back to list")').click()
    notBusy()

    cy.get('li:contains("Instructions!"):contains("Multiple choices")').should('exist')

    visit('/project-xkopqm/textbook-klxufv/page-7/exercise-dymwin')
    cy.get('label:contains("Adaptation type")').next().should('have.value', 'multiple-choices')
    cy.get('label:contains("Instructions")').next().should('have.text', 'Instructions!')
  })

  it('throttles updates of the preview', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/exercise-vodhqn')

    cy.get('label:contains("Wording")').next().type('{selectAll}{del}', {delay: 0})
    notBusy()

    cy.intercept('POST', '/api/parsedExercises', req => req.on('response', res => { res.delay = 300 })).as('parsedExercises')
    for (let i = 0; i !== 20; i += 1) {
      cy.get('label:contains("Wording")').next().type(' a', {delay: 0})
    }
    notBusy()

    cy.get('@parsedExercises.all').its('length').should('be.lessThan', 15)
  })

  it('edits MCQ choices - at the right end of the choices2 blot', () => {
    cy.viewport(1200, 800)
    visit('/project-xkopqm/textbook-klxufv/page-7/exercise-xnyegk')

    cy.get('label:contains("Instructions") + .ql-container > .ql-editor').click().type('{end}{leftArrow}blah')
    cy.get('choices2-blot:contains("vrai ou fauxblah")').should('exist')
  })

  it('edits MCQ choices - at the left end of the choices2 blot', () => {
    cy.viewport(1200, 800)
    visit('/project-xkopqm/textbook-klxufv/page-7/exercise-xnyegk')

    cy.get('label:contains("Instructions") + .ql-container > .ql-editor').click().type('{end}{leftArrow}{leftArrow}{leftArrow}{leftArrow}{leftArrow}{leftArrow}{leftArrow}{leftArrow}{leftArrow}{leftArrow}{leftArrow}{leftArrow}{leftArrow}blah')
    cy.get('choices2-blot:contains("blahvrai ou faux")').should('exist')
  })
})
