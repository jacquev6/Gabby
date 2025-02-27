import { loadFixtures, login, notBusy, visit } from './utils'


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

function pressEscape() {
  cy.document().trigger('keydown', {key: 'Escape'})
  cy.wait(100)
  cy.document().trigger('keyup', {key: 'Escape'})
}

describe('Gabby', () => {
  before(console.clear)

  beforeEach(() => {
    loadFixtures('more-test-exercises')
    login()
    cy.viewport(1000, 1000)
  })

  it('resets responses when changing adaptation type', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/exercise-dymwin')
    cy.get('label:contains("Number")').next().should('have.value', '11')

    cy.get('span[contenteditable]').first().type('Abcd')

    cy.get('label:contains("Adaptation type")').next().select('generic')
    cy.get('div:contains("Words") >input').check()
    cy.get('div:contains("Selectable") >input').check()
    notBusy()

    cy.get('span:contains("tracter")').first().click()
    cy.get('span:contains("tracter")').first().should('have.css', 'background-color', 'rgb(255, 255, 0)')

    cy.get('label:contains("Adaptation type")').next().select('fill-with-free-text')
    notBusy()

    cy.get('span[contenteditable]').first().should('have.value', '')

    cy.get('label:contains("Adaptation type")').next().select('generic')
    cy.get('div:contains("Selectable") >input').check()
    notBusy()

    cy.get('span:contains("tracter")').should('have.css', 'background-color', 'rgba(0, 0, 0, 0)')
  })

  it('closes fullscreen preview with escape key', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')

    cy.get('label:contains("Instructions") + .ql-container > .ql-editor').as('instructions')
    cy.get('label:contains("Wording") + .ql-container > .ql-editor').as('wording')

    cy.get('@instructions').click().type('{selectAll}alpha/bravo/charlie', {delay: 0})
    cy.get('@wording').click().type('{selectAll}QCM: @@@.', {delay: 0})

    cy.get('button:contains("Multiple choices")').click()
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 0, node, 19)
    })
    cy.get('label:contains("Placeholder to fill") + input').click().type('@@@')

    cy.get('button:contains("Full screen")').click()
    cy.get('button:contains("Exit full screen")').should('exist')
    pressEscape()
    cy.get('button:contains("Exit full screen")').should('not.exist')

    cy.get('button:contains("OK")').click()  // Use the pop-up after closing the fullscreen preview: the popup has NOT been closed by pressing Escape

    cy.get('button:contains("Full screen")').click()
    cy.get('button:contains("Exit full screen")').should('exist')
    cy.get('span.choice0').should('not.exist')
    cy.get('span.main').click()
    cy.get('span.choice0').should('exist')
    pressEscape()
    cy.get('button:contains("Exit full screen")').should('not.exist')
    cy.get('span.choice0').should('exist')
  })
})
