import { BModal } from "."

describe('Bootstrap Modal', () => {
  beforeEach(() => {
    cy.viewport(1000, 500)
  })

  it('shows and hides', () => {
    cy.mount(BModal).as('modal')

    cy.get('.modal').should('not.exist')

    cy.get('@modal').then(({component}) => component.show())
    
    cy.get('.modal').should('exist')
    cy.get('@modal').its('component.active').should('be.true')
    cy.get('.modal-backdrop').should('exist')

    cy.get('@modal').then(({component}) => component.hide())

    cy.get('.modal-backdrop').should('not.exist')
    cy.get('@modal').its('component.active').should('be.false')
    cy.get('.modal').should('not.exist')
  })

  it('tolerates being hidden multiple times', () => {
    cy.mount(BModal, {slots: {header: 'Header', body: 'Body', footer: 'Footer'}}).as('modal')
    cy.get('@modal').then(({component}) => component.show())
    cy.get('@modal').its('component.active').should('be.true')

    cy.get('@modal').then(({component}) => component.hide())
    cy.get('@modal').then(({component}) => component.hide())
    cy.get('@modal').then(({component}) => component.hide())

    cy.get('.modal').should('not.exist')

    cy.get('@modal').then(({component}) => component.hide())
    cy.get('@modal').then(({component}) => component.hide())
    cy.get('@modal').then(({component}) => component.hide())
  })

  it('tolerates being shown multiple times', () => {
    cy.mount(BModal, {slots: {header: 'Header', body: 'Body', footer: 'Footer'}}).as('modal')
    cy.get('@modal').then(({component}) => component.show())
    cy.get('@modal').then(({component}) => component.show())
    cy.get('@modal').then(({component}) => component.show())

    cy.get('@modal').its('component.active').should('be.true')

    cy.get('@modal').then(({component}) => component.show())
    cy.get('@modal').then(({component}) => component.show())
    cy.get('@modal').then(({component}) => component.show())

    cy.get('@modal').then(({component}) => component.hide())

    cy.get('.modal').should('not.exist')
  })

  it('renders its slots', () => {
    cy.mount(BModal, {slots: {header: 'Header', body: 'Body', footer: 'Footer'}}).as('modal')
    cy.get('@modal').then(({component}) => component.show())
    cy.get('@modal').its('component.active').should('be.true')

    cy.get('.modal-header').should('contain', 'Header')
    cy.get('.modal-body').should('contain', 'Body')
    cy.get('.modal-footer').should('contain', 'Footer')

    cy.get('@modal').then(({component}) => component.hide())
    cy.get('.modal').should('not.exist')
  })

  it('closes via its "Close" button', () => {
    cy.mount(BModal).as('modal')
    cy.get('@modal').then(({component}) => component.show())
    cy.get('@modal').its('component.active').should('be.true')

    cy.get('.modal-header button[aria-label=Close]').click()

    cy.get('.modal').should('not.exist')
  })

  it('has no "Close" button', () => {
    cy.mount(BModal, {props: {close: false}}).as('modal')
    cy.get('@modal').then(({component}) => component.show())
    cy.get('@modal').its('component.active').should('be.true')

    cy.get('.modal-header button[aria-label=Close]').should('not.exist')

    cy.get('@modal').then(({component}) => component.hide())
    cy.get('.modal').should('not.exist')
  })

  it('closes via its backdrop', () => {
    cy.mount(BModal).as('modal')
    cy.get('@modal').then(({component}) => component.show())
    cy.get('@modal').its('component.active').should('be.true')

    cy.get('.modal').click()

    cy.get('.modal').should('not.exist')
  })

  it('has no backdrop', () => {
    cy.mount(BModal, {props: {backdrop: false}}).as('modal')
    cy.get('@modal').then(({component}) => component.show())
    cy.get('@modal').its('component.active').should('be.true')

    cy.get('.modal-backdrop').should('not.exist')

    cy.get('.modal').click()

    cy.get('@modal').its('component.active').should('be.true')

    cy.get('@modal').then(({component}) => component.hide())
    cy.get('.modal').should('not.exist')
  })

  it('has a static backdrop', () => {
    cy.mount(BModal, {props: {backdrop: 'static'}}).as('modal')
    cy.get('@modal').then(({component}) => component.show())
    cy.get('@modal').its('component.active').should('be.true')

    cy.get('.modal').click()

    cy.get('@modal').its('component.active').should('be.true')

    cy.get('@modal').then(({component}) => component.hide())
    cy.get('.modal').should('not.exist')
  })
})
