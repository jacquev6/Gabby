import { setActivePinia, createPinia } from 'pinia'

import { defineApiStore } from '../api.js'
import ApiTestComponent from './ApiTestComponent.vue'  // @todo(Project management, later) Define this component locally


const useApiStore = defineApiStore('api', {baseUrl: 'http://fanout:8081/api/'})

describe('ApiStore', () => {
  beforeEach(() => {
    setActivePinia(createPinia())
  })

  it('fetches textbooks and sections', async () => {
    const api = useApiStore()

    expect(api.cache.get('textbook', '1')).to.equal(null)

    const textbooks = await api.client.get('textbooks')
    expect(textbooks.length).to.equal(1)
    expect(textbooks[0].attributes.title).to.equal('Français CE2')

    expect(api.cache.get('textbook', '0')).to.equal(null)
    expect(api.cache.get('textbook', '1').attributes.title).to.equal('Français CE2')
    expect(api.cache.get('textbook', '1').relationships.sections[0]).to.be.null

    await api.client.get('sections')

    expect(
      api.cache.get('textbook', '1').relationships.
        sections[0].attributes.textbookStartPage
    ).to.equal(6)
  })

  it('updates a component reactively', () => {
    cy.mount(ApiTestComponent)

    cy.get('p').should('contain', 'Textbook title: []')
    cy.get('p').should('contain', 'Section start page: []')
    cy.get('p').should('contain', 'Textbook section start page: []')

    cy.get('button').contains('Fetch textbooks').click()

    cy.get('p').should('contain', 'Textbook title: [Français CE2]')
    cy.get('p').should('contain', 'Section start page: []')
    cy.get('p').should('contain', 'Textbook section start page: []')

    cy.get('button').contains('Fetch sections').click()

    cy.get('p').should('contain', 'Textbook title: [Français CE2]')
    cy.get('p').should('contain', 'Section start page: [6]')
    cy.get('p').should('contain', 'Textbook section start page: [6]')
  })
})
