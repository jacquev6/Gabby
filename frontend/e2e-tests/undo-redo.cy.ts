import { loadFixtures, login, visit } from './utils'


describe('Gabby', () => {
  before(() => {
    console.clear()
  })

  beforeEach(() => {
    loadFixtures('more-test-exercises')
    login()
  })

  function expectUndoRedoHistory(undo: number, redo: number) {
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

  function expectStableUndoRedoHistory(undo: number, redo: number) {
    expectUndoRedoHistory(undo, redo)
    cy.wait(1500)  // Wait because the history is debounced: it can push a new snapshot in the undo queue during a 1s period.
    expectUndoRedoHistory(undo, redo)
  }

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

  it('has "undo/redo" on new exercise', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')

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

    cy.get('label:contains("Instructions")').next().type('First')
    expectUndoRedoHistory(2, 0)
    cy.get('label:contains("Instructions")').next().type('Second')
    cy.get('label:contains("Instructions")').next().should('have.text', 'FirstSecond')
    expectUndoRedoHistory(3, 0)
    cy.get('@undo').click()
    expectUndoRedoHistory(2, 1)
    cy.get('label:contains("Instructions")').next().should('have.text', 'First')
    cy.get('@undo').click()
    expectUndoRedoHistory(1, 2)
    cy.get('label:contains("Instructions")').next().should('have.text', '')
    cy.get('@redo').click()
    expectUndoRedoHistory(2, 1)
    cy.get('label:contains("Instructions")').next().should('have.text', 'First')
    cy.get('label:contains("Instructions")').next().type('Third')
    cy.get('label:contains("Instructions")').next().should('have.text', 'FirstThird')
    expectUndoRedoHistory(3, 0)
    cy.get('@undo').click()
    expectUndoRedoHistory(2, 1)
    cy.get('label:contains("Instructions")').next().should('have.text', 'First')
    cy.get('@redo').click()
    expectUndoRedoHistory(3, 0)
    cy.get('label:contains("Instructions")').next().should('have.text', 'FirstThird')

    // @todo Test that undo/redo works on all fields (incl. bounding rectangle, adaptation type, etc.)
  })

  it('has "undo/redo" using Ctrl+Z/Ctrl+Y', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')

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
    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')

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
    cy.get('label:contains("Instructions")').next().should('have.text', '')
    cy.get('@redo').click()
    expectUndoRedoHistory(1, 0)
    cy.get('label:contains("Number")').next().should('have.value', '12')  // Unchanged by 'redo'
    cy.get('label:contains("Instructions")').next().should('have.text', 'Blah blah')
  })

  it('clears "undo/redo" history on save', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')

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
    cy.get('label:contains("Instructions")').next().should('have.text', '')
    cy.get('@redo').click()
    expectUndoRedoHistory(1, 0)
    cy.get('label:contains("Number")').next().should('have.value', '13')  // Unchanged by 'redo'
    cy.get('label:contains("Instructions")').next().should('have.text', 'Blah blah')
  })

  it('clears "undo/redo" history when navigating exercise creation history', () => {
    cy.viewport(1000, 800)

    visit('/project-xkopqm/textbook-klxufv/page-5/new-exercise')

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
    visit('/project-xkopqm/textbook-klxufv/page-7/exercise-dymwin')

    expectStableUndoRedoHistory(0, 0)

    cy.get('label:contains("Instructions")').next().should('have.text', 'Ajoute le suffixe –eur aux verbes.Indique la classe des mots fabriqués.')
    cy.get('label:contains("Instructions")').next().type('{selectall}Blah blah')
    expectUndoRedoHistory(1, 0)

    cy.get('button:contains("Undo")').click()
    expectUndoRedoHistory(0, 1)
    cy.get('label:contains("Instructions")').next().should('have.text', 'Ajoute le suffixe –eur aux verbes.Indique la classe des mots fabriqués.')
  })

  it('has a *single* "undo/redo" history even for WYSIWYG fields', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/exercise-xnyegk')

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
})
