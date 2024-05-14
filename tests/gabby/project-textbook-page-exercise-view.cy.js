describe('Gabby\'s project\'s textbook page exercise view', () => {
  it('replaces all', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-7/exercise-dymwin')

    cy.get('label:contains("Wording")').next().should('have.value', 'nager ➞ … ◆ tracter ➞ … ◆ manger ➞ … ◆\ninventer ➞ … ◆ livrer ➞ …')

    cy.get('label:contains("Replace")').next().type('{line-end}', {parseSpecialCharSequences: false})
    cy.get('label:contains("With")').next().type(' ')
    cy.get('button:contains("Apply")').click()

    cy.get('label:contains("Wording")').next().should('have.value', 'nager ➞ … ◆ tracter ➞ … ◆ manger ➞ … ◆ inventer ➞ … ◆ livrer ➞ …')
    cy.get('label:contains("Replace")').next().should('have.value', '')
    cy.get('label:contains("With")').next().should('have.value', '')

    cy.get('label:contains("Replace")').next().type(' ◆ ')
    cy.get('label:contains("With")').next().type('{line-end}', {parseSpecialCharSequences: false})
    cy.get('button:contains("Apply")').click()

    cy.get('label:contains("Wording")').next().should('have.value', 'nager ➞ …\ntracter ➞ …\nmanger ➞ …\ninventer ➞ …\nlivrer ➞ …')
  })

  function select(selector, start, end) {
    cy.get(selector)
      .type('{moveToStart}')
      .then(el => el[0].setSelectionRange(start, end))
  }

  it('gets its selection from the form', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-7/exercise-dymwin')

    cy.get('label:contains("Instructions")').next().as('instructions')
    cy.get('label:contains("Wording")').next().as('wording')

    cy.get('label:contains("Replace")').next().should('have.value', '')

    select('@instructions', 0, 5)
    cy.get('label:contains("Replace")').next().should('have.value', 'Ajout')

    select('@wording', 9, 12)
    cy.get('label:contains("Replace")').next().should('have.value', ' ◆ ')

    // Empty selection is not propagated
    select('@wording', 7, 7)
    cy.get('label:contains("Replace")').next().should('have.value', ' ◆ ')

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
})
