describe('Gabby\'s project page', () => {
  before(console.clear)

  beforeEach(() => {
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=empty-project')
  })

  after(() => {
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=test-exercises')
  })

  it('displays an error message if the project does not exist', () => {
    cy.visit('/project/0')
    cy.get('div.busy').should('not.exist')

    cy.get('h1:contains("Project not found")').should('exist')
  })

  it('lands', () => {
    cy.visit('/project/1')

    cy.get('h1:contains("Test project")').should('exist')
    cy.get('p:contains("This is a test project, created empty in a fixture.")').should('exist')
  })

  it('edits title and description', () => {
    cy.visit('/project/1')
    cy.get('div.busy').should('not.exist')

    cy.get('h1:contains("Test project") button:contains("Edit")').click()
    cy.get('label:contains("Title")').next().clear().type('New title')
    cy.get('label:contains("Description")').next().clear().type('New description.')
    cy.get('button:contains("Save")').click()

    cy.get('h1:contains("New title")').should('exist')
    cy.get('p:contains("New description.")').should('exist')

    cy.visit('/project/1')
    cy.get('div.busy').should('not.exist')
    cy.get('h1:contains("New title")').should('exist')
    cy.get('p:contains("New description.")').should('exist')
  })
})
