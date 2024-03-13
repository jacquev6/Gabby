describe('Gabby has routes that', () => {
  before(console.clear)

  it('can access the default Vue Router view', () => {
    cy.visit('/')
    cy.contains('h1', 'Existing projects')
  })

  it('can access a Vue Router view without trailing /', () => {
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=test-exercises')

    cy.visit('/project/1/textbook/1/page/6')
    cy.get('select').select('en')
    cy.contains('h1', 'Edition')
  })

  it('can access a Vue Router view with trailing /', () => {
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=test-exercises')

    cy.visit('/project/1/textbook/1/page/6/')
    cy.get('select').select('en')
    cy.contains('h1', 'Edition')
  })

  it('can access Vue statics', () => {
    cy.request('/logo-cartable-fantastique.png').then(response => {
      expect(response.headers['content-type']).to.equal('image/png')
    })
  })

  it('can access its documentation as path to index file', () => {
    cy.visit('/doc/index.html')
    cy.contains('h1', 'Documentation de MALIN')
  })

  it('can access its documentation as path to directory with trailing /', () => {
    cy.visit('/doc/')
    cy.contains('h1', 'Documentation de MALIN')
  })

  it('can access its documentation as path to directory without trailing /', () => {
    cy.visit('/doc')
    cy.contains('h1', 'Documentation de MALIN')
  })

  it('can access Django API without trailing /', () => {
    cy.visit('/api')
    cy.contains('h1', 'Api Root')
  })

  it('can access Django API with trailing /', () => {
    cy.visit('/api/')
    cy.contains('h1', 'Api Root')
  })

  it('can access Django admin without trailing /', () => {
    cy.visit('/api/admin')
    cy.contains('header', 'Django administration')
  })

  it('can access Django admin with trailing /', () => {
    cy.visit('/api/admin/')
    cy.contains('header', 'Django administration')
  })

  it('can access Django statics', () => {
    cy.request('/api/static/admin/css/base.css').then(response => {
      expect(response.headers['content-type']).to.equal('text/css')
    })
  })
})
