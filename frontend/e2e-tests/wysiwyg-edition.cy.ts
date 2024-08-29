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

  cy.get('button[data-cy="format-bold"]').as('bold')
  cy.get('button[data-cy="format-italic"]').as('italic')
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
        cy.get(fieldAlias).click().type('{selectAll}plain', {delay: 0})
        cy.get('@bold').click()
        cy.get(fieldAlias).type('bold', {delay: 0})
        cy.get('@italic').click()
        cy.get(fieldAlias).type('italic', {delay: 0})

        cy.get(fieldAlias).should('contain.text', 'plainbolditalic')
        cy.get('bold-blot:contains("bold")').should('exist')
        cy.get('italic-blot:contains("italic")').should('exist')
        notBusy()
        cy.get(fieldAlias).should('contain.text', 'plainbolditalic')
        cy.get('bold-blot:contains("bold")').should('exist')
        cy.get('italic-blot:contains("italic")').should('exist')
        // cy.get('div:has(>h1:contains("Adapted exercise"))').its('length').should('eq', 1)
        cy.get('div:has(>h1:contains("Adapted exercise")) i:contains("italic")').should('exist')
        cy.get('div:has(>h1:contains("Adapted exercise")) b:contains("bold")').should('exist')

        cy.get(fieldAlias).type('{selectAll}X', {delay: 0})

        cy.get(fieldAlias).should('contain.text', 'X')
        cy.get('bold-blot:contains("bold")').should('not.exist')
        cy.get('italic-blot:contains("italic")').should('not.exist')
        notBusy()
        cy.get(fieldAlias).should('contain.text', 'X')
        cy.get('bold-blot:contains("bold")').should('not.exist')
        cy.get('italic-blot:contains("italic")').should('not.exist')
        cy.get('div:has(>h1:contains("Adapted exercise")) i:contains("italic")').should('not.exist')
        cy.get('div:has(>h1:contains("Adapted exercise")) b:contains("bold")').should('not.exist')
      }
    }
  })

  it('enables the "Choice" button', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')
    setAliases()
    cy.get('@number').type('test')
    cy.get('@adaptationType').select('multipleChoicesInInstructionsAdaptation')

    cy.get('button[data-cy="format-choice"]').should('be.disabled')

    cy.get('@instructions').click()
    cy.get('button[data-cy="format-choice"]').should('be.enabled')
    cy.get('@instructions').type('plain')
    cy.get('button[data-cy="format-choice"]').click()
    cy.get('@instructions').type('choice')
    cy.get('choice-blot:contains("choice")').should('exist')
    cy.get('@number').focus()
    cy.get('button[data-cy="format-choice"]').should('be.disabled')

    cy.get('@wording').click()
    cy.get('button[data-cy="format-choice"]').should('be.disabled')

    cy.get('@exampleHeader').click()
    cy.get('@example').should('exist')
    cy.get('button[data-cy="format-choice"]').should('be.disabled')

    cy.get('@clueHeader').click()
    cy.get('@clue').should('exist')
    cy.get('button[data-cy="format-choice"]').should('be.disabled')
  })

  it('enables the "Sel" buttons', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')
    setAliases()
    cy.get('@number').type('test')
    cy.get('@adaptationType').select('selectThingsAdaptation')
    cy.get('span.maybe-usable-colors-container span.usable-colors-button[data-cy-colors="2"]').click()

    cy.get('button[data-cy="format-color-1"]').as("button1").should('be.disabled')
    cy.get('button[data-cy="format-color-2"]').as("button2").should('be.disabled')
    cy.get('button[data-cy="format-color-3"]').should('not.exist')

    cy.get('@instructions').click()
    cy.get('@button1').should('be.enabled')
    cy.get('@button2').should('be.enabled')
    cy.get('@instructions').type('plain')
    cy.get('@button1').click()
    cy.get('@instructions').type('sel1')
    cy.get('@button2').click()
    cy.get('@instructions').type('sel2')
    cy.get('sel-blot[data-sel="1"]:contains("sel1")').should('exist')
    cy.get('sel-blot[data-sel="2"]:contains("sel2")').should('exist')
    cy.get('@instructions').type('{selectAll}{del}')
    cy.get('sel-blot').should('not.exist')

    cy.get('@wording').click()
    cy.get('@button1').should('be.disabled')
    cy.get('@button2').should('be.disabled')

    cy.get('@exampleHeader').click()
    cy.get('@button1').should('be.enabled')
    cy.get('@button2').should('be.enabled')
    cy.get('@example').type('plain')
    cy.get('@button1').click()
    cy.get('@example').type('sel1')
    cy.get('@button2').click()
    cy.get('@example').type('sel2')
    cy.get('sel-blot[data-sel="1"]:contains("sel1")').should('exist')
    cy.get('sel-blot[data-sel="2"]:contains("sel2")').should('exist')
    cy.get('@example').type('{selectAll}{del}')
    cy.get('sel-blot').should('not.exist')

    cy.get('@clueHeader').click()
    cy.get('@button1').should('be.enabled')
    cy.get('@button2').should('be.enabled')
    cy.get('@clue').type('plain')
    cy.get('@button1').click()
    cy.get('@clue').type('sel1')
    cy.get('@button2').click()
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
    cy.get('button[data-cy="format-choice"]').click()
    cy.get('@instructions').type('vrai')
    cy.get('button[data-cy="format-choice"]').click()
    cy.get('@instructions').type(' ou ')
    cy.get('button[data-cy="format-choice"]').click()
    cy.get('@instructions').type('faux')

    cy.get('choice-blot').should('have.length', 2)

    cy.get('button:contains("Save then back to list")').click()

    cy.get('li:contains("Choix : {choice|vrai} ou")').should('exist')
  })
})
