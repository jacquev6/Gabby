import MultipleChoicesInput from './MultipleChoicesInput.vue'


describe('MultipleChoicesInput', () => {
  before(console.clear)

  it('closes without value when clicking the backdrop', () => {
    let value: string | undefined = undefined

    cy.mount(MultipleChoicesInput, {props: {
      showArrowBefore: false,
      choices: ['alpha', 'beta'],
      placeholder: '....',
      showChoicesByDefault: false,
      modelValue: value,
      'onUpdate:modelValue': (v: string | undefined) => {
        value = v
        Cypress.vueWrapper.setProps({ modelValue: v })
      }
    }})

    cy.get('div.backdrop').should('not.exist')
    cy.get('span.main').should('have.text', '....').click()
    cy.get('div.backdrop').should('exist').click()
    cy.get('span.main').should('have.text', '....')
    cy.wait(0).then(() => expect(value).to.be.undefined)
  })

  it('closes with a value when clicking a value', () => {
    let value: string | undefined = undefined

    cy.mount(MultipleChoicesInput, {props: {
      showArrowBefore: false,
      choices: ['alpha', 'beta'],
      placeholder: '....',
      showChoicesByDefault: false,
      modelValue: value,
      'onUpdate:modelValue': (v: string | undefined) => {
        value = v
        Cypress.vueWrapper.setProps({ modelValue: v })
      }
    }})

    cy.get('span.choice0').should('not.exist')
    cy.get('span.main').should('have.text', '....').click()
    cy.get('span.choice0').should('exist').click()
    cy.get('span.main').should('have.text', 'alpha')
    cy.wait(0).then(() => expect(value).to.equal('alpha'))
  })

  it('closes without value when clicking the main span', () => {
    let value: string | undefined = undefined

    cy.mount(MultipleChoicesInput, {props: {
      showArrowBefore: false,
      choices: ['alpha', 'beta'],
      placeholder: '....',
      showChoicesByDefault: true,
      modelValue: value,
      'onUpdate:modelValue': (v: string | undefined) => {
        value = v
        Cypress.vueWrapper.setProps({ modelValue: v })
      }
    }})

    cy.get('div.backdrop').should('not.exist')
    cy.get('span.choice0').should('exist')
    cy.get('span.main').click()
    cy.get('span.main').should('have.text', '....')
    cy.get('span.choice0').should('not.exist')
    cy.wait(0).then(() => expect(value).to.be.undefined)
  })

  it('shows up again with a backdrop after selecting a value', () => {
    let value: string | undefined = undefined

    cy.mount(MultipleChoicesInput, {props: {
      showArrowBefore: false,
      choices: ['alpha', 'beta'],
      placeholder: '....',
      showChoicesByDefault: false,
      modelValue: value,
      'onUpdate:modelValue': (v: string | undefined) => {
        value = v
        Cypress.vueWrapper.setProps({ modelValue: v })
      }
    }})

    cy.get('span.main').should('have.text', '....').click()
    cy.get('span.choice0').should('exist').click().should('not.exist')
    cy.get('span.main').should('have.text', 'alpha').click()
    cy.get('div.backdrop').should('exist')
    cy.get('span.choice0').should('exist')
    cy.get('span.choice1').should('exist').click().should('not.exist')
    cy.get('span.main').should('have.text', 'beta')
  })

  it('shows up again without backdrop after selecting a value', () => {
    let value: string | undefined = undefined

    cy.mount(MultipleChoicesInput, {props: {
      showArrowBefore: false,
      choices: ['alpha', 'beta'],
      placeholder: '....',
      showChoicesByDefault: true,
      modelValue: value,
      'onUpdate:modelValue': (v: string | undefined) => {
        value = v
        Cypress.vueWrapper.setProps({ modelValue: v })
      }
    }})

    cy.get('span.choice0').click().should('not.exist')
    cy.get('span.main').should('have.text', 'alpha').click()
    cy.get('div.backdrop').should('not.exist')
    cy.get('span.choice0').should('exist')
    cy.get('span.choice1').should('exist').click().should('not.exist')
    cy.get('span.main').should('have.text', 'beta')
  })
})
