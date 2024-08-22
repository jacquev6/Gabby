import { BModal } from "."

describe('Bootstrap Modal', () => {
  before(console.clear)

  beforeEach(() => {
    cy.viewport(1000, 500)
  })

  function component(el: JQuery): InstanceType<typeof BModal> {
    return (el as any/* Work around Cypress typing limitations */).component
  }

  it('shows and hides', () => {
    // @ts-ignore// Work around Cypress typing limitations
    cy.mount(BModal).as('modal')

    cy.get('.modal').should('not.exist')

    cy.get('@modal').then(el => component(el).show())
    
    cy.get('.modal').should('exist')
    cy.get('@modal').its('component.active').should('be.true')
    cy.get('.modal-backdrop').should('exist')

    cy.get('@modal').then(el => component(el).hide())

    cy.get('.modal-backdrop').should('not.exist')
    cy.get('@modal').its('component.active').should('be.false')
    cy.get('.modal').should('not.exist')
  })

  function mountAndShowFloating(at: {x: number, y: number} | null, options = {}) {
    // @ts-ignore// Work around Cypress typing limitations
    cy.mount(BModal, options).as('modal')
    cy.get('@modal').then(el => component(el).show({at}))
    shouldExist()
  }

  function mountAndShow(options = {}) {
    mountAndShowFloating(null, options)
  }

  function shouldExist() {
    cy.wait(250)  // Removing this 'wait' causes a 'TypeError' in Bootstrap's 'modal.js', which breaks the next test
    cy.get('@modal').its('component.transitioning').should('be.false')
    cy.get('@modal').its('component.active').should('be.true')
    cy.get('.modal').should('exist')
  }

  function hide() {
    cy.get('@modal').then(el => component(el).hide())
    shouldNotExist()
  }

  function shouldNotExist() {
    cy.get('@modal').its('component.transitioning').should('be.false')
    cy.get('@modal').its('component.active').should('be.false')
    cy.get('.modal').should('not.exist')
  }

  it('tolerates being hidden multiple times', () => {
    mountAndShow()

    cy.get('@modal').then(el => component(el).hide())
    cy.get('@modal').then(el => component(el).hide())
    cy.get('@modal').then(el => component(el).hide())

    cy.get('.modal').should('not.exist')

    cy.get('@modal').then(el => component(el).hide())
    cy.get('@modal').then(el => component(el).hide())
    cy.get('@modal').then(el => component(el).hide())
  })

  it('tolerates being shown multiple times', () => {
    // @ts-ignore// Work around Cypress typing limitations
    cy.mount(BModal).as('modal')
    cy.get('@modal').then(el => component(el).show())
    cy.get('@modal').then(el => component(el).show())
    cy.get('@modal').then(el => component(el).show())

    cy.get('@modal').its('component.active').should('be.true')

    cy.get('@modal').then(el => component(el).show())
    cy.get('@modal').then(el => component(el).show())
    cy.get('@modal').then(el => component(el).show())

    hide()
  })

  it('renders its slots', () => {
    mountAndShow({slots: {header: 'Header', body: 'Body', footer: 'Footer'}})

    cy.get('.modal-header').should('contain', 'Header')
    cy.get('.modal-body').should('contain', 'Body')
    cy.get('.modal-footer').should('contain', 'Footer')

    hide()
  })

  it('closes via its "Close" button', () => {
    mountAndShow()

    cy.get('.modal-header button[aria-label=Close]').click()

    shouldNotExist()
  })

  it('has no "Close" button', () => {
    mountAndShow({props: {close: false}})

    cy.get('.modal-header button[aria-label=Close]').should('not.exist')

    hide()
  })

  it('closes via its backdrop', () => {
    mountAndShow()

    cy.get('.modal').click()

    shouldNotExist()
  })

  it('has no backdrop', () => {
    mountAndShow({props: {backdrop: false}})

    cy.get('.modal-backdrop').should('not.exist')

    cy.get('.modal').click()

    shouldExist()

    hide()
  })

  it('has a static backdrop', () => {
    mountAndShow({props: {backdrop: 'static'}})

    cy.get('.modal').click()

    shouldExist()

    hide()
  })

  it('closes via Esc key', () => {
    mountAndShow()

    cy.get('body').type('{esc}')

    shouldNotExist()
  })

  it('does not close via Esc key', () => {
    mountAndShow({props: {keyboard: false}})

    cy.get('body').type('{esc}')

    shouldExist()

    hide()
  })

  it('floats and closes via its backdrop', () => {
    mountAndShowFloating({x: 100, y: 400}, {props: {fade: false}})

    cy.get('.modal').click()

    shouldNotExist()
  })

  it('floats and closes via its "Close" button', () => {
    mountAndShowFloating({x: 100, y: 400}, {props: {fade: false}})

    cy.get('.modal-header button[aria-label=Close]').click()

    shouldNotExist()
  })

  it('floats and closes via Esc key', () => {
    mountAndShowFloating({x: 100, y: 400}, {props: {fade: false}})

    cy.get('body').type('{esc}')

    shouldNotExist()
  })
})
