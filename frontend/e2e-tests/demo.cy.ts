import { loadFixtures, loadPdf, login, notBusy, traceRectangle, visit } from "./utils"


describe('Gabby', () => {
  before(() => {
    console.clear()
  })

  beforeEach(() => {
    login()
  })

  it('creates a project with the demo PDF as a textbook', () => {
    loadFixtures('admin-user')
    visit('/')

    cy.get('label:contains("Title") + input').type('Demo', {delay: 0})
    cy.get('label:contains("Description") + textarea').type('Demonstration of all the supported types of exercice adaptations.', {delay: 0})

    cy.get('button:contains("Create project")').click()

    cy.location('pathname').should('equal', '/project-xkopqm')

    loadPdf('demo')

    cy.get('label:contains("Title") + input').type('Demo', {delay: 0})
    cy.get('label:contains("Publisher") + input').type('Gabby', {delay: 0})
    cy.get('label:contains("Year") + input').type('2024', {delay: 0})
    cy.get('label:contains("ISBN") + input').type('9783161484100', {delay: 0})

    cy.get('button:contains("Create textbook")').click()

    cy.location('pathname').should('equal', '/project-xkopqm/textbook-klxufv/page-1')
  })

  function setupAliases() {
    cy.get('canvas').last().as('canvas')
    cy.get('label:contains("Number") + input').as('number')
    cy.get('label:contains("Adaptation type") + select').as('adaptationType')
    cy.get('label:contains("Instructions") + div.ql-container div.ql-editor').as('instructions')
  }

  function selectRange(startNode: Node, startOffset: number, endNode: Node, endOffset: number) {
    cy.window().then(window => {
      cy.document().then(document => {
        var range = document.createRange()
        range.setStart(startNode, startOffset)
        range.setEnd(endNode, endOffset)

        var sel = window.getSelection()
        console.assert(sel !== null)
        sel.removeAllRanges()
        sel.addRange(range)
      })
    })
  }

  function screenshot(name: string) {
    cy.window().then(window => {
      var sel = window.getSelection()
      console.assert(sel !== null)
      sel.removeAllRanges()
    })
    cy.focused().blur()
    cy.screenshot(name)
  }

  it('drafts a "Select words" exercise', () => {
    cy.viewport(1200, 1200)
    visit('/project-xkopqm/textbook-klxufv/page-2/new-exercise', {pdf: 'demo'})
    setupAliases()

    cy.get('@adaptationType').select('selectThingsAdaptation').blur()
    cy.get('label:contains("Number of colors") + input').type('{selectAll}2', {delay: 0})

    traceRectangle('@canvas', 8, 5, 60, 9)
    cy.get('button:contains("Instructions")').click()
    notBusy()
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 39, node, 51)
    })
    cy.get('button:contains("2")').click()
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 25, node, 31)
    })
    cy.get('button:contains("1")').click()
    notBusy()

    traceRectangle('@canvas', 7, 9.5, 92, 19)
    cy.get('button:contains("Wording")').click()
    notBusy()

    screenshot('select-words')
  })

  it('drafts a "Multiple choices (in instructions)" exercise', () => {
    cy.viewport(1200, 850)
    visit('/project-xkopqm/textbook-klxufv/page-3/new-exercise', {pdf: 'demo'})
    setupAliases()

    cy.get('@adaptationType').select('multipleChoicesInInstructionsAdaptation').blur()
    cy.get('label:contains("Placeholder") + input').type('{selectAll}...', {delay: 0})

    traceRectangle('@canvas', 8, 5, 48, 9)
    cy.get('button:contains("Instructions")').click()
    notBusy()
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 30, node, 37)
    })
    cy.get('button:contains("Choice")').click()
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 21, node, 26)
    })
    cy.get('button:contains("Choice")').click()
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 14, node, 19)
    })
    cy.get('button:contains("Choice")').click()

    traceRectangle('@canvas', 7, 9.5, 62, 13)
    cy.get('button:contains("Wording")').click()
    notBusy()

    screenshot('multiple-choices-in-instructions')
  })

  it('drafts a "Fill with free text" exercise', () => {
    cy.viewport(1200, 850)
    visit('/project-xkopqm/textbook-klxufv/page-4/new-exercise', {pdf: 'demo'})
    setupAliases()

    cy.get('@adaptationType').select('fillWithFreeTextAdaptation').blur()
    cy.get('label:contains("Placeholder") + input').type('{selectAll}…', {delay: 0})

    traceRectangle('@canvas', 8, 5, 60, 9)
    cy.get('button:contains("Instructions")').click()

    traceRectangle('@canvas', 7, 9.5, 48, 13)
    cy.get('button:contains("Wording")').click()
    notBusy()

    screenshot('fill-with-free-text')
  })
})
