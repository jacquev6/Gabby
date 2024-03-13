describe('Gabby', () => {
  before(console.clear)

  after(() => {
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=test-exercises')
  })

  it('performs extraction from scratch', () => {
    cy.request('POST', '/reset-for-tests/yes-im-sure')

    cy.visit('/')
    cy.get('select').select('fr')

    cy.get('.spinner-border').should('not.exist')

    cy.get('p').contains('Aucun projet pour le moment').should('exist')
    cy.get('button').contains('Créer').should('be.disabled')
    cy.get('label').contains('Titre').next().type('Projet de test')
    cy.get('label').contains('Description').next().type('Quelques exercices de Slabeuf.')
    cy.get('button').contains('Créer').should('be.enabled').click()

    cy.get('.spinner-border').should('not.exist')

    cy.get('p').contains('Aucun exercice pour le moment').should('exist')
    cy.get('button').contains('Créer').should('be.disabled')
    cy.get('input[type=file]').selectFile('../pdf-examples/test.pdf')
    cy.get('label').contains('Titre').next().type('Français CE2')
    cy.get('label').contains('Éditeur').next().type('Slabeuf')
    cy.get('label').contains('Année').next().type('2021')
    cy.get('label').contains('ISBN').next().type('01234567890123')
    cy.get('button').contains('Créer').should('be.enabled').click()

    cy.get('.spinner-border').should('not.exist')

    // cy.screenshot('doc/index-new-pdf', { clip: { x: 0, y: 200, width: 666, height: 400 } })

    // cy.get('input[type=file]').should('have.value', 'C:\\fakepath\\test.pdf').should('be.enabled')
    // cy.get('button').contains('<').should('be.disabled')
    // cy.get('input.number-no-spin').should('have.value', '1').should('be.enabled')
    // cy.get('button').contains('>').should('be.enabled')

    // cy.get('button').contains('>').click()
    // cy.get('.spinner-border').should('not.exist')

    // cy.get('input[type=file]').should('have.value', 'C:\\fakepath\\test.pdf').should('be.enabled')
    // cy.get('button').contains('<').should('be.enabled')
    // cy.get('input.number-no-spin').should('have.value', '2').should('be.enabled')
    // cy.get('button').contains('>').should('be.disabled')

    // cy.get('button').contains('Nouveau manuel').click()

    // cy.get('label').contains('Titre').next().type('Français CE2')
    // cy.get('label').contains('Éditeur').next().type('Slabeuf')
    // cy.get('label').contains('Année').next().type('2021')
    // cy.get('label').contains('ISBN').next().type('01234567890123')

    // cy.screenshot('doc/index-new-textbook-form', { clip: { x: 0, y: 200, width: 666, height: 600 } })

    // cy.get('button').contains('Enregistrer').click()

    // cy.get('a').contains('les pages 1 à 2 de Français CE2, Slabeuf, 2021').should('exist')
    // cy.screenshot('doc/index-columns', { clip: { x: 0, y: 0, width: 1000, height: 400 } })

    // cy.get('a').contains('les pages 1 à 2 de Français CE2, Slabeuf, 2021').click()

    cy.get('h1').contains('Lien entre PDF et manuel').should('not.exist')
    cy.get('button').contains('⚙').click()
    cy.get('h1').contains('Lien entre PDF et manuel').should('exist')
    cy.get('button').contains('Enregistrer').should('be.enabled')

    // cy.get('.modal-content:visible').screenshot('doc/textbook-page-section-editor')

    cy.get('label').contains('Début dans le manuel').next().type('{selectAll}5')
    cy.get('button').contains('Enregistrer').click()
    cy.get('h1').contains('Lien entre PDF et manuel').should('not.exist')

    cy.get('label').contains('Page').click()
    cy.focused().type('{selectAll}6')

    cy.get('.spinner-border').should('not.exist')

    cy.get('p').contains('Pas encore d\'exercices').should('exist')

    cy.get('button').contains('Nouvel exercice').click()

    cy.get('button').contains('<').should('be.disabled')
    cy.get('input.number-no-spin').should('have.value', '6').should('be.disabled')
    cy.get('button').contains('>').should('be.disabled')
    cy.get('button').contains('Annuler').should('be.enabled')
    cy.get('button').contains('Enregistrer').should('be.disabled')

    cy.get('label').contains('Numéro').next().type(5)

    // cy.screenshot('doc/create-exercise')

    cy.get('button').contains('Enregistrer').should('be.enabled')

    const canvas = cy.get('canvas[style="position: absolute; top: 0px; left: 0px;"]')

    canvas.trigger('pointermove', 5, 5)
    canvas.trigger('pointerdown', 15, 15, { pointerId: 1 })
    canvas.trigger('pointermove', 25, 25)
    canvas.trigger('pointermove', 55, 35)
    canvas.trigger('pointermove', 75, 45)
    canvas.trigger('pointermove', 95, 55)
    canvas.trigger('pointermove', 140, 55)
    // canvas.screenshot('doc/selecting-in-pdf', { clip: { x: 0, y: 0, width: 190, height: 75 } })
    canvas.trigger('pointerup', 140, 55, { pointerId: 1 })
    // cy.screenshot('doc/selected-in-pdf', { clip: { x: 0, y: 0, width: 500, height: 660 } })
    cy.get('button').contains('Consigne').click()
    cy.get('label').contains('Consigne').next().should('have.value', 'Recopie les mots suivants, puis\nentoure les pronoms personnels.\nIndique la classe des autres mots.')

    canvas.trigger('pointerdown', 15, 45, { pointerId: 1 })
    canvas.trigger('pointerup', 140, 105, { pointerId: 1 })
    cy.get('button').contains('Énoncé').click()
    cy.get('label').contains('Énoncé').next().should('have.value', 'a. je ◆ une ◆ petit ◆ arroser\nb. vous ◆ un ◆ arbre ◆ ce\nc. ils ◆ des ◆ grandir ◆ port\nd. dessin ◆ tu ◆ aller ◆ mon\ne. elle ◆ gomme ◆ peindre ◆ ces\nf. histoire ◆ nous ◆ gentil ◆ la')

    // cy.screenshot('doc/three-columns', { clip: { x: 0, y: 0, width: 1000, height: 330 } })

    cy.get('button').contains('Enregistrer').click()
    cy.get('button').contains('Annuler').click()

    cy.get('li').contains('Recopie les mots suivants').should('exist')

    cy.visit('/')

    cy.get('a').contains('Projet de test').click()

    cy.get('a').contains('Français CE2').should('exist')
    cy.get('a').contains('Page 6').should('exist')
    cy.get('li').contains('5 : Recopie').should('exist')
  })

  it('shows project textbook even without exercises', () => {
    cy.request('POST', '/reset-for-tests/yes-im-sure')

    cy.visit('/')
    cy.get('select').select('fr')

    cy.get('.spinner-border').should('not.exist')

    cy.get('p').contains('Aucun projet pour le moment').should('exist')
    cy.get('button').contains('Créer').should('be.disabled')
    cy.get('label').contains('Titre').next().type('Projet de test')
    // @todo Allow creating a project with an empty description
    cy.get('label').contains('Description').next().type('Quelques exercices de Slabeuf.')
    cy.get('button').contains('Créer').should('be.enabled').click()

  
    cy.get('.spinner-border').should('not.exist')
  
    cy.get('p').contains('Aucun exercice pour le moment').should('exist')
    cy.get('button').contains('Créer').should('be.disabled')
    cy.get('input[type=file]').selectFile('../pdf-examples/test.pdf')
    cy.get('label').contains('Titre').next().type('Français CE2')
    // @todo Allow creating a project with empty publisher, year, and ISBN
    cy.get('label').contains('Éditeur').next().type('Slabeuf')
    cy.get('label').contains('Année').next().type('2021')
    cy.get('label').contains('ISBN').next().type('01234567890123')
    cy.get('button').contains('Créer').should('be.enabled').click()

    cy.get('.spinner-border').should('not.exist')

    cy.visit('/')

    cy.get('a').contains('Projet de test').click()

    cy.get('a').contains('Français CE2').should('exist')
  })

  it('shows and hides the section editor dialog', () => {
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=test-exercises')

    cy.visit('/project/1/textbook/1/page/6')
    cy.get('select').select('fr')
    cy.get('.spinner-border').should('not.exist')

    cy.get('h1').contains('Lien entre PDF et manuel').should('not.exist')

    cy.get('button').contains('⚙').click()
    cy.get('h1').contains('Lien entre PDF et manuel').should('exist')

    cy.get('button').contains('Annuler').click()
    cy.get('h1').contains('Lien entre PDF et manuel').should('not.exist')
  })

  it('loads and modifies existing project with exercises from textbook', () => {
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=test-exercises')

    cy.visit('/')
    cy.get('select').select('fr')
    cy.get('a').contains('Premier projet de test').click()

    cy.get('h3').contains('Français CE2, Slabeuf (2021)').should('exist')
    cy.get('li').contains('Page 7').should('exist')
    cy.get('li').contains('9 : Recopie').should('exist')
    cy.get('a').contains('Page 6').click()

    cy.get('p').contains('Exercices existants ').next().should('have.prop', 'tagName').should('eq', 'UL')
    cy.get('p').contains('Exercices existants ').next().children().should('have.length', 2)
    cy.get('p').contains('Exercices existants ').next().children().first().should('contain', '3 Complète avec : le, une, …')

    cy.screenshot('doc/existing-exercises', { clip: { x: 0, y: 0, width: 1000, height: 330 } })

    cy.get('button').contains('Modifier').click()

    // https://github.com/cypress-io/cypress/issues/2681#issuecomment-442890537
    cy.get('html').invoke('css', 'height', 'initial')
    cy.get('body').invoke('css', 'height', 'initial')
    // https://github.com/cypress-io/cypress/issues/2681#issuecomment-1120146874
    cy.get('html').invoke('css', 'scroll-behavior', 'auto')
    cy.get('body').invoke('css', 'scroll-behavior', 'auto')
    cy.screenshot('doc/modify-exercise')

    cy.get('label').contains('Consigne').next().type('{selectall}Blah blah')
    cy.get('button').contains('Enregistrer').click()

    cy.get('p').contains('Exercices existants ').next().children().first().should('contain', '3 Blah blah')
  })

  it('loads and modifies existing project with independent exercises', () => {
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=test-exercises')

    cy.visit('/')
    cy.get('select').select('fr')
    cy.get('a').contains('Deuxième projet de test').click()

    cy.get('h3').contains('Indépendants').should('exist')
    cy.get('li strong').contains('L1').should('exist')
  })

  // @todo Add test showing we can delete and recreate an exercise (hunt possible bug in deletion)

  it('navigates to user documentation', () => {
    cy.visit('/')
    cy.get('select').select('fr')
    cy.get('a').contains('Aide').click()
    cy.contains('h1', 'Documentation de MALIN')
  })

  it('allows textual exercise "number"', () => {
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=test-exercises')

    cy.visit('/project/1/textbook/1/page/6')
    cy.get('select').select('fr')
    cy.get('button').contains('Nouvel exercice').click()

    cy.get('label').contains('Numéro').next().type('Défis langue')
    cy.get('button').contains('Enregistrer').click()
    cy.get('label').contains('Numéro').next().should('have.value', '')
  })

  it('increments integer exercise number', () => {
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=test-exercises')

    cy.visit('/project/1/textbook/1/page/6')
    cy.get('select').select('fr')
    cy.get('button').contains('Nouvel exercice').click()

    cy.get('label').contains('Numéro').next().type('1')
    cy.get('button').contains('Enregistrer').click()
    cy.get('label').contains('Numéro').next().should('have.value', '2')
  })
})
