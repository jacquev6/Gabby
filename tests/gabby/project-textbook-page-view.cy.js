describe('Gabby\'s project\'s textbook page view', () => {
  before(console.clear)

  beforeEach(() => {
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=test-exercises')
  })

  after(() => {
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=test-exercises')
  })

  it('displays an error message if the project does not exist', () => {
    cy.visit('/project/0/textbook/1/page/6')
    cy.get('div.busy').should('not.exist')

    cy.get('h1:contains("Project not found")').should('exist')
    cy.title().should('eq', 'MALIN')
  })

  it('displays an error message if the textbook does not exist', () => {
    cy.visit('/project/1/textbook/0/page/6')
    cy.get('div.busy').should('not.exist')

    cy.get('h1:contains("Textbook not found")').should('exist')
    cy.title().should('eq', 'MALIN')
  })

  it('displays an error message if the textbook does not belong to this project', () => {
    cy.visit('/project/2/textbook/1/page/6')
    cy.get('div.busy').should('not.exist')

    cy.get('h1:contains("Textbook not found")').should('exist')
    cy.title().should('eq', 'MALIN')
  })

  // @todo Add test where the page is a negative number
  // @todo Add test where the page is larger than the textbook's number of pages
  // @todo Add test where the page is not a number

  it('lands', () => {
    cy.visit('/project/1/textbook/1/page/6')

    cy.title().should('eq', 'MALIN - Premier projet de test - Français CE2 - Page 6')
    cy.get('.navbar').should('contain', 'Premier projet de test')
    cy.get('.navbar').should('contain', 'Français CE2')
  })

  it('adjusts textarea heights', () => {
    cy.visit('/project/1/textbook/1/page/6')
    cy.get('button:contains("New exercise")').click()
    cy.get('p:contains("Example")').click()
    cy.get('p:contains("Clue")').click()

    for (const label of ['Instructions', 'Example', 'Clue', 'Wording']) {
      cy.get(`label:contains("${label}")`).next().should('have.attr', 'rows', '2')
      cy.get(`label:contains("${label}")`).next().type('a\nb\nc\nd')
      cy.get(`label:contains("${label}")`).next().should('have.attr', 'rows', '5')
    }
  })
})
