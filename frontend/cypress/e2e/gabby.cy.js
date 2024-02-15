describe('Gabby', () => {
  it('performs extraction', () => {
    cy.request('POST', '/reset-for-tests/yes-im-sure')

    cy.visit('/')
    cy.contains('nav', 'MALIN')

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

    cy.get('button').contains('Enregistrer').should('be.enabled')

    const canvas = cy.get('canvas[style="position: absolute; top: 0px; left: 0px;"]')

    canvas.trigger('pointermove', 5, 5)
    canvas.trigger('pointerdown', 15, 15, { pointerId: 1 })
    canvas.trigger('pointermove', 25, 25)
    canvas.trigger('pointermove', 55, 35)
    canvas.trigger('pointermove', 75, 45)
    canvas.trigger('pointermove', 95, 55)
    canvas.trigger('pointermove', 140, 55)
    canvas.screenshot('help/selecting-in-pdf', { clip: { x: 0, y: 0, width: 190, height: 75 } })
    canvas.trigger('pointerup', 140, 55, { pointerId: 1 })
    cy.screenshot('help/selected-in-pdf', { capture: 'viewport', clip: { x: 0, y: 0, width: 500, height: 660 } })
    cy.get('button').contains('Consigne').click()
    cy.get('label').contains('Consigne').next().should('have.value', 'Recopie les mots suivants, puis\nentoure les pronoms personnels.\nIndique la classe des autres mots.')

    canvas.trigger('pointerdown', 15, 45, { pointerId: 1 })
    canvas.trigger('pointerup', 140, 105, { pointerId: 1 })
    cy.get('button').contains('Énoncé').click()
    cy.get('label').contains('Énoncé').next().should('have.value', 'a. je ◆ une ◆ petit ◆ arroser\nb. vous ◆ un ◆ arbre ◆ ce\nc. ils ◆ des ◆ grandir ◆ port\nd. dessin ◆ tu ◆ aller ◆ mon\ne. elle ◆ gomme ◆ peindre ◆ ces\nf. histoire ◆ nous ◆ gentil ◆ la')

    cy.screenshot('help/three-columns', { capture: 'viewport' })

    cy.get('button').contains('Enregistrer').click()
    cy.get('button').contains('Annuler').click()

    cy.get('li').contains('Recopie les mots suivants').should('exist')
  })
})
