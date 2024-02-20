describe('Vue router', () => {
  it('is accessible directly without trailing /', () => {
    cy.visit('/other')
    cy.contains('h1', 'Other View')
  })

  it('is accessible directly with trailing /', () => {
    cy.visit('/other/')
    cy.contains('h1', 'Other View')
  })
})
