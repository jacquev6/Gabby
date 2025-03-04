import { visit, login, loadFixtures, notBusy, selectRange, pressEscape } from './utils'


describe('Gabby', () => {
  before(console.clear)

  beforeEach(() => {
    loadFixtures('test-exercises')
    login()
  })

  it('enables the "Save exercise" button', () => {
    visit('/project-xkopqm/textbook-klxufv/page-6/new-exercise')

    cy.get('button:contains("Save then next")').should('be.disabled')

    cy.get('label:contains("Number")').next().type('1')
    cy.get('button:contains("Save then next")').should('be.enabled')

    cy.get('label:contains("Number")').next().clear()
    cy.get('button:contains("Save then next")').should('be.disabled')

    cy.get('label:contains("Number")').next().type('A')
    cy.get('button:contains("Save then next")').should('be.enabled')
  })

  it('creates a minimal exercise', () => {
    visit('/project-xkopqm/textbook-klxufv/page-6/new-exercise')

    cy.get('label:contains("Number")').next().type('1')
    cy.get('button:contains("Save then next")').click()
    notBusy()

    cy.get('label:contains("Number")').next().should('have.value', '2')

    cy.get('a:contains("Back to list (without saving)")').click()
    notBusy()
    cy.get('li:contains("1")').should('exist')
  })

  it('creates a full exercise', () => {
    visit('/project-xkopqm/textbook-klxufv/page-6/new-exercise')

    cy.get('label:contains("Number")').next().type('Défis')
    cy.get('label:contains("Instructions")').next().type('Do the smartest thing ever.')
    cy.get('label:contains("Wording")').next().type('The wording of this exercise is a bit longer in a quite artificial way.')
    cy.get('p:contains("Example")').click()
    cy.focused().type('The example')
    cy.get('p:contains("Clue")').click()
    cy.focused().type('The clue')

    cy.get('label:contains("Adaptation type") + select').select('generic')
    cy.get('div:contains("Words") >input').check()
    cy.get('div:contains("Selectable") >input').check()
    cy.get('span.maybe-usable-colors-container span.usable-colors-button[data-cy-colors="2"]').click()

    cy.get('span:contains("artificial")').first().click()
    cy.get('span:contains("artificial")').first().should('have.css', 'background-color', 'rgb(255, 255, 0)')
    cy.get('span:contains("artificial")').first().click()
    cy.get('span:contains("artificial")').first().should('have.css', 'background-color', 'rgb(255, 192, 203)')
    cy.get('span:contains("artificial")').first().click()
    cy.get('span:contains("artificial")').first().should('have.css', 'background-color', 'rgba(0, 0, 0, 0)')

    cy.get('button:contains("Save then next")').click()
    notBusy()

    cy.get('label:contains("Number")').next().should('have.value', '')

    cy.get('a:contains("Back to list (without saving)")').click()
    notBusy()
    cy.get('li:contains("Défis")').should('exist')
  })

  it('detects when an exercise already exists', () => {
    visit('/project-xkopqm/textbook-klxufv/page-6/new-exercise')

    cy.get('label:contains("Number")').next().type('2')
    cy.get('button:contains("Save then next")').click()
    notBusy()

    cy.get('label:contains("Number")').next().should('have.value', '3')
    cy.get('button:contains("Save then next")').should('be.disabled')
    cy.get('button:contains("Skip to next exercise")').click()
    cy.get('label:contains("Number")').next().should('have.value', '4')
    cy.get('button:contains("Save then next")').should('be.disabled')
    cy.get('button:contains("Skip to next exercise")').click()
    cy.get('label:contains("Number")').next().should('have.value', '5')
    cy.get('button:contains("Save then next")').should('be.enabled')

    cy.get('label:contains("Number")').next().type('{selectAll}3')
    cy.get('button:contains("Save then next")').should('be.disabled')
    cy.get('button:contains("Skip to next exercise")').should('be.enabled')
    cy.get('label:contains("Number")').next().type('0')
    cy.get('button:contains("Save then next")').should('be.enabled')
    cy.get('button:contains("Skip to next exercise")').should('not.exist')
  })

  it('suggests items separators', () => {
    visit('/project-xkopqm/textbook-klxufv/page-6/new-exercise')

    cy.get('label:contains("Number")').next().type('5')
    cy.get('p.separatorSuggestion').should('not.exist')
    cy.get('div:contains("Delimited by") > span > input').should('have.value', '').click()
    cy.get('p.separatorSuggestion').should('not.exist')
    cy.get('div:contains("Delimited by") > span > input').type('*')
    cy.get('div:contains("Boxed") > input').check()
    cy.get('button:contains("Save then next")').click()
    notBusy()

    cy.get('p.separatorSuggestion').should('not.exist')
    cy.get('div:contains("Delimited by") > span > input').should('have.value', '').click()
    cy.get('p.separatorSuggestion').should('have.length', 1)
    cy.get('p.separatorSuggestion:contains("*")').should('exist')
    cy.get('div:contains("Delimited by") > span > input').type('/')
    cy.get('div:contains("Boxed") > input').check()
    cy.get('button:contains("Save then next")').click()
    notBusy()

    cy.get('p.separatorSuggestion').should('not.exist')
    cy.get('div:contains("Delimited by") > span > input').should('have.value', '').click()
    cy.get('p.separatorSuggestion').should('have.length', 2)
    cy.get('p.separatorSuggestion:contains("/")').should('exist')
    cy.get('p.separatorSuggestion:contains("*")').should('exist').click()
    cy.get('p.separatorSuggestion').should('not.exist')
    cy.get('div:contains("Delimited by") > span > input').should('have.value', '*').click()
    cy.get('p.separatorSuggestion:contains("*")').should('exist')
    cy.get('p.separatorSuggestion:contains("/")').should('exist').click()
    cy.get('p.separatorSuggestion').should('not.exist')
    cy.get('div:contains("Delimited by") > span > input').should('have.value', '/')
    cy.get('div:contains("Boxed") > input').check()
    cy.get('button:contains("Save then next")').click()
    notBusy()

    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')
    cy.get('p.separatorSuggestion').should('not.exist')
    cy.get('div:contains("Delimited by") > span > input').should('have.value', '').click()
    cy.get('p.separatorSuggestion').should('have.length', 2)
    cy.get('p.separatorSuggestion:contains("*")').should('exist')
    cy.get('p.separatorSuggestion:contains("/")').should('exist')
  })

  it('unchecks incompatible items', () => {
    visit('/project-xkopqm/textbook-klxufv/page-6/new-exercise')

    for (const tokens of ['Words', 'Punctuation']) {
      const items = ['Letters', tokens, 'Sentences', 'Delimited by', 'Manual selection']
      for (const item1 of items) {
        for (const item2 of items.slice(items.indexOf(item1) + 1)) {
          cy.get(`div:contains("${item1}") > input`).should('not.be.checked').check().should('be.checked')
          cy.get(`div:contains("${item2}") > input`).should('not.be.checked').check().should('be.checked')
          cy.get(`div:contains("${item1}") > input`).should('not.be.checked').check().should('be.checked')
          cy.get(`div:contains("${item2}") > input`).should('not.be.checked').check().should('be.checked')
          cy.get(`div:contains("${item1}") > input`).should('not.be.checked').check().should('be.checked')
          cy.get(`div:contains("${item2}") > input`).should('not.be.checked')
          cy.get(`div:contains("${item1}") > input`).should('be.checked').uncheck().should('not.be.checked')
        }
      }
    }
  })

  it('enables effects when items are selected', () => {
    visit('/project-xkopqm/textbook-klxufv/page-6/new-exercise')

    cy.get('div:contains("Beside each item") > input').should('be.disabled')
    cy.get('div:contains("Below each item") > input').should('be.disabled')
    cy.get('div:contains("Selectable") > input').should('be.disabled')
    cy.get('div:contains("Boxed") > input').should('be.disabled')
    cy.get('div:contains("1 item per line") > input').should('be.disabled')

    cy.get('div:contains("Words") > input').check()

    cy.get('div:contains("Beside each item") > input').should('be.enabled')
    cy.get('div:contains("Below each item") > input').should('be.enabled').check()
    cy.get('div:contains("Selectable") > input').should('be.enabled').check()
    cy.get('div:contains("Boxed") > input').should('be.enabled').check()
    cy.get('div:contains("1 item per line") > input').should('be.enabled').check()

    cy.get('div:contains("Words") > input').uncheck()

    cy.get('div:contains("Beside each item") > input').should('be.disabled').should('not.be.checked')
    cy.get('div:contains("Below each item") > input').should('be.disabled').should('not.be.checked')
    cy.get('div:contains("Selectable") > input').should('be.disabled').should('not.be.checked')
    cy.get('div:contains("Boxed") > input').should('be.disabled').should('not.be.checked')
    cy.get('div:contains("1 item per line") > input').should('be.disabled').should('not.be.checked')
  })

  it('applies choices to all MCQ fields - with MCQ definition with uid', () => {
    cy.viewport(1200, 1200)

    visit('/project-xkopqm/textbook-klxufv/page-6/new-exercise')

    cy.get('label:contains("Instructions") + .ql-container > .ql-editor').as('instructions')
    cy.get('label:contains("Wording") + .ql-container > .ql-editor').as('wording')

    cy.get('@instructions').type('alpha/bravo/delta')
    cy.get('@wording').type('Blah blah blah')

    cy.get('button:contains("Add an MCQ field")').click()
    cy.get('@wording').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 4, node, 4)
    })
    cy.get('button:contains("Cancel")').click()

    cy.get('button:contains("Add an MCQ field")').click()
    cy.get('@wording').find('p').then($el => {
      const node = $el[0].lastChild
      console.assert(node !== null)
      selectRange(node, 5, node, 5)
    })
    cy.wait(100)
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 0, node, 17)
    })
    cy.wait(100)
    pressEscape()
    notBusy()

    cy.get('span.main').should('have.length', 2)
    cy.get('span.choice1').should('not.exist')
    cy.get('span.main').eq(1).click()
    cy.get('span.choice1').should('have.length', 1)
    cy.get('div.backdrop').click()
    cy.get('span.choice1').should('not.exist')

    cy.get('span.main').eq(0).click()
    cy.get('span.choice1').should('not.exist')
    cy.get('div.backdrop').click()

    cy.get('button:contains("Apply choices to all MCQ fields")').click()
    notBusy()

    cy.get('span.main').should('have.length', 2)

    cy.get('span.choice1').should('not.exist')
    cy.get('span.main').eq(1).click()
    cy.get('span.choice1').should('have.length', 1)
    cy.get('div.backdrop').click()
    cy.get('span.choice1').should('not.exist')

    cy.get('span.choice1').should('not.exist')
    cy.get('span.main').eq(0).click()
    cy.get('span.choice1').should('have.length', 1)
    cy.get('div.backdrop').click()
    cy.get('span.choice1').should('not.exist')
  })

  it('applies choices to all MCQ fields - with MCQ definition without uid', () => {
    cy.viewport(1200, 1200)

    visit('/project-xkopqm/textbook-klxufv/page-6/new-exercise')

    cy.get('label:contains("Instructions") + .ql-container > .ql-editor').as('instructions')
    cy.get('label:contains("Wording") + .ql-container > .ql-editor').as('wording')

    cy.get('@instructions').type('alpha/bravo/delta')
    cy.get('@wording').type('Blah blah blah')

    cy.get('button:contains("Add an MCQ field")').click()
    cy.get('@wording').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 4, node, 4)
    })
    cy.get('button:contains("Cancel")').click()

    cy.get('button:contains("Add an MCQ field")').click()
    cy.get('@wording').find('p').then($el => {
      const node = $el[0].lastChild
      console.assert(node !== null)
      selectRange(node, 5, node, 5)
    })
    cy.get('button:contains("Cancel")').click()

    cy.get('button:contains("Multiple choices")').click()
    cy.get('@instructions').find('p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 0, node, 17)
    })
    cy.wait(100)
    pressEscape()
    notBusy()

    cy.get('span.main').should('have.length', 2)
    cy.get('span.main').eq(1).click()
    cy.get('span.choice1').should('not.exist')
    cy.get('div.backdrop').click()

    cy.get('span.main').eq(0).click()
    cy.get('span.choice1').should('not.exist')
    cy.get('div.backdrop').click()

    cy.get('button:contains("Apply choices to all MCQ fields")').click()
    notBusy()

    cy.get('span.main').should('have.length', 2)

    cy.get('span.choice1').should('not.exist')
    cy.get('span.main').eq(1).click()
    cy.get('span.choice1').should('have.length', 1)
    cy.get('div.backdrop').click()
    cy.get('span.choice1').should('not.exist')

    cy.get('span.choice1').should('not.exist')
    cy.get('span.main').eq(0).click()
    cy.get('span.choice1').should('have.length', 1)
    cy.get('div.backdrop').click()
    cy.get('span.choice1').should('not.exist')
  })

  it('does not crash when blanking the page number', () => {
    visit('/project-xkopqm/textbook-klxufv/page-6/new-exercise')

    cy.get('label:contains("Page")').eq(1).next().type('{backspace}').should('have.value', '')
    // Just check something to make sure the page did not show the "A bug happened" message
    cy.get('label:contains("Page")').eq(1).next().type('7')
    cy.get(':contains("not the one displayed")').should('exist')
  })
})
