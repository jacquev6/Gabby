const isProdPreview = Cypress.env('IS_PROD_PREVIEW')

function login() {
  cy.get('select').last().select('en')
  cy.get('h1:contains("Please log in")').should('exist')
  cy.get('[name=username]').type('admin')  // This often leaves the field with just the few characters, e.g. 'adm'. I can't figure out why; probably some race condition.
  cy.get('[name=password]').type('password')
  cy.get('[name=username]').type('{selectall}admin')  // This is a workaround for the above issue.
  cy.get('[name=username]').should('have.value', 'admin')
  cy.get('button:contains("Log in")').click()
  cy.get('h1:contains("Please log in")').should('not.exist')
}

describe('Gabby has routes that', () => {
  before(() => {
    console.clear()
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=admin-user,test-exercises')
  })

  it('can access the default Vue Router view', () => {
    cy.visit('/')
    login()
    cy.contains('h1', 'Existing projects')
  })

  it('can access a Vue Router view without trailing /', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-6')
    login()
    cy.contains('h1', 'Edition')
  })

  it('can access a Vue Router view with trailing /', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-6/')
    login()
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

  it('can access API docs without trailing /', () => {
    cy.visit('/api/docs')
    cy.contains('h2', 'FastAPI')
  })

  it('can access API docs with trailing /', () => {
    cy.visit('/api/docs/')
    cy.contains('h2', 'FastAPI')
  })

  it('can assess Adminer without trailing /', () => {
    cy.visit('/api/adminer')
    cy.contains('h1', 'Adminer')
  })

  it('can assess Adminer with trailing /', () => {
    cy.visit('/api/adminer/')
    cy.contains('h1', 'Adminer')
  })
})
