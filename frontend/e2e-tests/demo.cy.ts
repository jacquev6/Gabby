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
    cy.get('label:contains("Wording") + div.ql-container div.ql-editor').as('wording')
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

  function screenshot(testName: string, screenshotName: string, options: {clearSel: boolean} = {clearSel: true}) {
    if (options.clearSel) {
      cy.window().then(window => {
        var sel = window.getSelection()
        console.assert(sel !== null)
        sel.removeAllRanges()
      })
    }
    notBusy()
    cy.screenshot(`${testName}--${screenshotName}`)
  }

  it('creates a "Select words" exercise', () => {
    cy.viewport(1200, 1200)
    visit('/project-xkopqm/textbook-klxufv/page-2/new-exercise', {pdf: 'demo'})
    setupAliases()

    cy.get('@number').type('1')

    cy.get('span.maybe-usable-colors-container span.usable-colors-button[data-cy-colors="2"]').click()
    cy.get('div:contains("Selectable") >input').should('be.checked')

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

    cy.get('span.maybe-usable-colors-container span.usable-colors-button[data-cy-colors="2"]').click()
    cy.get('div:contains("Selectable") >input').should('be.checked')

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

  it('creates a "Multiple choices" exercise with choices in instructions', () => {
    cy.viewport(1200, 1000)
    visit('/project-xkopqm/textbook-klxufv/page-3/new-exercise', {pdf: 'demo'})
    setupAliases()

    cy.get('@number').type('1')

    cy.get('@adaptationType').select('multiple-choices')

    traceRectangle('@canvas', 8, 5, 48, 9)
    cy.get('button:contains("Instructions")').click()
    notBusy()
    traceRectangle('@canvas', 7, 9.5, 62, 13)
    cy.get('button:contains("Wording")').click()
    notBusy()

    cy.get('button:contains("Multiple choices")').click()
    screenshot('multiple-choices-with-choices-in-instructions', 'edit-1')
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 14, node, 37)
    })
    cy.get('button:contains("OK")').should('exist')
    cy.get('label + input').eq(3).should('be.enabled').type('{selectAll}ou', {delay: 0})  // Very fragile selector; sorry, future me!
    cy.get('label:contains("Separator") + input').should('be.enabled').type('{selectAll},', {delay: 0})
    cy.get('label:contains("Placeholder") + input').type('...', {delay: 0})
    screenshot('multiple-choices-with-choices-in-instructions', 'edit-2', {clearSel: false})
    cy.get('button:contains("OK")').click()
    screenshot('multiple-choices-with-choices-in-instructions', 'edit-3')

    cy.get('button:contains("Save then back")').click()
    visit('/project-xkopqm')
    cy.get('a:contains("the exported HTML")').should('have.attr', 'href').then(url => {
      cy.visit(url + '&download=false')
      cy.get('a').click()
      screenshot('multiple-choices-with-choices-in-instructions', 'export-1')
      cy.get('span.main').eq(1).click()
      screenshot('multiple-choices-with-choices-in-instructions', 'export-2')
      cy.get('span.choice0').click()
      screenshot('multiple-choices-with-choices-in-instructions', 'export-3')
    })
  })

  it('creates a "Multiple choices" exercise with two sets of choices in instructions', () => {
    cy.viewport(1200, 1000)
    visit('/project-xkopqm/textbook-klxufv/page-5/new-exercise', {pdf: 'demo'})
    setupAliases()

    cy.get('@number').type('1')

    cy.get('@adaptationType').select('multiple-choices').blur()

    traceRectangle('@canvas', 8, 5, 83, 9)
    cy.get('button:contains("Instructions")').click()
    notBusy()
    traceRectangle('@canvas', 7, 9.2, 52, 12)
    cy.get('button:contains("Wording")').click()
    notBusy()

    cy.get('@wording').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 11, node, 14)
    })
    cy.get('@wording').find('p').eq(0).type(' ... @@@\n')
    cy.get('@wording').find('p').then($el => {
      const node = $el[1].firstChild
      console.assert(node !== null)
      selectRange(node, 11, node, 14)
    })
    cy.get('@wording').find('p').eq(1).type(' ... @@@\n')
    cy.get('@wording').find('p').then($el => {
      const node = $el[2].firstChild
      console.assert(node !== null)
      selectRange(node, 8, node, 11)
    })
    cy.get('@wording').find('p').eq(2).type(' ... @@@\n')
    cy.get('@wording').find('p').eq(3).type('{end} ... @@@')

    cy.get('button:contains("Multiple choices")').click()
    screenshot('multiple-choices-with-two-set-of-choices-in-instructions', 'edit-1')
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 17, node, 35)
    })
    cy.get('button:contains("OK")').should('exist')
    cy.get('label + input').eq(3).should('be.enabled').type('{selectAll}{del}', {delay: 0})  // Very fragile selector; sorry, future me!
    cy.get('label:contains("Placeholder") + input').should('be.enabled').type('...', {delay: 0})
    screenshot('multiple-choices-with-two-set-of-choices-in-instructions', 'edit-2', {clearSel: false})
    cy.get('button:contains("OK")').click()
    screenshot('multiple-choices-with-two-set-of-choices-in-instructions', 'edit-3')

    cy.get('button:contains("Multiple choices")').click()
    screenshot('multiple-choices-with-two-set-of-choices-in-instructions', 'edit-4')
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild!.nextSibling!.nextSibling
      console.assert(node !== null)
      selectRange(node, 14, node, 33)
    })
    cy.get('button:contains("OK")').should('exist')
    cy.get('label + input').eq(3).should('be.enabled').type('{selectAll}{del}', {delay: 0})  // Very fragile selector; sorry, future me!
    cy.get('label:contains("Placeholder") + input').should('be.enabled').type('@@@', {delay: 0})
    screenshot('multiple-choices-with-two-set-of-choices-in-instructions', 'edit-5', {clearSel: false})
    cy.get('button:contains("OK")').click()
    screenshot('multiple-choices-with-two-set-of-choices-in-instructions', 'edit-6')

    cy.get('button:contains("Save then back")').click()
    visit('/project-xkopqm')
    cy.get('a:contains("the exported HTML")').should('have.attr', 'href').then(url => {
      cy.visit(url + '&download=false')
      cy.get('a').click()
      screenshot('multiple-choices-with-two-set-of-choices-in-instructions', 'export-1')
      cy.get('span.main').eq(1).click()
      screenshot('multiple-choices-with-two-set-of-choices-in-instructions', 'export-2')
      cy.get('span.choice0').click()
      screenshot('multiple-choices-with-two-set-of-choices-in-instructions', 'export-3')
      cy.get('span.main').eq(2).click()
      screenshot('multiple-choices-with-two-set-of-choices-in-instructions', 'export-4')
      cy.get('span.choice0').click()
      screenshot('multiple-choices-with-two-set-of-choices-in-instructions', 'export-5')
    })
  })

  it('creates a "Multiple choices" exercise with choices in wording', () => {
    cy.viewport(1200, 1000)
    visit('/project-xkopqm/textbook-klxufv/page-6/new-exercise', {pdf: 'demo'})
    setupAliases()

    cy.get('@number').type('1')

    cy.get('@adaptationType').select('multiple-choices').blur()

    traceRectangle('@canvas', 8, 5, 54, 9)
    cy.get('button:contains("Instructions")').click()
    notBusy()
    traceRectangle('@canvas', 7, 9, 49, 15)
    cy.get('button:contains("Wording")').click()
    notBusy()

    cy.get('button:contains("Multiple choices")').click()
    screenshot('multiple-choices-with-choices-in-wording', 'edit-1')
    cy.get('@wording').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 8, node, 31)
    })
    cy.get('button:contains("OK")').should('exist')
    cy.get('label + input').eq(3).should('be.enabled').type('{selectAll}{del}', {delay: 0})  // Very fragile selector; sorry, future me!
    screenshot('multiple-choices-with-choices-in-wording', 'edit-2', {clearSel: false})
    cy.get('button:contains("OK")').click()
    screenshot('multiple-choices-with-choices-in-wording', 'edit-3')

    cy.get('button:contains("Save then back")').click()
    visit('/project-xkopqm')
    cy.get('a:contains("the exported HTML")').should('have.attr', 'href').then(url => {
      cy.visit(url + '&download=false')
      cy.get('a').click()
      screenshot('multiple-choices-with-choices-in-wording', 'export-1')
      cy.get('span.main').eq(1).click()
      screenshot('multiple-choices-with-choices-in-wording', 'export-2')
      cy.get('span.choice0').click()
      screenshot('multiple-choices-with-choices-in-wording', 'export-3')
    })
  })

  it('creates a "Fill with free text" exercise', () => {
    cy.viewport(1200, 1000)
    visit('/project-xkopqm/textbook-klxufv/page-4/new-exercise', {pdf: 'demo'})
    setupAliases()

    cy.get('@number').type('1')

    cy.get('@adaptationType').select('fill-with-free-text').blur()
    cy.get('p:contains("Placeholder") >button:contains("+")').click()
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
