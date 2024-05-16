describe('Gabby', () => {
  before(console.clear)

  beforeEach(() => {
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=test-exercises,more-test-exercises')
    cy.viewport(1200, 200)
  })

  after(() => {
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=test-exercises,more-test-exercises')
  })

  function haveVerticalScrollbar(el) {
    expect(el.scrollHeight).to.not.be.undefined
    expect(el.clientHeight).to.not.be.undefined
    expect(el.scrollHeight).to.be.gt(el.clientHeight)
  }

  function haveNoVerticalScrollbar(el) {
    expect(el.scrollHeight).to.not.be.undefined
    expect(el.clientHeight).to.not.be.undefined
    expect(el.scrollHeight).to.eq(el.clientHeight)
  }

  function haveNoHorizontalScrollbar(el) {
    expect(el.scrollHeight).to.not.be.undefined
    expect(el.clientHeight).to.not.be.undefined
    expect(el.scrollWidth).to.eq(el.clientWidth)
  }

  function haveNoScrollbar(el) {
    haveNoVerticalScrollbar(el)
    haveNoHorizontalScrollbar(el)
  }

  function haveVerticalScrollbarOnly(el) {
    haveVerticalScrollbar(el)
    haveNoHorizontalScrollbar(el)
  }

  it('scrolls on index view', () => {
    cy.visit('/')
    cy.get('.busy').should('not.exist')
    cy.get('select').first().select('en')

    cy.get('html').its('0').should(haveNoScrollbar)
    cy.get('body').its('0').should(haveNoScrollbar)

    cy.get('[data-cy="root-container"]').should('have.length', 1).its('0').as('container')
    cy.get('@container').should(haveVerticalScrollbarOnly)
    cy.get('@container').its('scrollTop').should('eq', 0)

    cy.get('[data-cy="create-project"]').should('not.be.visible')
    cy.get('[data-cy="create-project"]').scrollIntoView()
    cy.get('[data-cy="create-project"]').should('be.visible')

    cy.get('@container').its('scrollTop').should('be.gt', 0)
  })

  it('scrolls on project view', () => {
    cy.visit('/project-xkopqm')
    cy.get('.busy').should('not.exist')
    cy.get('select').first().select('en')

    cy.get('html').its('0').should(haveNoScrollbar)
    cy.get('body').its('0').should(haveNoScrollbar)

    cy.get('[data-cy="root-container"]').should('have.length', 1).its('0').as('container')
    cy.get('@container').should(haveVerticalScrollbarOnly)
    cy.get('@container').its('scrollTop').should('eq', 0)

    cy.get('[data-cy="create-exercise"]').should('not.be.visible')
    cy.get('[data-cy="create-exercise"]').scrollIntoView()
    cy.get('[data-cy="create-exercise"]').should('be.visible')

    cy.get('@container').its('scrollTop').should('be.gt', 0)
  })

  it('scrolls on exercises list view', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-7')
    cy.get('.busy').should('not.exist')
    cy.get('select').first().select('en')

    cy.get('html').its('0').should(haveNoScrollbar)
    cy.get('body').its('0').should(haveNoScrollbar)

    cy.get('[data-cy="pdf-container"]').should('have.length', 1).its('0').as('container')
    cy.get('@container').should(haveVerticalScrollbarOnly)
    cy.get('@container').its('scrollTop').should('eq', 0)
    cy.get('input[type="file"]').should('not.be.visible')
    cy.get('input[type="file"]').scrollIntoView()
    cy.get('input[type="file"]').should('be.visible')
    cy.get('@container').its('scrollTop').should('be.gt', 0)

    cy.get('[data-cy="right-col-1"]').should('have.length', 1).its('0').as('container')
    cy.get('@container').should(haveVerticalScrollbarOnly)
    cy.get('@container').its('scrollTop').should('eq', 0)
    cy.get('[data-cy="new-exercise"]').should('not.be.visible')
    cy.get('[data-cy="new-exercise"]').scrollIntoView()
    cy.get('[data-cy="new-exercise"]').should('be.visible')
    cy.get('@container').its('scrollTop').should('be.gt', 0)
  })

  it('scrolls on exercise creation view', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')
    cy.get('.busy').should('not.exist')
    cy.get('select').first().select('en')

    cy.get('html').its('0').should(haveNoScrollbar)
    cy.get('body').its('0').should(haveNoScrollbar)

    cy.get('[data-cy="pdf-container"]').should('have.length', 1).its('0').as('container')
    cy.get('@container').should(haveVerticalScrollbarOnly)
    cy.get('@container').its('scrollTop').should('eq', 0)
    cy.get('input[type="file"]').should('not.be.visible')
    cy.get('input[type="file"]').scrollIntoView()
    cy.get('input[type="file"]').should('be.visible')
    cy.get('@container').its('scrollTop').should('be.gt', 0)

    cy.get('[data-cy="right-col-1"]').its('0').should(haveNoScrollbar)

    cy.get('[data-cy="left-col-2"]').should('have.length', 1).its('0').as('container')
    cy.get('@container').should(haveVerticalScrollbarOnly)
    cy.get('@container').its('scrollTop').should('eq', 0)
    cy.get('[data-cy="create-exercise"]').should('not.be.visible')
    cy.get('[data-cy="create-exercise"]').scrollIntoView()
    cy.get('[data-cy="create-exercise"]').should('be.visible')
    cy.get('@container').its('scrollTop').should('be.gt', 0)

    cy.get('[data-cy="gutter-2"]').should('have.length', 1).its('0').as('container')
    cy.get('@container').should(haveVerticalScrollbarOnly)
    cy.get('@container').its('scrollTop').should('eq', 0)
    cy.get('[data-cy="apply-replace"]').should('not.be.visible')
    cy.get('[data-cy="apply-replace"]').scrollIntoView()
    cy.get('[data-cy="apply-replace"]').should('be.visible')
    cy.get('@container').its('scrollTop').should('be.gt', 0)

    cy.get('label:contains("Adaptation type")').next().select('selectThingsAdaptation')
    cy.get('label:contains("Wording")').next().type('This is a quite long wording to ensure a scrollbar appears.')
    cy.get('label:contains("Instructions")').next().type('Hello')

    cy.get('[data-cy="right-col-2"]').should('have.length', 1).its('0').as('container')
    cy.get('@container').should(haveVerticalScrollbarOnly)
    cy.get('@container').its('scrollTop').should('eq', 0)
    cy.get('[data-cy="erase-responses"]').should('not.be.visible')
    cy.get('[data-cy="erase-responses"]').scrollIntoView()
    cy.get('[data-cy="erase-responses"]').should('be.visible')
    cy.get('@container').its('scrollTop').should('be.gt', 0)
  })

  it('scrolls on exercise edition view', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-7/exercise-vodhqn')
    cy.get('.busy').should('not.exist')
    cy.get('select').first().select('en')

    cy.get('html').its('0').should(haveNoScrollbar)
    cy.get('body').its('0').should(haveNoScrollbar)

    cy.get('[data-cy="pdf-container"]').should('have.length', 1).its('0').as('container')
    cy.get('@container').should(haveVerticalScrollbarOnly)
    cy.get('@container').its('scrollTop').should('eq', 0)
    cy.get('input[type="file"]').should('not.be.visible')
    cy.get('input[type="file"]').scrollIntoView()
    cy.get('input[type="file"]').should('be.visible')
    cy.get('@container').its('scrollTop').should('be.gt', 0)

    cy.get('[data-cy="right-col-1"]').its('0').should(haveNoScrollbar)

    cy.get('[data-cy="left-col-2"]').should('have.length', 1).its('0').as('container')
    cy.get('@container').should(haveVerticalScrollbarOnly)
    cy.get('@container').its('scrollTop').should('eq', 0)
    cy.get('[data-cy="save-exercise"]').should('not.be.visible')
    cy.get('[data-cy="save-exercise"]').scrollIntoView()
    cy.get('[data-cy="save-exercise"]').should('be.visible')
    cy.get('@container').its('scrollTop').should('be.gt', 0)

    cy.get('[data-cy="gutter-2"]').should('have.length', 1).its('0').as('container')
    cy.get('@container').should(haveVerticalScrollbarOnly)
    cy.get('@container').its('scrollTop').should('eq', 0)
    cy.get('[data-cy="apply-replace"]').should('not.be.visible')
    cy.get('[data-cy="apply-replace"]').scrollIntoView()
    cy.get('[data-cy="apply-replace"]').should('be.visible')
    cy.get('@container').its('scrollTop').should('be.gt', 0)

    cy.get('[data-cy="right-col-2"]').should('have.length', 1).its('0').as('container')
    cy.get('@container').should(haveVerticalScrollbarOnly)
    cy.get('@container').its('scrollTop').should('eq', 0)
    cy.get('[data-cy="erase-responses"]').should('not.be.visible')
    cy.get('[data-cy="erase-responses"]').scrollIntoView()
    cy.get('[data-cy="erase-responses"]').should('be.visible')
    cy.get('@container').its('scrollTop').should('be.gt', 0)
  })
})