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
    cy.get('div.backdrop').click({force: true})
    cy.get('span.main').eq(1).click()
    screenshot('mcq-choices-on-two-lines-2')
  })

  it('shows MCQ choices as well as possible when they are wider than the screen', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')

    cy.get('label:contains("Instructions") + .ql-container > .ql-editor').as('instructions')
    cy.get('label:contains("Wording") + .ql-container > .ql-editor').as('wording')

    cy.get('@instructions').click().type('{selectAll}Long choice half the screen/Other long choice half the screen/Alpha/Bravo', {delay: 0})
    cy.get('@wording').click().type('{selectAll}Blah ... blih.\nSecond ... line.', {delay: 0})

    cy.get('button:contains("Multiple choices")').click()
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 0, node, 73)
    })
    cy.get('label:contains("Placeholder") + input').click().should('be.enabled').type('...')
    cy.get('button:contains("OK")').click()

    cy.get('button:contains("Full screen")').click()
    cy.get('span.main').eq(0).click()
    screenshot('mcq-choices-as-well-as-possible-1')
    cy.get('div.backdrop').click({force: true})
    cy.get('span.main').eq(1).click()
    screenshot('mcq-choices-as-well-as-possible-2')
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
    cy.get('input[data-cy="second-mcq-separator"').should('have.value', '')
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
    cy.get('input[data-cy="second-mcq-separator"').should('have.value', '')
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
    cy.get('input[data-cy="second-mcq-separator"').should('have.value', '')
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
    cy.get('input[data-cy="second-mcq-separator"').should('have.value', 'ou')
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
    cy.get('input[data-cy="second-mcq-separator"').should('have.value', '')
  })

  it('detects similar MCQs automatically', () => {
    cy.viewport(1300, 800)
    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')

    cy.get('label:contains("Wording") + .ql-container > .ql-editor').as('wording')

    cy.get('@wording').click().type('{selectAll}a. Trou … (alpha – bravo)\nb. Le … trou (charlie – delta)\nc. Trou … (echo – foxtrot)', {delay: 0})

    cy.get('button:contains("Multiple choices")').click()
    cy.get('@wording').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 10, node, 25)
    })
    cy.get('label:contains("Separators") + input').should('have.value', '–')
    cy.get('input[data-cy="second-mcq-separator"').should('have.value', '')
    cy.get('label:contains("Start") + input').should('have.value', '(')
    cy.get('label:contains("Stop") + input').should('have.value', ')')
    cy.get('label:contains("Placeholder") + input').click().type('…')
    cy.get('button:contains("OK")').click()

    cy.get('button:contains("Full screen")').click()
    screenshot('similar-mcqs-1')
    cy.get('span.main').eq(2).click()
    screenshot('similar-mcqs-2')
  })

  it('shows MCQ choices by default - on two pagelets', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')

    cy.get('label:contains("Instructions") + .ql-container > .ql-editor').as('instructions')
    cy.get('label:contains("Wording") + .ql-container > .ql-editor').as('wording')

    cy.get('@instructions').click().type('{selectAll}vrai ou faux', {delay: 0})
    cy.get('@wording').click().type('{selectAll}a. blah ...\nb. bleh ...\nc. blih ...\nd. bloh ...', {delay: 0})

    cy.get('button:contains("Multiple choices")').click()
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 0, node, 12)
    })
    cy.get('label:contains("Separators") + input').should('have.value', 'ou')
    cy.get('label:contains("Placeholder") + input').click().type('...')
    cy.get('button:contains("OK")').click()
    cy.get('div:contains("Show choices by default") > input').click()
    cy.get('span[title="2 lines per page"]').click()
    cy.get('button:contains("Full screen")').click()

    cy.get('span.choice0').eq(0).should('be.visible')
    cy.get('span.choice0').eq(1).should('be.visible')
    cy.get('span.choice0').eq(0).click()
    cy.get('span.choice0').should('have.length', 1)

    cy.get('div.arrow').eq(1).click()
    cy.get('span.choice0').should('have.length', 2)
    cy.get('div.arrow').eq(0).click()
    cy.get('span.choice0').should('have.length', 1)
  })

  it('shows MCQ choices by default - second guessing initial answer', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')

    cy.get('label:contains("Instructions") + .ql-container > .ql-editor').as('instructions')
    cy.get('label:contains("Wording") + .ql-container > .ql-editor').as('wording')

    cy.get('@instructions').click().type('{selectAll}vrai ou faux', {delay: 0})
    cy.get('@wording').click().type('{selectAll}a. blah ...\nb. bleh ...', {delay: 0})

    cy.get('button:contains("Multiple choices")').click()
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 0, node, 12)
    })
    cy.get('label:contains("Separators") + input').should('have.value', 'ou')
    cy.get('label:contains("Placeholder") + input').click().type('...')
    cy.get('button:contains("OK")').click()
    cy.get('div:contains("Show choices by default") > input').click()
    cy.get('span[title="2 lines per page"]').click()
    cy.get('button:contains("Full screen")').click()

    cy.get('span.choice0').should('have.length', 2)
    cy.get('span.choice0').eq(0).click()
    cy.get('span.choice0').should('have.length', 1)
    cy.get('span.main').eq(0).click()
    cy.get('span.choice0').should('have.length', 2)
  })

  it('shows a single item per line even when no other effect has been selected', () => {
    visit('/project-xkopqm/textbook-klxufv/page-5/new-exercise')

    cy.get('label:contains("Number") + input').click().type('single')
    cy.get('label:contains("Wording") + .ql-container > .ql-editor').click().type('alpha bravo charlie delta', {delay: 0})
    cy.get('div:contains("Words") > input').check()
    cy.get('div:contains("1 item per line") > input').check()
    screenshot('single-item-per-line-1')
    cy.get('button:contains("Save then back to list")').click()
    notBusy()
    cy.get('a:contains("Edit")').click()
    notBusy()
    cy.get('div:contains("Words") > input').should('be.checked')
    cy.get('div:contains("1 item per line") > input').scrollIntoView().should('be.checked')
    screenshot('single-item-per-line-2')
  })

  it('allows bold and italic in MCQ choices in instructions', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')

    cy.get('label:contains("Instructions") + .ql-container > .ql-editor').as('instructions')
    cy.get('label:contains("Wording") + .ql-container > .ql-editor').as('wording')

    cy.get('@instructions').click().type('{selectAll}Choose between A plain choice/An italic choice/A bold choice.', {delay: 0})
    cy.get('@wording').click().type('{selectAll}...', {delay: 0})

    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 33, node, 39)
    })
    cy.get('button[data-cy="format-italic"]').click()

    cy.get('button:contains("Multiple choices")').click()
    cy.get('@instructions').find('p').then($el => {
      const startNode = $el[0].firstChild
      console.assert(startNode !== null)
      const endNode = $el[0].lastChild
      console.assert(endNode !== null)
      selectRange(startNode, 15, endNode, 21)
    })
    cy.get('label:contains("Separators") + input').should('have.value', '/')
    cy.get('label:contains("Placeholder") + input').click().type('...')
    cy.get('button:contains("OK")').click()
    cy.get('choices2-blot > italic-blot').should('exist')
    cy.get('italic-blot > choices2-blot').should('not.exist')
    cy.get('@instructions').click()
    cy.get('@instructions').find('choices2-blot').should('have.length', 1).then($el => {
      const node = $el[0].lastChild
      console.assert(node !== null)
      selectRange(node, 10, node, 14)
    })
    cy.get('button[data-cy="format-bold"]').scrollIntoView().should('be.enabled').click()
    cy.get('choices2-blot > bold-blot').should('exist')
    cy.get('bold-blot > choices2-blot').should('not.exist')
    cy.get('@instructions').find('choices2-blot').should('have.length', 1)

    cy.get('span.main').click()
    screenshot('mcq-in-instructions-with-formatted-choices-1')
    cy.get('button:contains("Full screen")').click()
    screenshot('mcq-in-instructions-with-formatted-choices-2')
  })

  it('allows bold and italic in MCQ placeholder in "Double: word -> MCQ"', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')

    cy.get('label:contains("Instructions") + .ql-container > .ql-editor').as('instructions')
    cy.get('label:contains("Wording") + .ql-container > .ql-editor').as('wording')

    cy.get('@instructions').click().type('{selectAll}Choisis le bon verbe conjugué disez/dites.', {delay: 0})
    cy.get('@wording').click().type('{selectAll}Vous (dire) toujours la vérité.', {delay: 0})

    cy.get('div:contains("Double: word → MCQ") > input').check()

    cy.get('@wording').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 7, node, 8)
    })
    cy.get('button[data-cy="format-bold"]').click()

    cy.get('@wording').find('p').then($el => {
      const startNode = $el[0].firstChild
      console.assert(startNode !== null)
      const endNode = $el[0].lastChild
      console.assert(endNode !== null)
      selectRange(startNode, 5, endNode, 3)
    })
    cy.get('button:contains("Word → MCQ")').click()
    cy.get('mcq-placeholder-blot > bold-blot').should('exist')
    cy.get('bold-blot > mcq-placeholder-blot').should('not.exist')
    cy.get('@wording').find('mcq-placeholder-blot').should('have.length', 1)

    cy.get('mcq-placeholder-blot').then($el => {
      const node = $el[0].lastChild
      console.assert(node !== null)
      selectRange(node, 0, node, 1)
    })
    cy.get('button[data-cy="format-italic"]').click()
    cy.get('mcq-placeholder-blot > italic-blot').should('exist')
    cy.get('italic-blot > mcq-placeholder-blot').should('not.exist')
    cy.get('@wording').find('mcq-placeholder-blot').should('have.length', 1)

    cy.get('button:contains("Multiple choices")').click()
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 30, node, 41)
    })
    cy.get('button:contains("OK")').click()

    cy.get('span.main').click()
    screenshot('bold-in-mcq-placeholder-1')
    cy.get('button:contains("Full screen")').click()
    screenshot('bold-in-mcq-placeholder-2')
  })

  it("doesn't show vertical borders around line breaks in boxed items", () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')

    cy.get('label:contains("Wording") + .ql-container > .ql-editor').type('This is a short sentence in a rectangle. This one is broken up in two half-rectangles. And this one spans three lines, so its middle part only has top and bottom borders.', {delay: 0})

    cy.get('div:contains("Sentences") > input').check()
    cy.get('div:contains("Boxed") > input').check()

    cy.get('button:contains("Full screen")').click()
    screenshot('no-vertical-border-around-line-breaks')
  })
})
