import { setActivePinia, createPinia } from 'pinia'

import { defineApiStore } from './api'


const useApiStore = defineApiStore('api', {baseUrl: 'http://fanout:8080/api/'})

describe('ApiStore', () => {
  before(console.clear)

  beforeEach(() => {
    setActivePinia(createPinia())
    cy.request('POST', 'http://fanout:8080/reset-for-tests/yes-im-sure?fixtures=test-exercises')
  })

  after(() => {
    cy.request('POST', 'http://fanout:8080/reset-for-tests/yes-im-sure?fixtures=test-exercises,more-test-exercises')
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

    expect((await api.client.getAll('exercises')).length).to.equal(6)
    expect((await api.client.getAll('exercises', {filter: {textbook: '1'}})).length).to.equal(3)
    expect((await api.client.getAll('exercises', {filter: {textbook: '1', textbookPage: 6}})).length).to.equal(2)
    expect((await api.client.getAll('exercises', {filter: {textbook: '1', textbookPage: 7}})).length).to.equal(1)
  })

  it('creates a new exercise', async () => {
    const api = useApiStore()

    expect((await api.client.getAll('exercises', {filter: {textbook: '1', textbookPage: 6}})).length).to.equal(2)

    expect(api.cache.getOne('textbook', '1').inCache).to.be.false

    const newExercise = await api.client.post(
      'exercise',
      {
        textbookPage: 6, number: '14',
        instructions: 'Do this',
        boundingRectangle: {start: {x: 0, y: 1}, stop: {x: 2, y: 3}},
      },
      {
        project: {type: 'project', id: '1'},
        textbook: {type: 'textbook', id: '1'},
      },
    )

    expect(newExercise.id).to.equal('7')
    expect(newExercise.attributes.instructions).to.equal('Do this')
    expect(newExercise.attributes.boundingRectangle).to.deep.equal({start: {x: 0, y: 1}, stop: {x: 2, y: 3}})

    expect(api.cache.getOne('textbook', '1').inCache).to.be.false

    expect((await api.client.getAll('exercises', {filter: {textbook: '1', textbookPage: 6}})).length).to.equal(3)
  })

  it('creates a new exercise and retrieves its textbook', async () => {
    const api = useApiStore()

    expect((await api.client.getAll('exercises', {filter: {textbook: '1', textbookPage: 6}})).length).to.equal(2)

    expect(api.cache.getOne('textbook', '1').inCache).to.be.false

    const newExercise = await api.client.post(
      'exercise',
      {
        textbookPage: 6, number: '14',
        instructions: 'Do that',
      },
      {
        project: {type: 'project', id: '1'},
        textbook: {type: 'textbook', id: '1'},
      },
      {
        include: 'textbook'
      },
    )

    expect(newExercise.id).to.equal('7')
    expect(newExercise.attributes.instructions).to.equal('Do that')

    expect(api.cache.getOne('textbook', '1').attributes.title).to.equal('Français CE2')

    expect((await api.client.getAll('exercises', {filter: {textbook: '1', textbookPage: 6}})).length).to.equal(3)
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
      {include: 'textbook'},
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
    expect((await api.client.getAll('exercises', {filter: {textbook: '1', textbookPage: 6}})).length).to.equal(1)
  })
})

describe('ApiStore', () => {
  before(console.clear)

  beforeEach(() => {
    setActivePinia(createPinia())
    cy.request('POST', 'http://fanout:8080/reset-for-tests/yes-im-sure?fixtures=test-exercises,more-test-exercises')
  })

  after(() => {
    cy.request('POST', 'http://fanout:8080/reset-for-tests/yes-im-sure?fixtures=test-exercises,more-test-exercises')
  })

  it('gets an exercise without an adaptation', async () => {
    const api = useApiStore()

    const exercise = await api.client.getOne('exercise', '2', {include: 'adaptation'})

    expect(exercise.attributes.instructions).to.equal('Écris une phrase en respectant l\'ordre des classes grammaticales indiquées.')
    expect(exercise.relationships.adaptation).to.be.null
  })

  it('gets an exercise with "select things" adaptation', async () => {
    const api = useApiStore()

    const exercise = await api.client.getOne('exercise', '7', {include: 'adaptation'})

    expect(exercise.attributes.instructions).to.equal('Relève dans le texte trois\n{sel1:déterminants}, un {sel2:nom propre}, quatre\n{sel3:noms communs} et trois {sel4:verbes}.')
    expect(exercise.relationships.adaptation.type).to.equal('selectThingsAdaptation')
    expect(exercise.relationships.adaptation.id).to.equal('2')
    expect(exercise.relationships.adaptation.attributes.colors).to.equal(4)
  })

  it('gets an exercise with "fill with free text" adaptation', async () => {
    const api = useApiStore()

    const exercise = await api.client.getOne('exercise', '8', {include: 'adaptation'})

    expect(exercise.attributes.instructions).to.equal('Ajoute le suffixe –eur aux verbes.\nIndique la classe des mots fabriqués.')
    expect(exercise.relationships.adaptation.type).to.equal('fillWithFreeTextAdaptation')
    expect(exercise.relationships.adaptation.attributes.placeholder).to.equal('…')
  })

  it('creates an exercise and its adaptation at once', async () => {
    const api = useApiStore()

    const response = await api.client.batch(
      [
        'add',
        'exercise', 'exo',
        {
          'textbookPage': 7,
          'number': '12',
          'instructions': 'Do this',
        },
        {
          'project': {type: 'project', id: '1'},
          'textbook': {type: 'textbook', id: '1'},
        },
      ],
      [
        'add',
        'selectThingsAdaptation', null,
        {
          'colors': 5,
          'words': true,
          'punctuation': true,
        },
        {
          'exercise': {type: 'exercise', lid: 'exo'},
        },
      ],
    )

    const exercise = response[0]

    // @todo Return up-to-date objects in batch response, then remove next line
    await api.client.getOne('exercise', response[0].id)

    expect(exercise.relationships.adaptation.type).to.equal('selectThingsAdaptation')
    expect(exercise.relationships.adaptation.attributes.colors).to.equal(5)
  })

  it('updates an adaptation', async () => {
    const api = useApiStore()

    const adapted = await api.client.patch('selectThingsAdaptation', '2', {colors: 17}, {})

    expect(adapted.attributes.colors).to.equal(17)
  })

  it('changes the type of an adaptation', async () => {
    const api = useApiStore()

    const previous = await api.client.getOne('selectThingsAdaptation', '2')
    expect(previous.relationships.exercise.id).to.equal('7')

    const adapted = await api.client.post('fillWithFreeTextAdaptation', {placeholder: '...'}, {exercise: {type: 'exercise', id: '7'}}, {include: 'exercise'})

    expect(adapted.attributes.placeholder).to.equal('...')
    expect(adapted.relationships.exercise.attributes.instructions).to.equal('Relève dans le texte trois\n{sel1:déterminants}, un {sel2:nom propre}, quatre\n{sel3:noms communs} et trois {sel4:verbes}.')

    await api.client.getOne('selectThingsAdaptation', '2')
    expect(previous.exists).to.be.false
  })
})
