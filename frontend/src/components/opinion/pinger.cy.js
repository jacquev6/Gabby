import { setActivePinia, createPinia } from 'pinia'

import { defineApiStore } from '../../stores/api'
import { i18n } from '../../locales/for-tests'
import Pinger from './pinger.vue'


const useApiStore = defineApiStore('api', {baseUrl: 'http://fanout:8080/api/'})

// @todo Access the https://test-utils.vuejs.org/api/#config wrapped by Cypress, to avoid repeating '{global}' on each 'mount'
const global = {
  plugins: [i18n],
}

describe('Pinger', () => {
  beforeEach(() => {
    cy.request('POST', 'http://fanout:8080/reset-for-tests/yes-im-sure')

    setActivePinia(createPinia())
    useApiStore()
  })

  it('says "No pings"', () => {
    cy.mount(Pinger, {global})

    cy.get('li').should('have.length', 0)
    cy.get('p').contains('No pings.').should('exist')
  })

  it('says "Pas de pings"', () => {
    cy.mount(Pinger, {global})

    cy.wrap(i18n).then(p => p.global.locale.value = 'fr')
    cy.get('li').should('have.length', 0)
    cy.get('p').contains('Pas de pings.').should('exist')

    cy.wrap(i18n).then(p => p.global.locale.value = 'en')
  })

  it('pings', () => {
    cy.mount(Pinger, {global})

    cy.get('button').contains('Ping').click()

    cy.get('li').should('have.length', 1)

    cy.get('button').contains('Ping').click()
    cy.get('button').contains('Ping').click()
    cy.get('button').contains('Ping').click()
    cy.get('button').contains('Ping').click()

    cy.get('li').should('have.length', 5)
  })

  // @todo Implement
  // it('detects failure to ping', () => {
  //   setActivePinia(createPinia())
  //   defineApiStore('api', {baseUrl: 'http://fanout:8080/not-the-api/'})()

  //   cy.mount(Pinger)

  //   cy.get('button').contains('Ping').click()
  // })
})
