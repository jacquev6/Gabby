import FloatingModal from '../FloatingModal.vue'


describe('FloatingModal', () => {
  it('renders its title', () => {
    cy.mount(FloatingModal, {props: {title: 'Hello Cypress', reference: {x: 200, y: 300}}})
    cy.get('h3').should('contain', 'Hello Cypress')
  })
})
