describe('Gabby', () => {
  before(console.clear)

  after(() => {
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=test-exercises,more-test-exercises')
  })

  it('performs extraction from scratch', () => {
    cy.request('POST', '/reset-for-tests/yes-im-sure')

    cy.visit('/')
    cy.get('select').select('fr')
    cy.get('select').blur()
    cy.get('div.busy').should('not.exist')

    cy.get('label:contains("Titre")').next().type('Projet de test')
    cy.get('button:contains("Créer")').click()
    cy.get('div.busy').should('not.exist')

    cy.get('input[type=file]').selectFile('../pdf-examples/test.pdf')
    cy.get('label:contains("Titre")').next().type('Français CE2')
    cy.get('label:contains("Éditeur")').next().type('Slabeuf')
    cy.get('label:contains("Année")').next().type('2021')
    cy.get('label:contains("ISBN")').next().type('01234567890123')
    cy.get('button:contains("Créer")').click()
    cy.get('div.busy').should('not.exist')

    cy.get('button').contains('⚙').click()
    cy.get('label').contains('Début dans le manuel').next().type('{selectAll}5')
    cy.get('button').contains('Enregistrer').click()
    cy.get('div.busy').should('not.exist')

    cy.get('label').contains('Page').click()
    cy.focused().type('{selectAll}6')
    cy.get('div.busy').should('not.exist')

    cy.get('a:contains("Nouvel exercice")').click()
    cy.get('label').contains('Numéro').next().type(5).blur()

    const canvas = cy.get('canvas[style="position: absolute; top: 0px; left: 0px;"]')

    canvas.trigger('pointermove', 5, 5)
    canvas.trigger('pointerdown', 15, 15, { pointerId: 1 })
    canvas.trigger('pointermove', 140, 105)
    canvas.screenshot('project-textbook-page-exercise/create-exercise-tracing-bounding-rectangle', {clip: {x: 0, y: 0, width: 1000, height: 200}})
    canvas.trigger('pointerup', 140, 105, { pointerId: 1 })

    cy.screenshot('project-textbook-page-exercise/create-exercise', {clip: {x: 0, y: 50, width: 575, height: 750}})

    canvas.trigger('pointermove', 5, 5)
    canvas.trigger('pointerdown', 20, 20, { pointerId: 1 })
    canvas.trigger('pointermove', 25, 25)
    canvas.trigger('pointermove', 55, 35)
    canvas.trigger('pointermove', 75, 45)
    canvas.trigger('pointermove', 95, 55)
    canvas.trigger('pointermove', 135, 55)
    canvas.screenshot('project-textbook-page-exercise/selecting-in-pdf', {clip: {x: 0, y: 0, width: 190, height: 75}})
    canvas.trigger('pointerup', 135, 55, { pointerId: 1 })
    cy.screenshot('project-textbook-page-exercise/selected-in-pdf', {clip: {x: 0, y: 0, width: 500, height: 660}})
    cy.get('button').contains('Consigne').click()

    canvas.trigger('pointerdown', 15, 45, { pointerId: 1 })
    canvas.trigger('pointerup', 140, 105, { pointerId: 1 })
    cy.get('button').contains('Énoncé').click()

    cy.get('button').contains('Enregistrer').click()
    cy.get('div.busy').should('not.exist')
    cy.get('a:contains("Annuler")').click()
    cy.get('div.busy').should('not.exist')

    cy.get('li').contains('Recopie les mots suivants').should('exist')
  })

  it('loads existing data', () => {
    cy.viewport(1000, 1000)

    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=test-exercises')

    cy.visit('/')
    cy.get('select').select('fr')
    cy.get('select').blur()
    cy.get('div.busy').should('not.exist')

    cy.screenshot('index/index', {clip: {x: 0, y: 0, width: 1000, height: 350}})

    cy.get('a:contains("Premier projet de test")').click()

    cy.get('div.busy').should('not.exist')
    cy.screenshot('project/project', {clip: {x: 0, y: 0, width: 1000, height: 450}})

    cy.get('button:contains("Modifier")').click()

    cy.get('div.busy').should('not.exist')
    cy.screenshot('project/edit', {clip: {x: 0, y: 0, width: 1000, height: 400}})

    cy.get('button:contains("Annuler")').first().click()

    cy.get('input[type=file]').selectFile('../pdf-examples/large.pdf')
    cy.get('label:contains("Titre")').next().type('Français CE2')
    cy.get('label:contains("Éditeur")').next().type('Dunod')
    cy.get('label:contains("Année")').next().type('2021')
    cy.get('label:contains("ISBN")').next().type('01234567890123')

    cy.get('div.busy').should('not.exist')
    cy.screenshot('project/new-textbook', {clip: {x: 0, y: 220, width: 660, height: 600}})

    cy.get('a').contains('Page 6').click()

    cy.get('div.busy').should('not.exist')
    cy.screenshot('project-textbook-page/pdf-not-loaded', {clip: {x: 0, y: 0, width: 330, height: 330}})
    cy.get('input[type=file]').selectFile('../pdf-examples/test.pdf')

    cy.get('div.busy').should('not.exist')

    cy.get('button').contains('⚙').click()
    cy.get('.modal-content:visible').screenshot('project-textbook-page/section-editor')

    cy.get('button:contains("Annuler")').click()
    cy.get('h1').contains('Lien entre PDF et manuel').should('not.exist')

    cy.get('div.busy').should('not.exist')
    cy.screenshot('project-textbook-page/project-textbook-page', {clip: {x: 0, y: 0, width: 1000, height: 400}})
    cy.screenshot('project-textbook-page/existing-exercises', {clip: {x: 330, y: 50, width: 500, height: 250}})
    cy.get('canvas').last().screenshot('project-textbook-page/existing-exercises-in-pdf', {clip: {x: 0, y: 233, width: 1000, height: 1000}})

    cy.get('a:contains("Modifier")').first().click()

    cy.get('div.busy').should('not.exist')
    cy.get('label:contains("Énoncé")').next().type('{selectAll}... vide\n... vident')
    // Image is cropped to 670px height in headless mode. I don't know why.
    cy.screenshot('project-textbook-page-exercise/modify-exercise', {clip: {x: 0, y: 50, width: 575, height: 1000}})

    cy.get('label:contains("Remplacer")').next().type('{selectAll}{backspace}')
    cy.get('label:contains("dans")').next().select('everywhere').blur()
    cy.screenshot('project-textbook-page-exercise/tools', {clip: {x: 560, y: 0, width: 210, height: 500}})

    cy.get('label:contains("Type d\'adaptation")').next().select('selectThingsAdaptation')
    cy.get('div.busy').should('exist')  // This may fail (race condition) but is required because the 'div.busy' is not displayed quickly enough.
    cy.get('div.busy').should('not.exist')
    cy.screenshot('project-textbook-page-exercise/project-textbook-page-exercise', {clip: {x: 0, y: 0, width: 1000, height: 330}})
  })
})
