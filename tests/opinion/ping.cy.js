describe('Ping', () => {
  beforeEach(() => {
    cy.request('POST', '/reset-for-tests/yes-im-sure')
  })

  after(() => {
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=test-exercises,more-test-exercises')
  })

  it('accesses the route without trailing slash', () => {
    cy.visit('/ping')
    cy.contains('h1', 'Pings')
  })

  it('accesses the route with a trailing slash', () => {
    cy.visit('/ping/')
    cy.contains('h1', 'Pings')
  })

  it('pings', () => {
    cy.visit('/ping/')

    cy.get('li button').should('not.exist')

    cy.get('button').contains('Ping').click()

    cy.get('li button').should('exist')
  })
});
