describe('Gabby', () => {
  it('performs extraction', () => {
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=test-exercises')

    cy.visit('/pdf')

    cy.get('input[type=file]').selectFile('../pdf-examples/test.pdf')
    cy.waitUntilLoaded()

    cy.get('input[type=file]').should('have.value', 'C:\\fakepath\\test.pdf').should('be.enabled')
    cy.get('button').contains('<').should('be.disabled')
    cy.get('input.number-no-spin').should('have.value', '1').should('be.enabled')
    cy.get('button').contains('>').should('be.enabled')

    cy.get('button').contains('>').click()
    cy.waitUntilLoaded()

    cy.get('input[type=file]').should('have.value', 'C:\\fakepath\\test.pdf').should('be.enabled')
    cy.get('button').contains('<').should('be.enabled')
    cy.get('input.number-no-spin').should('have.value', '2').should('be.enabled')
    cy.get('button').contains('>').should('be.disabled')

    cy.get('li').contains('Recopie les mots suivants').should('not.exist')

    cy.get('button').contains('Nouvel exercice').click()

    cy.get('input[type=file]').should('have.value', 'C:\\fakepath\\test.pdf').should('be.disabled')
    cy.get('button').contains('<').should('be.disabled')
    cy.get('input.number-no-spin').should('have.value', '2').should('be.disabled')
    cy.get('button').contains('>').should('be.disabled')
    cy.get('button').contains('Annuler').should('be.enabled')
    cy.get('button').contains('Enregistrer').should('be.disabled')

    cy.get('label').contains('Numéro').next().type(5)

    cy.screenshot('doc/create-exercise')

    cy.get('button').contains('Enregistrer').should('be.enabled')

    const canvas = cy.get('canvas[style="position: absolute; top: 0px; left: 0px;"]')

    canvas.trigger('pointermove', 5, 5)
    canvas.trigger('pointerdown', 15, 15, { pointerId: 1 })
    canvas.trigger('pointermove', 25, 25)
    canvas.trigger('pointermove', 55, 35)
    canvas.trigger('pointermove', 75, 45)
    canvas.trigger('pointermove', 95, 55)
    canvas.trigger('pointermove', 140, 55)
    canvas.screenshot('doc/selecting-in-pdf', { clip: { x: 0, y: 0, width: 190, height: 75 } })
    canvas.trigger('pointerup', 140, 55, { pointerId: 1 })
    cy.screenshot('doc/selected-in-pdf', { clip: { x: 0, y: 0, width: 500, height: 660 } })
    cy.get('button').contains('Consigne').click()
    cy.get('label').contains('Consigne').next().should('have.value', 'Recopie les mots suivants, puis\nentoure les pronoms personnels.\nIndique la classe des autres mots.')

    canvas.trigger('pointerdown', 15, 45, { pointerId: 1 })
    canvas.trigger('pointerup', 140, 105, { pointerId: 1 })
    cy.get('button').contains('Énoncé').click()
    cy.get('label').contains('Énoncé').next().should('have.value', 'a. je ◆ une ◆ petit ◆ arroser\nb. vous ◆ un ◆ arbre ◆ ce\nc. ils ◆ des ◆ grandir ◆ port\nd. dessin ◆ tu ◆ aller ◆ mon\ne. elle ◆ gomme ◆ peindre ◆ ces\nf. histoire ◆ nous ◆ gentil ◆ la')

    cy.screenshot('doc/three-columns', { clip: { x: 0, y: 0, width: 1000, height: 330 } })

    cy.get('button').contains('Enregistrer').click()
    cy.get('button').contains('Annuler').click()

    cy.get('li').contains('Recopie les mots suivants').should('exist')
  })

  it('loads and modifies exercises', () => {
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=test-exercises')

    cy.visit('/pdf')
    cy.get('input[type=file]').selectFile('../pdf-examples/test.pdf')
    cy.waitUntilLoaded()

    cy.get('p').contains('Exercices existants ').next().should('have.prop', 'tagName' ).should('eq', 'UL')
    cy.get('p').contains('Exercices existants ').next().children().should('have.length', 2)
    cy.get('p').contains('Exercices existants ').next().children().first().should('contain', '3 Complète avec : le, une, …')

    cy.screenshot('doc/existing-exercises', { clip: { x: 0, y: 0, width: 1000, height: 330 } })

    cy.get('button').contains('Modifier').click()

    // https://github.com/cypress-io/cypress/issues/2681#issuecomment-442890537
    cy.get('html').invoke('css', 'height', 'initial');
    cy.get('body').invoke('css', 'height', 'initial');
    // https://github.com/cypress-io/cypress/issues/2681#issuecomment-1120146874
    cy.get('html').invoke('css', 'scroll-behavior', 'auto');
    cy.get('body').invoke('css', 'scroll-behavior', 'auto');
    cy.screenshot('doc/modify-exercise')
  })

  it('navigates to user documentation', () => {
    cy.visit('/')
    cy.get('a').contains('Aide').click()
    cy.contains('h1', 'Documentation de MALIN')
  })
})
