import { loadFixtures, loadPdf, login, notBusy, traceRectangle, visit } from "./utils"


describe('Gabby', () => {
  before(() => {
    console.clear()
  })

  beforeEach(() => {
    login()
    loadFixtures('empty-demo-textbook')
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

  function screenshot(testName: string, screenshotName: string) {
    cy.window().then(window => {
      var sel = window.getSelection()
      console.assert(sel !== null)
      sel.removeAllRanges()
    })
    cy.screenshot(`${testName}--${screenshotName}`)
  }

  it('creates a "Select words" exercise', () => {
    cy.viewport(1200, 1200)
    visit('/project-xkopqm/textbook-klxufv/page-2/new-exercise', {pdf: 'demo'})
    setupAliases()

    cy.get('@number').type('1')

    cy.get('@adaptationType').select('select-things').blur()
    cy.get('span.maybe-usable-colors-container span.usable-colors-button[data-cy-colors="2"]').click()

    traceRectangle('@canvas', 8, 5, 60, 9)
    cy.get('button:contains("Instructions")').click()
    notBusy()
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 39, node, 51)
    })
    cy.get('button[data-cy="format-color-2"]').click()
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 25, node, 31)
    })
    cy.get('button[data-cy="format-color-1"]').click()
    notBusy()

    traceRectangle('@canvas', 7, 9.5, 92, 19)
    cy.get('button:contains("Wording")').click()
    notBusy()

    cy.focused().blur()
    screenshot('select-words', 'edit-1')

    cy.get('button:contains("Save then back")').click()
    visit('/project-xkopqm')
    cy.get('a:contains("the exported HTML")').should('have.attr', 'href').then(url => {
      cy.visit(url + '&download=false')
      cy.get('a').click()
      screenshot('select-words', 'export-1')
      cy.get('span[data-cy=selectable]').eq(5).click()
      cy.get('span[data-cy=selectable]').eq(7).click()
      cy.get('span[data-cy=selectable]').eq(7).click()
      screenshot('select-words', 'export-2')
    })
  })

  it('creates a "Select words" exercise with custom colors', () => {
    cy.viewport(1200, 1000)
    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise', {pdf: 'demo'})
    setupAliases()

    cy.get('@number').type('1')

    cy.get('@adaptationType').select('select-things').blur()
    cy.get('span.maybe-usable-colors-container span.usable-colors-button[data-cy-colors="2"]').click()

    traceRectangle('@canvas', 8, 5, 60, 9)
    cy.get('button:contains("Instructions")').click()
    notBusy()

    cy.get('span.maybe-usable-colors-container span.usable-colors-button[data-cy-colors="1"]').rightclick()
    cy.get('.picker-hue-range-slider').invoke('val', 320).trigger('input')
    cy.get('button:contains("OK")').click()
    cy.get('span.maybe-usable-colors-container span.usable-colors-button[data-cy-colors="2"]').rightclick()
    cy.get('.picker-hue-range-slider').invoke('val', 180).trigger('input')
    cy.get('.colour-area-mask').click(240, 10)
    cy.get('button:contains("OK")').click()
    notBusy()

    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 49, node, 58)
    })
    cy.get('button[data-cy="format-color-2"]').click()
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 24, node, 29)
    })
    cy.get('button[data-cy="format-color-1"]').click()
    notBusy()

    traceRectangle('@canvas', 7, 9.25, 92, 18)
    cy.get('button:contains("Wording")').click()
    notBusy()

    cy.focused().blur()
    screenshot('select-words-with-custom-colors', 'edit-1')

    cy.get('button:contains("Save then back")').click()
    visit('/project-xkopqm')
    cy.get('a:contains("the exported HTML")').should('have.attr', 'href').then(url => {
      cy.visit(url + '&download=false')
      cy.get('a').click()
      screenshot('select-words-with-custom-colors', 'export-1')
      cy.get('span[data-cy=selectable]').eq(5).click()
      cy.get('span[data-cy=selectable]').eq(7).click()
      cy.get('span[data-cy=selectable]').eq(7).click()
      screenshot('select-words-with-custom-colors', 'export-2')
    })
  })

  it('creates a "Multiple choices (in instructions)" exercise', () => {
    cy.viewport(1200, 850)
    visit('/project-xkopqm/textbook-klxufv/page-3/new-exercise', {pdf: 'demo'})
    setupAliases()

    cy.get('@number').type('1')

    cy.get('@adaptationType').select('multiple-choices-in-instructions').blur()
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

    cy.focused().blur()
    screenshot('multiple-choices-in-instructions', 'edit-1')

    cy.get('button:contains("Save then back")').click()
    visit('/project-xkopqm')
    cy.get('a:contains("the exported HTML")').should('have.attr', 'href').then(url => {
      cy.visit(url + '&download=false')
      cy.get('a').click()
      screenshot('multiple-choices-in-instructions', 'export-1')
      cy.get('span.main').eq(1).click()
      screenshot('multiple-choices-in-instructions', 'export-2')
      cy.get('span.choice0').click()
      screenshot('multiple-choices-in-instructions', 'export-3')
    })
  })

  it('creates a "Fill with free text" exercise', () => {
    cy.viewport(1200, 850)
    visit('/project-xkopqm/textbook-klxufv/page-4/new-exercise', {pdf: 'demo'})
    setupAliases()

    cy.get('@number').type('1')

    cy.get('@adaptationType').select('fill-with-free-text').blur()
    cy.get('label:contains("Placeholder") + input').type('{selectAll}…', {delay: 0})

    traceRectangle('@canvas', 8, 5, 60, 9)
    cy.get('button:contains("Instructions")').click()

    traceRectangle('@canvas', 7, 9.5, 48, 13)
    cy.get('button:contains("Wording")').click()
    notBusy()

    cy.focused().blur()
    screenshot('fill-with-free-text', 'edit-1')

    cy.get('button:contains("Save then back")').click()
    visit('/project-xkopqm')
    cy.get('a:contains("the exported HTML")').should('have.attr', 'href').then(url => {
      cy.visit(url + '&download=false')
      cy.get('a').click()
      screenshot('fill-with-free-text', 'export-1')
      cy.get('[contenteditable]').eq(1).type('coureuse')
      screenshot('fill-with-free-text', 'export-2')
    })
  })
})
