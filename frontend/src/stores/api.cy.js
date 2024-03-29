import { setActivePinia, createPinia } from 'pinia'

import { defineApiStore } from './api.js'
import TestComponent from './api.cy.vue'


const useApiStore = defineApiStore('api', {baseUrl: 'http://fanout:8080/api/'})
const useAnotherApiStore = defineApiStore('another-api', {baseUrl: 'http://fanout:8080/api/'})

// @todo Synchronize between tabs:
// Make api.cache an option store, synchronized using 'pinia-shared-state'
// Make api.client a simple manipulator of the cache, not an actual store

describe('ApiStore', () => {
  before(console.clear)

  beforeEach(() => {
    cy.request('POST', 'http://fanout:8080/reset-for-tests/yes-im-sure?fixtures=test-pings')

    cy.viewport(1300, 600)

    setActivePinia(createPinia())
    useApiStore()
  })

  it('gets all pings', async () => {
    const api = useApiStore()

    const before = api.cache.getOne('ping', '1')
    cy.expect(before.type).to.equal('ping')
    cy.expect(before.id).to.equal('1')
    cy.expect(before.inCache).to.be.false
    cy.expect(before.exists).to.be.undefined
    cy.expect(before.attributes).to.be.undefined
    cy.expect(before.relationships).to.be.undefined

    const pings = await api.client.getAll('pings')
    cy.expect(pings.length).to.equal(6)
    cy.expect(pings[0].id).to.equal('1')
    cy.expect(pings[1].id).to.equal('2')
    cy.expect(pings[2].id).to.equal('3')

    const after = api.cache.getOne('ping', '1')

    // Previously existing reference is still usable and has been updated
    for (const ping of [before, pings[0], after]) {
      cy.expect(ping.type).to.equal('ping')
      cy.expect(ping.id).to.equal('1')
      cy.expect(ping.inCache).to.be.true
      cy.expect(ping.exists).to.be.true
      cy.expect(ping.attributes.message).to.equal('Hello 1')
      cy.expect(ping.relationships.prev).to.be.null
    }

    // Implementation details that brings a lot of safety to the assertions above
    cy.expect(after).to.equal(before)
    cy.expect(pings[0]).to.equal(before)
  })

  it('gets all pings, filtered', async () => {
    const api = useApiStore()

    const pings = await api.client.getAll('pings', {filter: {message: 'Hello 1'}})
    cy.expect(pings.length).to.equal(1)
    cy.expect(pings[0].type).to.equal('ping')
    cy.expect(pings[0].id).to.equal('1')
    cy.expect(pings[0].inCache).to.be.true
    cy.expect(pings[0].exists).to.be.true
    cy.expect(pings[0].attributes.message).to.equal('Hello 1')
    cy.expect(pings[0].relationships.prev).to.be.null
  })

  it('gets one ping with empty relationships', async () => {
    const api = useApiStore()

    const before = api.cache.getOne('ping', '1')
    cy.expect(before.type).to.equal('ping')
    cy.expect(before.id).to.equal('1')
    cy.expect(before.inCache).to.be.false
    cy.expect(before.exists).to.be.undefined
    cy.expect(before.attributes).to.be.undefined
    cy.expect(before.relationships).to.be.undefined

    const got = await api.client.getOne('ping', '1')
    cy.expect(got.type).to.equal('ping')
    cy.expect(got.id).to.equal('1')
    cy.expect(got.inCache).to.be.true
    cy.expect(got.exists).to.be.true
    cy.expect(got.attributes.message).to.equal('Hello 1')
    cy.expect(got.relationships.prev).to.be.null
    cy.expect(got.relationships.next.length).to.equal(0)

    const after = api.cache.getOne('ping', '1')

    for (const ping of [before, after]) {
      cy.expect(ping.type).to.equal('ping')
      cy.expect(ping.id).to.equal('1')
      cy.expect(ping.inCache).to.be.true
      cy.expect(ping.exists).to.be.true
      cy.expect(ping.attributes.message).to.equal('Hello 1')
      cy.expect(ping.relationships.prev).to.be.null
      cy.expect(ping.relationships.next.length).to.equal(0)
    }

    cy.expect(after).to.equal(before)
    cy.expect(got).to.equal(before)
  })

  it('gets one ping with non-empty relationships', async () => {
    const api = useApiStore()

    const before = api.cache.getOne('ping', '3')
    cy.expect(before.type).to.equal('ping')
    cy.expect(before.id).to.equal('3')
    cy.expect(before.inCache).to.be.false
    cy.expect(before.exists).to.be.undefined
    cy.expect(before.attributes).to.be.undefined
    cy.expect(before.relationships).to.be.undefined

    const got = await api.client.getOne('ping', '3', {include: ['prev', 'next']})

    const after = api.cache.getOne('ping', '3')

    const ping6 = api.cache.getOne('ping', '6')
    cy.expect(ping6.type).to.equal('ping')
    cy.expect(ping6.id).to.equal('6')
    cy.expect(ping6.inCache).to.be.false
    cy.expect(ping6.exists).to.be.true
    cy.expect(ping6.attributes).to.be.undefined
    cy.expect(ping6.relationships).to.be.undefined

    for (const ping of [before, got, after]) {
      cy.expect(ping.type).to.equal('ping')
      cy.expect(ping.id).to.equal('3')
      cy.expect(ping.inCache).to.be.true
      cy.expect(ping.exists).to.be.true
      cy.expect(ping.attributes.message).to.equal('Hello 3')

      cy.expect(ping.relationships.prev.type).to.equal('ping')
      cy.expect(ping.relationships.prev.id).to.equal('2')
      cy.expect(ping.relationships.prev.inCache).to.be.true
      cy.expect(ping.relationships.prev.exists).to.be.true
      cy.expect(ping.relationships.prev.attributes.message).to.equal('Hello 2')
      cy.expect(ping.relationships.prev.relationships.prev).to.be.null
      cy.expect(ping.relationships.prev.relationships.next[0].type).to.equal('ping')
      cy.expect(ping.relationships.prev.relationships.next[0].id).to.equal('3')
      cy.expect(ping.relationships.prev.relationships.next[0].inCache).to.be.true
      cy.expect(ping.relationships.prev.relationships.next[0].exists).to.be.true
      cy.expect(ping.relationships.prev.relationships.next[0].attributes.message).to.equal('Hello 3')

      cy.expect(ping.relationships.next.length).to.equal(2)
      cy.expect(ping.relationships.next[0].type).to.equal('ping')
      cy.expect(ping.relationships.next[0].id).to.equal('4')
      cy.expect(ping.relationships.next[0].inCache).to.be.true
      cy.expect(ping.relationships.next[0].exists).to.be.true
      cy.expect(ping.relationships.next[0].attributes.message).to.equal('Hello 4')
      cy.expect(ping.relationships.next[0].relationships.prev.type).to.equal('ping')
      cy.expect(ping.relationships.next[0].relationships.prev.id).to.equal('3')
      cy.expect(ping.relationships.next[0].relationships.prev.inCache).to.be.true
      cy.expect(ping.relationships.next[0].relationships.prev.exists).to.be.true
      cy.expect(ping.relationships.next[0].relationships.prev.attributes.message).to.equal('Hello 3')
      cy.expect(ping.relationships.next[0].relationships.next.length).to.equal(0)

      cy.expect(ping.relationships.next[1].type).to.equal('ping')
      cy.expect(ping.relationships.next[1].id).to.equal('5')
      cy.expect(ping.relationships.next[1].inCache).to.be.true
      cy.expect(ping.relationships.next[1].exists).to.be.true
      cy.expect(ping.relationships.next[1].attributes.message).to.equal('Hello 5')
      cy.expect(ping.relationships.next[1].relationships.prev.type).to.equal('ping')
      cy.expect(ping.relationships.next[1].relationships.prev.id).to.equal('3')
      cy.expect(ping.relationships.next[1].relationships.prev.inCache).to.be.true
      cy.expect(ping.relationships.next[1].relationships.prev.exists).to.be.true
      cy.expect(ping.relationships.next[1].relationships.prev.attributes.message).to.equal('Hello 3')
      cy.expect(ping.relationships.next[1].relationships.next.length).to.equal(1)
      cy.expect(ping.relationships.next[1].relationships.next[0].type).to.equal('ping')
      cy.expect(ping.relationships.next[1].relationships.next[0].id).to.equal('6')
      cy.expect(ping.relationships.next[1].relationships.next[0].inCache).to.be.false
      cy.expect(ping.relationships.next[1].relationships.next[0].exists).to.be.true
      cy.expect(ping.relationships.next[1].relationships.next[0].attributes).to.be.undefined
    }

    cy.expect(after).to.equal(before)
    cy.expect(got).to.equal(before)
  })

  it('gets one ping with non-empty relationships but does not include related', async () => {
    const api = useApiStore()

    const before = api.cache.getOne('ping', '3')
    cy.expect(before.type).to.equal('ping')
    cy.expect(before.id).to.equal('3')
    cy.expect(before.inCache).to.be.false
    cy.expect(before.exists).to.be.undefined
    cy.expect(before.attributes).to.be.undefined
    cy.expect(before.relationships).to.be.undefined

    const got = await api.client.getOne('ping', '3')

    const after = api.cache.getOne('ping', '3')

    for (const ping of [before, got, after]) {
      cy.expect(ping.type).to.equal('ping')
      cy.expect(ping.id).to.equal('3')
      cy.expect(ping.inCache).to.be.true
      cy.expect(ping.exists).to.be.true
      cy.expect(ping.attributes.message).to.equal('Hello 3')

      cy.expect(ping.relationships.prev.type).to.equal('ping')
      cy.expect(ping.relationships.prev.id).to.equal('2')
      cy.expect(ping.relationships.prev.inCache).to.be.false
      cy.expect(ping.relationships.prev.exists).to.be.true
      cy.expect(ping.relationships.prev.attributes).to.be.undefined
      cy.expect(ping.relationships.prev.relationships).to.be.undefined

      cy.expect(ping.relationships.next.length).to.equal(2)
      cy.expect(ping.relationships.next[0].type).to.equal('ping')
      cy.expect(ping.relationships.next[0].id).to.equal('4')
      cy.expect(ping.relationships.next[0].inCache).to.be.false
      cy.expect(ping.relationships.next[0].exists).to.be.true
      cy.expect(ping.relationships.next[0].attributes).to.be.undefined
      cy.expect(ping.relationships.next[0].relationships).to.be.undefined

      cy.expect(ping.relationships.next[1].type).to.equal('ping')
      cy.expect(ping.relationships.next[1].id).to.equal('5')
      cy.expect(ping.relationships.next[1].inCache).to.be.false
      cy.expect(ping.relationships.next[1].exists).to.be.true
      cy.expect(ping.relationships.next[1].attributes).to.be.undefined
      cy.expect(ping.relationships.next[1].relationships).to.be.undefined
    }

    cy.expect(after).to.equal(before)
    cy.expect(got).to.equal(before)
  })

  it('get one non-cached ping', async () => {
    const api = useApiStore()

    const ping = api.cache.getOne('ping', '0')
    cy.expect(ping.type).to.equal('ping')
    cy.expect(ping.id).to.equal('0')
    cy.expect(ping.inCache).to.be.false
    cy.expect(ping.exists).to.be.undefined
    cy.expect(ping.attributes).to.be.undefined
    cy.expect(ping.relationships).to.be.undefined
  })

  it('gets one non-existing ping', async () => {
    const api = useApiStore()

    const got = await api.client.getOne('ping', '0')
    const cached = api.cache.getOne('ping', '0')

    for (const ping of [got, cached]) {
      cy.expect(ping.type).to.equal('ping')
      cy.expect(ping.id).to.equal('0')
      cy.expect(ping.inCache).to.be.true
      cy.expect(ping.exists).to.be.false
      cy.expect(ping.attributes).to.be.undefined
      cy.expect(ping.relationships).to.be.undefined
    }

    cy.expect(got).to.equal(cached)
  })

  it('creates one minimal ping', async () => {
    const api = useApiStore()

    const before = api.cache.getOne('ping', '7')
    cy.expect(before.type).to.equal('ping')
    cy.expect(before.id).to.equal('7')
    cy.expect(before.inCache).to.be.false
    cy.expect(before.exists).to.be.undefined
    cy.expect(before.attributes).to.be.undefined
    cy.expect(before.relationships).to.be.undefined

    const posted = await api.client.post('ping', {}, {next: []})
    const after = api.cache.getOne('ping', '7')
    const got = await api.client.getOne('ping', '7')

    for (const ping of [before, posted, after, got]) {
      cy.expect(ping.type).to.equal('ping')
      cy.expect(ping.id).to.equal('7')
      cy.expect(before.inCache).to.be.true
      cy.expect(before.exists).to.be.true
      cy.expect(ping.attributes.message).to.be.null
      cy.expect(ping.relationships.prev).to.be.null
      cy.expect(ping.relationships.next.length).to.equal(0)
    }

    cy.expect(after).to.equal(before)
    cy.expect(posted).to.equal(before)
    cy.expect(got).to.equal(before)
  })

  it('creates one full ping', async () => {
    const api = useApiStore()

    const before = api.cache.getOne('ping', '7')
    cy.expect(before.type).to.equal('ping')
    cy.expect(before.id).to.equal('7')
    cy.expect(before.inCache).to.be.false
    cy.expect(before.exists).to.be.undefined
    cy.expect(before.attributes).to.be.undefined
    cy.expect(before.relationships).to.be.undefined

    const posted = await api.client.post(
      'ping',
      {message: 'Hello 7'},
      {prev: {type: 'ping', id: '2'}, next: [{type: 'ping', id: '5'}]},
      {include: ['prev', 'next']},
    )
    const after = api.cache.getOne('ping', '7')
    const got = await api.client.getOne('ping', '7')

    for (const ping of [before, posted, after, got]) {
      cy.expect(ping.type).to.equal('ping')
      cy.expect(ping.id).to.equal('7')
      cy.expect(before.inCache).to.be.true
      cy.expect(before.exists).to.be.true
      cy.expect(ping.attributes.message).to.equal('Hello 7')
      cy.expect(ping.relationships.prev.type).to.equal('ping')
      cy.expect(ping.relationships.prev.id).to.equal('2')
      cy.expect(ping.relationships.prev.inCache).to.be.true
      cy.expect(ping.relationships.prev.exists).to.be.true
      cy.expect(ping.relationships.prev.attributes.message).to.equal('Hello 2')
      cy.expect(ping.relationships.next.length).to.equal(1)
      cy.expect(ping.relationships.next[0].type).to.equal('ping')
      cy.expect(ping.relationships.next[0].id).to.equal('5')
      cy.expect(ping.relationships.next[0].inCache).to.be.true
      cy.expect(ping.relationships.next[0].exists).to.be.true
      cy.expect(ping.relationships.next[0].attributes.message).to.equal('Hello 5')
    }

    cy.expect(after).to.equal(before)
    cy.expect(posted).to.equal(before)
    cy.expect(got).to.equal(before)
  })

  it('creates one full ping but does not include related', async () => {
    const api = useApiStore()

    const before = api.cache.getOne('ping', '7')
    cy.expect(before.type).to.equal('ping')
    cy.expect(before.id).to.equal('7')
    cy.expect(before.inCache).to.be.false
    cy.expect(before.exists).to.be.undefined
    cy.expect(before.attributes).to.be.undefined
    cy.expect(before.relationships).to.be.undefined

    const posted = await api.client.post(
      'ping',
      {message: 'Hello 7'},
      {prev: {type: 'ping', id: '2'}, next: [{type: 'ping', id: '5'}]},
    )
    const after = api.cache.getOne('ping', '7')
    const got = await api.client.getOne('ping', '7')

    for (const ping of [before, posted, after, got]) {
      cy.expect(ping.type).to.equal('ping')
      cy.expect(ping.id).to.equal('7')
      cy.expect(before.inCache).to.be.true
      cy.expect(before.exists).to.be.true
      cy.expect(ping.attributes.message).to.equal('Hello 7')
      cy.expect(ping.relationships.prev.type).to.equal('ping')
      cy.expect(ping.relationships.prev.id).to.equal('2')
      cy.expect(ping.relationships.prev.inCache).to.be.false
      cy.expect(ping.relationships.prev.exists).to.be.true
      cy.expect(ping.relationships.prev.attributes).to.be.undefined
      cy.expect(ping.relationships.prev.relationships).to.be.undefined
      cy.expect(ping.relationships.next.length).to.equal(1)
      cy.expect(ping.relationships.next[0].type).to.equal('ping')
      cy.expect(ping.relationships.next[0].id).to.equal('5')
      cy.expect(ping.relationships.next[0].inCache).to.be.false
      cy.expect(ping.relationships.next[0].exists).to.be.true
      cy.expect(ping.relationships.next[0].attributes).to.be.undefined
      cy.expect(ping.relationships.next[0].relationships).to.be.undefined
    }

    cy.expect(after).to.equal(before)
    cy.expect(posted).to.equal(before)
    cy.expect(got).to.equal(before)
  })

  it('makes a bad request', async () => {
    const api = useApiStore()

    try {
      await api.client.post('ping', {}, {next: null})
      cy.fail('expected error')
    } catch (e) {
      cy.expect(e.cause.errors[0]).to.deep.equal({
        code: 'null',
        detail: 'This field may not be null.',
        source: {pointer: '/data/relationships/next'},
        status: '400',
      })
    }
  })

  it('updates one ping', async () => {
    const api = useApiStore()

    const before = api.cache.getOne('ping', '1')
    cy.expect(before.type).to.equal('ping')
    cy.expect(before.id).to.equal('1')
    cy.expect(before.inCache).to.be.false
    cy.expect(before.exists).to.be.undefined
    cy.expect(before.attributes).to.be.undefined
    cy.expect(before.relationships).to.be.undefined

    const patched = await api.client.patch('ping', '1', {message: 'HELLO 1'}, {prev: {type: 'ping', id: '1'}})
    const after = api.cache.getOne('ping', '1')

    for(const ping of [before, patched, after]) {
      cy.expect(ping.type).to.equal('ping')
      cy.expect(ping.id).to.equal('1')
      cy.expect(ping.inCache).to.be.true
      cy.expect(ping.exists).to.be.true
      cy.expect(ping.attributes.message).to.equal('HELLO 1')
      cy.expect(ping.relationships.prev.type).equal('ping')
      cy.expect(ping.relationships.prev.id).equal('1')
      cy.expect(ping.relationships.prev.inCache).to.be.true
      cy.expect(ping.relationships.prev.exists).to.be.true
      cy.expect(ping.relationships.prev.attributes.message).equal('HELLO 1')
      cy.expect(ping.relationships.next.length).to.equal(1)
      cy.expect(ping.relationships.next[0].type).equal('ping')
      cy.expect(ping.relationships.next[0].id).equal('1')
      cy.expect(ping.relationships.next[0].inCache).to.be.true
      cy.expect(ping.relationships.next[0].exists).to.be.true
      cy.expect(ping.relationships.next[0].attributes.message).equal('HELLO 1')
    }

    cy.expect(after).to.equal(before)
    cy.expect(patched).to.equal(before)
  })

  it('deletes one ping', async () => {
    const api = useApiStore()

    const before = await api.client.getOne('ping', '1')
    cy.expect(before.type).to.equal('ping')
    cy.expect(before.id).to.equal('1')
    cy.expect(before.inCache).to.be.true
    cy.expect(before.exists).to.be.true
    cy.expect(before.attributes.message).to.equal('Hello 1')
    cy.expect(before.relationships.prev).to.be.null

    await api.client.delete('ping', '1')

    cy.expect((await api.client.getAll('pings')).length).to.equal(5)

    const after = api.cache.getOne('ping', '1')

    for (const ping of [before, after]) {
      cy.expect(ping.type).to.equal('ping')
      cy.expect(ping.id).to.equal('1')
      cy.expect(ping.inCache).to.be.true
      cy.expect(ping.exists).to.be.false
      cy.expect(ping.attributes).to.be.undefined
      cy.expect(ping.relationships).to.be.undefined
    }

    cy.expect(after).to.equal(before)
  })

  it('deletes one ping before ever interacting with it', async () => {
    const api = useApiStore()

    await api.client.delete('ping', '1')

    const after = api.cache.getOne('ping', '1')
    cy.expect(after.type).to.equal('ping')
    cy.expect(after.id).to.equal('1')
    cy.expect(after.inCache).to.be.true
    cy.expect(after.exists).to.be.false
    cy.expect(after.attributes).to.be.undefined
    cy.expect(after.relationships).to.be.undefined
  })

  it('refreshes a list', async () => {
    const api = useApiStore()
    const anotherApi = useAnotherApiStore()

    const all = await api.client.getAll('pings')
    cy.expect(all.length).to.equal(6)

    await anotherApi.client.delete('ping', '1')

    cy.expect(all.length).to.equal(6)

    await all.refresh()

    cy.expect(all.length).to.equal(5)
  })

  it('refreshes a list several times', async () => {
    const api = useApiStore()
    const anotherApi = useAnotherApiStore()

    const all = await api.client.getAll('pings')
    cy.expect(all.length).to.equal(6)

    all.refresh()
    all.refresh()
    all.refresh()
    all.refresh()

    anotherApi.client.delete('ping', '1')

    cy.expect(all.loading).to.be.true
    cy.expect(all.length).to.equal(6)

    all.refresh()
    all.refresh()
    all.refresh()
    await all.refresh()  // This last refresh must win
    cy.expect(all.loading).to.be.false

    cy.expect(all.length).to.equal(5)
    cy.expect(all[0].id).to.equal('2')
    cy.expect(all[1].id).to.equal('3')
    cy.expect(all[2].id).to.equal('4')
    cy.expect(all[3].id).to.equal('5')
    cy.expect(all[4].id).to.equal('6')
  })

  it('refreshes a list after many deletions', async () => {
    const api = useApiStore()
    const anotherApi = useAnotherApiStore()

    const all = await api.client.getAll('pings')
    cy.expect(all.length).to.equal(6)

    all.refresh()

    await anotherApi.client.delete('ping', '1')
    await anotherApi.client.delete('ping', '2')
    await anotherApi.client.delete('ping', '3')

    await all.refresh()

    cy.expect(all.length).to.equal(3)
  })

  it('refreshes a list when getting it again', async () => {
    const api = useApiStore()
    const anotherApi = useAnotherApiStore()

    const before = await api.client.getAll('pings')
    cy.expect(before.length).to.equal(6)

    await anotherApi.client.delete('ping', '1')

    cy.expect(before.length).to.equal(6)

    const after = await api.client.getAll('pings')

    for (const pings of [before, after]) {
      cy.expect(pings.length).to.equal(5)
    }

    cy.expect(after).to.equal(before)
  })

  it('deletes one ping that was in a list', async () => {
    const api = useApiStore()

    const pings = await api.client.getAll('pings')
    cy.expect(pings.length).to.equal(6)

    await api.client.delete('ping', '1')

    cy.expect(pings.length).to.equal(5)
  })

  // @todo Implement: remove the ping from the relationship list (lazily in 'get relationships', not proactively)
  // it('deletes one ping that was in a relationship', async () => {
  // })

  it('reacts to ping message edition', () => {
    cy.mount(TestComponent)

    cy.get('li').should('have.length', 18)
    cy.get('li:contains(Hello 3)').should('have.length', 3)

    cy.get('ul > :nth-child(3) button').contains('Reset message').click()

    cy.get('li').should('have.length', 18)
    cy.get('li:contains(Hello 3)').should('not.exist')
  })

  it('reacts to ping deletion', () => {
    cy.mount(TestComponent)

    cy.get('li').should('have.length', 18)
    cy.get('li:contains(Hello 3)').should('have.length', 3)

    cy.get('ul > :nth-child(3) button').contains('Delete').click()

    cy.get('li').should('have.length', 15)
    cy.get('li:contains(Hello 3)').should('not.exist')

    cy.get('.spinner-border').should('not.exist')
  })

  it('reacts to ping creation', () => {
    cy.mount(TestComponent)

    cy.get('.spinner-border').should('not.exist')
    cy.get('li').should('have.length', 18)

    cy.get('button').contains('Ping').click()

    cy.get('li').should('have.length', 21)
  })
})
