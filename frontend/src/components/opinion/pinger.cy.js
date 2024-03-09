import { setActivePinia, createPinia } from 'pinia'

import { defineApiStore } from '../../stores/api'
import Pinger from './pinger.vue'


const useApiStore = defineApiStore('api', {baseUrl: 'http://fanout:8080/api/'})

describe('Pinger', () => {
  before(console.clear)

  beforeEach(() => {
    cy.request('POST', 'http://fanout:8080/reset-for-tests/yes-im-sure')

    cy.viewport(700, 400)

    setActivePinia(createPinia())
    useApiStore()
  })

  it('says "No pings"', () => {
    cy.mount(Pinger)

    cy.get('li').should('have.length', 0)
    cy.get('p').contains('No pings.').should('exist')
  })

  it('pings', () => {
    cy.mount(Pinger)

    cy.get('button').contains('Ping (in English)').click()

    cy.get('li').should('have.length', 1)

    cy.get('button').contains('Ping').click()
    cy.get('button').contains('Ping').click()
    cy.get('button').contains('Ping').click()
    cy.get('button').contains('Ping').click()

    cy.get('li').should('have.length', 5)
  })

  it('pings with a message', () => {
    cy.mount(Pinger)

    cy.get('label').contains('Message').next().type('Hello, World!')
    cy.get('button').contains('Ping').click()

    cy.get('li').contains('Hello, World!').should('have.length', 1)
  })

  it('pings with a re-blanked message', () => {
    cy.mount(Pinger)

    cy.get('label').contains('Message').next().type('Message').blur()
    cy.get('label').contains('Message').next().type('{selectall}{backspace}')
    cy.get('button').contains('Ping').click()

    cy.get('li').should('have.length', 1)
  })

  it('sets and reset ping message', () => {
    cy.mount(Pinger)

    cy.get('button').contains('Ping').click()
    cy.get('button').contains('Ping').click()
    cy.get('button').contains('Ping').click()

    cy.get('li').should('have.length', 3)

    cy.get('ul > :nth-child(2) button').contains('Set message').click()

    cy.get('li').should('have.length', 3)
    cy.get('li').contains('Hello!').should('have.length', 1)

    cy.get('ul > :nth-child(2) button').contains('Reset message').click()

    cy.get('li').should('have.length', 3)
    cy.get('li').contains('Hello!').should('not.exist')
  })

  it('deletes a ping', () => {
    cy.mount(Pinger)

    cy.get('button').contains('Ping').click()
    cy.get('button').contains('Ping').click()
    cy.get('button').contains('Ping').click()

    cy.get('li').should('have.length', 3)

    cy.get('ul > :nth-child(2) button').contains('Delete').click()

    cy.get('li').should('have.length', 2)

    cy.focused().should('not.exist')  // This requires the ':key' on the '<li>' to be set
  })

  // it('detects failure to ping on no connection', () => {
  //   setActivePinia(createPinia())
  //   defineApiStore('api', {baseUrl: 'http://fanout:8181/not-the-api/'})()

  //   cy.mount(Pinger)
  // })

  // it('detects failure to ping on 404', () => {
  //   setActivePinia(createPinia())
  //   defineApiStore('api', {baseUrl: 'http://fanout:8080/not-the-api/'})()

  //   cy.mount(Pinger)

  //   // cy.get('button').contains('Ping').click()
  // })
})
