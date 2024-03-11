async function getAllExtractionEvents(exerciseId) {
  const all = []
  var url = `/api/extractionEvents?filter[exercise]=${exerciseId}`
  while (url) {
    const response = await (await fetch(url)).json()
    all.push(...response.data.map(event => JSON.parse(event.attributes.event)))
    url = response.links.next
  }
  return all
}

describe('Extraction events', () => {
  before(console.clear)

  it('are all gathered during extraction', () => {
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=test-exercises')

    cy.visit('/project/1')
    cy.get('input[type=file]').selectFile('../pdf-examples/test.pdf')
    cy.get('.spinner-border').should('exist')
    cy.get('.spinner-border').should('not.exist')

    cy.get('a').contains('Page 6').click()
    cy.get('.spinner-border').should('not.exist')

    cy.get('button').contains('Nouvel exercice').click()

    cy.get('label').contains('Numéro').next().type('1')
    cy.get('label').contains('Consigne').next().type('Ceci est la consigne')
    cy.get('p').contains('Exemple').click()
    cy.focused().type('Ceci est un exemple')
    cy.get('p').contains('Indice').click()
    cy.focused().type('Ceci est un indice')
    cy.get('label').contains('Énoncé').next().type('Ceci est l\'énoncé')
    cy.get('button').contains('Enregistrer').click()
    cy.get('.spinner-border').should('not.exist')

    cy.get('canvas[style="position: absolute; top: 0px; left: 0px;"]').as('canvas')
    cy.get('@canvas').trigger('pointermove', 5, 5)
    cy.get('@canvas').trigger('pointerdown', 15, 370, { pointerId: 1 })
    cy.get('@canvas').trigger('pointermove', 150, 395)
    cy.get('@canvas').trigger('pointerup', 150, 395, { pointerId: 1 })
    cy.get('button').contains('Consigne').click()
    cy.get('@canvas').trigger('pointermove', 5, 5)
    cy.get('@canvas').trigger('pointerdown', 15, 390, { pointerId: 1 })
    cy.get('@canvas').trigger('pointermove', 150, 415)
    cy.get('@canvas').trigger('pointerup', 150, 415, { pointerId: 1 })
    cy.get('label').contains('Texte sélectionné').next().type('Blah blah blah')
    cy.get('button').contains('Énoncé').click()
    cy.get('button').contains('Enregistrer').click()
    cy.get('.spinner-border').should('not.exist')
    
    cy.get('button').contains('Annuler').click()

    cy.wrap(getAllExtractionEvents).then(f => f(7)).should('deep.eq', [
      {kind: 'ExerciseNumberSetManually', value: 1},
      {kind: 'InstructionsSetManually', value: 'Ceci est la consigne'},
      {kind: 'ExampleSetManually', value: 'Ceci est un exemple'},
      {kind: 'ClueSetManually', value: 'Ceci est un indice'},
      {kind: 'WordingSetManually', value: 'Ceci est l\'énoncé'},
    ])

    // @todo Log a rectangle around the whole exercise
    cy.wrap(getAllExtractionEvents).then(f => f(8)).as('events')
    cy.get('@events').should('have.length', 6)
    cy.get('@events').its(0).should('deep.eq',
      {kind: 'ExerciseNumberSetAutomatically', value: 2},
    )
    cy.get('@events').its(1).should('deep.eq',
      {
        kind: 'TextSelectedInPdf',
        pdf: {
          name: 'test.pdf',
          sha256: 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
          page: 1,
          rectangle: {
            start: {x: 55.49873958525407, y: 142.81480621450703},
            stop: {x: 303.099891274904, y: 96.96235766003917},
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
    )
    cy.get('@events').its(2).should('deep.eq',
      {
        kind: 'SelectedTextAddedToInstructions',
        valueBefore: '',
        valueAfter: 'Classe les mots en trois groupes :\nnom, verbe, adjectif.',
      },
    )
    cy.get('@events').its(3).should('deep.eq',
      {
        kind: 'TextSelectedInPdf',
        pdf: {
          name: 'test.pdf',
          sha256: 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c',
          page: 1,
          rectangle: {
            start: {x: 55.49873958525407, y: 106.13284737093272},
            stop: {x: 303.099891274904, y: 60.28039881646487},
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
    )
    cy.get('@events').its(4).should('deep.eq',
      {
        kind: 'SelectedTextEdited',
        value: 'verrou ◆ baigner ◆ joli ◆ chaleur ◆ grosse ◆\nsurveiller ◆ degré ◆ librairie ◆ repas ◆ parlerBlah blah blah',
      },
    )
    cy.get('@events').its(5).should('deep.eq',
      {
        kind: 'SelectedTextAddedToWording',
        valueBefore: '',
        valueAfter: 'verrou ◆ baigner ◆ joli ◆ chaleur ◆ grosse ◆\nsurveiller ◆ degré ◆ librairie ◆ repas ◆ parlerBlah blah blah',
      },
    )
  })
})
