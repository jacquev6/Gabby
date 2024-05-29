import MultipleChoicesInput from './MultipleChoicesInput.vue'


describe('MultipleChoicesInput', () => {
  before(console.clear)

  it('works', () => {
    let value = undefined

    cy.mount(MultipleChoicesInput, {props: {
      choices: ['alpha', 'beta'],
      modelValue: value,
      'onUpdate:modelValue': (v) => {
        value = v
        Cypress.vueWrapper.setProps({ modelValue: v })
      }
    }})

    cy.get('span.main:contains("....")').should('exist')
    cy.get('span.choice').should('not.exist')

    cy.get('span.main').click()

    cy.get('span.main:contains("....")').should('exist')
    cy.get('span.choice:contains("alpha")').should('exist')
    cy.get('span.choice:contains("beta")').should('exist')
    cy.get('span.choice:contains("....")').should('exist')

    cy.get('div.backdrop').click()

    cy.get('span.main:contains("....")').should('exist')
    cy.get('span.choice').should('not.exist')

    cy.get('span.main').click()

    cy.get('span.main:contains("....")').should('exist')
    cy.get('span.choice:contains("alpha")').should('exist')
    cy.get('span.choice:contains("beta")').should('exist')
    cy.get('span.choice:contains("....")').should('exist')

    cy.get('span.choice:contains("alpha")').click().then(() => {
      cy.expect(value).to.equal("alpha")
    })

    cy.get('span.main:contains("....")').should('not.exist')
    cy.get('span.main:contains("alpha")').should('exist')
    cy.get('span.choice').should('not.exist')

    cy.get('span.main').click()

    cy.get('span.main:contains("....")').should('not.exist')
    cy.get('span.main:contains("alpha")').should('exist')
    cy.get('span.choice:contains("alpha")').should('exist')
    cy.get('span.choice:contains("beta")').should('exist')
    cy.get('span.choice:contains("....")').should('exist')

    cy.get('span.choice:contains("beta")').click().then(() => {
      cy.expect(value).to.equal("beta")
    })

    cy.get('span.main:contains("alpha")').should('not.exist')
    cy.get('span.main:contains("beta")').should('exist')
    cy.get('span.choice').should('not.exist')
  })
})
