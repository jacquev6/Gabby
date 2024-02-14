describe('Gabby', () => {
  it('responds to the root url', () => {
    cy.visit('/')
    cy.contains('nav', 'MALIN')
    cy.screenshot('three-columns')
  })
})
