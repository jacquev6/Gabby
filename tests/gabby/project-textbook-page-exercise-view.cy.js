import { useApiStore } from '../../frontend/src/frontend/stores/api'


function setLocale() {
  cy.get('select[data-cy="language"]').last().select('en')
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

  function expectUndoRedoHistory(undo, redo) {
    cy.get('button:contains("Undo")').should('have.attr', 'data-gab', undo.toString())
    if (undo === 0) {
      cy.get('button:contains("Undo")').should('be.disabled')
    } else {
      cy.get('button:contains("Undo")').should('be.enabled')
    }

    cy.get('button:contains("Redo")').should('have.attr', 'data-gab', redo.toString())
    if (redo === 0) {
      cy.get('button:contains("Redo")').should('be.disabled')
    } else {
      cy.get('button:contains("Redo")').should('be.enabled')
    }
  }

  function expectStableUndoRedoHistory(undo, redo) {
    expectUndoRedoHistory(undo, redo)
    cy.wait(1500)  // Wait because the history is debounced: it can push a new snapshot in the undo queue during a 1s period.
    expectUndoRedoHistory(undo, redo)
  }

  it('has "undo/redo" on new exercise', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')
    setLocale()

    cy.get('button:contains("Undo")').as('undo')
    cy.get('button:contains("Redo")').as('redo')

    expectStableUndoRedoHistory(0, 0)

    cy.get('label:contains("Number")').next().type('6')
    expectUndoRedoHistory(1, 0)
    cy.get('@undo').click()
    cy.get('label:contains("Number")').next().should('have.value', '')
    expectUndoRedoHistory(0, 1)
    cy.get('@redo').click()
    cy.get('label:contains("Number")').next().should('have.value', '6')
    expectUndoRedoHistory(1, 0)

    cy.get('label:contains("Instructions")').next().type('First\n')
    expectUndoRedoHistory(2, 0)
    cy.get('label:contains("Instructions")').next().type('Second')
    cy.get('label:contains("Instructions")').next().should('have.value', 'First\nSecond')
    expectUndoRedoHistory(3, 0)
    cy.get('@undo').click()
    expectUndoRedoHistory(2, 1)
    cy.get('label:contains("Instructions")').next().should('have.value', 'First\n')
    cy.get('@undo').click()
    expectUndoRedoHistory(1, 2)
    cy.get('label:contains("Instructions")').next().should('have.value', '')
    cy.get('@redo').click()
    expectUndoRedoHistory(2, 1)
    cy.get('label:contains("Instructions")').next().should('have.value', 'First\n')
    cy.get('label:contains("Instructions")').next().type('Third')
    cy.get('label:contains("Instructions")').next().should('have.value', 'First\nThird')
    expectUndoRedoHistory(3, 0)
    cy.get('@undo').click()
    expectUndoRedoHistory(2, 1)
    cy.get('label:contains("Instructions")').next().should('have.value', 'First\n')
    cy.get('@redo').click()
    expectUndoRedoHistory(3, 0)
    cy.get('label:contains("Instructions")').next().should('have.value', 'First\nThird')

    // @todo Test that undo/redo works on all fields (incl. bounding rectangle, adaptation type, etc.)
  })

  function undoUsingKeyboard() {
    cy.document().trigger('keydown', {key: 'Control', ctrlKey: true})
    cy.wait(100)
    cy.document().trigger('keydown', {key: 'z', ctrlKey: true})
    cy.wait(100)
    cy.document().trigger('keyup', {key: 'z', ctrlKey: true})
    cy.document().trigger('keyup', {key: 'Control', ctrlKey: false})
  }

  function redoUsingKeyboard() {
    cy.document().trigger('keydown', {key: 'Control', ctrlKey: true})
    cy.wait(100)
    cy.document().trigger('keydown', {key: 'Y', ctrlKey: true})
    cy.wait(100)
    cy.document().trigger('keyup', {key: 'Y', ctrlKey: true})
    cy.document().trigger('keyup', {key: 'Control', ctrlKey: false})
  }

  it('has "undo/redo" using Ctrl+Z/Ctrl+Y', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')
    setLocale()

    cy.get('button:contains("Undo")').as('undo')
    cy.get('button:contains("Redo")').as('redo')

    expectStableUndoRedoHistory(0, 0)

    cy.get('label:contains("Number")').next().type('6')
    expectUndoRedoHistory(1, 0)

    undoUsingKeyboard()
    cy.get('label:contains("Number")').next().should('have.value', '')
    expectUndoRedoHistory(0, 1)

    redoUsingKeyboard()
    cy.get('label:contains("Number")').next().should('have.value', '6')
    expectUndoRedoHistory(1, 0)
  })

  it('clears "undo/redo" history on skip', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')
    setLocale()

    cy.get('button:contains("Undo")').as('undo')
    cy.get('button:contains("Redo")').as('redo')

    cy.get('label:contains("Number")').next().type('11')
    expectUndoRedoHistory(1, 0)

    cy.get('button:contains("Skip")').click()

    expectStableUndoRedoHistory(0, 0)

    cy.get('label:contains("Instructions")').next().type('Blah blah')
    expectUndoRedoHistory(1, 0)
    cy.get('@undo').click()
    expectUndoRedoHistory(0, 1)
    cy.get('label:contains("Number")').next().should('have.value', '12')  // Unchanged by 'undo'
    cy.get('label:contains("Instructions")').next().should('have.value', '')
    cy.get('@redo').click()
    expectUndoRedoHistory(1, 0)
    cy.get('label:contains("Number")').next().should('have.value', '12')  // Unchanged by 'redo'
    cy.get('label:contains("Instructions")').next().should('have.value', 'Blah blah')
  })

  it('clears "undo/redo" history on save', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')
    setLocale()

    cy.get('button:contains("Undo")').as('undo')
    cy.get('button:contains("Redo")').as('redo')

    cy.get('label:contains("Number")').next().type('12')
    expectUndoRedoHistory(1, 0)

    cy.get('button:contains("Save then next")').click()

    expectStableUndoRedoHistory(0, 0)

    cy.get('label:contains("Instructions")').next().type('Blah blah')
    expectUndoRedoHistory(1, 0)
    cy.get('@undo').click()
    expectUndoRedoHistory(0, 1)
    cy.get('label:contains("Number")').next().should('have.value', '13')  // Unchanged by 'undo'
    cy.get('label:contains("Instructions")').next().should('have.value', '')
    cy.get('@redo').click()
    expectUndoRedoHistory(1, 0)
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
    expectUndoRedoHistory(1, 0)

    cy.get('button:contains("Previous (without saving)")').click()

    cy.location('pathname').should('equal', '/project-xkopqm/textbook-klxufv/page-5/exercise-fxcuac')
    expectStableUndoRedoHistory(0, 0)

    cy.get('label:contains("Instructions")').next().type('Blah blah')
    expectUndoRedoHistory(1, 0)

    cy.get('button:contains("Previous (without saving)")').click()

    cy.location('pathname').should('equal', '/project-xkopqm/textbook-klxufv/page-5/exercise-pghtfo')
    expectStableUndoRedoHistory(0, 0)

    cy.get('label:contains("Instructions")').next().type('Blah blah')
    expectUndoRedoHistory(1, 0)

    cy.get('button:contains("Save then next")').click()

    cy.location('pathname').should('equal', '/project-xkopqm/textbook-klxufv/page-5/exercise-fxcuac')
    expectStableUndoRedoHistory(0, 0)

    cy.get('label:contains("Instructions")').next().type('Blah blah')
    expectUndoRedoHistory(1, 0)

    cy.get('button:contains("Save then next")').click()

    cy.location('pathname').should('equal', '/project-xkopqm/textbook-klxufv/page-5/new-exercise')
    expectStableUndoRedoHistory(0, 0)
  })

  it('has "undo/redo" on existing exercise', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-7/exercise-dymwin')
    setLocale()
    cy.get('div.busy').should('not.exist')

    expectStableUndoRedoHistory(0, 0)

    cy.get('label:contains("Instructions")').next().should('have.value', 'Ajoute le suffixe –eur aux verbes.\nIndique la classe des mots fabriqués.')
    cy.get('label:contains("Instructions")').next().type('{selectall}Blah blah')
    expectUndoRedoHistory(1, 0)

    cy.get('button:contains("Undo")').click()
    expectUndoRedoHistory(0, 1)
    cy.get('label:contains("Instructions")').next().should('have.value', 'Ajoute le suffixe –eur aux verbes.\nIndique la classe des mots fabriqués.')
  })

  it('has a *single* "undo/redo" history even for WYSIWYG fields', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-7/exercise-xnyegk')
    setLocale()

    cy.get('button:contains("Undo")').as('undo')
    cy.get('button:contains("Redo")').as('redo')

    cy.get(':has(>label:contains("Instructions")) .ql-editor').as('editor')
    cy.get('@editor').focus().type('{selectall}Foo')
    expectUndoRedoHistory(1, 0)
    cy.get('@editor').should('contain.text', 'Foo')

    // Ctrl+Z specifically in the editor doesn't have any effect
    cy.get('@editor').focus().type('{ctrl+z}')  // Not caught by the undo/redo tool because of how Cypress emulates typing
    expectStableUndoRedoHistory(1, 0)  // With the default Quill settings, the undo stack would grow to 2
    cy.get('@editor').should('contain.text', 'Foo')

    undoUsingKeyboard()
    expectUndoRedoHistory(0, 1)
    cy.get('@editor').should('contain.text', 'Réponds par vrai ou faux.')
  })

  it('handles adaptation type changes from non-WYSIWYG to WYSIWYG', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-7/exercise-jkrudc')
    setLocale()

    cy.get('label:contains("Instructions")').next().type('{selectall}Réponds par {{}choice|vrai} ou {{}choice|faux}.')
    cy.get('div.busy').should('not.exist')
    cy.get('label:contains("Adaptation type")').next().select('multipleChoicesInInstructionsAdaptation')
    cy.get('div.busy').should('not.exist')

    cy.get(':has(>label:contains("Instructions")) .ql-editor').should('contain.text', 'Réponds par vrai ou faux.')
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

  it("keeps what's been typed in WYSIWYG fields regardless of the typing speed and server response time", () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-7/exercise-xnyegk')
    setLocale()

    cy.intercept('POST', '/api/parsedExercises', (req) => {
      const throttle = req.body.data.attributes.instructions === "Foo\n" ? 1000 : 0
      req.on('response', (res) => { res.delay = throttle })
    })

    cy.get(':has(>label:contains("Instructions")) .ql-editor').as('editor')

    cy.get('@editor').focus().type('{selectall}Foo')
    cy.get('@editor').focus().type('{selectall}Bar')

    cy.get('div.busy').should('not.exist')

    // The response for 'Foo' reaches the frontend after the response for 'Bar', but is discarded and 'Bar' is kept.
    cy.get('@editor').should('not.contain.text', 'Foo')
    cy.get('@editor').should('contain.text', 'Bar')
  })
})
