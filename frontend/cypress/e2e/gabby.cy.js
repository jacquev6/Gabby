describe('Gabby', () => {
  it('responds to the root url', () => {
    cy.visit('/')
    cy.contains('nav', 'MALIN')
  })

  it('performs extraction', () => {
    cy.visit('/')

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

    cy.get('button').contains('Nouvel exercice').click()

    cy.get('input[type=file]').should('have.value', 'C:\\fakepath\\test.pdf').should('be.disabled')
    cy.get('button').contains('<').should('be.disabled')
    cy.get('input.number-no-spin').should('have.value', '2').should('be.disabled')
    cy.get('button').contains('>').should('be.disabled')
    cy.get('button').contains('Annuler').should('be.enabled')
    cy.get('button').contains('Enregistrer').should('be.disabled')

    cy.get('label').contains('Numéro').next().type(5)

    cy.get('button').contains('Enregistrer').should('be.enabled')

    // @todo Simulate clicks in the PdfPicker instead of typing in the form
    cy.get('label').contains('Consigne').next().type('Recopie les mots suivants, puis\nentoure les pronoms personnels.\nIndique la classe des autres mots.')
    cy.get('label').contains('Énoncé').next().type('a. je ◆ une ◆ petit ◆ arroser\nb. vous ◆ un ◆ arbre ◆ ce\nc. ils ◆ des ◆ grandir ◆ port\nd. dessin ◆ tu ◆ aller ◆ mon\ne. elle ◆ gomme ◆ peindre ◆ ces\nf. histoire ◆ nous ◆ gentil ◆ la')

    cy.screenshot('help/three-columns', { capture: 'viewport' })
  })
})
