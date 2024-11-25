import { visit, login, loadFixtures, notBusy } from './utils'


describe('Gabby', () => {
  before(console.clear)

  beforeEach(() => {
    loadFixtures('more-test-exercises')
    login()
  })

  it('does not reproduce the bug anymore', () => {
    visit('/project-xkopqm/textbook-klxufv/page-6/new-exercise')

    // User filled the form on page 6, intending to create an exercise on that page.
    cy.get('label:contains("Number")').next().type('42')
    cy.get('label:contains("Instructions")').next().type('Do this')
    // But navigated to page 7 before saving.
    cy.get('p:contains("Page"):contains("(on 7)") :contains(">")').click()
    // Then saved.
    cy.get('button:contains("Save then back to list")').click()  // Created exercise on page 7 as specified, but not as intended by user. This was fixed and now creates the exercise on page 6.
    cy.get('button:contains("Confirm")').click()
    notBusy()
    // User did not notice this was page 7 instead of page 6. (Now on page 6)
    cy.location('pathname').should('eq', '/project-xkopqm/textbook-klxufv/page-6')
    cy.get('li:contains("42"):contains("Do this")').should('exist')

    // User then attempted to create exercise with same number on page 7.
    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')

    cy.get('label:contains("Number")').next().type('42')  // This should have displayed the message "Exercise 42 already exists.", but the request was cached.
    // This UI bug open the door to a constraint violation:
    cy.get('button:contains("Save then back to list")').click()  // BOOM
    // And the bug was reported to the helpless user.
    cy.get('pre').should('not.exist')  // Was: .should('contain', 'Message: Error: Failed to batch: 400')
  })
})
