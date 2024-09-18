import { visit, login, loadFixtures, notBusy, loadPdf } from './utils'


describe('Gabby', () => {
  before(console.clear)

  beforeEach(() => {
    loadFixtures('more-test-exercises')
    login()
  })

  it('navigates the textbook', () => {
    visit('/project-xkopqm/textbook-klxufv/page-6')

    cy.get('p:contains("Page"):contains("(on 7)") input').should('have.value', '6')
    cy.get('p:contains("The PDF that contains this page (test.pdf) has not been loaded yet.")').should('exist')

    cy.get('p:contains("Page"):contains("(on 7)") :contains(">")').click()
    cy.get('p:contains("Page"):contains("(on 7)") input').should('have.value', '7')
    cy.location('pathname').should('eq', '/project-xkopqm/textbook-klxufv/page-7')
    cy.get('p:contains("Page"):contains("(on 7)") :contains(">")').should('be.disabled')
    cy.get('p:contains("The PDF that contains this page (test.pdf) has not been loaded yet.")').should('exist')

    cy.get('p:contains("Page"):contains("(on 7)") :contains("<")').click()
    cy.get('p:contains("Page"):contains("(on 7)") :contains(">")').should('be.enabled')

    cy.get('p:contains("Page"):contains("(on 7)") :contains("<")').click()
    cy.get('p:contains("Page"):contains("(on 7)") input').should('have.value', '5')
    cy.location('pathname').should('eq', '/project-xkopqm/textbook-klxufv/page-5')
    cy.get('p:contains("No known PDF contains this page.")').should('exist')
    cy.get('p:contains("The PDF that contains this page (test.pdf) has not been loaded yet.")').should('not.exist')

    cy.get('p:contains("Page"):contains("(on 7)") input').clear().type('1')
    cy.location('pathname').should('eq', '/project-xkopqm/textbook-klxufv/page-1')
    cy.get('p:contains("Page"):contains("(on 7)") :contains("<")').should('be.disabled')
    cy.get('p:contains("No known PDF contains this page.")').should('exist')

    cy.get('p:contains("Page"):contains("(on 7)") input').clear().type('100').blur()
    notBusy()
    cy.get('p:contains("Page"):contains("(on 7)") input').should('have.value', '1')
    cy.location('pathname').should('eq', '/project-xkopqm/textbook-klxufv/page-1')

    cy.get('p:contains("Page"):contains("(on 7)") input').clear().type('200').blur()
    notBusy()
    cy.get('p:contains("Page"):contains("(on 7)") input').should('have.value', '2')
    cy.location('pathname').should('eq', '/project-xkopqm/textbook-klxufv/page-2')
  })

  it('loads a PDF', () => {
    visit('/project-xkopqm/textbook-klxufv/page-6')

    notBusy()
    cy.get('p:contains("The PDF that contains this page (test.pdf) has not been loaded yet.")').should('exist')

    loadPdf('test')
    cy.get('p:contains("The PDF that contains this page (test.pdf) has not been loaded yet.")').should('not.exist')
    cy.get('input[type=file]').should('not.exist')
  })

  it("navigates the PDF when creating an exercise - changes exercise's page", () => {
    visit('/project-xkopqm/textbook-klxufv/page-6/new-exercise', {wysiwyg: false, pdf: 'test'})

    cy.get('canvas').first().as('renderer')
    cy.get('canvas[style="position: absolute; top: 0px; left: 0px;"]').first().as('highlighter')

    cy.get('[data-cy-exercise-field="number"]').type('5')
    cy.get('[data-cy-exercise-field="page"]').should('have.value', 6)
    cy.get('@renderer').should('have.attr', 'data-cy-rendered-page', '1')
    cy.get('@highlighter').should('have.attr', 'data-cy-drawn-rectangles').then(JSON.parse as any/* Work around Cypress typing limitations */).should(
      'deep.equal',
      {
        "grey": [
          {
            "left": 321.7851195562453,
            "top": 165.01653324025676,
            "width": 241.30086580086578,
            "height": 133.5448844074425
          },
          {
            "left": 321.7851195562453,
            "top": 59.10162491711276,
            "width": 244.06385281385286,
            "height": 106.83590752595387
          },
        ],
        "surrounded": [],
      },
    )

    cy.get('p:contains("Page"):contains("(on 7)") :contains(">")').click()
    notBusy()
    cy.location('pathname').should('eq', '/project-xkopqm/textbook-klxufv/page-7/new-exercise')
    cy.location('search').should('eq', '')
    cy.get('[data-cy-exercise-field="number"]').should('have.value', '5')
    cy.get('[data-cy-exercise-field="page"]').should('have.value', 7)
    cy.get('@renderer').should('have.attr', 'data-cy-rendered-page', '2')
    cy.get('@highlighter').should('have.attr', 'data-cy-drawn-rectangles').then(JSON.parse as any/* Work around Cypress typing limitations */).should(
      'deep.equal',
      {
        "grey": [
          {
            "left": 41.81553087016726,
            "top": 340.0079023796095,
            "width": 266.18958445966337,
            "height": 172.8520559081844
          },
          {
            "left": 60,
            "top": 180,
            "width": 190,
            "height": 140
          },
          {
            "left": 313.4961585172843,
            "top": 689.0650796391174,
            "width": 223.80194805194805,
            "height": 101.30991230909444
          },
          {
            "left": 312.61445878367766,
            "top": 452.9379122396233,
            "width": 244.29520305389025,
            "height": 84.1213338753164
          },
        ],
        "surrounded": [],
      },
    )
    cy.get('[data-cy-exercise-field="instructions"]').type('Do this')

    cy.get('button:contains("Save then next")').click()
    notBusy()
    cy.get('a:contains("Back to list (without saving)")').click()

    notBusy()
    cy.location('pathname').should('eq', '/project-xkopqm/textbook-klxufv/page-7')
    cy.get('li:contains("5"):contains("Do this")').should('exist')
  })

  it("navigates the PDF when creating an exercise - doesn't change exercise's page - save then next", () => {
    visit('/project-xkopqm/textbook-klxufv/page-6/new-exercise', {wysiwyg: false, pdf: 'test'})

    cy.get('canvas').first().as('renderer')
    cy.get('canvas[style="position: absolute; top: 0px; left: 0px;"]').first().as('highlighter')

    cy.get('[data-cy-exercise-field="number"]').type('5')
    cy.get('[data-cy-exercise-field="page"]').should('have.value', 6)
    cy.get('[data-cy-exercise-field="instructions"]').type('Do that')
    cy.get('@renderer').should('have.attr', 'data-cy-rendered-page', '1')
    cy.get('@highlighter').should('have.attr', 'data-cy-drawn-rectangles').then(JSON.parse as any/* Work around Cypress typing limitations */).should(
      'deep.equal',
      {
        "grey": [
          {
            "left": 321.7851195562453,
            "top": 165.01653324025676,
            "width": 241.30086580086578,
            "height": 133.5448844074425
          },
          {
            "left": 321.7851195562453,
            "top": 59.10162491711276,
            "width": 244.06385281385286,
            "height": 106.83590752595387
          },
        ],
        "surrounded": [],
      },
    )

    cy.get('p:contains("Page"):contains("(on 7)") :contains(">")').click()
    notBusy()
    cy.location('pathname').should('eq', '/project-xkopqm/textbook-klxufv/page-6/new-exercise')
    cy.location('search').should('eq', '?displayPage=7')
    cy.get('[data-cy-exercise-field="number"]').should('have.value', '5')
    cy.get('[data-cy-exercise-field="page"]').should('have.value', 6)
    cy.get('label:contains("Page"):contains("not the one displayed")').should('exist')
    cy.get('@renderer').should('have.attr', 'data-cy-rendered-page', '2')
    cy.get('@highlighter').should('have.attr', 'data-cy-drawn-rectangles').then(JSON.parse as any/* Work around Cypress typing limitations */).should(
      'deep.equal',
      {
        "grey": [
          {
            "left": 41.81553087016726,
            "top": 340.0079023796095,
            "width": 266.18958445966337,
            "height": 172.8520559081844
          },
          {
            "left": 60,
            "top": 180,
            "width": 190,
            "height": 140
          },
          {
            "left": 313.4961585172843,
            "top": 689.0650796391174,
            "width": 223.80194805194805,
            "height": 101.30991230909444
          },
          {
            "left": 312.61445878367766,
            "top": 452.9379122396233,
            "width": 244.29520305389025,
            "height": 84.1213338753164
          },
        ],
        "surrounded": [],
      },
    )
    cy.get('[data-cy-exercise-field="instructions"]').should('have.value', 'Do that')

    cy.get('button:contains("Save then next")').click()
    notBusy()
    cy.location('pathname').should('eq', '/project-xkopqm/textbook-klxufv/page-7/new-exercise')

    cy.get('a:contains("Back to list (without saving)")').click()
    notBusy()
    cy.location('pathname').should('eq', '/project-xkopqm/textbook-klxufv/page-7')
    cy.get('li:contains("5"):contains("Do that")').should('not.exist')

    visit('/project-xkopqm/textbook-klxufv/page-6')
    cy.get('li:contains("5"):contains("Do that")').should('exist')
  })

  it("navigates the PDF when creating an exercise - doesn't change exercise's page - save then back", () => {
    visit('/project-xkopqm/textbook-klxufv/page-6/new-exercise', {wysiwyg: false, pdf: 'test'})

    cy.get('canvas').first().as('renderer')
    cy.get('canvas[style="position: absolute; top: 0px; left: 0px;"]').first().as('highlighter')

    cy.get('[data-cy-exercise-field="number"]').type('5')
    cy.get('[data-cy-exercise-field="page"]').should('have.value', 6)
    cy.get('[data-cy-exercise-field="instructions"]').type('Do that')
    cy.get('@renderer').should('have.attr', 'data-cy-rendered-page', '1')
    cy.get('@highlighter').should('have.attr', 'data-cy-drawn-rectangles').then(JSON.parse as any/* Work around Cypress typing limitations */).should(
      'deep.equal',
      {
        "grey": [
          {
            "left": 321.7851195562453,
            "top": 165.01653324025676,
            "width": 241.30086580086578,
            "height": 133.5448844074425
          },
          {
            "left": 321.7851195562453,
            "top": 59.10162491711276,
            "width": 244.06385281385286,
            "height": 106.83590752595387
          },
        ],
        "surrounded": [],
      },
    )

    cy.get('p:contains("Page"):contains("(on 7)") :contains(">")').click()
    notBusy()
    cy.location('pathname').should('eq', '/project-xkopqm/textbook-klxufv/page-6/new-exercise')
    cy.location('search').should('eq', '?displayPage=7')
    cy.get('[data-cy-exercise-field="number"]').should('have.value', '5')
    cy.get('[data-cy-exercise-field="page"]').should('have.value', 6)
    cy.get('label:contains("Page"):contains("not the one displayed")').should('exist')
    cy.get('@renderer').should('have.attr', 'data-cy-rendered-page', '2')
    cy.get('@highlighter').should('have.attr', 'data-cy-drawn-rectangles').then(JSON.parse as any/* Work around Cypress typing limitations */).should(
      'deep.equal',
      {
        "grey": [
          {
            "left": 41.81553087016726,
            "top": 340.0079023796095,
            "width": 266.18958445966337,
            "height": 172.8520559081844
          },
          {
            "left": 60,
            "top": 180,
            "width": 190,
            "height": 140
          },
          {
            "left": 313.4961585172843,
            "top": 689.0650796391174,
            "width": 223.80194805194805,
            "height": 101.30991230909444
          },
          {
            "left": 312.61445878367766,
            "top": 452.9379122396233,
            "width": 244.29520305389025,
            "height": 84.1213338753164
          },
        ],
        "surrounded": [],
      },
    )
    cy.get('[data-cy-exercise-field="instructions"]').should('have.value', 'Do that')

    cy.get('button:contains("Save then back to list")').click()
    notBusy()
    cy.location('pathname').should('eq', '/project-xkopqm/textbook-klxufv/page-6')
    cy.get('li:contains("5"):contains("Do that")').should('exist')
  })

  it("navigates the PDF when editing an exercise - doesn't change exercise's page", () => {
    visit('/project-xkopqm/textbook-klxufv/page-6/exercise-wbqloc', {pdf: 'test'})

    cy.get('canvas').first().as('renderer')
    cy.get('canvas[style="position: absolute; top: 0px; left: 0px;"]').first().as('highlighter')

    cy.get('[data-cy-exercise-field="number"]').should('have.value', '3')
    cy.get('[data-cy-exercise-field="page"]').should('have.value', 6)
    cy.get('@renderer').should('have.attr', 'data-cy-rendered-page', '1')
    cy.get('@highlighter').should('have.attr', 'data-cy-drawn-rectangles').then(JSON.parse as any/* Work around Cypress typing limitations */).should(
      'deep.equal',
      {
        "grey": [
          {
            "left": 321.7851195562453,
            "top": 59.10162491711276,
            "width": 244.06385281385286,
            "height": 106.83590752595387
          },
        ],
        "surrounded": [
          {
            "left": 321.7851195562453,
            "top": 165.01653324025676,
            "width": 241.30086580086578,
            "height": 133.5448844074425
          },
        ],
      },
    )

    cy.get('p:contains("Page"):contains("(on 7)") :contains(">")').click()
    notBusy()
    cy.location('pathname').should('eq', '/project-xkopqm/textbook-klxufv/page-6/exercise-wbqloc')
    cy.location('search').should('eq', '?displayPage=7')
    cy.get('[data-cy-exercise-field="number"]').should('have.value', '3')
    cy.get('[data-cy-exercise-field="page"]').should('have.value', 6)
    cy.get('label:contains("Page"):contains("not the one displayed")').should('exist')
    cy.get('@renderer').should('have.attr', 'data-cy-rendered-page', '2')
    cy.get('@highlighter').should('have.attr', 'data-cy-drawn-rectangles').then(JSON.parse as any/* Work around Cypress typing limitations */).should(
      'deep.equal',
      {
        "grey": [
          {
            "left": 41.81553087016726,
            "top": 340.0079023796095,
            "width": 266.18958445966337,
            "height": 172.8520559081844
          },
          {
            "left": 60,
            "top": 180,
            "width": 190,
            "height": 140
          },
          {
            "left": 313.4961585172843,
            "top": 689.0650796391174,
            "width": 223.80194805194805,
            "height": 101.30991230909444
          },
          {
            "left": 312.61445878367766,
            "top": 452.9379122396233,
            "width": 244.29520305389025,
            "height": 84.1213338753164
          },
        ],
        "surrounded": [],
      },
    )
  })
})
