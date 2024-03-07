import { setActivePinia, createPinia } from 'pinia'

import { defineApiStore } from '../api.js'
import ApiTestComponent from './ApiTestComponent.vue'  // @todo(Project management, later) Define this component locally


const useApiStore = defineApiStore('api', {baseUrl: 'http://fanout:8081/api/'})

describe('ApiStore', () => {
  beforeEach(() => {
    setActivePinia(createPinia())
    cy.request('POST', 'http://fanout:8081/reset-for-tests/yes-im-sure?fixtures=test-exercises')
  })

  it('gets all textbooks and sections', async () => {
    const api = useApiStore()

    expect(api.cache.get('textbook', '1')).to.equal(null)

    const textbooks = await api.client.get_all('textbooks')
    expect(textbooks.length).to.equal(1)
    expect(textbooks[0].attributes.title).to.equal('Français CE2')

    expect(api.cache.get('textbook', '0')).to.equal(null)
    expect(api.cache.get('textbook', '1').attributes.title).to.equal('Français CE2')
    expect(api.cache.get('textbook', '1').relationships.sections[0]).to.be.null

    await api.client.get_all('sections')

    expect(
      api.cache.get('textbook', '1').relationships.
        sections[0].attributes.textbookStartPage
    ).to.equal(6)
  })

  it('gets one textbook and its sections', async () => {
    const api = useApiStore()

    expect(api.cache.get('textbook', '1')).to.equal(null)

    const textbook = await api.client.get_one('textbook', '1', {include: 'sections'})
    expect(textbook.attributes.title).to.equal('Français CE2')

    expect(api.cache.get('textbook', '1').attributes.title).to.equal('Français CE2')
    expect(api.cache.get('textbook', '1').relationships.sections[0].attributes.textbookStartPage).to.equal(6)
  })

  it('keeps single included', async () => {
    const api = useApiStore()

    await api.client.get_all('textbooks', {include: 'sections'})

    expect(
      api.cache.get('textbook', '1').relationships.
        sections[0].attributes.textbookStartPage
    ).to.equal(6)
  })

  it('keeps deep included', async () => {
    const api = useApiStore()

    await api.client.get_all('textbooks', {include: 'sections.pdfFile.namings'})

    expect(
      api.cache.get('textbook', '1')
        .relationships.sections[0]
        .relationships.pdfFile
        .relationships.namings[0]
        .attributes.name
    ).to.equal('test.pdf')
  })

  it('keeps multiple included', async () => {
    const api = useApiStore()

    await api.client.get_all('sections', {include: ['textbook', 'pdfFile.namings']})

    expect(
      api.cache.get('section', '1')
        .relationships.textbook
        .attributes.title
    ).to.equal('Français CE2')
    expect(
      api.cache.get('section', '1')
        .relationships.pdfFile
        .relationships.namings[0]
        .attributes.name
    ).to.equal('test.pdf')
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

  it('paginates exercises', async () => {
    const api = useApiStore()

    const exercises = await api.client.get_all('exercises')

    expect(exercises.length).to.equal(3)
  })

  it('filters exercises by textbook and page', async () => {
    const api = useApiStore()

    expect((await api.client.get_all('exercises', {filter: {textbook: '1'}})).length).to.equal(3)
    expect((await api.client.get_all('exercises', {filter: {textbook: '1', page: 6}})).length).to.equal(2)
    expect((await api.client.get_all('exercises', {filter: {textbook: '1', page: 7}})).length).to.equal(1)
  })

  it('creates a new exercise', async () => {
    const api = useApiStore()

    expect((await api.client.get_all('exercises', {filter: {textbook: '1', page: 6}})).length).to.equal(2)

    expect(api.cache.get('textbook', '1')).to.be.null

    const newExercise = await api.client.post(
      'exercise',
      {
        page: 6,
        number: 14,
        instructions: 'Do this',
      },
      {
        textbook: {type: 'textbook', id: '1'},
        extractionEvents: [],
      },
    )

    expect(newExercise.id).to.equal('4')
    expect(newExercise.attributes.instructions).to.equal('Do this')

    expect(api.cache.get('textbook', '1')).to.be.null
  })

  it('creates a new exercise and retrieves its textbook', async () => {
    const api = useApiStore()

    expect((await api.client.get_all('exercises', {filter: {textbook: '1', page: 6}})).length).to.equal(2)

    expect(api.cache.get('textbook', '1')).to.be.null

    const newExercise = await api.client.post(
      'exercise',
      {
        page: 6,
        number: 14,
        instructions: 'Do that',
      },
      {
        textbook: {type: 'textbook', id: '1'},
        extractionEvents: [],
      },
      {
        include: 'textbook'
      },
    )

    expect(newExercise.id).to.equal('4')
    expect(newExercise.attributes.instructions).to.equal('Do that')

    expect(api.cache.get('textbook', '1').attributes.title).to.equal('Français CE2')
  })

  it('updates an exercise', async () => {
    const api = useApiStore()

    const updatedExercise = await api.client.patch('exercise', '1', {instructions: 'Do that'}, {})

    expect(updatedExercise.attributes.instructions).to.equal('Do that')
    expect(api.cache.get('exercise', '1').attributes.instructions).to.equal('Do that')
  })

  it('updates an exercise and retrieves its textbook', async () => {
    const api = useApiStore()

    expect(api.cache.get('textbook', '1')).to.be.null

    const updatedExercise = await api.client.patch(
      'exercise',
      '1',
      {instructions: 'Do that'},
      {},
      {include: 'textbook'},
    )

    expect(updatedExercise.attributes.instructions).to.equal('Do that')
    expect(api.cache.get('exercise', '1').attributes.instructions).to.equal('Do that')

    expect(api.cache.get('textbook', '1').attributes.title).to.equal('Français CE2')
  })

  it('deletes an exercise', async () => {
    const api = useApiStore()

    expect(api.cache.get('exercise', '1')).to.be.null

    await api.client.delete('exercise', '1')

    expect(api.cache.get('exercise', '1')).to.be.null
    expect((await api.client.get_all('exercises', {filter: {textbook: '1', page: 6}})).length).to.equal(1)
  })

  it('deletes an exercise and updates the cache', async () => {
    const api = useApiStore()

    expect((await api.client.get_all('exercises', {filter: {textbook: '1', page: 6}})).length).to.equal(2)
    expect(api.cache.get('exercise', '1').attributes.number).to.equal(3)

    await api.client.delete('exercise', '1')

    expect(api.cache.get('exercise', '1')).to.be.null
    expect((await api.client.get_all('exercises', {filter: {textbook: '1', page: 6}})).length).to.equal(1)
  })
})
