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

  it('creates a "Select letters" exercise', () => {
    cy.viewport(1300, 1300)
    visit('/project-xkopqm/textbook-klxufv/page-8/new-exercise', {pdf: 'demo'})
    setupAliases()

    cy.get('@number').type('1')

    cy.get('div:contains("Letters") >input').check()
    cy.get('span.maybe-usable-colors-container span.usable-colors-button[data-cy-colors="1"]').click()
    cy.get('div:contains("Selectable") >input').should('be.checked')

    traceRectangle('@canvas', 8, 5, 31, 9)
    cy.get('button:contains("Instructions")').click()
    notBusy()
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 16, node, 24)
    })
    cy.get('button[data-cy="format-color-1"]').click()
    notBusy()

    traceRectangle('@canvas', 7, 9.25, 60, 11)
    cy.get('button:contains("Wording")').click()
    notBusy()

    cy.focused().blur()
    screenshot('select-letters', 'edit-1')  // @todo Stabilize: the "highlight" button is sometimes enabled, sometimes disabled

    cy.get('button:contains("Save then back")').click()
    visit('/project-xkopqm')
    cy.get('a:contains("the exported HTML")').should('have.attr', 'href').then(url => {
      cy.visit(url + '&download=false')
      cy.get('a').click()
      screenshot('select-letters', 'export-1')
      cy.get('span[data-cy=selectable]').eq(5).click()
      screenshot('select-letters', 'export-2')
    })
  })

  it('creates a "Select words" exercise', () => {
    cy.viewport(1300, 1300)
    visit('/project-xkopqm/textbook-klxufv/page-2/new-exercise', {pdf: 'demo'})
    setupAliases()

    cy.get('@number').type('1')

    cy.get('div:contains("Words") >input').check()
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

  it('creates a "Select punctuation" exercise', () => {
    cy.viewport(1300, 1300)
    visit('/project-xkopqm/textbook-klxufv/page-9/new-exercise', {pdf: 'demo'})
    setupAliases()

    cy.get('@number').type('1')

    cy.get('div:contains("Punctuation") >input').check()
    cy.get('span.maybe-usable-colors-container span.usable-colors-button[data-cy-colors="2"]').click()
    cy.get('div:contains("Selectable") >input').should('be.checked')

    traceRectangle('@canvas', 8, 5, 92, 11)
    cy.get('button:contains("Instructions")').click()
    notBusy()
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 80, node, 119)
    })
    cy.get('button[data-cy="format-color-2"]').click()
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 25, node, 76)
    })
    cy.get('button[data-cy="format-color-1"]').click()
    notBusy()

    traceRectangle('@canvas', 7, 9.5, 92, 19)
    cy.get('button:contains("Wording")').click()
    notBusy()

    cy.focused().blur()
    screenshot('select-punctuation', 'edit-1')

    cy.get('button:contains("Save then back")').click()
    visit('/project-xkopqm')
    cy.get('a:contains("the exported HTML")').should('have.attr', 'href').then(url => {
      cy.visit(url + '&download=false')
      cy.get('a').click()
      screenshot('select-punctuation', 'export-1')
      cy.get('span[data-cy=selectable]').eq(1).click()
      cy.get('span[data-cy=selectable]').eq(1).click()
      cy.get('span[data-cy=selectable]').eq(2).click()
      screenshot('select-punctuation', 'export-2')
    })
  })

  it('creates a "Select words" exercise with custom colors', () => {
    cy.viewport(1300, 1300)
    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise', {pdf: 'demo'})
    setupAliases()

    cy.get('@number').type('1')

    cy.get('div:contains("Words") >input').check()
    cy.get('span.maybe-usable-colors-container span.usable-colors-button[data-cy-colors="2"]').click()
    cy.get('div:contains("Selectable") >input').should('be.checked')

    traceRectangle('@canvas', 8, 5, 60, 9)
    cy.get('button:contains("Instructions")').click()
    notBusy()

    cy.get('span.maybe-usable-colors-container span.usable-colors-button[data-cy-colors="1"]').rightclick()
    cy.get('.color').eq(9).click()
    cy.get('span.maybe-usable-colors-container span.usable-colors-button[data-cy-colors="2"]').rightclick()
    cy.get('.color').eq(1).click()
    notBusy()

    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 36, node, 44)
    })
    cy.get('button[data-cy="format-color-2"]').click()
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 12, node, 20)
    })
    cy.get('button[data-cy="format-color-1"]').click()
    notBusy()

    traceRectangle('@canvas', 7, 9.25, 92, 18)
    cy.get('button:contains("Wording")').click()
    notBusy()

    cy.focused().blur()
    cy.wait(100)  // Ensure buttons for highlighting are disabled
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

  it('creates a "Select sentences" exercise', () => {
    cy.viewport(1300, 1300)
    visit('/project-xkopqm/textbook-klxufv/page-10/new-exercise', {pdf: 'demo'})
    setupAliases()

    cy.get('@number').type('1')

    cy.get('div:contains("Sentences") >input').check()
    cy.get('span.maybe-usable-colors-container span.usable-colors-button[data-cy-colors="2"]').click()
    cy.get('div:contains("Selectable") >input').should('be.checked')

    traceRectangle('@canvas', 8, 5, 70, 9)
    cy.get('button:contains("Instructions")').click()
    notBusy()
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 52, node, 73)
    })
    cy.get('button[data-cy="format-color-2"]').click()
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 25, node, 44)
    })
    cy.get('button[data-cy="format-color-1"]').click()
    notBusy()

    traceRectangle('@canvas', 7, 9.5, 92, 19)
    cy.get('button:contains("Wording")').click()
    notBusy()

    cy.focused().blur()
    screenshot('select-sentences', 'edit-1')

    cy.get('button:contains("Save then back")').click()
    visit('/project-xkopqm')
    cy.get('a:contains("the exported HTML")').should('have.attr', 'href').then(url => {
      cy.visit(url + '&download=false')
      cy.get('a').click()
      screenshot('select-sentences', 'export-1')
      cy.get('span[data-cy=selectable]').eq(0).click()
      cy.get('span[data-cy=selectable]').eq(1).click()
      cy.get('span[data-cy=selectable]').eq(1).click()
      screenshot('select-sentences', 'export-2')
    })
  })

  it('creates a "Multiple choices" exercise with choices in instructions', () => {
    cy.viewport(1300, 1300)
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
    cy.get('label:contains("Start") + input').should('have.value', '')
    cy.get('label:contains("Stop") + input').should('have.value', '')
    cy.get('label:contains("Separators") + input').should('have.value', ',')
    cy.get('input[data-cy="second-mcq-separator"]').should('have.value', 'ou')
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

  it('creates a "Multiple choices" exercise with choices in wording', () => {
    cy.viewport(1300, 1300)
    visit('/project-xkopqm/textbook-klxufv/page-6/new-exercise', {pdf: 'demo'})
    setupAliases()

    cy.get('@number').type('1')

    cy.get('@adaptationType').select('multiple-choices').blur()

    traceRectangle('@canvas', 8, 5, 54, 9)
    cy.get('button:contains("Instructions")').click()
    notBusy()
    traceRectangle('@canvas', 7, 9, 51, 15)
    cy.get('button:contains("Wording")').click()
    notBusy()

    cy.get('button:contains("Multiple choices")').click()
    screenshot('multiple-choices-with-choices-in-wording', 'edit-1')
    cy.get('@wording').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 11, node, 34)
    })
    cy.get('button:contains("OK")').should('exist')
    cy.get('label:contains("Start") + input').should('have.value', '(')
    cy.get('label:contains("Stop") + input').should('have.value', ')')
    cy.get('label:contains("Separators") + input').should('have.value', '/')
    cy.get('input[data-cy="second-mcq-separator"]').should('have.value', '')
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
      cy.get('span.main').eq(1).click()
      screenshot('multiple-choices-with-choices-in-wording', 'export-4')
    })
  })

  it('creates a "Multiple choices" exercise with "Show choices by default"', () => {
    cy.viewport(1300, 1300)
    visit('/project-xkopqm/textbook-klxufv/page-6/new-exercise', {pdf: 'demo'})
    setupAliases()

    cy.get('@number').type('1')

    cy.get('@adaptationType').select('multiple-choices').blur()

    traceRectangle('@canvas', 8, 5, 54, 9)
    cy.get('button:contains("Instructions")').click()
    notBusy()
    traceRectangle('@canvas', 7, 9, 51, 15)
    cy.get('button:contains("Wording")').click()
    notBusy()

    cy.get('button:contains("Multiple choices")').click()
    cy.get('@wording').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 11, node, 34)
    })
    cy.get('button:contains("OK")').should('exist')
    cy.get('label:contains("Start") + input').should('have.value', '(')
    cy.get('label:contains("Stop") + input').should('have.value', ')')
    cy.get('label:contains("Separators") + input').should('have.value', '/')
    cy.get('input[data-cy="second-mcq-separator"]').should('have.value', '')
    cy.get('button:contains("OK")').click()

    cy.get('div:contains("Show choices by default") > input').click()
    screenshot('multiple-choices-with-show-choices-by-default', 'edit-1')

    cy.get('button:contains("Save then back")').click()
    visit('/project-xkopqm')
    cy.get('a:contains("the exported HTML")').should('have.attr', 'href').then(url => {
      cy.visit(url + '&download=false')
      cy.get('a').click()
      screenshot('multiple-choices-with-show-choices-by-default', 'export-1')
      cy.get('span.choice0').eq(1).click()
      screenshot('multiple-choices-with-show-choices-by-default', 'export-2')
      cy.get('span.main').eq(1).click()
      screenshot('multiple-choices-with-show-choices-by-default', 'export-3')
    })
  })

  it('creates a "Multiple choices" exercise with "Preceded by an arrow"', () => {
    cy.viewport(1300, 1300)
    visit('/project-xkopqm/textbook-klxufv/page-6/new-exercise', {pdf: 'demo'})
    setupAliases()

    cy.get('@number').type('1')

    cy.get('@adaptationType').select('multiple-choices').blur()

    traceRectangle('@canvas', 8, 5, 54, 9)
    cy.get('button:contains("Instructions")').click()
    notBusy()
    traceRectangle('@canvas', 7, 9, 51, 15)
    cy.get('button:contains("Wording")').click()
    notBusy()

    cy.get('button:contains("Multiple choices")').click()
    cy.get('@wording').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 11, node, 34)
    })
    cy.get('button:contains("OK")').should('exist')
    cy.get('label:contains("Start") + input').should('have.value', '(')
    cy.get('label:contains("Stop") + input').should('have.value', ')')
    cy.get('label:contains("Separators") + input').should('have.value', '/')
    cy.get('input[data-cy="second-mcq-separator"]').should('have.value', '')
    cy.get('button:contains("OK")').click()

    cy.get('div:contains("Preceded by an arrow") > input').click()
    screenshot('multiple-choices-preceded-by-an-arrow', 'edit-1')

    cy.get('button:contains("Save then back")').click()
    visit('/project-xkopqm')
    cy.get('a:contains("the exported HTML")').should('have.attr', 'href').then(url => {
      cy.visit(url + '&download=false')
      cy.get('a').click()
      screenshot('multiple-choices-preceded-by-an-arrow', 'export-1')
      cy.get('span.main').eq(1).click()
      screenshot('multiple-choices-preceded-by-an-arrow', 'export-2')
      cy.get('span.choice0').click()
      screenshot('multiple-choices-preceded-by-an-arrow', 'export-3')
      cy.get('span.main').eq(1).click()
      screenshot('multiple-choices-preceded-by-an-arrow', 'export-4')
    })
  })

  it('creates a "Fill with free text" exercise', () => {
    cy.viewport(1300, 1300)
    visit('/project-xkopqm/textbook-klxufv/page-4/new-exercise', {pdf: 'demo'})
    setupAliases()

    cy.get('@number').type('1')

    cy.get('@adaptationType').select('fill-with-free-text').blur()
    cy.get('p:contains("Placeholder") >button:contains("+")').click()
    cy.get('label:contains("Placeholder") + input').type('{selectAll}...', {delay: 0})

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

  it('creates a "Multiple choices" exercise where you choose a letter to complete words', () => {
    cy.viewport(1300, 1300)
    visit('/project-xkopqm/textbook-klxufv/page-11/new-exercise', {pdf: 'demo'})
    setupAliases()

    cy.get('@number').type('1')

    cy.get('@adaptationType').select('multiple-choices')

    traceRectangle('@canvas', 8, 5, 48, 9)
    cy.get('button:contains("Instructions")').click()
    notBusy()
    traceRectangle('@canvas', 7, 11, 36, 14)
    cy.get('button:contains("Wording")').click()
    notBusy()

    cy.get('button:contains("Multiple choices")').click()
    screenshot('multiple-choices-for-letter-in-word', 'edit-1')
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 23, node, 29)
    })
    cy.get('button:contains("OK")').should('exist')
    cy.get('label:contains("Start") + input').should('have.value', '')
    cy.get('label:contains("Stop") + input').should('have.value', '')
    cy.get('label:contains("Separators") + input').should('have.value', 'ou')
    cy.get('input[data-cy="second-mcq-separator"]').type('{selectAll}{del}')
    cy.get('label:contains("Placeholder") + input').click().type('...', {delay: 0})
    screenshot('multiple-choices-for-letter-in-word', 'edit-2', {clearSel: false})
    cy.get('button:contains("OK")').click()
    screenshot('multiple-choices-for-letter-in-word', 'edit-3')

    cy.get('button:contains("Save then back")').click()
    visit('/project-xkopqm')
    cy.get('a:contains("the exported HTML")').should('have.attr', 'href').then(url => {
      cy.visit(url + '&download=false')
      cy.get('a').click()
      screenshot('multiple-choices-for-letter-in-word', 'export-1')
      cy.get('span.main').eq(1).click()
      screenshot('multiple-choices-for-letter-in-word', 'export-2')
      cy.get('span.choice1').click()
      screenshot('multiple-choices-for-letter-in-word', 'export-3')
    })
  })

  it('creates a "Multiple choices" exercise with fields beside each word', () => {
    cy.viewport(1300, 1300)
    visit('/project-xkopqm/textbook-klxufv/page-12/new-exercise', {pdf: 'demo'})
    setupAliases()

    cy.get('@number').type('1')

    cy.get('@adaptationType').select('multiple-choices')

    traceRectangle('@canvas', 8, 5, 55, 9)
    cy.get('button:contains("Instructions")').click()
    notBusy()
    traceRectangle('@canvas', 7, 9.25, 28, 15)
    cy.get('button:contains("Wording")').click()
    notBusy()

    cy.get('button:contains("Multiple choices")').click()
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 31, node, 50)
    })
    cy.get('button:contains("OK")').should('exist')
    cy.get('label:contains("Start") + input').should('have.value', '')
    cy.get('label:contains("Stop") + input').should('have.value', '')
    cy.get('label:contains("Separators") + input').should('have.value', 'ou')
    cy.get('input[data-cy="second-mcq-separator"]').should('have.value', '')
    cy.get('label:contains("Placeholder") + input').should('have.value', '')
    cy.get('button:contains("OK")').click()
    cy.get('div:contains("Words") > input').click()
    cy.get('div:contains("Beside each item") > input').click()
    screenshot('multiple-choices-beside-each-word', 'edit-1')

    cy.get('button:contains("Save then back")').click()
    visit('/project-xkopqm')
    cy.get('a:contains("the exported HTML")').should('have.attr', 'href').then(url => {
      cy.visit(url + '&download=false')
      cy.get('a').click()
      screenshot('multiple-choices-beside-each-word', 'export-1')
      cy.get('span.main').eq(1).click()
      screenshot('multiple-choices-beside-each-word', 'export-2')
      cy.get('span.choice0').click()
      screenshot('multiple-choices-beside-each-word', 'export-3')
    })
  })

  it('creates a "Multiple choices" exercise with fields beside each word - one item per line', () => {
    cy.viewport(1300, 1300)
    visit('/project-xkopqm/textbook-klxufv/page-12/new-exercise', {pdf: 'demo'})
    setupAliases()

    cy.get('@number').type('1')

    cy.get('@adaptationType').select('multiple-choices')

    traceRectangle('@canvas', 8, 5, 55, 9)
    cy.get('button:contains("Instructions")').click()
    notBusy()
    traceRectangle('@canvas', 7, 9.25, 28, 15)
    cy.get('button:contains("Wording")').click()
    notBusy()

    cy.get('button:contains("Multiple choices")').click()
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 31, node, 50)
    })
    cy.get('button:contains("OK")').should('exist')
    cy.get('label:contains("Start") + input').should('have.value', '')
    cy.get('label:contains("Stop") + input').should('have.value', '')
    cy.get('label:contains("Separators") + input').should('have.value', 'ou')
    cy.get('input[data-cy="second-mcq-separator"]').should('have.value', '')
    cy.get('label:contains("Placeholder") + input').should('have.value', '')
    cy.get('button:contains("OK")').click()
    cy.get('div:contains("Words") > input').click()
    cy.get('div:contains("Beside each item") > input').click()
    cy.get('div:contains("1 item per line") > input').check()
    cy.get('span[title="3 lines per page"]').click()
    screenshot('multiple-choices-beside-each-word-with-one-item-per-line', 'edit-1')

    cy.get('button:contains("Save then back")').click()
    visit('/project-xkopqm')
    cy.get('a:contains("the exported HTML")').should('have.attr', 'href').then(url => {
      cy.visit(url + '&download=false')
      cy.get('a').click()
      screenshot('multiple-choices-beside-each-word-with-one-item-per-line', 'export-1')
      cy.get('span.main').eq(1).click()
      screenshot('multiple-choices-beside-each-word-with-one-item-per-line', 'export-2')
      cy.get('span.choice0').click()
      screenshot('multiple-choices-beside-each-word-with-one-item-per-line', 'export-3')
    })
  })

  it('creates a "Multiple choices" exercise with fields below each word', () => {
    cy.viewport(1300, 1300)
    visit('/project-xkopqm/textbook-klxufv/page-12/new-exercise', {pdf: 'demo'})
    setupAliases()

    cy.get('@number').type('1')

    cy.get('@adaptationType').select('multiple-choices')

    traceRectangle('@canvas', 8, 5, 55, 9)
    cy.get('button:contains("Instructions")').click()
    notBusy()
    traceRectangle('@canvas', 7, 9.25, 28, 15)
    cy.get('button:contains("Wording")').click()
    notBusy()

    cy.get('button:contains("Multiple choices")').click()
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 31, node, 50)
    })
    cy.get('button:contains("OK")').should('exist')
    cy.get('label:contains("Start") + input').should('have.value', '')
    cy.get('label:contains("Stop") + input').should('have.value', '')
    cy.get('label:contains("Separators") + input').should('have.value', 'ou')
    cy.get('input[data-cy="second-mcq-separator"]').should('have.value', '')
    cy.get('label:contains("Placeholder") + input').should('have.value', '')
    cy.get('button:contains("OK")').click()
    cy.get('div:contains("Words") > input').click()
    cy.get('div:contains("Below each item") > input').click()
    screenshot('multiple-choices-below-each-word', 'edit-1')

    cy.get('button:contains("Save then back")').click()
    visit('/project-xkopqm')
    cy.get('a:contains("the exported HTML")').should('have.attr', 'href').then(url => {
      cy.visit(url + '&download=false')
      cy.get('a').click()
      screenshot('multiple-choices-below-each-word', 'export-1')
      cy.get('span.main').eq(1).click()
      screenshot('multiple-choices-below-each-word', 'export-2')
      cy.get('span.choice0').click()
      screenshot('multiple-choices-below-each-word', 'export-3')
    })
  })

  it('creates a "Multiple choices" exercise with fields beside each sentence', () => {
    cy.viewport(1300, 1300)
    visit('/project-xkopqm/textbook-klxufv/page-13/new-exercise', {pdf: 'demo'})
    setupAliases()

    cy.get('@number').type('1')

    cy.get('@adaptationType').select('multiple-choices')

    traceRectangle('@canvas', 8, 5, 75, 9)
    cy.get('button:contains("Instructions")').click()
    notBusy()
    traceRectangle('@canvas', 7, 9.25, 39, 18)
    cy.get('button:contains("Wording")').click()
    notBusy()

    cy.get('button:contains("Multiple choices")').click()
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 33, node, 73)
    })
    cy.get('button:contains("OK")').should('exist')
    cy.get('label:contains("Start") + input').should('have.value', '')
    cy.get('label:contains("Stop") + input').should('have.value', '')
    cy.get('label:contains("Separators") + input').should('have.value', ',')
    cy.get('input[data-cy="second-mcq-separator"]').should('have.value', 'ou')
    cy.get('label:contains("Placeholder") + input').should('have.value', '')
    cy.get('button:contains("OK")').click()
    cy.get('div:contains("Sentences") > input').click()
    cy.get('div:contains("Beside each item") > input').click()
    screenshot('multiple-choices-beside-each-sentence', 'edit-1')

    cy.get('button:contains("Save then back")').click()
    visit('/project-xkopqm')
    cy.get('a:contains("the exported HTML")').should('have.attr', 'href').then(url => {
      cy.visit(url + '&download=false')
      cy.get('a').click()
      screenshot('multiple-choices-beside-each-sentence', 'export-1')
      cy.get('span.main').eq(1).click()
      screenshot('multiple-choices-beside-each-sentence', 'export-2')
      cy.get('span.choice0').click()
      screenshot('multiple-choices-beside-each-sentence', 'export-3')
    })
  })

  it('creates a "Multiple choices" exercise with fields below each sentence', () => {
    cy.viewport(1300, 1300)
    visit('/project-xkopqm/textbook-klxufv/page-13/new-exercise', {pdf: 'demo'})
    setupAliases()

    cy.get('@number').type('1')

    cy.get('@adaptationType').select('multiple-choices')

    traceRectangle('@canvas', 8, 5, 75, 9)
    cy.get('button:contains("Instructions")').click()
    notBusy()
    traceRectangle('@canvas', 7, 9.25, 39, 18)
    cy.get('button:contains("Wording")').click()
    notBusy()

    cy.get('button:contains("Multiple choices")').click()
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 33, node, 73)
    })
    cy.get('button:contains("OK")').should('exist')
    cy.get('label:contains("Start") + input').should('have.value', '')
    cy.get('label:contains("Stop") + input').should('have.value', '')
    cy.get('label:contains("Separators") + input').should('have.value', ',')
    cy.get('input[data-cy="second-mcq-separator"]').should('have.value', 'ou')
    cy.get('label:contains("Placeholder") + input').should('have.value', '')
    cy.get('button:contains("OK")').click()
    cy.get('div:contains("Sentences") > input').click()
    cy.get('div:contains("Below each item") > input').click()
    screenshot('multiple-choices-below-each-sentence', 'edit-1')

    cy.get('button:contains("Save then back")').click()
    visit('/project-xkopqm')
    cy.get('a:contains("the exported HTML")').should('have.attr', 'href').then(url => {
      cy.visit(url + '&download=false')
      cy.get('a').click()
      screenshot('multiple-choices-below-each-sentence', 'export-1')
      cy.get('span.main').eq(1).click()
      screenshot('multiple-choices-below-each-sentence', 'export-2')
      cy.get('span.choice0').click()
      screenshot('multiple-choices-below-each-sentence', 'export-3')
    })
  })

  it('creates a "Multiple choices" exercise with fields below each delimited item', () => {
    cy.viewport(1300, 1300)
    visit('/project-xkopqm/textbook-klxufv/page-14/new-exercise', {pdf: 'demo'})
    setupAliases()

    cy.get('@number').type('1')

    cy.get('@adaptationType').select('multiple-choices')

    traceRectangle('@canvas', 8, 5, 75, 9)
    cy.get('button:contains("Instructions")').click()
    notBusy()
    traceRectangle('@canvas', 7, 9.25, 55, 15)
    cy.get('button:contains("Wording")').click()
    notBusy()

    cy.get('button:contains("Multiple choices")').click()
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 52, node, 72)
    })
    cy.get('button:contains("OK")').should('exist')
    cy.get('label:contains("Start") + input').should('have.value', '')
    cy.get('label:contains("Stop") + input').should('have.value', '')
    cy.get('label:contains("Separators") + input').should('have.value', 'ou')
    cy.get('input[data-cy="second-mcq-separator"]').should('have.value', '')
    cy.get('label:contains("Placeholder") + input').should('have.value', '')
    cy.get('button:contains("OK")').click()
    cy.get('div:contains("Delimited by") > span > input').click().type('/')
    cy.get('div:contains("Delimited by") > input').should('be.checked')
    cy.get('div:contains("Below each item") > input').click()
    screenshot('multiple-choices-below-separated-items', 'edit-1')

    cy.get('button:contains("Save then back")').click()
    visit('/project-xkopqm')
    cy.get('a:contains("the exported HTML")').should('have.attr', 'href').then(url => {
      cy.visit(url + '&download=false')
      cy.get('a').click()
      screenshot('multiple-choices-below-separated-items', 'export-1')
      cy.get('span.main').eq(1).click()
      screenshot('multiple-choices-below-separated-items', 'export-2')
      cy.get('span.choice0').click()
      screenshot('multiple-choices-below-separated-items', 'export-3')
    })
  })

  it('create a "Multiple choices" with predefined "Gender" and "Number" choices', () => {
    cy.viewport(1300, 1300)
    visit('/project-xkopqm/textbook-klxufv/page-15/new-exercise', {pdf: 'demo'})
    setupAliases()

    cy.get('@number').type('1')

    cy.get('@adaptationType').select('multiple-choices')

    traceRectangle('@canvas', 8, 5, 61, 9)
    cy.get('button:contains("Instructions")').click()
    notBusy()
    traceRectangle('@canvas', 7, 9.25, 51, 12)
    cy.get('button:contains("Wording")').click()
    notBusy()

    cy.get('div:contains("Delimited by") > span > input').click().type('▪')
    cy.get('div:contains("1 item per line") > input').check()
    cy.get('div:contains("Gender") > input').check()
    screenshot('multiple-choices-gender-number', 'edit-1')
    cy.get('div:contains("Number") > input[type="checkbox"]').check()
    screenshot('multiple-choices-gender-number', 'edit-2')

    cy.get('button:contains("Save then back")').click()
    visit('/project-xkopqm')
    cy.get('a:contains("the exported HTML")').should('have.attr', 'href').then(url => {
      cy.visit(url + '&download=false')
      cy.get('a').click()
      screenshot('multiple-choices-gender-number', 'export-1')
      cy.get('span.main').eq(1).click()
      screenshot('multiple-choices-gender-number', 'export-2')
      cy.get('span.choice0').click()
      screenshot('multiple-choices-gender-number', 'export-3')
    })
  })
})
