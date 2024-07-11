import { useApiStore } from '../frontend/src/frontend/stores/api'


function setLocale() {
  cy.get('select').last().select('en')
}

describe('Gabby has routes that', () => {
  before(() => {
    console.clear
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=admin-user,test-exercises')
  })

  beforeEach(() => {
    cy.wrap(useApiStore()).then(api => api.auth.login('admin', 'password'))
  })

  it('can access the default Vue Router view', () => {
    cy.visit('/')
    setLocale()
    cy.contains('h1', 'Existing projects')
  })

  it('can access a Vue Router view without trailing /', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-6')
    setLocale()
    cy.contains('h1', 'Existing exercises')
  })

  it('can access a Vue Router view with trailing /', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-6/')
    setLocale()
    cy.contains('h1', 'Existing exercises')
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
