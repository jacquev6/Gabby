import { useApiStore } from '../../frontend/src/frontend/stores/api'


function setLocale() {
  cy.get('select').first().select('en')
}

describe('Gabby', () => {
  before(console.clear)

  beforeEach(() => {
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=admin-user,more-test-exercises')
    cy.wrap(useApiStore()).then(api => api.auth.login('admin', 'password'))
    cy.viewport(1200, 200)
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
    setLocale()
    cy.get('.busy').should('not.exist')

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
    setLocale()
    cy.get('.busy').should('not.exist')

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
    setLocale()
    cy.get('.busy').should('not.exist')

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
    cy.get('button:contains("Delete")').last().should('not.be.visible')
    cy.get('button:contains("Delete")').last().scrollIntoView()
    cy.get('button:contains("Delete")').last().should('be.visible')
    cy.get('@container').its('scrollTop').should('be.gt', 0)
  })

  it('scrolls on exercise creation view', () => {
    cy.visit('/project-xkopqm/textbook-klxufv/page-7/new-exercise')
    setLocale()
    cy.get('.busy').should('not.exist')

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
    cy.get('[data-cy="create-then-next"]').should('not.be.visible')
    cy.get('[data-cy="create-then-next"]').scrollIntoView()
    cy.get('[data-cy="create-then-next"]').should('be.visible')
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
    setLocale()
    cy.get('.busy').should('not.exist')

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
    cy.get('[data-cy="save-then-back"]').should('not.be.visible')
    cy.get('[data-cy="save-then-back"]').scrollIntoView()
    cy.get('[data-cy="save-then-back"]').should('be.visible')
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
