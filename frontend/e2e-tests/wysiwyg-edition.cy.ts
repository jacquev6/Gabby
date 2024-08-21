import { loadFixtures, login, notBusy, visit as visit } from './utils'


function setAliases() {
  cy.get('label:contains("Number") + input').as('number')
  cy.get('label:contains("Adaptation type") + select').as('adaptationType')
  cy.get('label:contains("Instructions") + .ql-container > .ql-editor').as('instructions')
  cy.get('label:contains("Wording") + .ql-container > .ql-editor').as('wording')
  cy.get('p:contains("Example")').as('exampleHeader')
  cy.get('@exampleHeader').click()
  cy.get('label:contains("Example") + .ql-container > .ql-editor').as('example')
  cy.get('p:contains("Clue")').as('clueHeader')
  cy.get('@clueHeader').click()
  cy.get('label:contains("Clue") + .ql-container > .ql-editor').as('clue')
  cy.get('@number').focus().blur()

  cy.get('button:contains("Bold")').as('bold')
  cy.get('button:contains("Italic")').as('italic')
}

describe('Gabby', () => {
  before(console.clear)

  beforeEach(() => {
    loadFixtures('more-test-exercises')
    login()
    cy.viewport(1000, 1000)
  })

  it('enables basic formatting buttons', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')
    setAliases()

    cy.get('@bold').should('be.disabled')
    cy.get('@italic').should('be.disabled')

    cy.get('@instructions').click()
    cy.get('@bold').should('be.enabled')
    cy.get('@italic').should('be.enabled')
    cy.get('@number').focus()
    cy.get('@bold').should('be.disabled')
    cy.get('@italic').should('be.disabled')

    cy.get('@wording').click()
    cy.get('@bold').should('be.enabled')
    cy.get('@italic').should('be.enabled')
    cy.get('@number').focus()
    cy.get('@bold').should('be.disabled')
    cy.get('@italic').should('be.disabled')

    cy.get('@exampleHeader').click()
    cy.get('@example').should('exist')
    cy.get('@bold').should('be.enabled')
    cy.get('@italic').should('be.enabled')
    cy.get('@number').focus()
    cy.get('@bold').should('be.disabled')
    cy.get('@italic').should('be.disabled')

    cy.get('@clueHeader').click()
    cy.get('@clue').should('exist')
    cy.get('@bold').should('be.enabled')
    cy.get('@italic').should('be.enabled')
    cy.get('@number').focus()
    cy.get('@bold').should('be.disabled')
    cy.get('@italic').should('be.disabled')
  })

  it('allows bold and italic in all fields for all adaptation types', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')
    setAliases()
    cy.get('@number').type('test')
    cy.get('@exampleHeader').click()
    cy.get('@example').type('X')
    cy.get('@clueHeader').click()
    cy.get('@clue').type('X')

    for (const adaptationType of ['-', 'selectThingsAdaptation', 'fillWithFreeTextAdaptation', 'multipleChoicesInInstructionsAdaptation']) {
      cy.get('@adaptationType').select(adaptationType)

      for (const fieldAlias of ['@instructions', '@wording', '@example', '@clue']) {
        cy.get(fieldAlias).click().type('plain')
        cy.get('@bold').click()
        cy.get(fieldAlias).type('bold')
        cy.get('@italic').click()
        cy.get(fieldAlias).type('italic')

        cy.get('bold-blot:contains("bold")').should('exist')
        cy.get('italic-blot:contains("italic")').should('exist')

        cy.get(fieldAlias).type('{selectAll}{del}X')

        cy.get('bold-blot:contains("bold")').should('not.exist')
        cy.get('italic-blot:contains("italic")').should('not.exist')
      }
    }
  })

  it('enables the "Choice" button', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')
    setAliases()
    cy.get('@number').type('test')
    cy.get('@adaptationType').select('multipleChoicesInInstructionsAdaptation')

    cy.get('button:contains("Choice")').should('be.disabled')

    cy.get('@instructions').click()
    cy.get('button:contains("Choice")').should('be.enabled')
    cy.get('@instructions').type('plain')
    cy.get('button:contains("Choice")').click()
    cy.get('@instructions').type('choice')
    cy.get('choice-blot:contains("choice")').should('exist')
    cy.get('@number').focus()
    cy.get('button:contains("Choice")').should('be.disabled')

    cy.get('@wording').click()
    cy.get('button:contains("Choice")').should('be.disabled')

    cy.get('@exampleHeader').click()
    cy.get('@example').should('exist')
    cy.get('button:contains("Choice")').should('be.disabled')

    cy.get('@clueHeader').click()
    cy.get('@clue').should('exist')
    cy.get('button:contains("Choice")').should('be.disabled')
  })

  it('enables the "Sel" buttons', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')
    setAliases()
    cy.get('@number').type('test')
    cy.get('@adaptationType').select('selectThingsAdaptation')
    cy.get('label:contains("Number of colors") + input').type('{selectAll}2')

    cy.get('button:contains("1")').should('be.disabled')
    cy.get('button:contains("2")').should('be.disabled')
    cy.get('button:contains("3")').should('not.exist')

    cy.get('@instructions').click()
    cy.get('button:contains("1")').should('be.enabled')
    cy.get('button:contains("2")').should('be.enabled')
    cy.get('@instructions').type('plain')
    cy.get('button:contains("1")').click()
    cy.get('@instructions').type('sel1')
    cy.get('button:contains("2")').click()
    cy.get('@instructions').type('sel2')
    cy.get('sel-blot[data-sel="1"]:contains("sel1")').should('exist')
    cy.get('sel-blot[data-sel="2"]:contains("sel2")').should('exist')
    cy.get('@instructions').type('{selectAll}{del}')
    cy.get('sel-blot').should('not.exist')

    cy.get('@wording').click()
    cy.get('button:contains("1")').should('be.disabled')
    cy.get('button:contains("2")').should('be.disabled')

    cy.get('@exampleHeader').click()
    cy.get('button:contains("1")').should('be.enabled')
    cy.get('button:contains("2")').should('be.enabled')
    cy.get('@example').type('plain')
    cy.get('button:contains("1")').click()
    cy.get('@example').type('sel1')
    cy.get('button:contains("2")').click()
    cy.get('@example').type('sel2')
    cy.get('sel-blot[data-sel="1"]:contains("sel1")').should('exist')
    cy.get('sel-blot[data-sel="2"]:contains("sel2")').should('exist')
    cy.get('@example').type('{selectAll}{del}')
    cy.get('sel-blot').should('not.exist')

    cy.get('@clueHeader').click()
    cy.get('button:contains("1")').should('be.enabled')
    cy.get('button:contains("2")').should('be.enabled')
    cy.get('@clue').type('plain')
    cy.get('button:contains("1")').click()
    cy.get('@clue').type('sel1')
    cy.get('button:contains("2")').click()
    cy.get('@clue').type('sel2')
    cy.get('sel-blot[data-sel="1"]:contains("sel1")').should('exist')
    cy.get('sel-blot[data-sel="2"]:contains("sel2")').should('exist')
    cy.get('@clue').type('{selectAll}{del}')
    cy.get('sel-blot').should('not.exist')
  })

  it("keeps what's been typed in WYSIWYG fields regardless of the typing speed and server response time", () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/exercise-xnyegk')

    cy.intercept('POST', '/api/parsedExercises', (req) => {
      const throttle = req.body.data.attributes.instructions === "Foo\n" ? 1000 : 0
      req.on('response', (res) => { res.delay = throttle })
    })

    cy.get('label:contains("Instructions") + .ql-container .ql-editor').as('editor')

    cy.get('@editor').focus().type('{selectall}Foo')
    cy.get('@editor').focus().type('{selectall}Bar')
    cy.get('@editor').should('contain.text', 'Bar')

    notBusy()

    // The response for 'Foo' reaches the frontend after the response for 'Bar', but is discarded and 'Bar' is kept.
    cy.get('@editor').should('not.contain.text', 'Foo')
    cy.get('@editor').should('contain.text', 'Bar')
  })

  it('handles switching from non-WYSIWYG to WYSIWYG', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/exercise-jkrudc', {wysiwyg: false})

    cy.get('label:contains("Instructions")').next().type('{selectall}Réponds par {{}choice|vrai} ou {{}choice|faux}.', {delay: 0})
    cy.get('label:contains("Adaptation type")').next().select('multipleChoicesInInstructionsAdaptation')
    notBusy()

    cy.get('span:contains("WYSIWYG") input').check()

    cy.get(':has(>label:contains("Instructions")) .ql-editor').should('contain.text', 'Réponds par vrai ou faux.')
  })

  it('creates an exercise with a WYSIWYG field', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')

    cy.get('label:contains("Number")').next().type('6')
    cy.get('label:contains("Adaptation type")').next().select('multipleChoicesInInstructionsAdaptation')
    cy.get('label:contains("Instructions") + .ql-container .ql-editor').as('instructions')
    cy.get('@instructions').click().type('Choix : ')
    cy.get('button:contains("Choice")').click()
    cy.get('@instructions').type('vrai')
    cy.get('button:contains("Choice")').click()
    cy.get('@instructions').type(' ou ')
    cy.get('button:contains("Choice")').click()
    cy.get('@instructions').type('faux')

    cy.get('choice-blot').should('have.length', 2)

    cy.get('button:contains("Save then back to list")').click()

    cy.get('li:contains("Choix : {choice|vrai} ou")').should('exist')
  })
})
