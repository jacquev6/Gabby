import { useApiStore } from '../../frontend/src/frontend/stores/api'


function setLocale() {
  cy.get('select').last().select('en')
}

describe('Gabby\'s project\'s textbook page exercise view', () => {
  before(console.clear)

  beforeEach(() => {
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=admin-user,more-test-exercises')
    cy.wrap(useApiStore()).then(api => api.auth.login('admin', 'password'))
  })

  it('replaces all in given fields', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')
    setLocale()

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
    setLocale()

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

  it('gets its "replace all" selection from the form', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-7/exercise-dymwin')
    setLocale()

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

  it('selects new text in field but keeps its "replace all" selection unchanged when selecting text from the PDF', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-7/exercise-dymwin')
    setLocale()

    cy.get('input[type=file]').selectFile('../pdf-examples/test.pdf')
    cy.get('div.busy').should('not.exist')

    cy.get('label:contains("Wording")').next().type('{selectall}{backspace}blah blah')

    cy.get('label:contains("Replace")').next().type('{selectall}{backspace}')
    cy.get('label:contains("Wording")').next().its('0.selectionStart').should('eq', 9)
    cy.get('label:contains("Wording")').next().its('0.selectionEnd').should('eq', 9)

    cy.get('canvas[style="position: absolute; top: 0px; left: 0px;"]').last().as('canvas')
    cy.get('@canvas').trigger('pointermove', 5, 5)
    cy.get('@canvas').trigger('pointerdown', 165, 175, { pointerId: 1 })
    cy.get('@canvas').trigger('pointermove', 300, 202)
    cy.get('@canvas').trigger('pointerup', 300, 202, { pointerId: 1 })
    cy.get('textarea').first().should('have.value', 'nager ➞ … ◆ tracter ➞ … ◆ manger ➞ … ◆\ninventer ➞ … ◆ livrer ➞ …')
    cy.get('button:contains("Wording")').click()

    cy.get('label:contains("Wording")').next().should('have.value', 'blah blah\nnager ➞ … ◆ tracter ➞ … ◆ manger ➞ … ◆\ninventer ➞ … ◆ livrer ➞ …')
    cy.get('label:contains("Wording")').next().its('0.selectionStart').should('eq', 10)
    cy.get('label:contains("Wording")').next().its('0.selectionEnd').should('eq', 74)

    cy.get('label:contains("Replace")').next().should('have.value', '')
  })

  function undoRedoHistoryShouldBeCleared() {
    cy.wait(1500)  // We have to wait because the history is debounced: it always starts disabled and gets enabled after 1s.
    cy.get('@undo').should('be.disabled')
    cy.get('@redo').should('be.disabled')
  }

  it('has "undo/redo" on new exercise', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')
    setLocale()

    cy.get('button:contains("Undo")').as('undo')
    cy.get('button:contains("Redo")').as('redo')

    undoRedoHistoryShouldBeCleared()

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

    cy.get('label:contains("Instructions")').next().type('First\n')
    cy.wait(1500)
    cy.get('label:contains("Instructions")').next().type('Second')
    cy.get('label:contains("Instructions")').next().should('have.value', 'First\nSecond')
    cy.wait(1500)
    cy.get('@undo').click()
    cy.get('label:contains("Instructions")').next().should('have.value', 'First\n')
    cy.get('@redo').should('be.enabled')
    cy.get('@undo').click()
    cy.get('label:contains("Instructions")').next().should('have.value', '')
    cy.get('@redo').click()
    cy.get('label:contains("Instructions")').next().should('have.value', 'First\n')
    cy.get('label:contains("Instructions")').next().type('Third')
    cy.get('label:contains("Instructions")').next().should('have.value', 'First\nThird')
    cy.get('@redo').should('be.disabled')
    cy.get('@undo').click()
    cy.get('label:contains("Instructions")').next().should('have.value', 'First\n')
    cy.get('@redo').click()
    cy.get('label:contains("Instructions")').next().should('have.value', 'First\nThird')

    // @todo Test that undo/redo works on all fields (incl. bounding rectangle, adaptation type, etc.)
  })

  it('clears "undo/redo" history on skip', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')
    setLocale()

    cy.get('button:contains("Undo")').as('undo')
    cy.get('button:contains("Redo")').as('redo')

    cy.get('label:contains("Number")').next().type('11')
    cy.get('@undo').should('be.enabled')

    cy.get('button:contains("Skip")').click()

    undoRedoHistoryShouldBeCleared()

    cy.get('label:contains("Instructions")').next().type('Blah blah')
    cy.get('@undo').should('be.enabled')
    cy.get('@redo').should('be.disabled')
    cy.get('@undo').click()
    cy.get('label:contains("Number")').next().should('have.value', '12')  // Unchanged by 'undo'
    cy.get('label:contains("Instructions")').next().should('have.value', '')
    cy.get('@redo').click()
    cy.get('label:contains("Number")').next().should('have.value', '12')  // Unchanged by 'redo'
    cy.get('label:contains("Instructions")').next().should('have.value', 'Blah blah')
  })

  it('clears "undo/redo" history on save', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')
    setLocale()

    cy.get('button:contains("Undo")').as('undo')
    cy.get('button:contains("Redo")').as('redo')

    cy.get('label:contains("Number")').next().type('12')
    cy.get('@undo').should('be.enabled')

    cy.get('button:contains("Save then next")').click()

    undoRedoHistoryShouldBeCleared()

    cy.get('label:contains("Instructions")').next().type('Blah blah')
    cy.get('@undo').should('be.enabled')
    cy.get('@redo').should('be.disabled')
    cy.get('@undo').click()
    cy.get('label:contains("Number")').next().should('have.value', '13')  // Unchanged by 'undo'
    cy.get('label:contains("Instructions")').next().should('have.value', '')
    cy.get('@redo').click()
    cy.get('label:contains("Number")').next().should('have.value', '13')  // Unchanged by 'redo'
    cy.get('label:contains("Instructions")').next().should('have.value', 'Blah blah')
  })

  it('clears "undo/redo" history when navigating exercise creation history', () => {
    cy.viewport(1000, 800)

    cy.visit('/project-xkopqm/textbook-klxufv/page-5/new-exercise')
    setLocale()

    cy.get('button:contains("Undo")').as('undo')
    cy.get('button:contains("Redo")').as('redo')

    cy.get('label:contains("Number")').next().type('1')
    cy.get('button:contains("Save then next")').click()
    cy.get('button:contains("Save then next")').click()

    cy.get('label:contains("Instructions")').next().type('Blah blah')
    cy.get('@undo').should('be.enabled')

    cy.get('button:contains("Previous (without saving)")').click()

    cy.location('pathname').should('equal', '/project-xkopqm/textbook-klxufv/page-5/exercise-fxcuac')
    undoRedoHistoryShouldBeCleared()

    cy.get('label:contains("Instructions")').next().type('Blah blah')
    cy.get('@undo').should('be.enabled')

    cy.get('button:contains("Previous (without saving)")').click()

    cy.location('pathname').should('equal', '/project-xkopqm/textbook-klxufv/page-5/exercise-pghtfo')
    undoRedoHistoryShouldBeCleared()

    cy.get('label:contains("Instructions")').next().type('Blah blah')
    cy.get('@undo').should('be.enabled')

    cy.get('button:contains("Save then next")').click()

    cy.location('pathname').should('equal', '/project-xkopqm/textbook-klxufv/page-5/exercise-fxcuac')
    undoRedoHistoryShouldBeCleared()

    cy.get('label:contains("Instructions")').next().type('Blah blah')
    cy.get('@undo').should('be.enabled')

    cy.get('button:contains("Save then next")').click()

    cy.location('pathname').should('equal', '/project-xkopqm/textbook-klxufv/page-5/new-exercise')
    undoRedoHistoryShouldBeCleared()
  })

  it('has "undo/redo" on existing exercise', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-7/exercise-dymwin')
    setLocale()
    cy.get('div.busy').should('not.exist')

    cy.wait(1500)  // We have to wait, see comment above
    cy.get('button:contains("Undo")').should('be.disabled')
    cy.get('button:contains("Redo")').should('be.disabled')

    cy.get('label:contains("Instructions")').next().should('have.value', 'Ajoute le suffixe –eur aux verbes.\nIndique la classe des mots fabriqués.')
    cy.get('label:contains("Instructions")').next().type('{selectall}Blah blah')
    cy.get('button:contains("Undo")').should('be.enabled')
    cy.get('button:contains("Redo")').should('be.disabled')

    cy.get('button:contains("Undo")').click()
    cy.get('label:contains("Instructions")').next().should('have.value', 'Ajoute le suffixe –eur aux verbes.\nIndique la classe des mots fabriqués.')
  })

  it('saves an exercise after setting its adaptation', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-7/exercise-jkrudc')
    setLocale()
    cy.get('div.busy').should('not.exist')

    cy.get('label:contains("Adaptation type")').next().should('have.value', '-')

    cy.get('label:contains("Adaptation type")').next().select('selectThingsAdaptation')
    cy.get('label:contains("Instructions")').next().type('{selectAll}Instructions!')
    cy.get('div.busy').should('not.exist')
    // There was a bug with a 422 response from POST /api/fillWithFreeTextAdaptations
    cy.get('button:contains("Save then back to list")').click()
    cy.get('div.busy').should('not.exist')

    cy.get('li:contains("Instructions!"):contains("Select words")').should('exist')

    cy.visit('/project-xkopqm/textbook-klxufv/page-7/exercise-jkrudc')
    setLocale()
    cy.get('div.busy').should('not.exist')
    cy.get('label:contains("Adaptation type")').next().should('have.value', 'selectThingsAdaptation')
    cy.get('label:contains("Instructions")').next().should('have.value', 'Instructions!')
  })

  it('saves an exercise after resetting its pre-existing adaptation', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-7/exercise-dymwin')
    setLocale()
    cy.get('div.busy').should('not.exist')

    cy.get('label:contains("Adaptation type")').next().should('have.value', 'fillWithFreeTextAdaptation')

    cy.get('label:contains("Adaptation type")').next().select('-')
    cy.get('label:contains("Instructions")').next().type('{selectAll}Instructions!')
    cy.get('div.busy').should('not.exist')
    cy.get('button:contains("Save then back to list")').click()
    cy.get('div.busy').should('not.exist')

    cy.get('li:contains("Instructions!")').should('exist').should('not.contain', 'Fill with free text')

    cy.visit('/project-xkopqm/textbook-klxufv/page-7/exercise-dymwin')
    setLocale()
    cy.get('div.busy').should('not.exist')
    cy.get('label:contains("Adaptation type")').next().should('have.value', '-')
    cy.get('label:contains("Instructions")').next().should('have.value', 'Instructions!')
  })

  it('saves an exercise without changing its pre-existing adaptation', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-7/exercise-dymwin')
    setLocale()
    cy.get('div.busy').should('not.exist')

    cy.get('label:contains("Adaptation type")').next().should('have.value', 'fillWithFreeTextAdaptation')

    cy.get('label:contains("Instructions")').next().type('{selectAll}Instructions!')
    cy.get('div.busy').should('not.exist')
    // There was a bug with a 422 response from POST /api/fillWithFreeTextAdaptations
    cy.get('button:contains("Save then back to list")').click()
    cy.get('div.busy').should('not.exist')

    cy.get('li:contains("Instructions!"):contains("Fill with free text")').should('exist')

    cy.visit('/project-xkopqm/textbook-klxufv/page-7/exercise-dymwin')
    setLocale()
    cy.get('div.busy').should('not.exist')
    cy.get('label:contains("Adaptation type")').next().should('have.value', 'fillWithFreeTextAdaptation')
    cy.get('label:contains("Instructions")').next().should('have.value', 'Instructions!')
  })

  it('saves an exercise after changing the type of its pre-existing adaptation', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-7/exercise-dymwin')
    setLocale()
    cy.get('div.busy').should('not.exist')

    cy.get('label:contains("Adaptation type")').next().should('have.value', 'fillWithFreeTextAdaptation')

    cy.get('label:contains("Adaptation type")').next().select('selectThingsAdaptation')
    cy.get('label:contains("Instructions")').next().type('{selectAll}Instructions!')
    cy.get('div.busy').should('not.exist')
    cy.get('button:contains("Save then back to list")').click()
    cy.get('div.busy').should('not.exist')

    cy.get('li:contains("Instructions!"):contains("Select words")').should('exist')

    cy.visit('/project-xkopqm/textbook-klxufv/page-7/exercise-dymwin')
    setLocale()
    cy.get('div.busy').should('not.exist')
    cy.get('label:contains("Adaptation type")').next().should('have.value', 'selectThingsAdaptation')
    cy.get('label:contains("Instructions")').next().should('have.value', 'Instructions!')
  })
})
