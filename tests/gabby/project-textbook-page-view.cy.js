import { useApiStore } from '../../frontend/src/frontend/stores/api'


const isProdPreview = Cypress.env('IS_PROD_PREVIEW')

function setLocale(locale = 'en') {
  cy.get('select[data-cy="language"]').last().select(locale)
}

describe('Gabby\'s project\'s textbook page view', () => {
  before(console.clear)

  beforeEach(() => {
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=admin-user,test-exercises')
    cy.wrap(useApiStore()).then(api => api.auth.login('admin', 'password'))
  })

  it('displays an error message if the project does not exist', () => {
    cy.visit('/project-nope/textbook-klxufv/page-6')
    setLocale()
    cy.get('div.busy').should('not.exist')

    cy.get('h1:contains("Project not found")').should('exist')
    cy.title().should('eq', 'MALIN - Project not found')
  })

  it('displays an error message if the textbook does not exist', () => {
    cy.visit('/project-xkopqm/textbook-nope/page-6')
    setLocale()
    cy.get('div.busy').should('not.exist')

    cy.get('h1:contains("Textbook not found")').should('exist')
    cy.title().should('eq', 'MALIN - Premier projet de test - Textbook not found')
  })

  it('displays an error message if the textbook does not belong to this project', () => {
    cy.visit('/project-fryrbl/textbook-klxufv/page-6')
    setLocale()
    cy.get('div.busy').should('not.exist')

    cy.get('h1:contains("Textbook not found")').should('exist')
    cy.title().should('eq', 'MALIN - Deuxième projet de test - Textbook not found')
  })

  // @todo Add test where the page is a negative number
  // @todo Add test where the page is larger than the textbook's number of pages
  // @todo Add test where the page is not a number

  it('lands', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-6')
    setLocale()

    cy.title().should('eq', 'MALIN - Premier projet de test - Français CE2 - Page 6')
    cy.get('.navbar').should('contain', 'Premier projet de test')
    cy.get('.navbar').should('contain', 'Français CE2')
  })

  it('adjusts textarea heights', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-6/new-exercise')
    setLocale()

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

  it('navigates the textbook', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-6')
    setLocale()
    cy.get('p:contains("Page"):contains("(on 7)") input').should('have.value', '6')
    cy.get('p:contains("The PDF that contains this page (test.pdf) has not been loaded yet.")').should('exist')

    cy.get('p:contains("Page"):contains("(on 7)") :contains(">")').click()
    cy.get('p:contains("Page"):contains("(on 7)") input').should('have.value', '7')
    cy.url().should('eq', `${Cypress.config().baseUrl}project-xkopqm/textbook-klxufv/page-7`)
    cy.get('p:contains("Page"):contains("(on 7)") :contains(">")').should('be.disabled')
    cy.get('p:contains("The PDF that contains this page (test.pdf) has not been loaded yet.")').should('exist')

    cy.get('p:contains("Page"):contains("(on 7)") :contains("<")').click()
    cy.get('p:contains("Page"):contains("(on 7)") :contains(">")').should('be.enabled')

    cy.get('p:contains("Page"):contains("(on 7)") :contains("<")').click()
    cy.get('p:contains("Page"):contains("(on 7)") input').should('have.value', '5')
    cy.url().should('eq', `${Cypress.config().baseUrl}project-xkopqm/textbook-klxufv/page-5`)
    cy.get('p:contains("No known PDF contains this page.")').should('exist')
    cy.get('p:contains("The PDF that contains this page (test.pdf) has not been loaded yet.")').should('not.exist')

    cy.get('p:contains("Page"):contains("(on 7)") input').clear().type('1')
    cy.url().should('eq', `${Cypress.config().baseUrl}project-xkopqm/textbook-klxufv/page-1`)
    cy.get('p:contains("Page"):contains("(on 7)") :contains("<")').should('be.disabled')
    cy.get('p:contains("No known PDF contains this page.")').should('exist')

    cy.get('p:contains("Page"):contains("(on 7)") input').clear().type('100').blur()
    cy.get('div.busy').should('not.exist')
    cy.get('p:contains("Page"):contains("(on 7)") input').should('have.value', '1')
    cy.url().should('eq', `${Cypress.config().baseUrl}project-xkopqm/textbook-klxufv/page-1`)

    cy.get('p:contains("Page"):contains("(on 7)") input').clear().type('200').blur()
    cy.get('div.busy').should('not.exist')
    cy.get('p:contains("Page"):contains("(on 7)") input').should('have.value', '2')
    cy.url().should('eq', `${Cypress.config().baseUrl}project-xkopqm/textbook-klxufv/page-2`)
  })

  it('enables the "Save exercise" button', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-6/new-exercise')
    setLocale()

    cy.get('button:contains("Save then next")').should('be.disabled')

    cy.get('label:contains("Number")').next().type('1')
    cy.get('button:contains("Save then next")').should('be.enabled')

    cy.get('label:contains("Number")').next().clear()
    cy.get('button:contains("Save then next")').should('be.disabled')

    cy.get('label:contains("Number")').next().type('A')
    cy.get('button:contains("Save then next")').should('be.enabled')
  })

  it('lists existing exercises', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-7')
    setLocale()
    cy.get('button:contains("Delete")').click()
    cy.get('div.busy').should('not.exist')
    cy.get('p:contains("No exercises yet.")').should('exist')

    cy.visit('/project-xkopqm/textbook-klxufv/page-7')
    setLocale()
    cy.get('div.busy').should('not.exist')
    cy.get('p:contains("No exercises yet.")').should('exist')

    cy.get('button:contains("<")').click()
    cy.get('li:contains("3 Complète avec : le, une, …")').should('exist')
    cy.get('li:contains("4 Écris une phrase en respe…")').should('exist')
  })

  it('loads a PDF', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-6')
    setLocale()
    cy.get('div.busy').should('not.exist')
    cy.get('p:contains("The PDF that contains this page (test.pdf) has not been loaded yet.")').should('exist')

    cy.get('input[type=file]').selectFile('../pdf-examples/test.pdf')
    cy.get('div.busy').should('not.exist')
    cy.get('p:contains("The PDF that contains this page (test.pdf) has not been loaded yet.")').should('not.exist')
    cy.get('input[type=file]').should('not.exist')
  })

  it('creates a minimal exercise', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-6/new-exercise')
    setLocale()

    cy.get('label:contains("Number")').next().type('1')
    cy.get('button:contains("Save then next")').click()
    cy.get('div.busy').should('not.exist')

    cy.get('label:contains("Number")').next().should('have.value', '2')

    cy.get('a:contains("Back to list (without saving)")').click()
    cy.get('div.busy').should('not.exist')
    cy.get('li:contains("1")').should('exist')
  })

  it('creates a full exercise', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-6/new-exercise')
    setLocale()

    cy.get('label:contains("Number")').next().type('Défis')
    cy.get('label:contains("Instructions")').next().type('Do the smartest thing ever.')
    cy.get('label:contains("Wording")').next().type('The wording of this exercise is a bit longer in a quite artificial way.')
    cy.get('p:contains("Example")').click()
    cy.focused().type('The example')
    cy.get('p:contains("Clue")').click()
    cy.focused().type('The clue')

    cy.get('label:contains("Adaptation type")').next().select('selectThingsAdaptation')
    cy.get('label:contains("Number of colors")').next().type('{selectAll}2')

    cy.get('span:contains("artificial")').last().click()
    cy.get('span:contains("artificial")').last().should('have.css', 'background-color', 'rgb(255, 255, 0)')
    cy.get('span:contains("artificial")').last().click()
    cy.get('span:contains("artificial")').last().should('have.css', 'background-color', 'rgb(255, 192, 203)')
    cy.get('span:contains("artificial")').last().click()
    cy.get('span:contains("artificial")').last().should('have.css', 'background-color', 'rgba(0, 0, 0, 0)')

    cy.get('button:contains("Save then next")').click()
    cy.get('div.busy').should('not.exist')

    cy.get('label:contains("Number")').next().should('have.value', '')

    cy.get('a:contains("Back to list (without saving)")').click()
    cy.get('div.busy').should('not.exist')
    cy.get('li:contains("Défis")').should('exist')
  })

  const prevWidth = 309
  const prevHeight = 436
  const newWidth = 322
  const newHeight = 454
  const xRatio = newWidth / prevWidth
  const yRatio = newHeight / prevHeight

  // @todo Add test showing we can delete and recreate an exercise (hunt possible bug in deletion)

  it('shows and hides the section editor dialog', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-6')
    setLocale('fr')
    cy.get('div.busy').should('not.exist')

    cy.get('h1').contains('Lien entre PDF et manuel').should('not.exist')

    cy.get('button').contains('⚙').click()
    cy.get('h1').contains('Lien entre PDF et manuel').should('exist')

    cy.get('button').contains('Annuler').click()
    cy.get('h1').contains('Lien entre PDF et manuel').should('not.exist')
  })

  it('detects when an exercise already exists', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-6/new-exercise')
    setLocale()
    cy.get('div.busy').should('not.exist')

    cy.get('label:contains("Number")').next().type('2')
    cy.get('button:contains("Save then next")').click()
    cy.get('div.busy').should('not.exist')

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

  it('allows navigating the PDF when creating an exercise', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-6/new-exercise')
    setLocale()
    cy.get('input[type=file]').selectFile('../pdf-examples/test.pdf')
    cy.get('div.busy').should('not.exist')

    cy.get('label:contains("Number")').next().type('5')

    cy.get('p:contains("Page"):contains("(on 7)") :contains(">")').click()
    cy.url().should('eq', `${Cypress.config().baseUrl}project-xkopqm/textbook-klxufv/page-7/new-exercise`)
    cy.get('label:contains("Number")').next().should('have.value', '5')

    cy.get('button:contains("Save then next")').click()
    cy.get('div.busy').should('not.exist')
    cy.get('a:contains("Back to list (without saving)")').click()

    cy.get('div.busy').should('not.exist')
    cy.url().should('eq', `${Cypress.config().baseUrl}project-xkopqm/textbook-klxufv/page-7`)
    cy.get('li:contains("5")').should('exist')
  })

  it('resets responses when changing adaptation type', () => {
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=admin-user,more-test-exercises')
    cy.viewport(1000, 1100)

    cy.visit('/project-xkopqm/textbook-klxufv/page-7/exercise-dymwin')
    setLocale()
    cy.get('label:contains("Number")').next().should('have.value', '11')
    cy.get('div.busy').should('not.exist')

    cy.get('span[contenteditable]').first().type('Abcd')

    cy.get('label:contains("Adaptation type")').next().select('selectThingsAdaptation')
    cy.get('div.busy').should('not.exist')

    cy.get('span:contains("tracter")').eq(1).click()
    cy.get('span:contains("tracter")').eq(1).should('have.css', 'background-color', 'rgb(255, 255, 0)')

    cy.get('label:contains("Adaptation type")').next().select('fillWithFreeTextAdaptation')
    cy.get('div.busy').should('not.exist')

    cy.get('span[contenteditable]').first().should('have.value', '')

    cy.get('label:contains("Adaptation type")').next().select('selectThingsAdaptation')
    cy.get('div.busy').should('not.exist')

    cy.get('span:contains("tracter")').eq(1).should('have.css', 'background-color', 'rgba(0, 0, 0, 0)')
  })
})
