import { loadFixtures, login, notBusy, visit } from './utils'


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

    for (const adaptationType of ['-', 'fill-with-free-text', 'multiple-choices']) {
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

  it('enables the "Sel" buttons', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')
    setAliases()
    cy.get('@number').type('test')
    cy.get('@adaptationType').select('generic')
    cy.get('div:contains("Words") >input').check()
    cy.get('div:contains("Selectable") >input').check()
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

  it('remove "sel" blots when the number of usable colors is reduced', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')
    setAliases()

    cy.get('div:contains("Words") >input').check()
    cy.get('span.maybe-usable-colors-container span.usable-colors-button[data-cy-colors="4"]').click()
    cy.get('button[data-cy="format-color-1"]').as("button1").should('be.disabled')
    cy.get('button[data-cy="format-color-2"]').as("button2").should('be.disabled')
    cy.get('button[data-cy="format-color-3"]').as("button3").should('be.disabled')
    cy.get('button[data-cy="format-color-4"]').as("button4").should('be.disabled')

    cy.get('@instructions').click()
    cy.get('@instructions').type('plain ', {delay: 0})
    cy.get('@button1').click()
    cy.get('@instructions').type('sel1', {delay: 0})
    cy.get('@button1').click()
    cy.get('@instructions').type(' plain ', {delay: 0})
    cy.get('@button2').click()
    cy.get('@instructions').type('sel2', {delay: 0})
    cy.get('@button2').click()
    cy.get('@instructions').type(' plain ', {delay: 0})
    cy.get('@button3').click()
    cy.get('@instructions').type('sel3', {delay: 0})
    cy.get('@button3').click()
    cy.get('@instructions').type(' plain ', {delay: 0})
    cy.get('@button4').click()
    cy.get('@instructions').type('sel4', {delay: 0})
    cy.get('@button4').click()
    cy.get('@instructions').type(' plain', {delay: 0})

    cy.get('sel-blot[data-sel="1"]').should('exist')
    cy.get('sel-blot[data-sel="2"]').should('exist')
    cy.get('sel-blot[data-sel="3"]').should('exist')
    cy.get('sel-blot[data-sel="4"]').should('exist')

    cy.get('span.maybe-usable-colors-container span.usable-colors-button[data-cy-colors="3"]').click()

    cy.get('sel-blot[data-sel="1"]').should('exist')
    cy.get('sel-blot[data-sel="2"]').should('exist')
    cy.get('sel-blot[data-sel="3"]').should('exist')
    cy.get('sel-blot[data-sel="4"]').should('not.exist')

    cy.get('span.maybe-usable-colors-container span.usable-colors-button[data-cy-colors="4"]').click()

    cy.get('sel-blot[data-sel="1"]').should('exist')
    cy.get('sel-blot[data-sel="2"]').should('exist')
    cy.get('sel-blot[data-sel="3"]').should('exist')
    cy.get('sel-blot[data-sel="4"]').should('not.exist')
  })
})
