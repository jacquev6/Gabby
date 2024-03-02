import { setActivePinia, createPinia } from 'pinia'

import { defineApiStore } from '../../stores/api'
import Pinger from './pinger.vue'


const useApiStore = defineApiStore('api', {baseUrl: 'http://fanout:8080/api/'})

describe('Pinger', () => {
  beforeEach(() => {
    cy.request('POST', 'http://fanout:8080/reset-for-tests/yes-im-sure')

    setActivePinia(createPinia())
    useApiStore()
  })

  it('pings', () => {
    cy.mount(Pinger)

    cy.get('li').should('have.length', 0)

    cy.get('button').contains('Ping').click()

    cy.get('li').should('have.length', 1)

    cy.get('button').contains('Ping').click()
    cy.get('button').contains('Ping').click()
    cy.get('button').contains('Ping').click()
    cy.get('button').contains('Ping').click()

    cy.get('li').should('have.length', 5)
  })

  // it('detects failure to ping', () => {
  //   setActivePinia(createPinia())
  //   defineApiStore('api', {baseUrl: 'http://fanout:8080/not-the-api/'})()

  //   cy.mount(Pinger)

  //   cy.get('button').contains('Ping').click()
  // })
})
