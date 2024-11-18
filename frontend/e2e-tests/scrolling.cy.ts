import { loadFixtures, login, visit } from './utils'


describe('Gabby', () => {
  before(() => {
    console.clear()
    loadFixtures('more-test-exercises')
  })

  beforeEach(() => {
    cy.viewport(1200, 200)
    login()
  })

  function haveVerticalScrollbar(el: JQuery) {
    expect(el[0].scrollHeight).to.not.be.undefined
    expect(el[0].clientHeight).to.not.be.undefined
    expect(el[0].scrollHeight).to.be.gt(el[0].clientHeight)
  }

  function haveNoVerticalScrollbar(el: JQuery) {
    expect(el[0].scrollHeight).to.not.be.undefined
    expect(el[0].clientHeight).to.not.be.undefined
    expect(el[0].scrollHeight).to.eq(el[0].clientHeight)
  }

  function haveNoHorizontalScrollbar(el: JQuery) {
    expect(el[0].scrollHeight).to.not.be.undefined
    expect(el[0].clientHeight).to.not.be.undefined
    expect(el[0].scrollWidth).to.eq(el[0].clientWidth)
  }

  function haveNoScrollbar(el: JQuery) {
    haveNoVerticalScrollbar(el)
    haveNoHorizontalScrollbar(el)
  }

  function haveVerticalScrollbarOnly(el: JQuery) {
    haveVerticalScrollbar(el)
    haveNoHorizontalScrollbar(el)
  }

  function beAtTop(el: JQuery) {
    expect(el[0].scrollTop).to.eq(0)
  }

  function beScrolledDown(el: JQuery) {
    expect(el[0].scrollTop).to.be.gt(0)
  }

  it('scrolls on index view', () => {
    visit('/')

    cy.get('html').should(haveNoScrollbar)
    cy.get('body').should(haveNoScrollbar)

    cy.get('[data-cy="root-container"]').should('have.length', 1).as('container')
    cy.get('@container').should(haveVerticalScrollbarOnly)
    cy.get('@container').should(beAtTop)

    cy.get('[data-cy="create-project"]').should('not.be.visible')
    cy.get('[data-cy="create-project"]').scrollIntoView()
    cy.get('[data-cy="create-project"]').should('be.visible')

    cy.get('@container').should(beScrolledDown)
  })

  it('scrolls on project view', () => {
    visit('/project-xkopqm')

    cy.get('html').should(haveNoScrollbar)
    cy.get('body').should(haveNoScrollbar)

    cy.get('[data-cy="root-container"]').should('have.length', 1).as('container')
    cy.get('@container').should(haveVerticalScrollbarOnly)
    cy.get('@container').should(beAtTop)

    cy.get('[data-cy="create-exercise"]').should('not.be.visible')
    cy.get('[data-cy="create-exercise"]').scrollIntoView()
    cy.get('[data-cy="create-exercise"]').should('be.visible')

    cy.get('@container').should(beScrolledDown)
  })

  it('scrolls on exercises list view', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7')

    cy.get('html').should(haveNoScrollbar)
    cy.get('body').should(haveNoScrollbar)

    cy.get('[data-cy="pdf-container"]').should('have.length', 1).as('container')
    cy.get('@container').should(haveVerticalScrollbarOnly)
    cy.get('@container').should(beAtTop)
    cy.get('input[type="file"]').should('not.be.visible')
    cy.get('input[type="file"]').scrollIntoView()
    cy.get('input[type="file"]').should('be.visible')
    cy.get('@container').should(beScrolledDown)

    cy.get('[data-cy="right-col-1"]').should('have.length', 1).as('container')
    cy.get('@container').should(haveVerticalScrollbarOnly)
    cy.get('@container').should(beAtTop)
    cy.get('button:contains("Delete")').last().should('not.be.visible')
    cy.get('button:contains("Delete")').last().scrollIntoView()
    cy.get('button:contains("Delete")').last().should('be.visible')
    cy.get('@container').should(beScrolledDown)
  })

  it('scrolls on exercise creation view', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')

    cy.get('html').should(haveNoScrollbar)
    cy.get('body').should(haveNoScrollbar)

    cy.get('[data-cy="pdf-container"]').should('have.length', 1).as('container')
    cy.get('@container').should(haveVerticalScrollbarOnly)
    cy.get('@container').should(beAtTop)
    cy.get('input[type="file"]').should('not.be.visible')
    cy.get('input[type="file"]').scrollIntoView()
    cy.get('input[type="file"]').should('be.visible')
    cy.get('@container').should(beScrolledDown)

    cy.get('[data-cy="right-col-1"]').should(haveNoScrollbar)

    cy.get('[data-cy="left-col-2"]').should('have.length', 1).as('container')
    cy.get('@container').should(haveVerticalScrollbarOnly)
    cy.get('@container').should(beAtTop)
    cy.get('[data-cy="create-then-next"]').should('not.be.visible')
    cy.get('[data-cy="create-then-next"]').scrollIntoView()
    cy.get('[data-cy="create-then-next"]').should('be.visible')
    cy.get('@container').should(beScrolledDown)

    cy.get('label:contains("Adaptation type")').next().select('generic')
    cy.get('label:contains("Wording")').next().type('This is a quite long wording to ensure a scrollbar appears.', {delay: 0})
    cy.get('label:contains("Instructions")').next().type('Hello', {delay: 0})

    cy.get('[data-cy="gutter-2"]').should('have.length', 1).as('container')
    cy.get('@container').should(haveVerticalScrollbarOnly)
    cy.get('@container').should(beAtTop)
    cy.get('label:contains("Punctuation")').should('not.be.visible')
    cy.get('label:contains("Punctuation")').scrollIntoView()
    cy.get('label:contains("Punctuation")').should('be.visible')
    cy.get('@container').should(beScrolledDown)

    cy.get('[data-cy="right-col-2"]').should('have.length', 1).as('container')
    cy.get('@container').should(haveVerticalScrollbarOnly)
    cy.get('@container').should(beAtTop)
    cy.get('[data-cy="erase-responses"]').should('not.be.visible')
    cy.get('[data-cy="erase-responses"]').scrollIntoView()
    cy.get('[data-cy="erase-responses"]').should('be.visible')
    cy.get('@container').should(beScrolledDown)
  })

  it('scrolls on exercise edition view', () => {
    visit('/project-xkopqm/textbook-klxufv/page-7/exercise-vodhqn')

    cy.get('html').should(haveNoScrollbar)
    cy.get('body').should(haveNoScrollbar)

    cy.get('[data-cy="pdf-container"]').should('have.length', 1).as('container')
    cy.get('@container').should(haveVerticalScrollbarOnly)
    cy.get('@container').should(beAtTop)
    cy.get('input[type="file"]').should('not.be.visible')
    cy.get('input[type="file"]').scrollIntoView()
    cy.get('input[type="file"]').should('be.visible')
    cy.get('@container').should(beScrolledDown)

    cy.get('[data-cy="right-col-1"]').should(haveNoScrollbar)

    cy.get('[data-cy="left-col-2"]').should('have.length', 1).as('container')
    cy.get('@container').should(haveVerticalScrollbarOnly)
    cy.get('@container').should(beAtTop)
    cy.get('[data-cy="save-then-back"]').should('not.be.visible')
    cy.get('[data-cy="save-then-back"]').scrollIntoView()
    cy.get('[data-cy="save-then-back"]').should('be.visible')
    cy.get('@container').should(beScrolledDown)

    cy.get('[data-cy="gutter-2"]').should('have.length', 1).as('container')
    cy.get('@container').should(haveVerticalScrollbarOnly)
    cy.get('@container').should(beAtTop)
    cy.get('label:contains("Punctuation")').should('not.be.visible')
    cy.get('label:contains("Punctuation")').scrollIntoView()
    cy.get('label:contains("Punctuation")').should('be.visible')
    cy.get('@container').should(beScrolledDown)

    cy.get('[data-cy="right-col-2"]').should('have.length', 1).as('container')
    cy.get('@container').should(haveVerticalScrollbarOnly)
    cy.get('@container').should(beAtTop)
    cy.get('[data-cy="erase-responses"]').should('not.be.visible')
    cy.get('[data-cy="erase-responses"]').scrollIntoView()
    cy.get('[data-cy="erase-responses"]').should('be.visible')
    cy.get('@container').should(beScrolledDown)
  })
})
