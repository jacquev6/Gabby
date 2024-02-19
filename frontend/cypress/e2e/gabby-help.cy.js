describe('Gabby help', () => {
  it('is accessible from default', () => {
    cy.visit('/')
    cy.get('a').contains('Aide').click()
    cy.contains('h1', 'Documentation utilisateur')
  })

  it('is accessible directly without trailing /', () => {
    cy.visit('/help')
    cy.contains('h1', 'Documentation utilisateur')
  })

  it('is accessible directly with trailing /', () => {
    cy.visit('/help/')
    cy.contains('h1', 'Documentation utilisateur')
  })
})
