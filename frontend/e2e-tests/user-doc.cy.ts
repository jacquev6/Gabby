import { loadFixtures, loadPdf, login, notBusy, visit } from './utils'


describe('Gabby', () => {
  before(console.clear)

  it('performs extraction from scratch', () => {
    loadFixtures('admin-user')
    login()
    cy.viewport(1000, 1000)

    visit('/', {locale: 'fr'})

    cy.get('label:contains("Titre")').next().type('Projet de test')
    cy.get('button:contains("Créer le projet")').click()
    notBusy()

    loadPdf('test')
    cy.get('label:contains("Titre")').next().type('Français CE2')
    cy.get('label:contains("Éditeur")').next().type('Slabeuf')
    cy.get('label:contains("Année")').next().type('2021')
    cy.get('label:contains("ISBN")').next().type('01234567890123')
    cy.get('button:contains("Créer le manuel")').click()
    notBusy()

    cy.get('button').contains('⚙').click()
    cy.get('label').contains('Début dans le manuel').next().type('{selectAll}5')
    cy.get('button').contains('Enregistrer').click()
    notBusy()

    cy.get('label').contains('Page').click()
    cy.focused().type('{selectAll}6')
    notBusy()

    cy.get('a:contains("Nouvel exercice")').click()
    cy.get('label').contains('Numéro').next().type('5').blur()

    const canvas = cy.get('canvas[style="position: absolute; top: 0px; left: 0px;"]').last()

    cy.screenshot('project-textbook-page-exercise/create-exercise', {clip: {x: 0, y: 50, width: 575, height: 740}})

    canvas.trigger('pointermove', 5, 5)
    canvas.trigger('pointerdown', 20, 20, { pointerId: 1 })
    canvas.trigger('pointermove', 25, 25)
    canvas.trigger('pointermove', 55, 35)
    canvas.trigger('pointermove', 75, 45)
    canvas.trigger('pointermove', 95, 55)
    canvas.trigger('pointermove', 135, 55)
    canvas.screenshot('project-textbook-page-exercise/selecting-in-pdf', {clip: {x: 0, y: 0, width: 190, height: 75}})
    canvas.trigger('pointerup', 135, 55, { pointerId: 1 })
    cy.screenshot('project-textbook-page-exercise/selected-in-pdf', {clip: {x: 0, y: 0, width: 415, height: 395}})
    cy.get('button').contains('Consigne').click()

    canvas.trigger('pointerdown', 15, 45, { pointerId: 1 })
    canvas.trigger('pointerup', 140, 105, { pointerId: 1 })
    cy.get('button').contains('Énoncé').click()

    cy.get('button').contains('Enregistrer puis suivant').click()
    notBusy()
    cy.get('a:contains("Retour à la liste (sans enregistrer)")').click()
    notBusy()

    cy.get('li').contains('Recopie les mots suivants').should('exist')
  })

  it('loads existing data', () => {
    cy.viewport(1000, 1000)

    loadFixtures('test-exercises')
    login()

    visit('/', {locale: 'fr'})

    cy.screenshot('index/index', {clip: {x: 0, y: 0, width: 1000, height: 350}})

    cy.get('a:contains("Premier projet de test")').click()

    notBusy()
    cy.screenshot('project/project', {clip: {x: 0, y: 0, width: 1000, height: 450}})

    cy.get('button:contains("Modifier")').click()

    notBusy()
    cy.screenshot('project/edit', {clip: {x: 0, y: 0, width: 1000, height: 400}})

    cy.get('button:contains("Annuler")').first().click()

    loadPdf('large')
    cy.get('label:contains("Titre")').next().type('Français CE2')
    cy.get('label:contains("Éditeur")').next().type('Dunod')
    cy.get('label:contains("Année")').next().type('2021')
    cy.get('label:contains("ISBN")').next().type('01234567890123')

    notBusy()
    cy.screenshot('project/new-textbook', {clip: {x: 0, y: 220, width: 660, height: 510}})

    cy.get('a').contains('Page 6').click()

    notBusy()
    cy.screenshot('project-textbook-page/pdf-not-loaded', {clip: {x: 0, y: 0, width: 340, height: 310}})
    loadPdf('test')

    notBusy()

    cy.get('button').contains('⚙').click()
    cy.get('.modal-content:visible').screenshot('project-textbook-page/section-editor')

    cy.get('button:contains("Annuler")').click()
    cy.get('h1').contains('Lien entre PDF et manuel').should('not.exist')

    notBusy()
    cy.screenshot('project-textbook-page/project-textbook-page', {clip: {x: 0, y: 0, width: 1000, height: 400}})
    cy.screenshot('project-textbook-page/existing-exercises', {clip: {x: 330, y: 50, width: 480, height: 230}})
    cy.get('canvas').last().screenshot('project-textbook-page/existing-exercises-in-pdf', {clip: {x: 0, y: 233, width: 1000, height: 1000}})
  })

  it('modifies existing exercise', () => {
    cy.viewport(1000, 1000)

    loadFixtures('test-exercises')
    login()

    visit('/project-xkopqm/textbook-klxufv/page-6/exercise-wbqloc', {locale: 'fr', pdf: 'test'})

    cy.get('label:contains("Type d\'adaptation") + select').select('-')
    cy.get('label:contains("Énoncé") + div.ql-container > div.ql-editor').type('{selectAll}... vide\n... vident')
    notBusy()
    cy.screenshot('project-textbook-page-exercise/modify-exercise', {clip: {x: 0, y: 50, width: 575, height: 800}})

    cy.screenshot('project-textbook-page-exercise/tools', {clip: {x: 560, y: 40, width: 210, height: 260}})

    cy.get('label:contains("Type d\'adaptation") + select').select('generic')
    cy.get('div:contains("Cochable") >input').check()
    cy.get('div.busy').should('exist')  // This may fail (race condition) but is required because the 'div.busy' is not displayed quickly enough.
    notBusy()
    cy.screenshot('project-textbook-page-exercise/project-textbook-page-exercise', {clip: {x: 0, y: 0, width: 1000, height: 330}})

    cy.get('span[data-cy-colors="3"]').click()
    notBusy()
    cy.get('span.maybe-usable-colors-container').screenshot('project-textbook-page-exercise/select-things-usable-colors')
    cy.get('label:contains("Consigne") + div.ql-container > div.ql-editor').click()
    cy.screenshot('project-textbook-page-exercise/select-things-color-formatting-button', {clip: {x: 560, y: 630, width: 140, height: 100}})
    cy.get('span[data-cy-colors="2"]').rightclick()
    cy.screenshot('project-textbook-page-exercise/select-things-color-customization', {clip: {x: 450, y: 530, width: 340, height: 300}})
  })
})
