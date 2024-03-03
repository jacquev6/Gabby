import { ref, reactive } from 'vue'

import { BSelect } from '.'


describe('BSelect', () => {
  beforeEach(() => {
    cy.viewport(250, 150)
  })

  it('renders properly', () => {
    cy.mount(
      BSelect, 
      {
        props:{
          options: [
            {value: 'en', label: '🇺🇸 English'},
            {value: 'fr', label: '🇫🇷 Français'},
            {value: 'jp', label: '🇯🇵 日本語'},
          ],
        },
      },
    )

    cy.get('select').select('jp')
    cy.get('select').should('have.value', 'jp')
    cy.get('select').screenshot('jp')
  })

  it('reacts to options', () => {
    cy.mount(BSelect, {props: {options: [
      {value: 1, label: 'One'},
      {value: 2, label: 'Two'},
    ]}})

    cy.get('option').should('have.length', 2)

    cy.vue().then((w) => w.setProps({options: [
      {value: 1, label: 'One'},
      {value: 2, label: 'Two'},
      {value: 3, label: 'Three'},
    ]}))

    cy.get('option').should('have.length', 3)
  })

  it('supports string options', () => {
    cy.mount(BSelect, {props: {options: ['One', 'Two']}})

    cy.get('option').should('have.length', 2)
    cy.get('option').eq(0).should('have.value', 'One')
    cy.get('option').eq(1).should('have.value', 'Two')
  })

  it('reacts to its model', () => {
    cy.mount(BSelect, {props: {modelValue: 'Two', options: ['One', 'Two', 'Three']}})

    cy.get('select').should('have.value', 'Two')

    cy.vue().then((w) => w.setProps({modelValue: 'Three'}))
    cy.get('select').should('have.value', 'Three')
  })

  it('sends model updates', () => {
    cy.mount(BSelect, {props: {options: ['One', 'Two', 'Three']}})

    cy.get('select').select('Three')
    cy.get('select').should('have.value', 'Three')
    cy.vue().then((w) => w.emitted('update:modelValue')[0]).should('deep.eq', ['Three'])

    cy.get('select').select('Two')
    cy.get('select').should('have.value', 'Two')
    cy.vue().then((w) => w.emitted('update:modelValue')[1]).should('deep.eq', ['Two'])
  })
})
