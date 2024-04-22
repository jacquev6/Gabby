import FillWithFreeText from "./FillWithFreeText.vue"


const wording = 'This is a ... exercise, with ... placeholders.'

describe('FillWithFreeText', () => {
  before(console.clear)

  it('renders fillable text', () => {
    cy.mount(FillWithFreeText, {props: {exercise: {wording, adaptation: {placeholder: '...'}}}})

    cy.get('input').should('have.length', 2)
  })
})
