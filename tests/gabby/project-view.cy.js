describe('Gabby\'s project view', () => {
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
    cy.title().should('eq', 'MALIN')
  })

  it('lands', () => {
    cy.visit('/project/1')

    cy.get('h1:contains("Test project")').should('exist')
    cy.title().should('eq', 'MALIN - Test project')
    cy.get('p:contains("This is a test project, created empty in a fixture.")').should('exist')
    cy.get('.navbar').should('contain', 'Test project')
    cy.get('h2:contains("New textbook")').should('exist')
    cy.get('h2:contains("New independent exercise")').should('exist')
    cy.get('h2:contains("Existing textbooks and exercises")').should('exist')
  })

  it('edits title and description', () => {
    cy.visit('/project/1')

    cy.get('h1:contains("Test project") button:contains("Edit")').click()
    cy.get('label:contains("Title")').first().next().clear().type('New title')
    cy.get('label:contains("Description")').next().clear().type('New description.')
    cy.get('button:contains("Save")').click()

    cy.get('h1:contains("New title")').should('exist')
    cy.title().should('eq', 'MALIN - New title')
    cy.get('p:contains("New description.")').should('exist')

    cy.visit('/project/1')
    cy.get('h1:contains("New title")').should('exist')
    cy.title().should('eq', 'MALIN - New title')
    cy.get('p:contains("New description.")').should('exist')
  })

  it('refuses to empty title', () => {
    cy.visit('/project/1')

    cy.get('h1:contains("Test project") button:contains("Edit")').click()
    cy.get('label:contains("Title")').first().next().clear()
    cy.get('button:contains("Save")').should('be.disabled')
  })

  it('enables the "Create textbook" button', () => {
    cy.visit('/project/1')
    cy.get('button:contains("Create textbook")').should('be.disabled')

    cy.get('label:contains("Title")').next().type('Test textbook')
    cy.get('button:contains("Create textbook")').should('be.disabled')

    cy.get('input[type=file]').selectFile('../pdf-examples/test.pdf')
    cy.get('button:contains("Create textbook")').should('be.disabled')

    cy.get('label:contains("Title")').next().type('Test textbook')
    cy.get('button:contains("Create textbook")').should('be.enabled')

    cy.get('label:contains("Title")').next().clear()
    cy.get('button:contains("Create textbook")').should('be.disabled')
  })

  it('creates a minimal textbook', () => {
    cy.visit('/project/1')

    cy.get('input[type=file]').selectFile('../pdf-examples/test.pdf')
    cy.get('label:contains("Title")').next().type('Test textbook')
    cy.get('button:contains("Create textbook")').click()

    cy.get('p:contains("No exercises yet")').should('exist')

    cy.visit('/project/1')

    cy.get('h3:contains("Test textbook")').should('exist')
  })

  it('creates a full textbook', () => {
    cy.visit('/project/1')

    cy.get('input[type=file]').selectFile('../pdf-examples/test.pdf')
    cy.get('label:contains("Title")').next().type('Test textbook')
    cy.get('label:contains("Publisher")').next().type('Test publisher')
    cy.get('label:contains("Year")').next().type('2024')
    cy.get('label:contains("ISBN")').next().type('1234567890123')
    cy.get('button:contains("Create textbook")').click()

    cy.get('p:contains("No exercises yet")').should('exist')

    cy.visit('/project/1')

    cy.get('h3:contains("Test textbook, Test publisher (2024)")').should('exist')
  })

  it('creates two textbooks from the same PDF', () => {
    cy.visit('/project/1')
    cy.get('input[type=file]').selectFile('../pdf-examples/test.pdf')
    cy.get('label:contains("Title")').next().type('First textbook')
    cy.get('button:contains("Create textbook")').click()
    cy.get('p:contains("No exercises yet")').should('exist')
    cy.visit('/project/1')

    cy.get('input[type=file]').selectFile('../pdf-examples/test.pdf')
    cy.get('label:contains("Title")').next().type('Second textbook')
    cy.get('button:contains("Create textbook")').click()
    cy.get('p:contains("No exercises yet")').should('exist')

    cy.visit('/project/1')
    cy.get('h3:contains("First textbook")').should('exist')
    cy.get('h3:contains("Second textbook")').should('exist')
  })

  it('lists textbooks and exercises', () => {
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=test-exercises')

    cy.visit('/project/1')

    cy.get('h3:contains("Français CE2, Slabeuf (2021)")').should('exist')
    cy.get('a:contains("Français CE2")').should('exist')
    cy.get('li a:contains("Page 6")').should('exist')
    cy.get('li:contains("Page 6") ul li:contains("3 : Complète avec : le, une, …")').should('exist')
    cy.get('li:contains("Page 6") ul li:contains("4 : Écris une phrase en respe…")').should('exist')
    cy.get('li a:contains("Page 7")').should('exist')
    cy.get('li:contains("Page 7") ul li:contains("9 : Recopie l’intrus qui se c…")').should('exist')
  })

  it('lists independent exercises', () => {
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=test-exercises')

    cy.visit('/project/2')
    cy.get('li:contains("L1 : Faire des choses intellig…")').should('exist')
    cy.get('li:contains("L2 : Faire d\'autres choses int…")').should('exist')
    cy.get('li:contains("L3 : Prendre le temps de faire…")').should('exist')
  })

  it('enables the "Create exercise" button', () => {
    cy.visit('/project/1')
    cy.get('button:contains("Create exercise")').should('be.disabled')

    cy.get('label:contains("Number")').next().type('a')

    cy.get('button:contains("Create exercise")').should('be.enabled')

    cy.get('label:contains("Number")').next().clear()

    cy.get('button:contains("Create exercise")').should('be.disabled')
  })

  it('creates a minimal independent exercise', () => {
    cy.visit('/project/1')

    cy.get('label:contains("Number")').next().type('10')
    cy.get('label:contains("Instructions")').next().type('Do something smart.')
    cy.get('button:contains("Create exercise")').click()

    cy.get('div.busy').should('not.exist')

    cy.get('label:contains("Number")').next().should('have.value', '11')

    cy.get('li:contains("10 : Do something smart.")').should('exist')
  })

  it('creates a full independent exercise', () => {
    cy.visit('/project/1')

    cy.get('label:contains("Number")').next().type('L10')
    cy.get('label:contains("Instructions")').next().type('Do the smartest thing ever.')
    cy.get('label:contains("Wording")').next().type('The wording')
    cy.get('p:contains("Example")').click()
    cy.focused().type('The example')
    cy.get('p:contains("Clue")').click()
    cy.focused().type('The clue')
    cy.get('button:contains("Create exercise")').click()

    cy.get('div.busy').should('not.exist')

    cy.get('label:contains("Number")').next().should('have.value', '')

    cy.get('li:contains("L10 : Do the smartest thing eve…")').should('exist')
  })

  // @todo Edit independent exercise
})
