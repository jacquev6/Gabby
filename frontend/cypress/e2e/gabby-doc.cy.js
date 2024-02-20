describe('Gabby doc', () => {
  it('is accessible from default', () => {
    cy.visit('/')
    cy.get('a').contains('Aide').click()
    cy.contains('h1', 'Documentation de MALIN')
  })

  it('is accessible as path to index', () => {
    cy.visit('/doc/index.html')
    cy.contains('h1', 'Documentation de MALIN')
  })

  // @todo(Project management, soon) Fix this test in prod preview
  // it('is accessible as path to directory with trailing /', () => {
  //   cy.visit('/doc/')
  //   cy.contains('h1', 'Documentation de MALIN')
  // })

  // @todo(Project management, soon) Fix this test in prod preview
  // it('is accessible as path to directory without trailing /', () => {
  //   cy.visit('/doc')
  //   cy.contains('h1', 'Documentation de MALIN')
  // })
})
