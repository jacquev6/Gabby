import { visit, login, loadFixtures, traceRectangle, notBusy } from './utils'


describe('Gabby', () => {
  before(console.clear)

  beforeEach(() => {
    loadFixtures('more-test-exercises')
    login()
  })

  it('collects rectangles', () => {
    const isProdPreview = Cypress.env('IS_PROD_PREVIEW')
    cy.viewport(1600, 1000)

    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise', {wysiwyg: false, pdf: 'test'})

    cy.get('label:contains("Number")').next().type('5')

    cy.get('canvas[style="position: absolute; top: 0px; left: 0px;"]').last().as('canvas')
    cy.get('canvas[style="position: absolute; top: 0px; left: 0px;"]').first().as('highlighter')

    traceRectangle('@canvas', 5, 4, 45, 12)
    cy.get('textarea').first().should('have.value', 'Recopie les mots suivants, puis\nentoure les pronoms personnels.\nIndique la classe des autres mots.')
    cy.get('button:contains("Instructions")').click()
    cy.get('@highlighter').should('have.attr', 'data-cy-drawn-rectangles').then(JSON.parse as any/* Work around Cypress typing limitations */).its('surrounded').should('deep.equal', [{
      'left': 56.26098090252517,
      'top': isProdPreview ? 726.5359457228192 : 725.8392892267519,
      'width': 226.18785085087657,
      'height': isProdPreview ? 63.072900326865806 : 64.16036412560493,
    }])

    traceRectangle('@canvas', 6, 13, 44, 15.5)
    cy.get('textarea').first().should('have.value', 'b. vous ◆ un ◆ arbre ◆ ce')
    cy.get('button:contains("Wording")').click()
    cy.get('@highlighter').should('have.attr', 'data-cy-drawn-rectangles').then(JSON.parse as any/* Work around Cypress typing limitations */).its('surrounded').should('deep.equal', [{
      'left': 56.26098090252517,
      'top': isProdPreview ? 698.2618869556034 : 698.6526942582752,
      'width': 226.18785085087657,
      'height': isProdPreview ? 91.34695909408163 : 91.34695909408163,
    }])

    traceRectangle('@canvas', 6, 15, 38, 17.5)
    cy.get('textarea').first().should('have.value', 'c. ils ◆ des ◆ grandir ◆ port')
    cy.get('button:contains("Wording")').click()
    cy.get('@highlighter').should('have.attr', 'data-cy-drawn-rectangles').then(JSON.parse as any/* Work around Cypress typing limitations */).its('surrounded').should('deep.equal', [{
      'left': 56.26098090252517,
      'top': isProdPreview ? 683.0373937732564 : 682.3407372771892,
      'width': 226.18785085087657,
      'height': isProdPreview ? 106.57145227642854 : 107.65891607516767,
    }])

    traceRectangle('@canvas', 6, 17, 35, 19.5)
    cy.get('textarea').first().should('have.value', 'd. dessin ◆ tu ◆ aller ◆ mon')
    cy.get('button:contains("Example")').click()
    cy.get('@highlighter').should('have.attr', 'data-cy-drawn-rectangles').then(JSON.parse as any/* Work around Cypress typing limitations */).its('surrounded').should('deep.equal', [{
      'left': 56.26098090252517,
      'top': isProdPreview ? 666.7254367921705 : 667.1162440948424,
      'width': 226.18785085087657,
      'height': isProdPreview ? 122.88340925751447 : 122.88340925751447,
    }])

    traceRectangle('@canvas', 6, 19, 37, 21.5)
    cy.get('textarea').first().should('have.value', 'e. elle ◆ gomme ◆ peindre ◆ ces')
    cy.get('button:contains("Clue")').click()
    cy.get('@highlighter').should('have.attr', 'data-cy-drawn-rectangles').then(JSON.parse as any/* Work around Cypress typing limitations */).its('surrounded').should('deep.equal', [{
      'left': 56.26098090252517,
      'top': isProdPreview ? 651.5009436098235 : 650.8042871137563,
      'width': 226.18785085087657,
      'height': isProdPreview ? 138.1079024398615 : 139.1953662386005,
    }])

    notBusy()

    cy.get('button:contains("Save then back to list")').click()
    cy.location('pathname').should('equal', '/project-xkopqm/textbook-klxufv/page-7')
    notBusy()

    cy.intercept('GET', '/api/exercises/pghtfo?include=adaptation').as('getExercise')

    visit('/project-xkopqm/textbook-klxufv/page-7/exercise-pghtfo', {wysiwyg: false, pdf: 'test'})

    cy.get('@getExercise').its('response.body.data.attributes.rectangles').should('deep.equal', [
      {
        'pdf_sha256': 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
        'pdf_page': 2,
        'coordinates': 'pdfjs',
        'start': {
          'x': 56.26098090252517,
          'y': isProdPreview ? 789.608846049685 : 789.9996533523569
        },
        'stop': {
          'x': 282.44883175340175,
          'y': isProdPreview ? 726.5359457228192 : 725.8392892267519
        },
        'text': 'Recopie les mots suivants, puis\nentoure les pronoms personnels.\nIndique la classe des autres mots.',
        'role': 'instructions',
      },
      {
        'pdf_sha256': 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
        'pdf_page': 2,
        'coordinates': 'pdfjs',
        'start': {
          'x': 62.78563044630046,
          'y': isProdPreview ? 717.8362353329067 : 718.2270426355784
        },
        'stop': {
          'x': 277.0116238002557,
          'y': isProdPreview ? 698.2618869556034 : 698.6526942582752
        },
        'text': 'b. vous ◆ un ◆ arbre ◆ ce',
        'role': 'wording',
      },
      {
        'pdf_sha256': 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
        'pdf_page': 2,
        'coordinates': 'pdfjs',
        'start': {
          'x': 62.78563044630046,
          'y': isProdPreview ? 702.6117421505596 : 703.0025494532315
        },
        'stop': {
          'x': 243.30093449075005,
          'y': isProdPreview ? 683.0373937732564 : 682.3407372771892
        },
        'text': 'c. ils ◆ des ◆ grandir ◆ port',
        'role': 'wording',
      },
      {
        'pdf_sha256': 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
        'pdf_page': 2,
        'coordinates': 'pdfjs',
        'start': {
          'x': 62.78563044630046,
          'y': isProdPreview ? 686.2997851694737 : 686.6905924721455
        },
        'stop': {
          'x': 225.9018690406826,
          'y': isProdPreview ? 666.7254367921705 : 667.1162440948424
        },
        'text': 'd. dessin ◆ tu ◆ aller ◆ mon',
        'role': 'example',
      },
      {
        'pdf_sha256': 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
        'pdf_page': 2,
        'coordinates': 'pdfjs',
        'start': {
          'x': 62.78563044630046,
          'y': isProdPreview ? 671.0752919871268 : 671.4660992897986
        },
        'stop': {
          'x': 237.86372653760395,
          'y': isProdPreview ? 651.5009436098235 : 650.8042871137563
        },
        'text': 'e. elle ◆ gomme ◆ peindre ◆ ces',
        'role': 'clue',
      },
    ])

    traceRectangle('@canvas', 6, 21, 37, 23.5)
    cy.get('textarea').first().should('have.value', 'f. histoire ◆ nous ◆ gentil ◆ la')
    cy.get('button:contains("Wording")').click()
    cy.get('@highlighter').should('have.attr', 'data-cy-drawn-rectangles').then(JSON.parse as any/* Work around Cypress typing limitations */).its('surrounded').should('deep.equal', [{
      'left': 56.26098090252517,
      'top': isProdPreview ? 635.1889866287376 : 635.5797939314094,
      'width': 226.18785085087657,
      'height': isProdPreview ? 154.41985942094743 : 154.41985942094743,
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
          'y': isProdPreview ? 789.608846049685 : 789.9996533523569
        },
        'stop': {
          'x': 282.44883175340175,
          'y': isProdPreview ? 726.5359457228192 : 725.8392892267519
        },
        'text': 'Recopie les mots suivants, puis\nentoure les pronoms personnels.\nIndique la classe des autres mots.',
        'role': 'instructions',
      },
      {
        'pdf_sha256': 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
        'pdf_page': 2,
        'coordinates': 'pdfjs',
        'start': {
          'x': 62.78563044630046,
          'y': isProdPreview ? 717.8362353329067 : 718.2270426355784
        },
        'stop': {
          'x': 277.0116238002557,
          'y': isProdPreview ? 698.2618869556034 : 698.6526942582752
        },
        'text': 'b. vous ◆ un ◆ arbre ◆ ce',
        'role': 'wording',
      },
      {
        'pdf_sha256': 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
        'pdf_page': 2,
        'coordinates': 'pdfjs',
        'start': {
          'x': 62.78563044630046,
          'y': isProdPreview ? 702.6117421505596 : 703.0025494532315
        },
        'stop': {
          'x': 243.30093449075005,
          'y': isProdPreview ? 683.0373937732564 : 682.3407372771892
        },
        'text': 'c. ils ◆ des ◆ grandir ◆ port',
        'role': 'wording',
      },
      {
        'pdf_sha256': 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
        'pdf_page': 2,
        'coordinates': 'pdfjs',
        'start': {
          'x': 62.78563044630046,
          'y': isProdPreview ? 686.2997851694737 : 686.6905924721455
        },
        'stop': {
          'x': 225.9018690406826,
          'y': isProdPreview ? 666.7254367921705 : 667.1162440948424
        },
        'text': 'd. dessin ◆ tu ◆ aller ◆ mon',
        'role': 'example',
      },
      {
        'pdf_sha256': 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
        'pdf_page': 2,
        'coordinates': 'pdfjs',
        'start': {
          'x': 62.78563044630046,
          'y': isProdPreview ? 671.0752919871268 : 671.4660992897986
        },
        'stop': {
          'x': 237.86372653760395,
          'y': isProdPreview ? 651.5009436098235 : 650.8042871137563
        },
        'text': 'e. elle ◆ gomme ◆ peindre ◆ ces',
        'role': 'clue',
      },
      {
        'pdf_sha256': 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
        'pdf_page': 2,
        'coordinates': 'pdfjs',
        'start': {
            'x': 62.78563044630046,
            'y': isProdPreview ? 654.7633350060407 : 655.1541423087126
        },
        'stop': {
            'x': 237.86372653760395,
            'y': isProdPreview ? 635.1889866287376 : 635.5797939314094
        },
        'text': 'f. histoire ◆ nous ◆ gentil ◆ la',
        'role': 'wording',
      },
    ])
  })

  // @todo Add test for an exercise split on two pages
})
