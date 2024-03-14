const isProdPreview = Cypress.env('IS_PROD_PREVIEW')

describe('Gabby\'s project\'s textbook page view', () => {
  before(console.clear)

  beforeEach(() => {
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=test-exercises')
  })

  after(() => {
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=test-exercises')
  })

  it('displays an error message if the project does not exist', () => {
    cy.visit('/project/0/textbook/1/page/6')
    cy.get('div.busy').should('not.exist')
    cy.get('select').select('en')

    cy.get('h1:contains("Project not found")').should('exist')
    cy.title().should('eq', 'MALIN')
  })

  it('displays an error message if the textbook does not exist', () => {
    cy.visit('/project/1/textbook/0/page/6')
    cy.get('div.busy').should('not.exist')
    cy.get('select').select('en')

    cy.get('h1:contains("Textbook not found")').should('exist')
    cy.title().should('eq', 'MALIN')
  })

  it('displays an error message if the textbook does not belong to this project', () => {
    cy.visit('/project/2/textbook/1/page/6')
    cy.get('div.busy').should('not.exist')
    cy.get('select').select('en')

    cy.get('h1:contains("Textbook not found")').should('exist')
    cy.title().should('eq', 'MALIN')
  })

  // @todo Add test where the page is a negative number
  // @todo Add test where the page is larger than the textbook's number of pages
  // @todo Add test where the page is not a number

  it('lands', () => {
    cy.visit('/project/1/textbook/1/page/6')
    cy.get('select').select('en')

    cy.title().should('eq', 'MALIN - Premier projet de test - Français CE2 - Page 6')
    cy.get('.navbar').should('contain', 'Premier projet de test')
    cy.get('.navbar').should('contain', 'Français CE2')
  })

  it('adjusts textarea heights', () => {
    cy.visit('/project/1/textbook/1/page/6')
    cy.get('select').select('en')
    cy.get('button:contains("New exercise")').click()
    cy.get('button:contains("Passer cette étape")').click()
    cy.get('p:contains("Example")').click()
    cy.get('p:contains("Clue")').click()

    for (const label of ['Instructions', 'Example', 'Clue', 'Wording']) {
      cy.get(`label:contains("${label}")`).next().should('have.attr', 'rows', '2')
      cy.get(`label:contains("${label}")`).next().type('a\nb\nc\nd')
      cy.get(`label:contains("${label}")`).next().should('have.attr', 'rows', '5')
    }
  })

  it('navigates the textbook', () => {
    cy.visit('/project/1/textbook/1/page/6')
    cy.get('select').select('en')
    cy.get('p:contains("Page"):contains("(on 7)") input').should('have.value', '6')
    cy.get('p:contains("The PDF that contains this page (test.pdf) has not been loaded yet.")').should('exist')

    cy.get('p:contains("Page"):contains("(on 7)") :contains(">")').click()
    cy.get('p:contains("Page"):contains("(on 7)") input').should('have.value', '7')
    cy.url().should('eq', `${Cypress.config().baseUrl}project/1/textbook/1/page/7`)
    cy.get('p:contains("Page"):contains("(on 7)") :contains(">")').should('be.disabled')
    cy.get('p:contains("The PDF that contains this page (test.pdf) has not been loaded yet.")').should('exist')

    cy.get('p:contains("Page"):contains("(on 7)") :contains("<")').click()
    cy.get('p:contains("Page"):contains("(on 7)") :contains(">")').should('be.enabled')

    cy.get('p:contains("Page"):contains("(on 7)") :contains("<")').click()
    cy.get('p:contains("Page"):contains("(on 7)") input').should('have.value', '5')
    cy.url().should('eq', `${Cypress.config().baseUrl}project/1/textbook/1/page/5`)
    cy.get('p:contains("No known PDF contains this page.")').should('exist')
    cy.get('p:contains("The PDF that contains this page (test.pdf) has not been loaded yet.")').should('not.exist')

    cy.get('p:contains("Page"):contains("(on 7)") input').clear().type('1')
    cy.url().should('eq', `${Cypress.config().baseUrl}project/1/textbook/1/page/1`)
    cy.get('p:contains("Page"):contains("(on 7)") :contains("<")').should('be.disabled')
    cy.get('p:contains("No known PDF contains this page.")').should('exist')

    cy.get('p:contains("Page"):contains("(on 7)") input').clear().type('100').blur()
    cy.get('div.busy').should('not.exist')
    cy.get('p:contains("Page"):contains("(on 7)") input').should('have.value', '1')
    cy.url().should('eq', `${Cypress.config().baseUrl}project/1/textbook/1/page/1`)

    cy.get('p:contains("Page"):contains("(on 7)") input').clear().type('200').blur()
    cy.get('div.busy').should('not.exist')
    cy.get('p:contains("Page"):contains("(on 7)") input').should('have.value', '2')
    cy.url().should('eq', `${Cypress.config().baseUrl}project/1/textbook/1/page/2`)
  })

  it('enables the "Save exercise" button', () => {
    cy.visit('/project/1/textbook/1/page/6')
    cy.get('select').select('en')
    cy.get('button:contains("New exercise")').click()
    cy.get('button:contains("Passer cette étape")').click()

    cy.get('button:contains("Save then create next")').should('be.disabled')

    cy.get('label:contains("Number")').next().type('1')
    cy.get('button:contains("Save then create next")').should('be.enabled')

    cy.get('label:contains("Number")').next().clear()
    cy.get('button:contains("Save then create next")').should('be.disabled')

    cy.get('label:contains("Number")').next().type('A')
    cy.get('button:contains("Save then create next")').should('be.enabled')
  })

  it('lists existing exercises', () => {
    cy.visit('/project/1/textbook/1/page/7')
    cy.get('select').select('en')
    cy.get('button:contains("Delete")').click()
    cy.get('div.busy').should('not.exist')
    cy.get('p:contains("No exercises yet.")').should('exist')

    cy.visit('/project/1/textbook/1/page/7')
    cy.get('div.busy').should('not.exist')
    cy.get('select').select('en')
    cy.get('p:contains("No exercises yet.")').should('exist')

    cy.get('button:contains("<")').click()
    cy.get('p:contains("Existing exercises:")').should('exist')
    cy.get('li:contains("3 Complète avec : le, une, …")').should('exist')
    cy.get('li:contains("4 Écris une phrase en respe…")').should('exist')
  })

  it('loads a PDF', () => {
    cy.visit('/project/1/textbook/1/page/6')
    cy.get('select').select('en')
    cy.get('div.busy').should('not.exist')
    cy.get('p:contains("The PDF that contains this page (test.pdf) has not been loaded yet.")').should('exist')

    cy.get('input[type=file]').selectFile('../pdf-examples/test.pdf')
    cy.get('div.busy').should('not.exist')
    cy.get('p:contains("The PDF that contains this page (test.pdf) has not been loaded yet.")').should('not.exist')
    cy.get('input[type=file]').should('not.exist')
  })

  it('creates a minimal exercise', () => {
    cy.visit('/project/1/textbook/1/page/6')
    cy.get('select').select('en')
    cy.get('button:contains("New exercise")').click()
    cy.get('button:contains("Passer cette étape")').click()

    cy.get('label:contains("Number")').next().type('1')
    cy.get('button:contains("Save")').click()
    cy.get('div.busy').should('not.exist')
    cy.get('button:contains("Passer cette étape")').click()

    cy.get('label:contains("Number")').next().should('have.value', '2')

    cy.get('button:contains("Cancel")').click()
    cy.get('div.busy').should('not.exist')
    cy.get('li:contains("1")').should('exist')
  })

  it('creates a full exercise', () => {
    cy.visit('/project/1/textbook/1/page/6')
    cy.get('select').select('en')
    cy.get('button:contains("New exercise")').click()
    cy.get('button:contains("Passer cette étape")').click()

    cy.get('label:contains("Number")').next().type('Défis')
    cy.get('label:contains("Instructions")').next().type('Do the smartest thing ever.')
    cy.get('label:contains("Wording")').next().type('The wording')
    cy.get('p:contains("Example")').click()
    cy.focused().type('The example')
    cy.get('p:contains("Clue")').click()
    cy.focused().type('The clue')
    cy.get('button:contains("Save")').click()
    cy.get('div.busy').should('not.exist')
    cy.get('button:contains("Passer cette étape")').click()

    cy.get('label:contains("Number")').next().should('have.value', '')

    cy.get('button:contains("Cancel")').click()
    cy.get('div.busy').should('not.exist')
    cy.get('li:contains("Défis")').should('exist')
  })

  it('collects extraction events on new exercises', () => {
    cy.visit('/project/1/textbook/1/page/6')
    cy.get('select').select('en')
    cy.get('input[type=file]').selectFile('../pdf-examples/test.pdf')
    cy.get('div.busy').should('not.exist')

    cy.get('button:contains("New exercise")').click()
    cy.get('button:contains("Passer cette étape")').click()

    cy.get('label:contains("Number")').next().type('1')
    cy.get('label:contains("Instructions")').next().type('Ceci est la consigne')
    cy.get('p:contains("Example")').click()
    cy.focused().type('Ceci est un exemple')
    cy.get('p:contains("Clue")').click()
    cy.focused().type('Ceci est un indice')
    cy.get('label:contains("Wording")').next().type('Ceci est l\'énoncé')
    cy.get('button:contains("Save")').click()
    cy.get('div.busy').should('not.exist')

    cy.get('canvas[style="position: absolute; top: 0px; left: 0px;"]').as('canvas')
    cy.get('button:contains("Passer cette étape")').should('exist')
    cy.get('@canvas').trigger('pointermove', 5, 5)
    cy.get('@canvas').trigger('pointerdown', 15, 370, { pointerId: 1 })
    cy.get('@canvas').trigger('pointermove', 150, 420)
    cy.get('@canvas').trigger('pointerup', 150, 420, { pointerId: 1 })
    cy.get('button:contains("Passer cette étape")').should('not.exist')
    cy.get('@canvas').trigger('pointermove', 5, 5)
    cy.get('@canvas').trigger('pointerdown', 15, 370, { pointerId: 1 })
    cy.get('@canvas').trigger('pointermove', 150, 395)
    cy.get('@canvas').trigger('pointerup', 150, 395, { pointerId: 1 })
    cy.get('button:contains("Instructions")').click()
    cy.get('@canvas').trigger('pointermove', 5, 5)
    cy.get('@canvas').trigger('pointerdown', 15, 390, { pointerId: 1 })
    cy.get('@canvas').trigger('pointermove', 150, 415)
    cy.get('@canvas').trigger('pointerup', 150, 415, { pointerId: 1 })
    cy.get('label:contains("Selected text")').next().type('Blah blah blah')
    cy.get('button:contains("Wording")').click()
    cy.get('button:contains("Save")').click()
    cy.get('div.busy').should('not.exist')

    cy.visit('/project/1')
    cy.get('select').select('en')

    cy.get('a').contains('the extraction report').should('have.attr', 'href', '/api/project-1-extraction-report.json')

    cy.request('/api/project-1-extraction-report.json').its('body').should('deep.eq', {project: {
      title: 'Premier projet de test',
      textbooks: [
        {
          title: 'Français CE2',
          exercises: [
            {
              page: 6,
              number: '1',
              events: [
                {kind: 'ExerciseNumberSetManually', value: '1'},
                {kind: 'InstructionsSetManually', value: 'Ceci est la consigne'},
                {kind: 'ExampleSetManually', value: 'Ceci est un exemple'},
                {kind: 'ClueSetManually', value: 'Ceci est un indice'},
                {kind: 'WordingSetManually', value: 'Ceci est l\'énoncé'},
              ],
            },
            {
              page: 6,
              number: '2',
              events: [
                {kind: 'ExerciseNumberSetAutomatically', value: '2'},
                {
                  kind: 'BoundingRectangleSelectedInPdf',
                  pdf: {
                    name: 'test.pdf',
                    sha256: 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
                    page: 1,
                    rectangle: {
                      start: {x: 55.49873958525407, y: (isProdPreview ? 142.1556772665365 : 142.81480621450703)},
                      stop: {x: 303.099891274904, y: (isProdPreview ? 50.45078015760089 : 51.10990910557143)},
                    },
                  },
                },
                {
                  kind: 'TextSelectedInPdf',
                  pdf: {
                    name: 'test.pdf',
                    sha256: 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
                    page: 1,
                    rectangle: {
                      start: {x: 55.49873958525407, y: (isProdPreview ? 142.1556772665365 : 142.81480621450703)},
                      stop: {x: 303.099891274904, y: (isProdPreview ? 96.30322871206863 : 96.96235766003917)},
                    },
                  },
                  value: '2\nClasse les mots en trois groupes :\nnom, verbe, adjectif.',
                  textItems: [
                    {
                      str: '',
                      font: 'g_d0_f11',
                      left: 79.1057,
                      width: 0,
                      right: 79.1057,
                      bottom: 118.3111,
                      height: 0,
                      top: 118.3111,
                    },
                    {
                      str: '2',
                      font: 'g_d0_f11',
                      left: 79.1057,
                      width: 6.492245200000001,
                      right: 85.5979452,
                      bottom: 118.3111,
                      height: 11.6767,
                      top: 129.9878,
                    },
                    {
                      str: ' ',
                      font: 'g_d0_f11',
                      left: 85.5979452,
                      width: 1.4357784990622353,
                      right: 87.03372369906224,
                      bottom: 118.3111,
                      height: 0,
                      top: 118.3111,
                    },
                    {
                      str: 'Classe les mots en trois groupes',
                      font: 'g_d0_f2',
                      left: 102.3631,
                      width: 171.22250000000005,
                      right: 273.58560000000006,
                      bottom: 117.1983,
                      height: 12.5,
                      top: 129.69830000000002,
                    },
                    {
                      str: ' ',
                      font: 'g_d0_f2',
                      left: 273.58559999999994,
                      width: 0.12520000000000436,
                      right: 273.71079999999995,
                      bottom: 117.1983,
                      height: 0,
                      top: 117.1983,
                    },
                    {
                      str: ':',
                      font: 'g_d0_f2',
                      left: 275.1506,
                      width: 3.4750000000000005,
                      right: 278.6256,
                      bottom: 117.1983,
                      height: 12.5,
                      top: 129.69830000000002,
                    },
                    {
                      str: '',
                      font: 'g_d0_f12',
                      left: 73.70060000000001,
                      width: 0,
                      right: 73.70060000000001,
                      bottom: 102.0858,
                      height: 0,
                      top: 102.0858,
                    },
                    {
                      str: 'nom',
                      font: 'g_d0_f12',
                      left: 73.70060000000001,
                      width: 23.5375,
                      right: 97.2381,
                      bottom: 102.0858,
                      height: 12.5,
                      top: 114.5858,
                    },
                    {
                      str: ',',
                      font: 'g_d0_f2',
                      left: 97.2381,
                      width: 3.4000000000000004,
                      right: 100.63810000000001,
                      bottom: 102.0858,
                      height: 12.5,
                      top: 114.5858,
                    },
                    {
                      str: ' ',
                      font: 'g_d0_f2',
                      left: 100.63810000000001,
                      width: 0.2059999999999991,
                      right: 100.84410000000001,
                      bottom: 102.0858,
                      height: 0,
                      top: 102.0858,
                    },
                    {
                      str: 'verbe',
                      font: 'g_d0_f12',
                      left: 103.2131,
                      width: 29.72500000000001,
                      right: 132.93810000000002,
                      bottom: 102.0858,
                      height: 12.5,
                      top: 114.5858,
                    },
                    {
                      str: ',',
                      font: 'g_d0_f2',
                      left: 132.9381,
                      width: 3.4000000000000004,
                      right: 136.3381,
                      bottom: 102.0858,
                      height: 12.5,
                      top: 114.5858,
                    },
                    {
                      str: ' ',
                      font: 'g_d0_f2',
                      left: 136.3381,
                      width: 0.2059999999999991,
                      right: 136.5441,
                      bottom: 102.0858,
                      height: 0,
                      top: 102.0858,
                    },
                    {
                      str: 'adjectif',
                      font: 'g_d0_f12',
                      left: 138.9131,
                      width: 40.150000000000006,
                      right: 179.0631,
                      bottom: 102.0858,
                      height: 12.5,
                      top: 114.5858,
                    },
                    {
                      str: '.',
                      font: 'g_d0_f2',
                      left: 179.0631,
                      width: 3.4000000000000004,
                      right: 182.4631,
                      bottom: 102.0858,
                      height: 12.5,
                      top: 114.5858,
                    },
                  ],
                },
                {
                  kind: 'SelectedTextAddedToInstructions',
                  valueBefore: '',
                  valueAfter: 'Classe les mots en trois groupes :\nnom, verbe, adjectif.',
                },
                {
                  kind: 'TextSelectedInPdf',
                  pdf: {
                    name: 'test.pdf',
                    sha256: 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
                    page: 1,
                    rectangle: {
                      start: {x: 55.49873958525407, y: (isProdPreview ? 105.47371842296229 : 106.13284737093272)},
                      stop: {x: 303.099891274904, y: (isProdPreview ? 59.62126986849444 : 60.28039881646487)},
                    },
                  },
                  value: 'verrou ◆ baigner ◆ joli ◆ chaleur ◆ grosse ◆\nsurveiller ◆ degré ◆ librairie ◆ repas ◆ parler',
                  textItems: [
                    {
                      str: '',
                      font: 'g_d0_f12',
                      left: 73.70060000000001,
                      width: 0,
                      right: 73.70060000000001,
                      bottom: 102.0858,
                      height: 0,
                      top: 102.0858,
                    },
                    {
                      str: ' ',
                      font: 'g_d0_f2',
                      left: 100.63810000000001,
                      width: 0.2059999999999991,
                      right: 100.84410000000001,
                      bottom: 102.0858,
                      height: 0,
                      top: 102.0858,
                    },
                    {
                      str: ' ',
                      font: 'g_d0_f2',
                      left: 136.3381,
                      width: 0.2059999999999991,
                      right: 136.5441,
                      bottom: 102.0858,
                      height: 0,
                      top: 102.0858,
                    },
                    {
                      str: '',
                      font: 'g_d0_f8',
                      left: 73.7006,
                      width: 0,
                      right: 73.7006,
                      bottom: 86.47330000000001,
                      height: 0,
                      top: 86.47330000000001,
                    },
                    {
                      str: 'verrou',
                      font: 'g_d0_f8',
                      left: 73.7006,
                      width: 33.00000000000001,
                      right: 106.70060000000001,
                      bottom: 86.47330000000001,
                      height: 12.5,
                      top: 98.97330000000001,
                    },
                    {
                      str: ' ',
                      font: 'g_d0_f8',
                      left: 106.70060000000001,
                      width: 0.2086153846153838,
                      right: 106.9092153846154,
                      bottom: 86.47330000000001,
                      height: 0,
                      top: 86.47330000000001,
                    },
                    {
                      str: '◆',
                      font: 'g_d0_f8',
                      left: 109.4126,
                      width: 5.902,
                      right: 115.3146,
                      bottom: 86.4769,
                      height: 13,
                      top: 99.4769,
                    },
                    {
                      str: ' ',
                      font: 'g_d0_f8',
                      left: 115.3146,
                      width: 0.21699200000000018,
                      right: 115.531592,
                      bottom: 86.4769,
                      height: 0,
                      top: 86.4769,
                    },
                    {
                      str: 'baigner',
                      font: 'g_d0_f8',
                      left: 118.027,
                      width: 38.42375,
                      right: 156.45075,
                      bottom: 86.4769,
                      height: 12.5,
                      top: 98.9769,
                    },
                    {
                      str: ' ',
                      font: 'g_d0_f8',
                      left: 156.45075,
                      width: 0.2086730769230769,
                      right: 156.65942307692308,
                      bottom: 86.4769,
                      height: 0,
                      top: 86.4769,
                    },
                    {
                      str: '◆',
                      font: 'g_d0_f8',
                      left: 159.1635,
                      width: 5.902,
                      right: 165.0655,
                      bottom: 86.4769,
                      height: 13,
                      top: 99.4769,
                    },
                    {
                      str: ' ',
                      font: 'g_d0_f8',
                      left: 165.0655,
                      width: 0.21699200000000246,
                      right: 165.282492,
                      bottom: 86.4769,
                      height: 0,
                      top: 86.4769,
                    },
                    {
                      str: 'joli',
                      font: 'g_d0_f8',
                      left: 167.77790000000002,
                      width: 14.962499999999995,
                      right: 182.74040000000002,
                      bottom: 86.4769,
                      height: 12.5,
                      top: 98.9769,
                    },
                    {
                      str: ' ',
                      font: 'g_d0_f8',
                      left: 182.74040000000002,
                      width: 0.20860769230769122,
                      right: 182.9490076923077,
                      bottom: 86.4769,
                      height: 0,
                      top: 86.4769,
                    },
                    {
                      str: '◆',
                      font: 'g_d0_f8',
                      left: 185.4523,
                      width: 5.902,
                      right: 191.3543,
                      bottom: 86.4769,
                      height: 13,
                      top: 99.4769,
                    },
                    {
                      str: ' ',
                      font: 'g_d0_f8',
                      left: 191.3543,
                      width: 0.21699200000000018,
                      right: 191.571292,
                      bottom: 86.4769,
                      height: 0,
                      top: 86.4769,
                    },
                    {
                      str: 'chaleur',
                      font: 'g_d0_f8',
                      left: 194.0667,
                      width: 36.462500000000006,
                      right: 230.5292,
                      bottom: 86.4769,
                      height: 12.5,
                      top: 98.9769,
                    },
                    {
                      str: ' ',
                      font: 'g_d0_f8',
                      left: 230.5292,
                      width: 0.20862307692307633,
                      right: 230.7378230769231,
                      bottom: 86.4769,
                      height: 0,
                      top: 86.4769,
                    },
                    {
                      str: '◆',
                      font: 'g_d0_f8',
                      left: 233.2413,
                      width: 5.902,
                      right: 239.14329999999998,
                      bottom: 86.4769,
                      height: 13,
                      top: 99.4769,
                    },
                    {
                      str: ' ',
                      font: 'g_d0_f8',
                      left: 239.14329999999998,
                      width: 0.21699200000000246,
                      right: 239.360292,
                      bottom: 86.4769,
                      height: 0,
                      top: 86.4769,
                    },
                    {
                      str: 'grosse',
                      font: 'g_d0_f8',
                      left: 241.8557,
                      width: 31.799999999999983,
                      right: 273.6557,
                      bottom: 86.4769,
                      height: 12.5,
                      top: 98.9769,
                    },
                    {
                      str: ' ',
                      font: 'g_d0_f8',
                      left: 273.65569999999997,
                      width: 0.2086076923076934,
                      right: 273.86430769230765,
                      bottom: 86.4769,
                      height: 0,
                      top: 86.4769,
                    },
                    {
                      str: '◆',
                      font: 'g_d0_f8',
                      left: 276.3676,
                      width: 5.902,
                      right: 282.26959999999997,
                      bottom: 86.4769,
                      height: 13,
                      top: 99.4769,
                    },
                    {
                      str: 'surveiller',
                      font: 'g_d0_f8',
                      left: 73.70700000000002,
                      width: 45.56124999999999,
                      right: 119.26825000000001,
                      bottom: 70.8644,
                      height: 12.5,
                      top: 83.3644,
                    },
                    {
                      str: ' ',
                      font: 'g_d0_f8',
                      left: 119.26825000000002,
                      width: 0.20816538461538306,
                      right: 119.47641538461541,
                      bottom: 70.8644,
                      height: 0,
                      top: 70.8644,
                    },
                    {
                      str: '◆',
                      font: 'g_d0_f8',
                      left: 121.9744,
                      width: 5.902,
                      right: 127.8764,
                      bottom: 70.8662,
                      height: 13,
                      top: 83.8662,
                    },
                    {
                      str: ' ',
                      font: 'g_d0_f8',
                      left: 127.8764,
                      width: 0.21699199999999905,
                      right: 128.093392,
                      bottom: 70.8662,
                      height: 0,
                      top: 70.8662,
                    },
                    {
                      str: 'degré',
                      font: 'g_d0_f8',
                      left: 130.5888,
                      width: 29.612500000000008,
                      right: 160.2013,
                      bottom: 70.8662,
                      height: 12.5,
                      top: 83.3662,
                    },
                    {
                      str: ' ',
                      font: 'g_d0_f8',
                      left: 160.20129999999997,
                      width: 0.20861538461538595,
                      right: 160.40991538461537,
                      bottom: 70.8662,
                      height: 0,
                      top: 70.8662,
                    },
                    {
                      str: '◆',
                      font: 'g_d0_f8',
                      left: 162.9133,
                      width: 5.902,
                      right: 168.81529999999998,
                      bottom: 70.8662,
                      height: 13,
                      top: 83.8662,
                    },
                    {
                      str: ' ',
                      font: 'g_d0_f8',
                      left: 168.81529999999998,
                      width: 0.21700000000000272,
                      right: 169.0323,
                      bottom: 70.8662,
                      height: 0,
                      top: 70.8662,
                    },
                    {
                      str: 'librairie',
                      font: 'g_d0_f8',
                      left: 171.5278,
                      width: 38.19874999999998,
                      right: 209.72655,
                      bottom: 70.8662,
                      height: 12.5,
                      top: 83.3662,
                    },
                    {
                      str: ' ',
                      font: 'g_d0_f8',
                      left: 209.72655000000003,
                      width: 0.20864230769230446,
                      right: 209.93519230769235,
                      bottom: 70.8662,
                      height: 0,
                      top: 70.8662,
                    },
                    {
                      str: '◆',
                      font: 'g_d0_f8',
                      left: 212.4389,
                      width: 5.902,
                      right: 218.34089999999998,
                      bottom: 70.8662,
                      height: 13,
                      top: 83.8662,
                    },
                    {
                      str: ' ',
                      font: 'g_d0_f8',
                      left: 218.34089999999998,
                      width: 0.21700000000000272,
                      right: 218.5579,
                      bottom: 70.8662,
                      height: 0,
                      top: 70.8662,
                    },
                    {
                      str: 'repas',
                      font: 'g_d0_f8',
                      left: 221.0534,
                      width: 27.325,
                      right: 248.3784,
                      bottom: 70.8662,
                      height: 12.5,
                      top: 83.3662,
                    },
                    {
                      str: ' ',
                      font: 'g_d0_f8',
                      left: 248.3784,
                      width: 0.2086153846153838,
                      right: 248.58701538461537,
                      bottom: 70.8662,
                      height: 0,
                      top: 70.8662,
                    },
                    {
                      str: '◆',
                      font: 'g_d0_f8',
                      left: 251.0904,
                      width: 5.902,
                      right: 256.9924,
                      bottom: 70.8662,
                      height: 13,
                      top: 83.8662,
                    },
                    {
                      str: ' ',
                      font: 'g_d0_f8',
                      left: 256.9924,
                      width: 0.21699200000000018,
                      right: 257.209392,
                      bottom: 70.8662,
                      height: 0,
                      top: 70.8662,
                    },
                    {
                      str: 'parler',
                      font: 'g_d0_f8',
                      left: 259.7048,
                      width: 30.16249999999998,
                      right: 289.86729999999994,
                      bottom: 70.8662,
                      height: 12.5,
                      top: 83.3662,
                    },
                  ],
                },
                {
                  kind: 'SelectedTextEdited',
                  value: 'verrou ◆ baigner ◆ joli ◆ chaleur ◆ grosse ◆\nsurveiller ◆ degré ◆ librairie ◆ repas ◆ parlerBlah blah blah',
                },
                {
                  kind: 'SelectedTextAddedToWording',
                  valueBefore: '',
                  valueAfter: 'verrou ◆ baigner ◆ joli ◆ chaleur ◆ grosse ◆\nsurveiller ◆ degré ◆ librairie ◆ repas ◆ parlerBlah blah blah',
                },
              ],
            },
            {
              page: 6,
              number: '3',
              events: []
            },
            {
              page: 6,
              number: '4',
              events: [],
            },
            {
              page: 7,
              number: '9',
              events: [],
            },
          ],
        },
      ],
    }})
  })

  it('collects extraction events when editing exercises', () => {
    cy.visit('/project/1/textbook/1/page/6')
    cy.get('select').select('en')
    cy.get('input[type=file]').selectFile('../pdf-examples/test.pdf')
    cy.get('div.busy').should('not.exist')

    cy.get('li:contains("3 Complète avec : le, une, …") button:contains("Edit")').click()
    cy.get('label:contains("Instructions")').next().clear().type('Ceci est la consigne')
    cy.get('button:contains("Save")').click()
    cy.get('div.busy').should('not.exist')

    cy.get('li:contains("4 Écris une phrase en respe…") button:contains("Edit")').click()
    cy.get('canvas[style="position: absolute; top: 0px; left: 0px;"]').as('canvas')
    cy.get('@canvas').trigger('pointermove', 5, 5)
    cy.get('@canvas').trigger('pointerdown', 150, 375, { pointerId: 1 })
    cy.get('@canvas').trigger('pointermove', 300, 400)
    cy.get('@canvas').trigger('pointerup', 300, 400, { pointerId: 1 })
    cy.get('button:contains("Example")').click()
    cy.get('button:contains("Save")').click()
    cy.get('div.busy').should('not.exist')

    cy.request('/api/project-1-extraction-report.json').as('report')
    cy.get('@report').its('body.project.textbooks[0].exercises[0].events').should('deep.eq', [
      {'kind': 'InstructionsSetManually', 'value': 'Ceci est la consigne'},
    ])
    cy.get('@report').its('body.project.textbooks[0].exercises[1].events').should('deep.eq', [
      {
        kind: 'TextSelectedInPdf',
        pdf: {
          name: 'test.pdf',
          sha256: 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
          page: 1,
          rectangle: {
            start: {x: 303.099891274904, y: (isProdPreview ? 132.98518755564305 : 133.64431650361348)},
            stop: {x: 578.2122820411818, y: (isProdPreview ? 87.13273900117508 : 87.79186794914563)},
          },
        },
        value: 'pronom personnel / verbe / déterminant / nom\ncommun : Je mange une pomme.',
        textItems: [
          {
            str: '',
            font: 'g_d0_f6',
            left: 328.8189,
            width: 0,
            right: 328.8189,
            bottom: 115.6276,
            height: 0,
            top: 115.6276,
          },
          {
            str: 'pronom personnel / verbe / déterminant / nom',
            font: 'g_d0_f6',
            left: 328.8189,
            width: 215.80899999999994,
            right: 544.6279,
            bottom: 115.6276,
            height: 11.5,
            top: 127.1276,
          },
          {
            str: 'commun : Je mange une pomme.',
            font: 'g_d0_f6',
            left: 328.8189,
            width: 152.8580000000001,
            right: 481.67690000000005,
            bottom: 102.6096,
            height: 11.5,
            top: 114.1096,
          },
        ],
      },
      {
        'kind': 'SelectedTextAddedToExample',
        'valueBefore': 'pronom personnel / verbe / déterminant / nom commun :\r\nJe mange une pomme.',
        'valueAfter': 'pronom personnel / verbe / déterminant / nom commun :\r\nJe mange une pomme.\npronom personnel / verbe / déterminant / nom\ncommun : Je mange une pomme.',
      },
    ])
  })

  // @todo Add test showing we can delete and recreate an exercise (hunt possible bug in deletion)

  it('shows and hides the section editor dialog', () => {
    cy.visit('/project/1/textbook/1/page/6')
    cy.get('select').select('fr')
    cy.get('div.busy').should('not.exist')

    cy.get('h1').contains('Lien entre PDF et manuel').should('not.exist')

    cy.get('button').contains('⚙').click()
    cy.get('h1').contains('Lien entre PDF et manuel').should('exist')

    cy.get('button').contains('Annuler').click()
    cy.get('h1').contains('Lien entre PDF et manuel').should('not.exist')
  })
})
