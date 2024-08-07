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

  it('creates an exercise with a WYSIWYG field', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')
    setLocale()

    cy.get('label:contains("Number")').next().type('6')
    cy.get('label:contains("Adaptation type")').next().select('multipleChoicesInInstructionsAdaptation')
    cy.get(':has(>label:contains("Instructions")) .ql-editor').as('instructions')
    cy.get('@instructions').focus().type('Choix : ')
    cy.get('button:contains("Choice")').click()
    cy.get('@instructions').focus().type('vrai')
    cy.get('button:contains("Choice")').click()
    cy.get('@instructions').focus().type(' ou ')
    cy.get('button:contains("Choice")').click()
    cy.get('@instructions').focus().type('faux')

    cy.get('choice-blot').should('have.length', 2)

    cy.get('button:contains("Save then back to list")').click()

    cy.get('li:contains("Choix : {choice|vrai} ou")').should('exist')
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

  // Coordinates are in percentage of the canvas, for stability
  function traceRectangle(alias, x1, y1, x2, y2, up=true) {
    cy.get(alias).then(canvas => {
      const w = canvas[0].width
      const h = canvas[0].height
      cy.get(alias).trigger('pointermove', x1 / 100 * w, y1 / 100 * h)
      cy.get(alias).trigger('pointerdown', x1 / 100 * w, y1 / 100 * h, { pointerId: 1 })
      cy.get(alias).trigger('pointermove', x2 / 100 * w, y2 / 100 * h)
      if (up) {
        cy.get(alias).trigger('pointerup', x2 / 100 * w, y2 / 100 * h, { pointerId: 1 })
      }
    })
  }

  it('collects rectangles', () => {
    cy.viewport(1600, 1000)

    cy.visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')
    setLocale()
    cy.get('input[type=file]').selectFile('../pdf-examples/test.pdf')
    cy.get('div.busy').should('not.exist')

    cy.get('label:contains("Number")').next().type('5')

    cy.get('canvas[style="position: absolute; top: 0px; left: 0px;"]').last().as('canvas')
    cy.get('canvas[style="position: absolute; top: 0px; left: 0px;"]').first().as('highlighter')

    traceRectangle('@canvas', 5, 4, 45, 12)
    cy.get('textarea').first().should('have.value', 'Recopie les mots suivants, puis\nentoure les pronoms personnels.\nIndique la classe des autres mots.')
    cy.get('button:contains("Instructions")').click()
    cy.get('@highlighter').should('have.attr', 'data-cy-drawnrectangles').then(JSON.parse).its('surrounded')
      .should('deep.equal', [{'left': 56.26098090252517, 'top': 725.8392892267519, 'width': 226.18785085087657, 'height': 64.16036412560493}])

    traceRectangle('@canvas', 6, 13, 44, 15.5)
    cy.get('textarea').first().should('have.value', 'b. vous ◆ un ◆ arbre ◆ ce')
    cy.get('button:contains("Wording")').click()
    cy.get('@highlighter').should('have.attr', 'data-cy-drawnrectangles').then(JSON.parse).its('surrounded')
      .should('deep.equal', [{'left': 56.26098090252517, 'top': 698.6526942582752, 'width': 226.18785085087657, 'height': 91.34695909408163}])

    traceRectangle('@canvas', 6, 15, 38, 17.5)
    cy.get('textarea').first().should('have.value', 'c. ils ◆ des ◆ grandir ◆ port')
    cy.get('button:contains("Wording")').click()
    cy.get('@highlighter').should('have.attr', 'data-cy-drawnrectangles').then(JSON.parse).its('surrounded')
      .should('deep.equal', [{'left': 56.26098090252517, 'top': 682.3407372771892, 'width': 226.18785085087657, 'height': 107.65891607516767}])

    traceRectangle('@canvas', 6, 17, 35, 19.5)
    cy.get('textarea').first().should('have.value', 'd. dessin ◆ tu ◆ aller ◆ mon')
    cy.get('button:contains("Example")').click()
    cy.get('@highlighter').should('have.attr', 'data-cy-drawnrectangles').then(JSON.parse).its('surrounded')
      .should('deep.equal', [{'left': 56.26098090252517, 'top': 667.1162440948424, 'width': 226.18785085087657, 'height': 122.88340925751447}])

    traceRectangle('@canvas', 6, 19, 37, 21.5)
    cy.get('textarea').first().should('have.value', 'e. elle ◆ gomme ◆ peindre ◆ ces')
    cy.get('button:contains("Clue")').click()
    cy.get('@highlighter').should('have.attr', 'data-cy-drawnrectangles').then(JSON.parse).its('surrounded')
      .should('deep.equal', [{'left': 56.26098090252517, 'top': 650.8042871137563, 'width': 226.18785085087657, 'height': 139.1953662386005}])

    cy.get('div.busy').should('not.exist')

    cy.get('button:contains("Save then back to list")').click()
    cy.location('pathname').should('equal', '/project-xkopqm/textbook-klxufv/page-7')
    cy.get('div.busy', {timeout: 10000}).should('not.exist')

    cy.intercept('GET', '/api/exercises/pghtfo?include=adaptation').as('getExercise')

    cy.visit('/project-xkopqm/textbook-klxufv/page-7/exercise-pghtfo')
    setLocale()
    cy.get('input[type=file]').selectFile('../pdf-examples/test.pdf')
    cy.get('div.busy').should('not.exist')

    cy.get('@getExercise').its('response.body.data.attributes.rectangles').should('deep.equal', [
      {
        'pdf_sha256': 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
        'pdf_page': 2,
        'coordinates': 'pdfjs',
        'start': {
          'x': 56.26098090252517,
          'y': 789.9996533523569
        },
        'stop': {
          'x': 282.44883175340175,
          'y': 725.8392892267519
        },
        'text': 'Recopie les mots suivants, puis\nentoure les pronoms personnels.\nIndique la classe des autres mots.',
        'role': 'instructions',
      },
      {
        'pdf_sha256': 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
        'pdf_page': 2,
        'coordinates': 'pdfjs',
        'start': {
          'x': 62.78563044630046,
          'y': 718.2270426355784
        },
        'stop': {
          'x': 277.0116238002557,
          'y': 698.6526942582752
        },
        'text': 'b. vous ◆ un ◆ arbre ◆ ce',
        'role': 'wording',
      },
      {
        'pdf_sha256': 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
        'pdf_page': 2,
        'coordinates': 'pdfjs',
        'start': {
          'x': 62.78563044630046,
          'y': 703.0025494532315
        },
        'stop': {
          'x': 243.30093449075005,
          'y': 682.3407372771892
        },
        'text': 'c. ils ◆ des ◆ grandir ◆ port',
        'role': 'wording',
      },
      {
        'pdf_sha256': 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
        'pdf_page': 2,
        'coordinates': 'pdfjs',
        'start': {
          'x': 62.78563044630046,
          'y': 686.6905924721455
        },
        'stop': {
          'x': 225.9018690406826,
          'y': 667.1162440948424
        },
        'text': 'd. dessin ◆ tu ◆ aller ◆ mon',
        'role': 'example',
      },
      {
        'pdf_sha256': 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
        'pdf_page': 2,
        'coordinates': 'pdfjs',
        'start': {
          'x': 62.78563044630046,
          'y': 671.4660992897986
        },
        'stop': {
          'x': 237.86372653760395,
          'y': 650.8042871137563
        },
        'text': 'e. elle ◆ gomme ◆ peindre ◆ ces',
        'role': 'clue',
      },
    ])

    traceRectangle('@canvas', 6, 21, 37, 23.5)
    cy.get('textarea').first().should('have.value', 'f. histoire ◆ nous ◆ gentil ◆ la')
    cy.get('button:contains("Wording")').click()
    cy.get('@highlighter').should('have.attr', 'data-cy-drawnrectangles').then(JSON.parse).its('surrounded')
      .should('deep.equal', [{'left': 56.26098090252517, 'top': 635.5797939314094, 'width': 226.18785085087657, 'height': 154.41985942094743}])

    cy.get('button:contains("Save then back to list")').click()
    cy.location('pathname').should('equal', '/project-xkopqm/textbook-klxufv/page-7')
    cy.get('div.busy', {timeout: 10000}).should('not.exist')

    cy.visit('/project-xkopqm/textbook-klxufv/page-7/exercise-pghtfo')

    cy.get('@getExercise').its('response.body.data.attributes.rectangles').should('deep.equal', [
      {
        'pdf_sha256': 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
        'pdf_page': 2,
        'coordinates': 'pdfjs',
        'start': {
          'x': 56.26098090252517,
          'y': 789.9996533523569
        },
        'stop': {
          'x': 282.44883175340175,
          'y': 725.8392892267519
        },
        'text': 'Recopie les mots suivants, puis\nentoure les pronoms personnels.\nIndique la classe des autres mots.',
        'role': 'instructions',
      },
      {
        'pdf_sha256': 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
        'pdf_page': 2,
        'coordinates': 'pdfjs',
        'start': {
          'x': 62.78563044630046,
          'y': 718.2270426355784
        },
        'stop': {
          'x': 277.0116238002557,
          'y': 698.6526942582752
        },
        'text': 'b. vous ◆ un ◆ arbre ◆ ce',
        'role': 'wording',
      },
      {
        'pdf_sha256': 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
        'pdf_page': 2,
        'coordinates': 'pdfjs',
        'start': {
          'x': 62.78563044630046,
          'y': 703.0025494532315
        },
        'stop': {
          'x': 243.30093449075005,
          'y': 682.3407372771892
        },
        'text': 'c. ils ◆ des ◆ grandir ◆ port',
        'role': 'wording',
      },
      {
        'pdf_sha256': 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
        'pdf_page': 2,
        'coordinates': 'pdfjs',
        'start': {
          'x': 62.78563044630046,
          'y': 686.6905924721455
        },
        'stop': {
          'x': 225.9018690406826,
          'y': 667.1162440948424
        },
        'text': 'd. dessin ◆ tu ◆ aller ◆ mon',
        'role': 'example',
      },
      {
        'pdf_sha256': 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
        'pdf_page': 2,
        'coordinates': 'pdfjs',
        'start': {
          'x': 62.78563044630046,
          'y': 671.4660992897986
        },
        'stop': {
          'x': 237.86372653760395,
          'y': 650.8042871137563
        },
        'text': 'e. elle ◆ gomme ◆ peindre ◆ ces',
        'role': 'clue',
      },
      {
        'pdf_sha256': 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
        'pdf_page': 2,
        'coordinates': 'pdfjs',
        'start': {
            'x': 62.78563044630046,
            'y': 655.1541423087126
        },
        'stop': {
            'x': 237.86372653760395,
            'y': 635.5797939314094
        },
        'text': 'f. histoire ◆ nous ◆ gentil ◆ la',
        'role': 'wording',
      },
    ])
  })
})
