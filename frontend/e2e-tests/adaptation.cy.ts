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

function screenshot(screenshotName: string, options: {clearSel: boolean} = {clearSel: true}) {
  if (options.clearSel) {
    cy.window().then(window => {
      var sel = window.getSelection()
      console.assert(sel !== null)
      sel.removeAllRanges()
    })
  }
  notBusy()
  cy.screenshot(screenshotName)
}

describe('Gabby', () => {
  before(console.clear)

  beforeEach(() => {
    loadFixtures('more-test-exercises')
    login()
  })

  it('shows MCQ choices on two lines even near the right edge of the screen', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')

    cy.get('label:contains("Instructions") + .ql-container > .ql-editor').as('instructions')
    cy.get('label:contains("Wording") + .ql-container > .ql-editor').as('wording')

    cy.get('@instructions').click().type('{selectAll}Les Japonais/La taille de cet animal marin/Jorunna/Il', {delay: 0})
    cy.get('@wording').click().type('{selectAll}... est un animal marin qui ressemble à un lapin. ... vit dans les mers chaudes près du Japon.', {delay: 0})

    cy.get('button:contains("Multiple choices")').click()
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 0, node, 53)
    })
    cy.get('label:contains("Placeholder") + input').click().should('be.enabled').type('...')
    cy.get('button:contains("OK")').click()

    cy.get('button:contains("Full screen")').click()
    cy.get('span.main').eq(0).click()
    screenshot('mcq-choices-on-two-lines-1')
    cy.get('div.backdrop').click()
    cy.get('span.main').eq(1).click()
    screenshot('mcq-choices-on-two-lines-2')
  })

  it('detects comma as the only MCQ separator', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')

    cy.get('label:contains("Instructions") + .ql-container > .ql-editor').as('instructions')

    cy.get('@instructions').click().type('{selectAll}alpha, bravo, charlie', {delay: 0})

    cy.get('button:contains("Multiple choices")').click()
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 0, node, 21)
    })
    cy.get('label:contains("Separators") + input').should('have.value', ',')
    cy.get('label + input').eq(4).should('have.value', '')  // Very fragile selector; sorry, future me!
  })

  it('detects "◆" as the only MCQ separator', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')

    cy.get('label:contains("Instructions") + .ql-container > .ql-editor').as('instructions')

    cy.get('@instructions').click().type('{selectAll}alpha ◆ bravo ◆ charlie', {delay: 0})

    cy.get('button:contains("Multiple choices")').click()
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 0, node, 23)
    })
    cy.get('label:contains("Separators") + input').should('have.value', '◆')
    cy.get('label + input').eq(4).should('have.value', '')  // Very fragile selector; sorry, future me!
  })

  it('detects "ou" as the only MCQ separator', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')

    cy.get('label:contains("Instructions") + .ql-container > .ql-editor').as('instructions')

    cy.get('@instructions').click().type('{selectAll}alpha ou bravo', {delay: 0})

    cy.get('button:contains("Multiple choices")').click()
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 0, node, 14)
    })
    cy.get('label:contains("Separators") + input').should('have.value', 'ou')
    cy.get('label + input').eq(4).should('have.value', '')  // Very fragile selector; sorry, future me!
  })

  it('detects comma and "ou" as a MCQ separators', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')

    cy.get('label:contains("Instructions") + .ql-container > .ql-editor').as('instructions')

    cy.get('@instructions').click().type('{selectAll}alpha, bravo ou charlie', {delay: 0})

    cy.get('button:contains("Multiple choices")').click()
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 0, node, 23)
    })
    cy.get('label:contains("Separators") + input').should('have.value', ',')
    cy.get('label + input').eq(4).should('have.value', 'ou')  // Very fragile selector; sorry, future me!
  })

  it('does not detect "or" as a MCQ separator', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')

    cy.get('label:contains("Instructions") + .ql-container > .ql-editor').as('instructions')

    cy.get('@instructions').click().type('{selectAll}alpha or bravo', {delay: 0})

    cy.get('button:contains("Multiple choices")').click()
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 0, node, 14)
    })
    cy.get('label:contains("Separators") + input').should('have.value', '')
    cy.get('label + input').eq(4).should('have.value', '')  // Very fragile selector; sorry, future me!
  })
})
