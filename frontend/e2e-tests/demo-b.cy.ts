import { loadFixtures, login, notBusy, traceRectangle, visit } from "./utils"


describe('Gabby', () => {
  before(() => {
    console.clear()
  })

  beforeEach(() => {
    login()
    loadFixtures('empty-demo-textbook')
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

  it('creates a "Multiple choices" exercise with two sets of choices in instructions', () => {
    cy.viewport(1300, 1300)
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

    cy.get('span[title="3 lines per page"]').click()

    cy.get('button:contains("Multiple choices")').click()
    screenshot('multiple-choices-with-two-set-of-choices-in-instructions', 'edit-1')
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 18, node, 34)
    })
    cy.get('button:contains("OK")').should('exist')
    cy.get('label:contains("Start") + input').should('have.value', '')
    cy.get('label:contains("Stop") + input').should('have.value', '')
    cy.get('label:contains("Separators") + input').should('have.value', '/')
    cy.get('input[data-cy="second-mcq-separator"]').should('have.value', '')
    cy.get('label:contains("Placeholder") + input').click().type('...')
    cy.get('label:contains("Placeholder") + input').should('be.focused').blur()
    screenshot('multiple-choices-with-two-set-of-choices-in-instructions', 'edit-2', {clearSel: false})
    cy.get('button:contains("OK")').click()
    screenshot('multiple-choices-with-two-set-of-choices-in-instructions', 'edit-3')

    cy.get('button:contains("Multiple choices")').click()
    screenshot('multiple-choices-with-two-set-of-choices-in-instructions', 'edit-4')
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild!.nextSibling!.nextSibling
      console.assert(node !== null)
      selectRange(node, 16, node, 35)
    })
    cy.get('button:contains("OK")').should('exist')
    cy.get('label:contains("Start") + input').should('have.value', '')
    cy.get('label:contains("Stop") + input').should('have.value', '')
    cy.get('label:contains("Separators") + input').should('have.value', '*')
    cy.get('input[data-cy="second-mcq-separator"]').should('have.value', '')
    cy.get('label:contains("Placeholder") + input').click().type('@@@')
    cy.get('label:contains("Placeholder") + input').should('be.focused').blur()
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
})
