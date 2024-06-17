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

describe('Gabby\'s index view', () => {
  before(console.clear)

  beforeEach(() => {
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=admin-user')
  })

  after(() => {
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=more-test-exercises')
  })

  it('lands', () => {
    cy.visit('/')
    login()

    cy.get('div.busy').should('not.exist')
    cy.get('p').should('contain', 'No projects')
    cy.title().should('eq', 'MALIN')
  })

  it('enables the "Create project" button', () => {
    cy.visit('/')
    login()

    cy.get('button:contains("Create project")').should('be.disabled')

    cy.get('label:contains("Title")').next().type('Test project')

    cy.get('button:contains("Create project")').should('be.enabled')

    cy.get('label:contains("Title")').next().clear()

    cy.get('button:contains("Create project")').should('be.disabled')
  })

  it('creates a minimal project', () => {
    cy.visit('/')
    login()

    cy.get('label:contains("Title")').next().type('Test project')
    cy.get('button:contains("Create project")').click()

    cy.get('h1:contains("Test project")').should('exist')

    cy.visit('/')

    cy.get('li a:contains("Test project")').should('exist')
  })

  it('creates a full project', () => {
    cy.visit('/')
    login()

    cy.get('label:contains("Title")').next().type('Test project')
    cy.get('label:contains("Description")').next().type('This is a test project')
    cy.get('button:contains("Create project")').click()

    cy.get('h1:contains("Test project")').should('exist')
    cy.get('p:contains("This is a test project")').should('exist')

    cy.visit('/')

    cy.get('li a:contains("Test project")').should('exist')
  })

  it('navigates to user documentation', () => {
    cy.visit('/')
    login()

    cy.get('a:contains("Help")').click()
    cy.contains('h1', 'Documentation de MALIN')
  })
})
