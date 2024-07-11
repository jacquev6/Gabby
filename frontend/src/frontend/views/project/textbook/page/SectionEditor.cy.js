import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'

import { defineApiStore, resetApiStores } from '$frontend/stores/api'
import SectionEditor from './SectionEditor.vue'


const useApiStore = defineApiStore('api', {baseUrl: 'http://fanout:8080/api'})

describe('SectionEditor', () => {
  beforeEach(() => {
    cy.request('POST', 'http://fanout:8080/reset-for-tests/yes-im-sure?fixtures=test-exercises')

    resetApiStores()
    cy.wrap(useApiStore()).then((api) => api.auth.login('admin', 'password'))
    cy.wrap(useApiStore()).then((api) => api.client.getAll('section')).its('items').should('have.length', 1)

    cy.viewport(1000, 500)

    cy.mount(SectionEditor).as('editor')
    cy.get('@editor').then(({component}) => component.show('eyjahd'))
    cy.get('@editor').its('component.active').should('be.true')
  })

  afterEach(() => {
    cy.get('@editor').then(({component}) => component.hide())
    cy.get('@editor').its('component.active').should('be.false')
  })

  it('reacts to changes', () => {
    cy.get('label').contains('Début dans le PDF').next().type('{selectAll}4')
    cy.get('label').contains('Début dans le manuel').next().type('{selectAll}14')
    cy.get('label').contains('Fin dans le PDF').next().type('{selectAll}7')

    cy.get('p').should('contain', 'Les pages 4 à 7 du PDF')
    cy.get('p').should('contain', 'correspondent aux pages 14 à 17 du manuel.')
  })

  it('disables "Save" button on invalid inputs', () => {
    for (const label of ['Début dans le PDF', 'Fin dans le PDF', 'Début dans le manuel']) {
      cy.get('label').contains(label).next().type('{selectAll}{backspace}')
      cy.get('button').contains('Enregistrer').should('be.disabled')
      cy.get('label').contains(label).next().type('{selectAll}-15')
      cy.get('button').contains('Enregistrer').should('be.disabled')
      cy.get('label').contains(label).next().type('{selectAll}0')
      cy.get('button').contains('Enregistrer').should('be.disabled')
      cy.get('label').contains(label).next().type('{selectAll}1')
      cy.get('button').contains('Enregistrer').should('be.enabled')
    }
  })

  it('disables "Save" button on invalid order', () => {
    cy.get('label').contains('Début dans le PDF').next().type('{selectAll}5')
    cy.get('button').contains('Enregistrer').should('be.disabled')
  })

  it('keeps pages counts in sync', () => {
    cy.get('label').contains('Fin dans le PDF').next().type('{selectAll}4')
    cy.get('label').contains('Fin dans le manuel').next().should('have.value', 9)

    cy.get('label').contains('Début dans le PDF').next().type('{selectAll}3')
    cy.get('label').contains('Fin dans le manuel').next().should('have.value', 7)

    cy.get('label').contains('Début dans le manuel').next().type('{selectAll}13')
    cy.get('label').contains('Fin dans le manuel').next().should('have.value', 14)
  })

  it('saves', () => {
    cy.get('label').contains('Début dans le PDF').next().type('{selectAll}10')
    cy.get('label').contains('Fin dans le PDF').next().type('{selectAll}15')
    cy.get('label').contains('Début dans le manuel').next().type('{selectAll}20')

    cy.wrap(useApiStore()).then((api) => api.client.getOne('section', 'eyjahd')).as('section')
    cy.get('@section').its('attributes.pdfFileStartPage').should('eq', 1)
    cy.get('@section').its('attributes.textbookStartPage').should('eq', 6)
    cy.get('@section').its('attributes.pagesCount').should('eq', 2)

    cy.get('button').contains('Enregistrer').click()
    cy.get('@editor').its('component.active').should('be.false')

    cy.wrap(useApiStore()).then((api) => api.client.getOne('section', 'eyjahd')).as('section')
    cy.get('@section').its('attributes.pdfFileStartPage').should('eq', 10)
    cy.get('@section').its('attributes.textbookStartPage').should('eq', 20)
    cy.get('@section').its('attributes.pagesCount').should('eq', 6)
  })

  it('cancels', () => {
    cy.get('label').contains('Début dans le PDF').next().type('{selectAll}10')
    cy.get('label').contains('Fin dans le PDF').next().type('{selectAll}15')
    cy.get('label').contains('Début dans le manuel').next().type('{selectAll}20')

    cy.wrap(useApiStore()).then((api) => api.client.getOne('section', 'eyjahd')).as('section')
    cy.get('@section').its('attributes.pdfFileStartPage').should('eq', 1)
    cy.get('@section').its('attributes.textbookStartPage').should('eq', 6)
    cy.get('@section').its('attributes.pagesCount').should('eq', 2)

    cy.get('button').contains('Annuler').click()
    cy.get('@editor').its('component.active').should('be.false')

    cy.wrap(useApiStore()).then((api) => api.client.getOne('section', 'eyjahd')).as('section')
    cy.get('@section').its('attributes.pdfFileStartPage').should('eq', 1)
    cy.get('@section').its('attributes.textbookStartPage').should('eq', 6)
    cy.get('@section').its('attributes.pagesCount').should('eq', 2)
  })
})
