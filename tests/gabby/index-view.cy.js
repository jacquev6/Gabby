import { useApiStore } from '../../frontend/src/frontend/stores/api'


function setLocale() {
  cy.get('select[data-cy="language"]').last().select('en')
}

describe('Gabby\'s index view', () => {
  before(console.clear)

  beforeEach(() => {
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=admin-user')
    cy.wrap(useApiStore()).then(api => api.auth.login('admin', 'password'))
  })

  it('lands', () => {
    cy.visit('/')
    setLocale()

    cy.get('div.busy').should('not.exist')
    cy.get('p').should('contain', 'No projects')
    cy.title().should('eq', 'MALIN')
  })

  it('enables the "Create project" button', () => {
    cy.visit('/')
    setLocale()

    cy.get('button:contains("Create project")').should('be.disabled')

    cy.get('label:contains("Title")').next().type('Test project')

    cy.get('button:contains("Create project")').should('be.enabled')

    cy.get('label:contains("Title")').next().clear()

    cy.get('button:contains("Create project")').should('be.disabled')
  })

  it('creates a minimal project', () => {
    cy.visit('/')
    setLocale()

    cy.get('label:contains("Title")').next().type('Test project')
    cy.get('button:contains("Create project")').click()

    cy.get('h1:contains("Test project")').should('exist')

    cy.visit('/')
    setLocale()

    cy.get('li a:contains("Test project")').should('exist')
  })

  it('creates a full project', () => {
    cy.visit('/')
    setLocale()

    cy.get('label:contains("Title")').next().type('Test project')
    cy.get('label:contains("Description")').next().type('This is a test project')
    cy.get('button:contains("Create project")').click()

    cy.get('h1:contains("Test project")').should('exist')
    cy.get('p:contains("This is a test project")').should('exist')

    cy.visit('/')
    setLocale()

    cy.get('li a:contains("Test project")').should('exist')
  })

  it('navigates to user documentation', () => {
    cy.visit('/')
    setLocale()

    cy.get('a:contains("Help")').click()
    cy.contains('h1', 'Documentation de MALIN')
  })
})
