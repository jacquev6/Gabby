describe('Gabby\'s project\'s textbook page exercise view', () => {
  it('replaces all in given fields', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')
    cy.get('select').select('en')

    cy.get('label:contains("Instructions")').next().type('Instructions!')
    cy.get('label:contains("Wording")').next().type('Wording!')
    cy.get('p:contains("Example")').click()
    cy.focused().type('Example!')
    cy.get('p:contains("Clue")').click()
    cy.focused().type('Clue!')

    cy.get('label:contains("Replace")').next().type('!')
    cy.get('label:contains("with")').next().type('.')
    cy.get('label:contains("in")').last().next().select('everywhere')
    cy.get('button:contains("Apply")').click()
    cy.get('label:contains("Instructions")').next().should('have.value', 'Instructions.')
    cy.get('label:contains("Wording")').next().should('have.value', 'Wording.')
    cy.get('label:contains("Example")').next().should('have.value', 'Example.')
    cy.get('label:contains("Clue")').next().should('have.value', 'Clue.')

    cy.get('label:contains("Replace")').next().type('.')
    cy.get('label:contains("with")').next().type('!')
    cy.get('label:contains("in")').last().next().select('instructions')
    cy.get('button:contains("Apply")').click()
    cy.get('label:contains("Instructions")').next().should('have.value', 'Instructions!')
    cy.get('label:contains("Wording")').next().should('have.value', 'Wording.')
    cy.get('label:contains("Example")').next().should('have.value', 'Example.')
    cy.get('label:contains("Clue")').next().should('have.value', 'Clue.')
    cy.get('label:contains("Instructions")').next().type('{moveToEnd}{backspace}.')
    
    cy.get('label:contains("Replace")').next().type('.')
    cy.get('label:contains("with")').next().type('!')
    cy.get('label:contains("in")').last().next().select('wording')
    cy.get('button:contains("Apply")').click()
    cy.get('label:contains("Instructions")').next().should('have.value', 'Instructions.')
    cy.get('label:contains("Wording")').next().should('have.value', 'Wording!')
    cy.get('label:contains("Example")').next().should('have.value', 'Example.')
    cy.get('label:contains("Clue")').next().should('have.value', 'Clue.')
    cy.get('label:contains("Wording")').next().type('{moveToEnd}{backspace}.')

    cy.get('label:contains("Replace")').next().type('.')
    cy.get('label:contains("with")').next().type('!')
    cy.get('label:contains("in")').last().next().select('example')
    cy.get('button:contains("Apply")').click()
    cy.get('label:contains("Instructions")').next().should('have.value', 'Instructions.')
    cy.get('label:contains("Wording")').next().should('have.value', 'Wording.')
    cy.get('label:contains("Example")').next().should('have.value', 'Example!')
    cy.get('label:contains("Clue")').next().should('have.value', 'Clue.')
    cy.get('label:contains("Example")').next().type('{moveToEnd}{backspace}.')

    cy.get('label:contains("Replace")').next().type('.')
    cy.get('label:contains("with")').next().type('!')
    cy.get('label:contains("in")').last().next().select('clue')
    cy.get('button:contains("Apply")').click()
    cy.get('label:contains("Instructions")').next().should('have.value', 'Instructions.')
    cy.get('label:contains("Wording")').next().should('have.value', 'Wording.')
    cy.get('label:contains("Example")').next().should('have.value', 'Example.')
    cy.get('label:contains("Clue")').next().should('have.value', 'Clue!')
    cy.get('label:contains("Clue")').next().type('{moveToEnd}{backspace}.')
  })

  it('replaces line and paragraph ends', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-7/exercise-dymwin')
    cy.get('select').select('en')

    cy.get('label:contains("Wording")').next().should('have.value', 'nager ➞ … ◆ tracter ➞ … ◆ manger ➞ … ◆\ninventer ➞ … ◆ livrer ➞ …')

    cy.get('label:contains("Replace")').next().type('{line-end}', {parseSpecialCharSequences: false})
    cy.get('label:contains("with")').next().type(' ')
    cy.get('button:contains("Apply")').click()

    cy.get('label:contains("Wording")').next().should('have.value', 'nager ➞ … ◆ tracter ➞ … ◆ manger ➞ … ◆ inventer ➞ … ◆ livrer ➞ …')
    cy.get('label:contains("Replace")').next().should('have.value', '')
    cy.get('label:contains("with")').next().should('have.value', '')

    cy.get('label:contains("Replace")').next().type(' ◆ ')
    cy.get('label:contains("with")').next().type('{line-end}', {parseSpecialCharSequences: false})
    cy.get('button:contains("Apply")').click()

    cy.get('label:contains("Wording")').next().should('have.value', 'nager ➞ …\ntracter ➞ …\nmanger ➞ …\ninventer ➞ …\nlivrer ➞ …')

    cy.get('label:contains("Replace")').next().type('{line-end}', {parseSpecialCharSequences: false})
    cy.get('label:contains("with")').next().type('{paragraph-end}', {parseSpecialCharSequences: false})
    cy.get('button:contains("Apply")').click()

    cy.get('label:contains("Wording")').next().should('have.value', 'nager ➞ …\n\ntracter ➞ …\n\nmanger ➞ …\n\ninventer ➞ …\n\nlivrer ➞ …')

    cy.get('label:contains("Replace")').next().type('…{paragraph-end}', {parseSpecialCharSequences: false})
    cy.get('label:contains("with")').next().type('...#', {parseSpecialCharSequences: false})
    cy.get('button:contains("Apply")').click()

    cy.get('label:contains("Wording")').next().should('have.value', 'nager ➞ ...#tracter ➞ ...#manger ➞ ...#inventer ➞ ...#livrer ➞ …')
  })

  it('gets its selection from the form', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-7/exercise-dymwin')
    cy.get('select').select('en')

    function select(selector, start, end) {
      cy.get(selector)
        .type('{moveToStart}')
        .then(el => el[0].setSelectionRange(start, end))
    }
  
    cy.get('label:contains("Instructions")').next().as('instructions')
    cy.get('label:contains("Wording")').next().as('wording')

    cy.get('label:contains("Replace")').next().should('have.value', '')

    select('@instructions', 0, 5)
    cy.get('label:contains("Replace")').next().should('have.value', 'Ajout')
    cy.get('label:contains("in")').last().next().should('have.value', 'instructions')

    select('@wording', 9, 12)
    cy.get('label:contains("Replace")').next().should('have.value', ' ◆ ')
    cy.get('label:contains("in")').last().next().should('have.value', 'wording')

    // Empty selection is not propagated
    select('@instructions', 7, 7)
    cy.get('label:contains("Replace")').next().should('have.value', ' ◆ ')
    cy.get('label:contains("in")').last().next().should('have.value', 'wording')

    // Selection after typing is not propagated
    cy.get('label:contains("Replace")').next().type('bl')
    select('@wording', 0, 5)
    cy.get('label:contains("Replace")').next().should('have.value', ' ◆ bl')  // This test is not sufficient:
    // this might be observed shortly after selecting, but might disappear after a while.
    // So we strengthen the test with these two lines:
    cy.get('label:contains("Replace")').next().type('ah')
    cy.get('label:contains("Replace")').next().should('have.value', ' ◆ blah')

    // Selection after clearing is propagated
    cy.get('label:contains("Replace")').next().type('{selectall}{backspace}')
    select('@wording', 0, 5)
    cy.get('label:contains("Replace")').next().should('have.value', 'nager')
  })

  it('has undo/redo', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')
    cy.get('select').select('en')

    cy.get('input[type=file]').selectFile('../pdf-examples/test.pdf')
    cy.get('div.busy').should('not.exist')

    cy.get('button:contains("Undo")').as('undo')
    cy.get('button:contains("Redo")').as('redo')
    cy.get('@undo').should('be.disabled')
    cy.get('@redo').should('be.disabled')

    cy.get('label:contains("Number")').next().type('6')
    cy.get('@undo').should('be.enabled')
    cy.get('@redo').should('be.disabled')
    cy.get('@undo').click()
    cy.get('label:contains("Number")').next().should('have.value', '')
    cy.get('@undo').should('be.disabled')
    cy.get('@redo').should('be.enabled')
    cy.get('@redo').click()
    cy.get('label:contains("Number")').next().should('have.value', '6')
    cy.get('@undo').should('be.enabled')
    cy.get('@redo').should('be.disabled')

    // @todo Extend this test to show undo/redo works on all fields (incl. bounding rectangle, adaptation type, etc.)
  })
})
