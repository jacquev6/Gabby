import { visit, login, loadFixtures, traceRectangle, notBusy } from './utils'


describe('Gabby', () => {
  before(console.clear)

  beforeEach(() => {
    loadFixtures('more-test-exercises')
    login()
  })

  function expectRectangles(alias: string, key: string, rectangles: object) {
    cy.get(alias).should('have.attr', 'data-cy-drawn-rectangles').then(JSON.parse as any/* Work around Cypress typing limitations */).its(key).should('deep.equal', rectangles)
  }

  it('collects rectangles when creating and editing an exercise split on two pages', () => {
    visit('/project-xkopqm/textbook-klxufv/page-6/new-exercise', {pdf: 'test'})

    cy.get('label:contains("Number")').next().type('1')

    cy.get('canvas[style="position: absolute; top: 0px; left: 0px;"]').last().as('canvas')
    cy.get('canvas[style="position: absolute; top: 0px; left: 0px;"]').first().as('highlighter')

    expectRectangles('@highlighter', 'surrounded', [])

    traceRectangle('@canvas', 6, 72, 45, 79)
    cy.get('textarea').first().should('have.value', 'Cherche les mots suivants dans le dictionnaire et indique leur classe. Combien de classes as-tu trouvées ?')
    cy.get('button:contains("Instructions")').click()
    expectRectangles('@highlighter', 'surrounded', [{
      'left': 63.24492293708562,
      'top': 199.1302780207111,
      'width': 218.59602260325397,
      'height': 54.650524417037445,
    }])

    cy.get('p:contains("Page"):contains("(on 7)") :contains(">")').click()
    notBusy()
    expectRectangles('@highlighter', 'surrounded', [])

    traceRectangle('@canvas', 6, 11, 38, 24)
    cy.get('textarea').first().should('have.value', 'a. je ◆ une ◆ petit ◆ arroser\nb. vous ◆ un ◆ arbre ◆ ce\nc. ils ◆ des ◆ grandir ◆ port\nd. dessin ◆ tu ◆ aller ◆ mon\ne. elle ◆ gomme ◆ peindre ◆ ces\nf. histoire ◆ nous ◆ gentil ◆ la')
    cy.get('button:contains("Wording")').click()
    expectRectangles('@highlighter', 'surrounded', [{
      'left': 63.24492293708562,
      'top': 631.045712929555,
      'width': 179.81285730267666,
      'height': 102.24936826413443,
    }])

    cy.get('p:contains("Page"):contains("(on 7)") :contains("<")').click()
    notBusy()
    expectRectangles('@highlighter', 'surrounded', [{
      'left': 63.24492293708562,
      'top': 199.1302780207111,
      'width': 218.59602260325397,
      'height': 54.650524417037445,
    }])

    cy.get('p:contains("Page"):contains("(on 7)") :contains(">")').click()
    notBusy()
    expectRectangles('@highlighter', 'surrounded', [{
      'left': 63.24492293708562,
      'top': 631.045712929555,
      'width': 179.81285730267666,
      'height': 102.24936826413443,
    }])

    cy.get('button:contains("Save then back to list")').click()
    cy.get('button:contains("Confirm")').click()
    notBusy()
    expectRectangles('@highlighter', 'grey.0', {
      'left': 63.24492293708562,
      'top': 199.1302780207111,
      'width': 218.59602260325397,
      'height': 54.650524417037445,
    })

    cy.get('p:contains("Page"):contains("(on 7)") :contains(">")').click()
    notBusy()
    expectRectangles('@highlighter', 'grey.0', {
      'left': 63.24492293708562,
      'top': 631.045712929555,
      'width': 179.81285730267666,
      'height': 102.24936826413443,
    })

    cy.get('p:contains("Page"):contains("(on 7)") :contains("<")').click()
    notBusy()

    cy.get('li:contains("1") a:contains("Edit")').click()
    notBusy()
    expectRectangles('@highlighter', 'surrounded', [{
      'left': 63.24492293708562,
      'top': 199.1302780207111,
      'width': 218.59602260325397,
      'height': 54.650524417037445,
    }])

    traceRectangle('@canvas', 6, 78, 22, 85)
    cy.get('textarea').first().should('have.value', 'a. copie\nb. tu\nc. rouge')
    cy.get('button:contains("Wording")').click()
    expectRectangles('@highlighter', 'surrounded', [{
      'left': 63.24492293708562,
      'top': 151.531434173614,
      'width': 218.59602260325397,
      'height': 102.24936826413455,
    }])

    cy.get('p:contains("Page"):contains("(on 7)") :contains(">")').click()
    notBusy()
    expectRectangles('@highlighter', 'surrounded', [{
      'left': 63.24492293708562,
      'top': 631.045712929555,
      'width': 179.81285730267666,
      'height': 102.24936826413443,
    }])

    traceRectangle('@canvas', 6, 5, 45, 10)
    cy.get('textarea').first().should('have.value', '5 Recopie les mots suivants, puis entoure les pronoms personnels.')
    cy.get('button:contains("Instructions")').click()
    expectRectangles('@highlighter', 'surrounded', [{
      'left': 63.24492293708562,
      'top': 631.045712929555,
      'width': 218.59602260325397,
      'height': 149.84821211123153,
    }])

    cy.get('button:contains("Save then back to list")').click()
    notBusy()
    expectRectangles('@highlighter', 'grey.0', {
      'left': 63.24492293708562,
      'top': 151.531434173614,
      'width': 218.59602260325397,
      'height': 102.24936826413455,
    })

    cy.get('p:contains("Page"):contains("(on 7)") :contains(">")').click()
    notBusy()
    expectRectangles('@highlighter', 'grey.0', {
      'left': 63.24492293708562,
      'top': 631.045712929555,
      'width': 218.59602260325397,
      'height': 149.84821211123153,
    })
  })
})
