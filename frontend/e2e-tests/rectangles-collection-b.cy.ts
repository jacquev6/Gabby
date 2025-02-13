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

  it('collects rectangles when creating and editing an exercise (on a single page)', () => {
    cy.viewport(1600, 1000)

    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise', {pdf: 'test'})

    cy.get('label:contains("Number")').next().type('5')

    cy.get('canvas[style="position: absolute; top: 0px; left: 0px;"]').last().as('canvas')
    cy.get('canvas[style="position: absolute; top: 0px; left: 0px;"]').first().as('highlighter')

    traceRectangle('@canvas', 5, 4, 45, 12)
    cy.get('textarea').first().should('have.value', 'Recopie les mots suivants, puis entoure les pronoms personnels. Indique la classe des autres mots.')
    cy.get('button:contains("Instructions")').click()
    expectRectangles('@highlighter', 'surrounded', [{
      'left': 56.26098090252517,
      'top': 725.8392892267519,
      'width': 226.18785085087657,
      'height': 64.16036412560493,
    }])

    traceRectangle('@canvas', 6, 13, 44, 15.5)
    cy.get('textarea').first().should('have.value', 'b. vous ◆ un ◆ arbre ◆ ce')
    cy.get('button:contains("Wording")').click()
    expectRectangles('@highlighter', 'surrounded', [{
      'left': 56.26098090252517,
      'top': 698.6526942582752,
      'width': 226.18785085087657,
      'height': 91.34695909408163,
    }])

    traceRectangle('@canvas', 6, 15, 38, 17.5)
    cy.get('textarea').first().should('have.value', 'c. ils ◆ des ◆ grandir ◆ port')
    cy.get('button:contains("Wording")').click()
    expectRectangles('@highlighter', 'surrounded', [{
      'left': 56.26098090252517,
      'top': 682.3407372771892,
      'width': 226.18785085087657,
      'height': 107.65891607516767,
    }])

    traceRectangle('@canvas', 6, 17, 35, 19.5)
    cy.get('textarea').first().should('have.value', 'd. dessin ◆ tu ◆ aller ◆ mon')
    cy.get('button:contains("Example")').click()
    expectRectangles('@highlighter', 'surrounded', [{
      'left': 56.26098090252517,
      'top': 667.1162440948424,
      'width': 226.18785085087657,
      'height': 122.88340925751447,
    }])

    traceRectangle('@canvas', 6, 19, 37, 21.5)
    cy.get('textarea').first().should('have.value', 'e. elle ◆ gomme ◆ peindre ◆ ces')
    cy.get('button:contains("Clue")').click()
    expectRectangles('@highlighter', 'surrounded', [{
      'left': 56.26098090252517,
      'top': 650.8042871137563,
      'width': 226.18785085087657,
      'height': 139.1953662386005,
    }])

    notBusy()

    cy.get('button:contains("Save then back to list")').click()
    cy.location('pathname').should('equal', '/project-xkopqm/textbook-klxufv/page-7')
    notBusy()

    cy.intercept('GET', '/api/exercises/pghtfo').as('getExercise')

    visit('/project-xkopqm/textbook-klxufv/page-7/exercise-pghtfo', {pdf: 'test'})

    cy.get('@getExercise').its('response.body.data.attributes.rectangles').should('deep.equal', [
      {
        'pdf_sha256': 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
        'pdf_page': 2,
        'coordinates': 'pdfjs',
        'start': {
          'x': 56.26098090252517,
          'y': 789.9996533523569
        },
        'stop': {
          'x': 282.44883175340175,
          'y': 725.8392892267519
        },
        'text': 'Recopie les mots suivants, puis entoure les pronoms personnels. Indique la classe des autres mots.\n',
        'role': 'instructions',
      },
      {
        'pdf_sha256': 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
        'pdf_page': 2,
        'coordinates': 'pdfjs',
        'start': {
          'x': 62.78563044630046,
          'y': 718.2270426355784
        },
        'stop': {
          'x': 277.0116238002557,
          'y': 698.6526942582752
        },
        'text': 'b. vous ◆ un ◆ arbre ◆ ce\n',
        'role': 'wording',
      },
      {
        'pdf_sha256': 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
        'pdf_page': 2,
        'coordinates': 'pdfjs',
        'start': {
          'x': 62.78563044630046,
          'y': 703.0025494532315
        },
        'stop': {
          'x': 243.30093449075005,
          'y': 682.3407372771892
        },
        'text': 'c. ils ◆ des ◆ grandir ◆ port\n',
        'role': 'wording',
      },
      {
        'pdf_sha256': 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
        'pdf_page': 2,
        'coordinates': 'pdfjs',
        'start': {
          'x': 62.78563044630046,
          'y': 686.6905924721455
        },
        'stop': {
          'x': 225.9018690406826,
          'y': 667.1162440948424
        },
        'text': 'd. dessin ◆ tu ◆ aller ◆ mon\n',
        'role': 'example',
      },
      {
        'pdf_sha256': 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
        'pdf_page': 2,
        'coordinates': 'pdfjs',
        'start': {
          'x': 62.78563044630046,
          'y': 671.4660992897986
        },
        'stop': {
          'x': 237.86372653760395,
          'y': 650.8042871137563
        },
        'text': 'e. elle ◆ gomme ◆ peindre ◆ ces\n',
        'role': 'clue',
      },
    ])

    traceRectangle('@canvas', 6, 21, 37, 23.5)
    cy.get('textarea').first().should('have.value', 'f. histoire ◆ nous ◆ gentil ◆ la')
    cy.get('button:contains("Wording")').click()
    expectRectangles('@highlighter', 'surrounded', [{
      'left': 56.26098090252517,
      'top': 635.5797939314094,
      'width': 226.18785085087657,
      'height': 154.41985942094743,
    }])

    cy.get('button:contains("Save then back to list")').click()
    cy.location('pathname').should('equal', '/project-xkopqm/textbook-klxufv/page-7')
    notBusy()

    visit('/project-xkopqm/textbook-klxufv/page-7/exercise-pghtfo')

    cy.get('@getExercise').its('response.body.data.attributes.rectangles').should('deep.equal', [
      {
        'pdf_sha256': 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
        'pdf_page': 2,
        'coordinates': 'pdfjs',
        'start': {
          'x': 56.26098090252517,
          'y': 789.9996533523569
        },
        'stop': {
          'x': 282.44883175340175,
          'y': 725.8392892267519
        },
        'text': 'Recopie les mots suivants, puis entoure les pronoms personnels. Indique la classe des autres mots.\n',
        'role': 'instructions',
      },
      {
        'pdf_sha256': 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
        'pdf_page': 2,
        'coordinates': 'pdfjs',
        'start': {
          'x': 62.78563044630046,
          'y': 718.2270426355784
        },
        'stop': {
          'x': 277.0116238002557,
          'y': 698.6526942582752
        },
        'text': 'b. vous ◆ un ◆ arbre ◆ ce\n',
        'role': 'wording',
      },
      {
        'pdf_sha256': 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
        'pdf_page': 2,
        'coordinates': 'pdfjs',
        'start': {
          'x': 62.78563044630046,
          'y': 703.0025494532315
        },
        'stop': {
          'x': 243.30093449075005,
          'y': 682.3407372771892
        },
        'text': 'c. ils ◆ des ◆ grandir ◆ port\n',
        'role': 'wording',
      },
      {
        'pdf_sha256': 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
        'pdf_page': 2,
        'coordinates': 'pdfjs',
        'start': {
          'x': 62.78563044630046,
          'y': 686.6905924721455
        },
        'stop': {
          'x': 225.9018690406826,
          'y': 667.1162440948424
        },
        'text': 'd. dessin ◆ tu ◆ aller ◆ mon\n',
        'role': 'example',
      },
      {
        'pdf_sha256': 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
        'pdf_page': 2,
        'coordinates': 'pdfjs',
        'start': {
          'x': 62.78563044630046,
          'y': 671.4660992897986
        },
        'stop': {
          'x': 237.86372653760395,
          'y': 650.8042871137563
        },
        'text': 'e. elle ◆ gomme ◆ peindre ◆ ces\n',
        'role': 'clue',
      },
      {
        'pdf_sha256': 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
        'pdf_page': 2,
        'coordinates': 'pdfjs',
        'start': {
            'x': 62.78563044630046,
            'y': 655.1541423087126
        },
        'stop': {
            'x': 237.86372653760395,
            'y': 635.5797939314094
        },
        'text': 'f. histoire ◆ nous ◆ gentil ◆ la\n',
        'role': 'wording',
      },
    ])
  })
})
