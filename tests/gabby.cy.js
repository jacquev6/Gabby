describe('Gabby', () => {
  before(console.clear)

  after(() => {
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=test-exercises,more-test-exercises')
  })

  it('performs extraction from scratch', () => {
    cy.request('POST', '/reset-for-tests/yes-im-sure')

    cy.visit('/')
    cy.get('select').select('fr')
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
    cy.get('label').contains('Numéro').next().type(5)

    const canvas = cy.get('canvas[style="position: absolute; top: 0px; left: 0px;"]')

    canvas.trigger('pointermove', 5, 5)
    canvas.trigger('pointerdown', 15, 15, { pointerId: 1 })
    canvas.trigger('pointermove', 140, 105)
    canvas.trigger('pointerup', 140, 105, { pointerId: 1 })

    cy.screenshot('doc/textbook-page-create-exercise', {clip: {x: 0, y: 50, width: 670, height: 750}})

    canvas.trigger('pointermove', 5, 5)
    canvas.trigger('pointerdown', 15, 15, { pointerId: 1 })
    canvas.trigger('pointermove', 25, 25)
    canvas.trigger('pointermove', 55, 35)
    canvas.trigger('pointermove', 75, 45)
    canvas.trigger('pointermove', 95, 55)
    canvas.trigger('pointermove', 140, 55)
    canvas.screenshot('doc/textbook-page-selecting-in-pdf', {clip: {x: 0, y: 0, width: 190, height: 75}})
    canvas.trigger('pointerup', 140, 55, { pointerId: 1 })
    cy.screenshot('doc/textbook-page-selected-in-pdf', {clip: {x: 0, y: 0, width: 500, height: 660}})
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
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=test-exercises')

    cy.visit('/')
    cy.get('select').select('fr')

    cy.get('div.busy').should('not.exist')
    cy.screenshot('doc/index', {clip: {x: 0, y: 0, width: 1000, height: 400}})

    cy.get('a:contains("Premier projet de test")').click()

    cy.get('div.busy').should('not.exist')
    cy.screenshot('doc/project', {clip: {x: 0, y: 0, width: 1000, height: 400}})

    cy.get('button:contains("Modifier")').click()

    cy.get('div.busy').should('not.exist')
    cy.screenshot('doc/project-edit', {clip: {x: 0, y: 0, width: 1000, height: 400}})

    cy.get('button:contains("Annuler")').first().click()

    cy.get('input[type=file]').selectFile('../pdf-examples/large.pdf')
    cy.get('label:contains("Titre")').next().type('Français CE2')
    cy.get('label:contains("Éditeur")').next().type('Dunod')
    cy.get('label:contains("Année")').next().type('2021')
    cy.get('label:contains("ISBN")').next().type('01234567890123')

    cy.get('div.busy').should('not.exist')
    cy.screenshot('doc/project-new-textbook', {clip: {x: 0, y: 180, width: 660, height: 600}})

    cy.get('a').contains('Page 6').click()

    cy.get('div.busy').should('not.exist')
    cy.screenshot('doc/textbook-page-pdf-not-loaded', {clip: {x: 0, y: 0, width: 330, height: 330}})
    cy.get('input[type=file]').selectFile('../pdf-examples/test.pdf')

    cy.get('div.busy').should('not.exist')
    cy.screenshot('doc/textbook-page-three-columns', {clip: {x: 0, y: 0, width: 1000, height: 330}})

    cy.get('button').contains('⚙').click()
    cy.get('.modal-content:visible').screenshot('doc/textbook-page-section-editor')

    cy.get('button:contains("Annuler")').click()
    cy.get('h1').contains('Lien entre PDF et manuel').should('not.exist')

    cy.get('div.busy').should('not.exist')
    cy.screenshot('doc/textbook-page-existing-exercises', {clip: {x: 330, y: 50, width: 336, height: 300}})

    cy.get('a:contains("Modifier")').first().click()

    cy.get('div.busy').should('not.exist')
    // https://github.com/cypress-io/cypress/issues/2681#issuecomment-442890537
    cy.get('html').invoke('css', 'height', 'initial')
    cy.get('body').invoke('css', 'height', 'initial')
    // https://github.com/cypress-io/cypress/issues/2681#issuecomment-1120146874
    cy.get('html').invoke('css', 'scroll-behavior', 'auto')
    cy.get('body').invoke('css', 'scroll-behavior', 'auto')
    cy.screenshot('doc/textbook-page-modify-exercise', {clip: {x: 0, y: 50, width: 670, height: 800}})

    cy.get('a:contains("Annuler")').click()
    cy.get('div.busy').should('not.exist')
  })
})
