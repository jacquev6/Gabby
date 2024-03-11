import { setActivePinia, createPinia } from 'pinia'

import { defineApiStore } from './api.js'


const useApiStore = defineApiStore('api', {baseUrl: 'http://fanout:8080/api/'})

describe('ApiStore', () => {
  before(console.clear)

  beforeEach(() => {
    setActivePinia(createPinia())
    cy.request('POST', 'http://fanout:8080/reset-for-tests/yes-im-sure?fixtures=test-exercises')
  })

  it('gets all textbooks and sections', async () => {
    const api = useApiStore()

    expect(api.cache.getOne('textbook', '1').inCache).to.be.false

    const textbooks = await api.client.getAll('textbooks')
    expect(textbooks.length).to.equal(1)
    expect(textbooks[0].attributes.title).to.equal('Français CE2')

    expect(api.cache.getOne('textbook', '0').inCache).to.be.false
    expect(api.cache.getOne('textbook', '1').attributes.title).to.equal('Français CE2')
    expect(api.cache.getOne('textbook', '1').relationships.sections[0].inCache).to.be.false

    await api.client.getAll('sections')

    expect(
      api.cache.getOne('textbook', '1').relationships.
        sections[0].attributes.textbookStartPage
    ).to.equal(6)
  })

  it('gets one textbook and its sections', async () => {
    const api = useApiStore()

    expect(api.cache.getOne('textbook', '1').inCache).to.be.false

    const textbook = await api.client.getOne('textbook', '1', {include: 'sections'})
    expect(textbook.attributes.title).to.equal('Français CE2')

    expect(api.cache.getOne('textbook', '1').attributes.title).to.equal('Français CE2')
    expect(api.cache.getOne('textbook', '1').relationships.sections[0].attributes.textbookStartPage).to.equal(6)
  })

  it('keeps single included', async () => {
    const api = useApiStore()

    await api.client.getAll('textbooks', {include: 'sections'})

    expect(
      api.cache.getOne('textbook', '1').relationships.
        sections[0].attributes.textbookStartPage
    ).to.equal(6)
  })

  it('keeps deep included', async () => {
    const api = useApiStore()

    await api.client.getAll('textbooks', {include: 'sections.pdfFile.namings'})

    expect(
      api.cache.getOne('textbook', '1')
        .relationships.sections[0]
        .relationships.pdfFile
        .relationships.namings[0]
        .attributes.name
    ).to.equal('test.pdf')
  })

  it('keeps multiple included', async () => {
    const api = useApiStore()

    await api.client.getAll('sections', {include: ['textbook', 'pdfFile.namings']})

    expect(
      api.cache.getOne('section', '1')
        .relationships.textbook
        .attributes.title
    ).to.equal('Français CE2')
    expect(
      api.cache.getOne('section', '1')
        .relationships.pdfFile
        .relationships.namings[0]
        .attributes.name
    ).to.equal('test.pdf')
  })

  it('paginates exercises', async () => {
    const api = useApiStore()

    const exercises = await api.client.getAll('exercises')

    expect(exercises.length).to.equal(6)
  })

  it('filters exercises by textbook and page', async () => {
    const api = useApiStore()

    expect((await api.client.getAll('exercises', {filter: {'textbookExercise.textbook': '1'}})).length).to.equal(3)
    expect((await api.client.getAll('exercises', {filter: {'textbookExercise.textbook': '1', 'textbookExercise.page': 6}})).length).to.equal(2)
    expect((await api.client.getAll('exercises', {filter: {'textbookExercise.textbook': '1', 'textbookExercise.page': 7}})).length).to.equal(1)
  })

  it('creates a new exercise', async () => {
    const api = useApiStore()

    expect((await api.client.getAll('exercises', {filter: {'textbookExercise.textbook': '1', 'textbookExercise.page': 6}})).length).to.equal(2)

    expect(api.cache.getOne('textbook', '1').inCache).to.be.false

    const textbookExercise = await api.client.post(
      'textbookExercise',
      {page: 6, number: 14},
      {textbook: {type: 'textbook', id: '1'}},
    )

    const newExercise = await api.client.post(
      'exercise',
      {
        instructions: 'Do this',
      },
      {
        project: {type: 'project', id: '1'},
        textbookExercise: {type: 'textbookExercise', id: textbookExercise.id},
        extractionEvents: [],
      },
    )

    expect(newExercise.id).to.equal('7')
    expect(newExercise.attributes.instructions).to.equal('Do this')

    expect(api.cache.getOne('textbook', '1').inCache).to.be.false
  })

  it('creates a new exercise and retrieves its textbook', async () => {
    const api = useApiStore()

    expect((await api.client.getAll('exercises', {filter: {'textbookExercise.textbook': '1', 'textbookExercise.page': 6}})).length).to.equal(2)

    expect(api.cache.getOne('textbook', '1').inCache).to.be.false

    const textbookExercise = await api.client.post(
      'textbookExercise',
      {page: 6, number: 14},
      {textbook: {type: 'textbook', id: '1'}},
    )

    const newExercise = await api.client.post(
      'exercise',
      {
        instructions: 'Do that',
      },
      {
        project: {type: 'project', id: '1'},
        textbookExercise: {type: 'textbookExercise', id: textbookExercise.id},
        extractionEvents: [],
      },
      {
        include: 'textbookExercise.textbook'
      },
    )

    expect(newExercise.id).to.equal('7')
    expect(newExercise.attributes.instructions).to.equal('Do that')

    expect(api.cache.getOne('textbook', '1').attributes.title).to.equal('Français CE2')
  })

  it('updates an exercise', async () => {
    const api = useApiStore()

    const updatedExercise = await api.client.patch('exercise', '1', {instructions: 'Do that'}, {})

    expect(updatedExercise.attributes.instructions).to.equal('Do that')
    expect(api.cache.getOne('exercise', '1').attributes.instructions).to.equal('Do that')
  })

  it('updates an exercise and retrieves its textbook', async () => {
    const api = useApiStore()

    expect(api.cache.getOne('textbook', '1').inCache).to.be.false

    const updatedExercise = await api.client.patch(
      'exercise',
      '1',
      {instructions: 'Do that'},
      {},
      {include: 'textbookExercise.textbook'},
    )

    expect(updatedExercise.attributes.instructions).to.equal('Do that')
    expect(api.cache.getOne('exercise', '1').attributes.instructions).to.equal('Do that')

    expect(api.cache.getOne('textbook', '1').attributes.title).to.equal('Français CE2')
  })

  it('deletes an exercise', async () => {
    const api = useApiStore()

    expect(api.cache.getOne('exercise', '1').inCache).to.be.false

    await api.client.delete('exercise', '1')

    expect(api.cache.getOne('exercise', '1').inCache).to.be.true
    expect(api.cache.getOne('exercise', '1').exists).to.be.false
    expect((await api.client.getAll('exercises', {filter: {'textbookExercise.textbook': '1', 'textbookExercise.page': 6}})).length).to.equal(1)
  })
})
