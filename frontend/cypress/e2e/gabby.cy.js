describe('Gabby', () => {
  it('responds to the root url', () => {
    cy.visit('/')
    cy.contains('h1', 'Gabby')
  })
})
