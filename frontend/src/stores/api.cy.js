import { setActivePinia, createPinia } from 'pinia'

import { defineApiStore } from './api.js'


const useApiStore = defineApiStore('api', {baseUrl: 'http://fanout:8080/api/'})

describe('ApiStore', () => {
  beforeEach(() => {
    setActivePinia(createPinia())
    cy.request('POST', 'http://fanout:8080/reset-for-tests/yes-im-sure?fixtures=test-pings')
  })

  it('gets all pings', async () => {
    const api = useApiStore()

    cy.expect(api.cache.try_get_one('ping', '1')).to.be.null

    const pings = await api.client.get_all('pings')
    cy.expect(pings.length).to.equal(6)

    cy.expect(api.cache.get_one('ping', '1').id).to.equal('1')
    cy.expect(api.cache.get_one('ping', '2').id).to.equal('2')
    cy.expect(api.cache.get_one('ping', '3').id).to.equal('3')
  })

  it('gets all pings, filtered', async () => {
    const api = useApiStore()

    cy.expect(api.cache.try_get_one('ping', '1')).to.be.null

    const pings = await api.client.get_all('pings', {filter: {message: 'Hello 1'}})
    cy.expect(pings.length).to.equal(1)
    cy.expect(pings[0].id).to.equal('1')
  })

  it('gets one ping with empty relationships', async () => {
    const api = useApiStore()

    cy.expect(api.cache.try_get_one('ping', '1')).to.be.null

    function check(ping) {
      cy.expect(ping.type).to.equal('ping')
      cy.expect(ping.id).to.equal('1')
      cy.expect(ping.attributes.message).to.equal('Hello 1')
      cy.expect(ping.relationships.prev).to.be.null
      cy.expect(ping.relationships.next).to.deep.equal([])
    }

    check(await api.client.get_one('ping', '1'))
    check(api.cache.get_one('ping', '1'))
  })

  it('gets one ping with non-empty relationships', async () => {
    const api = useApiStore()

    cy.expect(api.cache.try_get_one('ping', '3')).to.be.null

    function check(ping) {
      cy.expect(ping.type).to.equal('ping')
      cy.expect(ping.id).to.equal('3')
      cy.expect(ping.attributes.message).to.equal('Hello 3')

      cy.expect(ping.relationships.prev.type).to.equal('ping')
      cy.expect(ping.relationships.prev.id).to.equal('2')
      cy.expect(ping.relationships.prev.attributes.message).to.equal('Hello 2')
      cy.expect(ping.relationships.prev.relationships.prev).to.be.null
      cy.expect(ping.relationships.prev.relationships.next[0].type).to.equal('ping')
      cy.expect(ping.relationships.prev.relationships.next[0].id).to.equal('3')
      cy.expect(ping.relationships.prev.relationships.next[0].attributes.message).to.equal('Hello 3')

      cy.expect(ping.relationships.next.length).to.equal(2)
      cy.expect(ping.relationships.next[0].type).to.equal('ping')
      cy.expect(ping.relationships.next[0].id).to.equal('4')
      cy.expect(ping.relationships.next[0].attributes.message).to.equal('Hello 4')
      cy.expect(ping.relationships.next[0].relationships.prev.type).to.equal('ping')
      cy.expect(ping.relationships.next[0].relationships.prev.id).to.equal('3')
      cy.expect(ping.relationships.next[0].relationships.prev.attributes.message).to.equal('Hello 3')
      cy.expect(ping.relationships.next[0].relationships.next.length).to.equal(0)
      cy.expect(ping.relationships.next[0].relationships.next).to.deep.equal([])

      cy.expect(ping.relationships.next[1].type).to.equal('ping')
      cy.expect(ping.relationships.next[1].id).to.equal('5')
      cy.expect(ping.relationships.next[1].attributes.message).to.equal('Hello 5')
      cy.expect(ping.relationships.next[1].relationships.prev.type).to.equal('ping')
      cy.expect(ping.relationships.next[1].relationships.prev.id).to.equal('3')
      cy.expect(ping.relationships.next[1].relationships.prev.attributes.message).to.equal('Hello 3')
      cy.expect(ping.relationships.next[1].relationships.next.length).to.equal(1)
      cy.expect(ping.relationships.next[1].relationships.next[0].type).to.equal('ping')
      cy.expect(ping.relationships.next[1].relationships.next[0].id).to.equal('6')
    }

    check(await api.client.get_one('ping', '3', {include: ['prev', 'next']}))
    check(api.cache.get_one('ping', '3'))
  })

  function checkNotInCache(o) {
    try {
      o.attributes
      cy.fail('expected error')
    } catch (e) {
      cy.expect(e.message).to.equal(`${o.type} ${o.id} not in cache`)
    }
    try {
      o.relationships
      cy.fail('expected error')
    } catch (e) {
      cy.expect(e.message).to.equal(`${o.type} ${o.id} not in cache`)
    }
  }

  it('gets one ping with non-empty relationships but does not include related', async () => {
    const api = useApiStore()

    cy.expect(api.cache.try_get_one('ping', '3')).to.be.null

    function check(ping) {
      cy.expect(ping.type).to.equal('ping')
      cy.expect(ping.id).to.equal('3')
      cy.expect(ping.attributes.message).to.equal('Hello 3')

      cy.expect(ping.relationships.prev.type).to.equal('ping')
      cy.expect(ping.relationships.prev.id).to.equal('2')
      checkNotInCache(ping.relationships.prev)

      cy.expect(ping.relationships.next.length).to.equal(2)
      cy.expect(ping.relationships.next[0].type).to.equal('ping')
      cy.expect(ping.relationships.next[0].id).to.equal('4')
      checkNotInCache(ping.relationships.next[0])

      cy.expect(ping.relationships.next[1].type).to.equal('ping')
      cy.expect(ping.relationships.next[1].id).to.equal('5')
      checkNotInCache(ping.relationships.next[1])
    }

    check(await api.client.get_one('ping', '3'))
    check(api.cache.get_one('ping', '3'))
  })

  it('tries to get one non-existing ping', async () => {
    const api = useApiStore()

    cy.expect(await api.client.try_get_one('ping', '0')).to.be.null
    cy.expect(api.cache.try_get_one('ping', '0')).to.be.null
  })

  it('gets one non-existing ping', async () => {
    const api = useApiStore()

    try {
      await api.client.get_one('ping', '0')
      cy.fail('expected error')
    } catch (e) {
      cy.expect(e.message).to.equal('ping 0 does not exist')
    }
    try {
      api.cache.get_one('ping', '0')
      cy.fail('expected error')
    } catch (e) {
      cy.expect(e.message).to.equal('ping 0 not in cache')
    }
  })

  it('creates one minimal ping', async () => {
    const api = useApiStore()

    function check(ping) {
      cy.expect(ping.type).to.equal('ping')
      cy.expect(ping.id).to.equal('7')
      cy.expect(ping.attributes.message).to.be.null
      cy.expect(ping.relationships.prev).to.be.null
      cy.expect(ping.relationships.next).to.deep.equal([])
    }

    check(await api.client.post('ping', {}, {next: []}))
    check(api.cache.get_one('ping', '7'))
    check(await api.client.get_one('ping', '7'))
  })
  
  it('creates one full ping', async () => {
    const api = useApiStore()

    function check(ping) {
      cy.expect(ping.type).to.equal('ping')
      cy.expect(ping.id).to.equal('7')
      cy.expect(ping.attributes.message).to.equal('Hello 7')
      cy.expect(ping.relationships.prev.type).to.equal('ping')
      cy.expect(ping.relationships.prev.id).to.equal('2')
      cy.expect(ping.relationships.prev.attributes.message).to.equal('Hello 2')
      cy.expect(ping.relationships.next.length).to.equal(1)
      cy.expect(ping.relationships.next[0].type).to.equal('ping')
      cy.expect(ping.relationships.next[0].id).to.equal('5')
      cy.expect(ping.relationships.next[0].attributes.message).to.equal('Hello 5')
    }

    check(await api.client.post(
      'ping',
      {message: 'Hello 7'},
      {prev: {type: 'ping', id: '2'}, next: [{type: 'ping', id: '5'}]},
      {include: ['prev', 'next']},
    ))
    check(api.cache.get_one('ping', '7'))
    check(await api.client.get_one('ping', '7'))
  })

  it('creates one full ping but does not include related', async () => {
    const api = useApiStore()

    function check(ping) {
      cy.expect(ping.type).to.equal('ping')
      cy.expect(ping.id).to.equal('7')
      cy.expect(ping.attributes.message).to.equal('Hello 7')
      cy.expect(ping.relationships.prev.type).to.equal('ping')
      cy.expect(ping.relationships.prev.id).to.equal('2')
      checkNotInCache(ping.relationships.prev)
      cy.expect(ping.relationships.next.length).to.equal(1)
      cy.expect(ping.relationships.next[0].type).to.equal('ping')
      cy.expect(ping.relationships.next[0].id).to.equal('5')
      checkNotInCache(ping.relationships.next[0])
    }

    check(await api.client.post(
      'ping',
      {message: 'Hello 7'},
      {prev: {type: 'ping', id: '2'}, next: [{type: 'ping', id: '5'}]},
    ))
    check(api.cache.get_one('ping', '7'))
    check(await api.client.get_one('ping', '7'))
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

    function check(ping) {
      cy.expect(ping.type).to.equal('ping')
      cy.expect(ping.id).to.equal('1')
      cy.expect(ping.attributes.message).to.equal('HELLO 1')
      cy.expect(ping.relationships.prev.type).equal('ping')
      cy.expect(ping.relationships.prev.id).equal('1')
      cy.expect(ping.relationships.prev.attributes.message).equal('HELLO 1')
      cy.expect(ping.relationships.next.length).to.equal(1)
      cy.expect(ping.relationships.next[0].type).equal('ping')
      cy.expect(ping.relationships.next[0].id).equal('1')
      cy.expect(ping.relationships.next[0].attributes.message).equal('HELLO 1')
    }

    check(await api.client.patch('ping', '1', {message: 'HELLO 1'}, {prev: {type: 'ping', id: '1'}}))
    check(api.cache.get_one('ping', '1'))
  })

  it('deletes one ping', async () => {
    const api = useApiStore()

    await api.client.delete('ping', '1')

    cy.expect(api.cache.try_get_one('ping', '1')).to.be.null

    const pings = await api.client.get_all('pings')
    cy.expect(pings.length).to.equal(5)
  })
})
