import { visit, login, loadFixtures } from './utils'


describe('Gabby', () => {
  before(console.clear)

  beforeEach(() => {
    loadFixtures('admin-user')
    login()
  })

  it('lists no projects', () => {
    visit('/')

    cy.get('p').should('contain', 'No projects')
    cy.title().should('eq', 'MALIN')
  })

  it('enables the "Create project" button', () => {
    visit('/')

    cy.get('button:contains("Create project")').should('be.disabled')

    cy.get('label:contains("Title")').next().type('Test project')

    cy.get('button:contains("Create project")').should('be.enabled')

    cy.get('label:contains("Title")').next().clear()

    cy.get('button:contains("Create project")').should('be.disabled')
  })

  it('creates a minimal project', () => {
    visit('/')

    cy.get('label:contains("Title")').next().type('Test project')
    cy.get('button:contains("Create project")').click()

    cy.get('h1:contains("Test project")').should('exist')

    visit('/')

    cy.get('li a:contains("Test project")').should('exist')
  })

  it('creates a full project', () => {
    visit('/')

    cy.get('label:contains("Title")').next().type('Test project')
    cy.get('label:contains("Description")').next().type('This is a test project')
    cy.get('button:contains("Create project")').click()

    cy.get('h1:contains("Test project")').should('exist')
    cy.get('p:contains("This is a test project")').should('exist')

    visit('/')

    cy.get('li a:contains("Test project")').should('exist')
  })
})
