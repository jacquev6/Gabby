import { defineApiStore, resetApiStores } from './api'
import type { FillWithFreeTextAdaptation, SelectThingsAdaptation } from './api'
import TestComponent from './api.cy.vue'
import { computed, watch } from 'vue'


const useApiStore = defineApiStore('api', {baseUrl: 'http://fanout:8080/api'})
const useAnotherApiStore = defineApiStore('another-api', {baseUrl: 'http://fanout:8080/api'})

// It would look better if we could type:
//   expect(value).to.be.true
// as:
//   asserts value is true
// but I don't know how yet, so this will do for now.
function expectToBeTrue(value: boolean): asserts value is true { expect(value).to.be.true }
function expectToNotBeNull<T>(value: T | null): asserts value is T { expect(value).to.not.be.null }

describe('ApiStore - Basic functionality', () => {
  before(console.clear)

  beforeEach(() => {
    cy.request('POST', 'http://fanout:8080/reset-for-tests/yes-im-sure?fixtures=admin-user,test-pings')

    resetApiStores()
  })

  it('creates a ping with attributes', async () => {
    const api = useApiStore()

    const ping = await api.client.createOne('ping', {message: 'NEW'}, {})

    expect(ping.loading).to.be.false
    expectToBeTrue(ping.exists)
    expect(ping.attributes.message).to.equal('NEW')
    expect(ping.relationships.prev).to.be.null
    expect(ping.relationships.next).to.have.length(0)
  })

  it("creates a ping with 'prev' relationship", async () => {
    const api = useApiStore()

    const prev = api.cache.getOne('ping', '1')

    const ping = await api.client.createOne('ping', {}, {prev})

    expect(ping.loading).to.be.false
    expectToBeTrue(ping.exists)
    expect(ping.attributes.message).to.be.null
    expect(ping.relationships.prev).to.equal(prev)
    expect(ping.relationships.next).to.have.length(0)

    expect(prev.inCache).to.be.false
  })

  it("creates a ping with 'next' relationship", async () => {
    const api = useApiStore()

    const next = api.cache.getOne('ping', '1')

    const ping = await api.client.createOne('ping', {}, {next: [next]})

    expect(ping.loading).to.be.false
    expectToBeTrue(ping.exists)
    expect(ping.attributes.message).to.be.null
    expect(ping.relationships.prev).to.be.null
    expect(ping.relationships.next).to.have.length(1)
    expect(ping.relationships.next[0]).to.equal(next)

    expect(next.inCache).to.be.false
  })

  it("creates a ping with relationships, including related", async () => {
    const api = useApiStore()

    const prev = api.cache.getOne('ping', '2')
    const next = api.cache.getOne('ping', '1')

    const ping = await api.client.createOne('ping', {}, {prev, next: [next]}, {include: ['prev', 'next']})

    expect(ping.loading).to.be.false
    expectToBeTrue(ping.exists)
    expect(ping.attributes.message).to.be.null
    expect(ping.relationships.prev).to.equal(prev)
    expect(ping.relationships.next).to.have.length(1)
    expect(ping.relationships.next[0]).to.equal(next)

    expect(prev.inCache).to.be.true
    expect(next.inCache).to.be.true
  })

  it('creates pings in batches', async () => {
    const api = useApiStore()

    await api.auth.login('admin', 'password')

    const posted = await api.client.batch(
      [
        'add',
        'ping', 'prev',
        {message: 'Hello 7'},
        {},
      ],
      [
        'add',
        'ping', 'next',
        {message: 'Hello 8'},
        {},
      ],
      [
        'add',
        'ping', null,
        {message: 'Hello 9'},
        {prev: {type: 'ping', lid: 'prev'}, next: [{type: 'ping', lid: 'next'}]},
      ],
    )

    const fromCache = api.cache.getOne('ping', posted[2].id)
    expect(fromCache).to.equal(posted[2])
  })

  it("gets one ping from cache then refreshes it, awaiting on '.refresh()'", async () => {
    const api = useApiStore()

    const ping = api.cache.getOne('ping', '1')

    expect(ping.loading).to.be.false
    expect(ping.inCache).to.be.false

    await ping.refresh()

    expect(ping.loading).to.be.false
    expect(ping.inCache).to.be.true
  })

  it("gets one ping from cache then refreshes it, awaiting on the return value of '.refresh()'", async () => {
    const api = useApiStore()

    const ping = api.cache.getOne('ping', '1')

    expect(ping.loading).to.be.false
    expect(ping.inCache).to.be.false

    const loaded = ping.refresh()

    expect(ping.loading).to.be.true
    expect(ping.inCache).to.be.false

    await loaded

    expect(ping.loading).to.be.false
    expect(ping.inCache).to.be.true
  })

  it("gets one ping from cache then refreshes it, awaiting on '.loaded'", async () => {
    const api = useApiStore()

    const ping = api.cache.getOne('ping', '1')

    expect(ping.loading).to.be.false
    expect(ping.inCache).to.be.false

    ping.refresh()

    expect(ping.loading).to.be.true
    expect(ping.inCache).to.be.false

    await ping.loaded

    expect(ping.loading).to.be.false
    expect(ping.inCache).to.be.true
  })

  it("gets one ping from cache then refreshes it several times", () => {
    const api = useApiStore()

    const ping = api.cache.getOne('ping', '1')

    cy.intercept('GET', 'http://fanout:8080/api/pings/1').as('getPing').then(async () => {
      ping.refresh()  // Triggers a refresh

      expect(ping.loading).to.be.true

      ping.refresh()  // Takes a note to refresh after the current one
      ping.refresh()  // Confirms the note
      ping.refresh()  // Confirms the note
      ping.refresh()  // Confirms the note

      await ping.loaded

      expect(ping.loading).to.be.false

      cy.get('@getPing.all').should('have.length', 2).then(async () => {
        ping.refresh()  // Triggers a refresh

        expect(ping.loading).to.be.true

        ping.refresh()  // Takes a note
        ping.refresh()
        ping.refresh()
        ping.refresh()

        await ping.loaded

        expect(ping.loading).to.be.false

        cy.get('@getPing.all').should('have.length', 4)
      })
    })
  })

  it("gets one ping from cache, awaits on '.loaded' without '.refresh()'ing it", async () => {
    const api = useApiStore()

    const ping = api.cache.getOne('ping', '1')

    await ping.loaded.then(
      () => { throw new Error('promise should have rejected') },
      (error: Error) => expect(error.message).to.equal('Never refreshed'),
    )
  })

  it("gets one ping from auto, awaits on '.loaded'", async () => {
    const api = useApiStore()

    const ping = api.auto.getOne('ping', '1')

    expect(ping.loading).to.be.true
    expect(ping.inCache).to.be.false

    await ping.loaded

    expect(ping.loading).to.be.false
    expectToBeTrue(ping.inCache)
    expect(ping.exists).to.be.true
  })

  it('gets the same ping from all access methods', async () => {
    const api = useApiStore()

    const fromCache = api.cache.getOne('ping', '1')
    const fromAuto = api.auto.getOne('ping', '1')
    const fromClient = await api.client.getOne('ping', '1')

    expect(fromCache).to.equal(fromAuto)
    expect(fromCache).to.equal(fromClient)
  })

  it("gets one non-existing ping from client", async () => {
    const api = useApiStore()

    const ping = await api.client.getOne('ping', '0')

    expect(ping.loading).to.be.false
    expect(ping.inCache).to.be.true
    expect(ping.exists).to.be.false
  })

  it("gets one existing ping without relationships from client", async () => {
    const api = useApiStore()

    const ping = await api.client.getOne('ping', '1')

    expect(ping.loading).to.be.false
    expectToBeTrue(ping.exists)
    console.assert(ping.attributes !== undefined)
    expect(ping.attributes.message).to.equal('Hello 1')
    console.assert(ping.relationships !== undefined)
    expect(ping.relationships.prev).to.be.null
    expect(ping.relationships.next).to.have.length(0)
  })

  it("gets one existing ping with relationships from client", async () => {
    const api = useApiStore()

    const ping = await api.client.getOne('ping', '3')

    expect(ping.loading).to.be.false
    expectToBeTrue(ping.exists)
    console.assert(ping.attributes !== undefined)
    expect(ping.attributes.message).to.equal('Hello 3')
    console.assert(ping.relationships !== undefined)
    console.assert(ping.relationships.prev !== null)
    expect(ping.relationships.prev.type).to.equal('ping')
    expect(ping.relationships.prev.id).to.equal('2')
    expect(ping.relationships.prev.inCache).to.be.false
    expect(ping.relationships.next).to.have.length(2)
    expect(ping.relationships.next[0].type).to.equal('ping')
    expect(ping.relationships.next[0].id).to.equal('4')
    expect(ping.relationships.next[0].inCache).to.be.false
    expect(ping.relationships.next[1].type).to.equal('ping')
    expect(ping.relationships.next[1].id).to.equal('5')
    expect(ping.relationships.next[1].inCache).to.be.false
  })

  it("gets one existing ping with relationships from client, including related", async () => {
    const api = useApiStore()

    const ping = await api.client.getOne('ping', '3', {include: ['prev', 'next']})

    expect(ping.loading).to.be.false
    expectToBeTrue(ping.exists)

    expect(ping.attributes.message).to.equal('Hello 3')

    console.assert(ping.relationships.prev !== null)
    expect(ping.relationships.prev.type).to.equal('ping')
    expect(ping.relationships.prev.id).to.equal('2')
    expectToBeTrue(ping.relationships.prev.inCache)
    expectToBeTrue(ping.relationships.prev.exists)
    expect(ping.relationships.prev.relationships.next).to.have.length(1)
    expect(ping.relationships.prev.relationships.next[0]).to.equal(ping)

    expect(ping.relationships.next).to.have.length(2)
    expect(ping.relationships.next[0].type).to.equal('ping')
    expect(ping.relationships.next[0].id).to.equal('4')
    expectToBeTrue(ping.relationships.next[0].inCache)
    expectToBeTrue(ping.relationships.next[0].exists)
    expect(ping.relationships.next[0].attributes.message).to.equal('Hello 4')
    expect(ping.relationships.next[0].relationships.prev).to.equal(ping)
    expect(ping.relationships.next[1].type).to.equal('ping')
    expect(ping.relationships.next[1].id).to.equal('5')
    expectToBeTrue(ping.relationships.next[1].inCache)
    expectToBeTrue(ping.relationships.next[1].exists)
    expect(ping.relationships.next[1].attributes.message).to.equal('Hello 5')
    expect(ping.relationships.next[1].relationships.prev).to.equal(ping)
  })

  it('gets a ping from cache, only including prev', async () => {
    const api = useApiStore()

    const ping = api.cache.getOne('ping', '3', {include: ['prev']})

    await ping.refresh()

    expectToBeTrue(ping.inCache)
    expectToBeTrue(ping.exists)
    expectToNotBeNull(ping.relationships.prev)
    expect(ping.relationships.prev.inCache).to.be.true
    expect(ping.relationships.next).to.have.length(2)
    expect(ping.relationships.next[0].inCache).to.be.false
    expect(ping.relationships.next[1].inCache).to.be.false
  })

  it('gets a ping from cache, merging the inclusion options', async () => {
    const api = useApiStore()

    const ping = api.cache.getOne('ping', '3', {include: ['prev']})
    api.cache.getOne('ping', '3', {include: ['next']})

    await ping.refresh()

    expectToBeTrue(ping.inCache)
    expectToBeTrue(ping.exists)
    expectToNotBeNull(ping.relationships.prev)
    expect(ping.relationships.prev.inCache).to.be.true
    expect(ping.relationships.next).to.have.length(2)
    expect(ping.relationships.next[0].inCache).to.be.true
    expect(ping.relationships.next[1].inCache).to.be.true
  })

  it("gets a list of pings from cache, then refreshes it, awaiting on '.refresh()'", async () => {
    const api = useApiStore()

    const pings = api.cache.getAll('ping')

    expect(pings.loading).to.be.false
    expect(pings.inCache).to.be.false
    expect(pings.items).to.have.length(0)

    await pings.refresh()

    expect(pings.loading).to.be.false
    expect(pings.inCache).to.be.true
    expect(pings.items).to.have.length(6)
  })

  it("gets a list of pings from cache, then refreshes it, awaiting on the return value of '.refresh()'", async () => {
    const api = useApiStore()

    const pings = api.cache.getAll('ping')

    expect(pings.loading).to.be.false
    expect(pings.inCache).to.be.false
    expect(pings.items).to.have.length(0)

    const loaded = pings.refresh()

    expect(pings.loading).to.be.true
    expect(pings.inCache).to.be.false
    expect(pings.items).to.have.length(0)

    await loaded

    expect(pings.loading).to.be.false
    expect(pings.inCache).to.be.true
    expect(pings.items).to.have.length(6)
  })

  it("gets a list of pings from cache, then refreshes it, awaiting on '.fullyLoaded'", async () => {
    const api = useApiStore()

    const pings = api.cache.getAll('ping')

    expect(pings.loading).to.be.false
    expect(pings.inCache).to.be.false
    expect(pings.items).to.have.length(0)

    pings.refresh()

    expect(pings.loading).to.be.true
    expect(pings.inCache).to.be.false
    expect(pings.items).to.have.length(0)

    await pings.fullyLoaded

    expect(pings.loading).to.be.false
    expect(pings.inCache).to.be.true
    expect(pings.items).to.have.length(6)
  })

  it("gets a list of pings from cache, then refreshes it several times", () => {
    const api = useApiStore()

    const pings = api.cache.getAll('ping')

    cy.intercept('GET', 'http://fanout:8080/api/pings').as('getPings1')
    cy.intercept('GET', 'http://fanout:8080/api/pings?page%5Bnumber%5D=2').as('getPings2').then(async () => {
      pings.refresh()  // Triggers a refresh

      expect(pings.loading).to.be.true

      pings.refresh()  // Takes a note to refresh after the current one
      pings.refresh()  // Confirms the note
      pings.refresh()  // Confirms the note
      pings.refresh()  // Confirms the note

      await pings.fullyLoaded

      expect(pings.loading).to.be.false
      expect(pings.items).to.have.length(6)

      cy.get('@getPings1.all').should('have.length', 2)
      cy.get('@getPings2.all').should('have.length', 1).then(async () => {
        pings.refresh()  // Triggers a refresh

        expect(pings.loading).to.be.true

        pings.refresh()  // Takes a note
        pings.refresh()
        pings.refresh()
        pings.refresh()

        await pings.fullyLoaded

        expect(pings.loading).to.be.false
        expect(pings.items).to.have.length(6)

        cy.get('@getPings1.all').should('have.length', 4)
        cy.get('@getPings2.all').should('have.length', 2)
      })
    })
  })

  it("gets a list of pings from cache, awaits on '.fullyLoaded' without '.reresh()'ing it", async () => {
    const api = useApiStore()

    const pings = api.cache.getAll('ping')

    await pings.fullyLoaded.then(
      () => { throw new Error('promise should have rejected') },
      (error: Error) => expect(error.message).to.equal('Never refreshed'),
    )
  })

  it("gets a list of pings from auto, awaits on '.fullyLoaded'", async () => {
    const api = useApiStore()

    const pings = api.auto.getAll('ping')

    expect(pings.loading).to.be.true
    expect(pings.inCache).to.be.false
    expect(pings.items).to.have.length(0)

    await pings.fullyLoaded

    expect(pings.loading).to.be.false
    expect(pings.inCache).to.be.true
    expect(pings.items).to.have.length(6)
  })

  it("gets the same list from all access methods", async () => {
    const api = useApiStore()

    const fromCache = api.cache.getAll('ping')
    const fromAuto = api.auto.getAll('ping')
    const fromClient = await api.client.getAll('ping')

    expect(fromCache).to.equal(fromAuto)
    expect(fromCache).to.equal(fromClient)
  })

  it('gets the same filtered list from all access methods', async () => {
    const api = useApiStore()

    const fromCache = api.cache.getAll('ping', {filters: {message: 'Hello 1'}})
    const fromAuto = api.auto.getAll('ping', {filters: {message: 'Hello 1'}})
    const fromClient = await api.client.getAll('ping', {filters: {message: 'Hello 1'}})

    expect(fromCache).to.equal(fromAuto)
    expect(fromCache).to.equal(fromClient)

    expect(fromClient.items).to.have.length(1)
  })

  it('gets a filtered list from cache, including related', async () => {
    const api = useApiStore()

    const pings = api.cache.getAll('ping', {filters: {message: 'Hello 3'}, include: ['prev', 'next']})
    await pings.refresh()

    expect(pings.items).to.have.length(1)
    expectToBeTrue(pings.items[0].exists)
    expectToNotBeNull(pings.items[0].relationships.prev)
    expect(pings.items[0].relationships.prev.inCache).to.be.true
    expect(pings.items[0].relationships.prev).to.equal(api.cache.getOne('ping', '2'))
    expect(pings.items[0].relationships.next).to.have.length(2)
    expect(pings.items[0].relationships.next[0].inCache).to.be.true
    expect(pings.items[0].relationships.next[0]).to.equal(api.cache.getOne('ping', '4'))
    expect(pings.items[0].relationships.next[1].inCache).to.be.true
    expect(pings.items[0].relationships.next[1]).to.equal(api.cache.getOne('ping', '5'))
  })

  it('gets a filtered list from auto, including related', async () => {
    const api = useApiStore()

    const pings = api.auto.getAll('ping', {filters: {message: 'Hello 3'}, include: ['prev', 'next']})

    await pings.fullyLoaded

    expect(pings.items).to.have.length(1)
    expectToBeTrue(pings.items[0].exists)
    expectToNotBeNull(pings.items[0].relationships.prev)
    expect(pings.items[0].relationships.prev.inCache).to.be.true
    expect(pings.items[0].relationships.prev).to.equal(api.cache.getOne('ping', '2'))
    expect(pings.items[0].relationships.next).to.have.length(2)
    expect(pings.items[0].relationships.next[0].inCache).to.be.true
    expect(pings.items[0].relationships.next[0]).to.equal(api.cache.getOne('ping', '4'))
    expect(pings.items[0].relationships.next[1].inCache).to.be.true
    expect(pings.items[0].relationships.next[1]).to.equal(api.cache.getOne('ping', '5'))
  })

  it('gets a filtered list from client, including related', async () => {
    const api = useApiStore()

    const pings = await api.client.getAll('ping', {filters: {message: 'Hello 3'}, include: ['prev', 'next']})

    expect(pings.items).to.have.length(1)
    expectToBeTrue(pings.items[0].exists)
    expectToNotBeNull(pings.items[0].relationships.prev)
    expect(pings.items[0].relationships.prev.inCache).to.be.true
    expect(pings.items[0].relationships.prev).to.equal(api.cache.getOne('ping', '2'))
    expect(pings.items[0].relationships.next).to.have.length(2)
    expect(pings.items[0].relationships.next[0].inCache).to.be.true
    expect(pings.items[0].relationships.next[0]).to.equal(api.cache.getOne('ping', '4'))
    expect(pings.items[0].relationships.next[1].inCache).to.be.true
    expect(pings.items[0].relationships.next[1]).to.equal(api.cache.getOne('ping', '5'))
  })

  it('gets a filtered list from cache, only including prev', async () => {
    const api = useApiStore()

    const pings = api.cache.getAll('ping', {filters: {message: 'Hello 3'}, include: ['prev']})
    await pings.refresh()

    expect(pings.items).to.have.length(1)
    expectToBeTrue(pings.items[0].exists)
    expectToNotBeNull(pings.items[0].relationships.prev)
    expect(pings.items[0].relationships.prev.inCache).to.be.true
    expect(pings.items[0].relationships.next).to.have.length(2)
    expect(pings.items[0].relationships.next[0].inCache).to.be.false
    expect(pings.items[0].relationships.next[1].inCache).to.be.false
  })

  it('gets a filtered list from cache, merging the inclusion options', async () => {
    const api = useApiStore()

    const pings = api.cache.getAll('ping', {filters: {message: 'Hello 3'}, include: ['prev']})
    api.cache.getAll('ping', {filters: {message: 'Hello 3'}, include: ['next']})
    await pings.refresh()

    expect(pings.items).to.have.length(1)
    expectToBeTrue(pings.items[0].exists)
    expectToNotBeNull(pings.items[0].relationships.prev)
    expect(pings.items[0].relationships.prev.inCache).to.be.true
    expect(pings.items[0].relationships.next).to.have.length(2)
    expect(pings.items[0].relationships.next[0].inCache).to.be.true
    expect(pings.items[0].relationships.next[1].inCache).to.be.true
  })

  it('gets different paginated lists for different filters', async () => {
    const api = useApiStore()

    const notFiltered = api.cache.getAll('ping')
    const filtered1 = api.cache.getAll('ping', {filters: {message: 'Hello 1'}})
    const filtered2 = api.cache.getAll('ping', {filters: {message: 'Hello 2'}})

    expect(notFiltered).to.not.equal(filtered1)
    expect(notFiltered).to.not.equal(filtered2)
    expect(filtered1).to.not.equal(filtered2)
  })

  it('keeps the items in a list during refresh until it gets the first page', async () => {
    const api = useApiStore()

    const pings = await api.client.getAll('ping')

    expect(pings.items).to.have.length(6)

    pings.refresh()

    expect(pings.loading).to.be.true
    expect(pings.items).to.have.length(6)

    await pings.pageLoaded

    expect(pings.loading).to.be.true
    expect(pings.items).to.have.length(2)

    await pings.pageLoaded

    expect(pings.loading).to.be.true
    expect(pings.items).to.have.length(4)

    await pings.pageLoaded

    expect(pings.loading).to.be.false
    expect(pings.items).to.have.length(6)
  })

  it('patches a ping', async () => {
    const api = useApiStore()

    const ping = await api.client.getOne('ping', '1')

    expect(ping.patching).to.be.false
    expectToBeTrue(ping.exists)
    expect(ping.attributes.message).to.equal('Hello 1')

    const patched = ping.patch({message: 'HELLO 1'}, {})

    expect(ping.patching).to.be.true
    expect(ping.attributes.message).to.equal('Hello 1')

    await patched

    expect(ping.patching).to.be.false
    expect(ping.attributes.message).to.equal('HELLO 1')
  })

  it("patches a never-heard-of existing ping's attributes", async () => {
    const api = useApiStore()

    const ping = api.cache.getOne('ping', '1')

    await ping.patch({message: 'HELLO 1'}, {})
    expectToBeTrue(ping.inCache)
    expectToBeTrue(ping.exists)
    expect(ping.attributes.message).to.equal('HELLO 1')
  })

  it("patches a known existing ping's attributes", async () => {
    const api = useApiStore()

    const ping = await api.client.getOne('ping', '1')

    await ping.patch({message: 'HELLO 1'}, {})
    expectToBeTrue(ping.exists)
    expect(ping.attributes.message).to.equal('HELLO 1')
  })

  it("patches a never-heard-of existing ping's 'prev' relationship", async () => {
    const api = useApiStore()

    const ping = api.cache.getOne('ping', '1')

    const prev = api.cache.getOne('ping', '2')

    await ping.patch({}, {prev})
    expectToBeTrue(ping.inCache)
    expectToBeTrue(ping.exists)
    expect(ping.relationships.prev).to.equal(prev)

    expect(prev.inCache).to.be.false
  })

  it("patches a never-heard-of existing ping's 'next' relationship", async () => {
    const api = useApiStore()

    const ping = api.cache.getOne('ping', '1')

    const next = api.cache.getOne('ping', '2')

    await ping.patch({}, {next: [next]})

    expectToBeTrue(ping.inCache)
    expectToBeTrue(ping.exists)
    expect(ping.relationships.next).to.have.length(1)
    expect(ping.relationships.next[0]).to.equal(next)

    expect(next.inCache).to.be.false
  })

  it("patches a never-heard-of existing ping's relationships, including related", async () => {
    const api = useApiStore()

    const ping = api.cache.getOne('ping', '1')

    const prev = api.cache.getOne('ping', '2')
    const next = api.cache.getOne('ping', '3')

    await ping.patch({}, {prev, next: [next]}, {include: ['prev', 'next']})
    expectToBeTrue(ping.inCache)
    expectToBeTrue(ping.exists)
    expect(ping.relationships.next).to.have.length(1)
    expect(ping.relationships.next[0]).to.equal(next)

    expect(prev.inCache).to.be.true
    expect(next.inCache).to.be.true
  })

  it('deletes a ping', async () => {
    const api = useApiStore()

    const ping = await api.client.getOne('ping', '1')

    expect(ping.inCache).to.be.true
    expect(ping.exists).to.be.true
    expect(ping.deleting).to.be.false

    const deleted = ping.delete()

    expect(ping.inCache).to.be.true
    expect(ping.exists).to.be.true
    expect(ping.deleting).to.be.true

    await deleted

    expect(ping.inCache).to.be.true
    expect(ping.exists).to.be.false
    expect(ping.deleting).to.be.false
  })

  it('deletes a never-heard-of ping', () => {
    const api = useApiStore()

    cy.intercept('DELETE', 'http://fanout:8080/api/pings/1').as('deletePing')
    cy.intercept('GET', 'http://fanout:8080/api/pings/1').as('getPing').then(async () => {
      const ping = api.cache.getOne('ping', '1')

      await ping.delete()
      expectToBeTrue(ping.inCache)
      expect(ping.exists).to.be.false

      cy.get('@getPing.all').should('have.length', 0)
      cy.get('@deletePing.all').should('have.length', 1).then(async () => {
        await ping.loaded

        cy.get('@getPing.all').should('have.length', 0)
      }).then(async () => {
        await ping.refresh()

        expect(ping.inCache).to.be.true
        expect(ping.exists).to.be.false

        cy.get('@getPing.all').should('have.length', 1)
      })
    })
  })

  it("doesn't leak items between stores", async () => {
    const api1 = useApiStore()
    const api2 = useAnotherApiStore()

    await api1.client.getOne('ping', '1')
    await api1.cache.getOne('ping', '1').loaded

    const ping = api2.cache.getOne('ping', '1')
    expect(ping.inCache).to.be.false

    await ping.loaded.then(
      () => { throw new Error('promise should have rejected') },
      (error: Error) => expect(error.message).to.equal('Never refreshed'),
    )
  })
})

describe('ApiStore - (inCache, exists)', () => {
  before(console.clear)

  beforeEach(() => {
    cy.request('POST', 'http://fanout:8080/reset-for-tests/yes-im-sure?fixtures=test-pings')

    resetApiStores()
  })

  it('can be (true, true) after getting an existing item', async () => {
    const api = useApiStore()

    const ping = await api.client.getOne('ping', '1')

    expect(ping.inCache).to.be.true
    expect(ping.exists).to.be.true
  })

  it('can be (true, false) after getting a non-existing item', async () => {
    const api = useApiStore()

    const ping = await api.client.getOne('ping', '0')

    expect(ping.inCache).to.be.true
    expect(ping.exists).to.be.false
  })

  it('can be (true, false) after deleting an item', async () => {
    const api = useApiStore()

    const ping = api.cache.getOne('ping', '1')
    await ping.delete()

    expect(ping.inCache).to.be.true
    expect(ping.exists).to.be.false
  })

  it('can be (false, undefined) after getting a never-heard-of item from cache', async () => {
    const api = useApiStore()

    const ping = api.cache.getOne('ping', '1')

    expect(ping.inCache).to.be.false
    expect(ping.exists).to.be.undefined
  })

  it('can be (false, true) after learning the item exists via a scalar relationship', async () => {
    const api = useApiStore()

    await api.client.getOne('ping', '3')

    const ping = api.cache.getOne('ping', '2')

    expect(ping.inCache).to.be.false
    expect(ping.exists).to.be.true
  })

  it('can be (false, true) after learning the item exists via a list relationship', async () => {
    const api = useApiStore()

    await api.client.getOne('ping', '3')

    const ping = api.cache.getOne('ping', '4')

    expect(ping.inCache).to.be.false
    expect(ping.exists).to.be.true
  })

  it("can't be (false, false)", () => {
    // This is only for documentation as it's impossible to test
  })
})

describe('ApiStore - Reactivity', () => {
  before(console.clear)

  beforeEach(() => {
    cy.request('POST', 'http://fanout:8080/reset-for-tests/yes-im-sure?fixtures=admin-user,test-pings')

    cy.viewport(1300, 600)

    resetApiStores()
    useApiStore()  // Pre-initialize the store for TestComponent
  })

  it('reacts to ping message edition', () => {
    cy.mount(TestComponent)

    cy.get('li').should('have.length', 18)
    cy.get('li:contains("Hello 3")').should('have.length', 3)

    cy.get('ul > :nth-child(3) button').contains('Reset message').click()

    cy.get('li').should('have.length', 18)
    cy.get('li:contains("Hello 3")').should('not.exist')
  })

  it('reacts to ping deletion', () => {
    cy.mount(TestComponent)

    cy.get('li').should('have.length', 18)
    cy.get('li:contains("Hello 3")').should('have.length', 3)

    cy.get('ul > :nth-child(3) button').contains('Delete').click()

    cy.get('li').should('have.length', 15)
    cy.get('li:contains("Hello 3")').should('not.exist')

    cy.get('.spinner-border').should('not.exist')
  })

  it('reacts to ping creation', () => {
    cy.mount(TestComponent)

    cy.get('.spinner-border').should('not.exist')
    cy.get('li').should('have.length', 18)

    cy.get('button').contains('Ping').click()

    cy.get('li').should('have.length', 21)
  })

  it("allows use of 'auto.getOne' inside a 'computed'", async () => {
    const api = useApiStore()
    await api.auth.login('admin', 'password')

    let counter = 0
    const ping = computed(() => {
      counter += 1
      return api.auto.getOne('ping', '1')
    })

    expect(counter).to.equal(0)
    expect(ping.value.inCache).to.be.false
    expect(counter).to.equal(1)

    await ping.value.loaded

    expect(counter).to.equal(1)
    expectToBeTrue(ping.value.inCache)
    expectToBeTrue(ping.value.exists)
    expect(ping.value.attributes.message).to.equal('Hello 1')

    await ping.value.loaded

    expect(counter).to.equal(1)
    expect(ping.value.attributes.message).to.equal('Hello 1')

    await ping.value.loaded

    expect(counter).to.equal(1)
    expect(ping.value.attributes.message).to.equal('Hello 1')
  })

  it("makes sure 'getOne().inCache' is reactive", async () => {
    const api = useApiStore()

    const ping = api.cache.getOne('ping', '1')
    const inCache = computed(() => ping.inCache)
    let counter = 0
    watch(inCache, () => { counter += 1 })

    expect(counter).to.equal(0)

    await ping.refresh()

    expect(counter).to.equal(1)

    await ping.refresh()

    expect(counter).to.equal(1)

    await ping.refresh()

    expect(counter).to.equal(1)
  })

  it("makes sure 'getOne().loading' is reactive", async () => {
    const api = useApiStore()

    const ping = api.cache.getOne('ping', '1')
    const loading = computed(() => ping.loading)
    let counter = 0
    watch(loading, () => { counter += 1 })

    expect(counter).to.equal(0)

    await ping.refresh()

    expect(counter).to.equal(2)

    await ping.refresh()

    expect(counter).to.equal(4)

    await ping.refresh()

    expect(counter).to.equal(6)
  })

  it("makes sure 'getOne().exists' is reactive", async () => {
    const api = useApiStore()

    const ping = api.cache.getOne('ping', '1')
    const exists = computed(() => ping.inCache && ping.exists)
    let counter = 0
    watch(exists, () => { counter += 1 })

    expect(counter).to.equal(0)

    await ping.refresh()

    expect(counter).to.equal(1)

    await ping.refresh()

    expect(counter).to.equal(1)

    await ping.refresh()

    expect(counter).to.equal(1)
  })

  it("makes sure 'getOne().attributes' is reactive", async () => {
    const api = useApiStore()

    const ping = api.cache.getOne('ping', '1')
    const attributes = computed(() => ping.inCache && ping.exists ? ping.attributes : null)
    let counter = 0
    watch(attributes, () => { counter += 1 })

    expect(counter).to.equal(0)

    await ping.refresh()

    expect(counter).to.equal(1)

    await ping.refresh()

    expect(counter).to.equal(2)

    await ping.refresh()

    expect(counter).to.equal(3)
  })

  it("makes sure 'getOne().relationships' is reactive", async () => {
    const api = useApiStore()

    const ping = api.cache.getOne('ping', '1')
    const relationships = computed(() => ping.inCache && ping.exists ? ping.relationships : null)
    let counter = 0
    watch(relationships, () => { counter += 1 })

    expect(counter).to.equal(0)

    await ping.refresh()

    expect(counter).to.equal(1)

    await ping.refresh()

    expect(counter).to.equal(2)

    await ping.refresh()

    expect(counter).to.equal(3)
  })

  it("allows use of 'auto.getAll' inside a 'computed'", async () => {
    const api = useApiStore()
    await api.auth.login('admin', 'password')

    let counter = 0
    const pings = computed(() => {
      counter += 1
      return api.auto.getAll('ping', {filters: {message: 'Hello 1'}})
    })

    expect(counter).to.equal(0)
    expect(pings.value.items).to.have.length(0)
    expect(counter).to.equal(1)

    await pings.value.fullyLoaded

    expect(counter).to.equal(1)
    expect(pings.value.items).to.have.length(1)

    await pings.value.fullyLoaded

    expect(counter).to.equal(1)
    expect(pings.value.items).to.have.length(1)

    await pings.value.fullyLoaded

    expect(counter).to.equal(1)
    expect(pings.value.items).to.have.length(1)
  })

  it("makes sure 'getAll().inCache' is reactive", async () => {
    const api = useApiStore()

    const pings = api.cache.getAll('ping')
    const inCache = computed(() => pings.inCache)
    let counter = 0
    watch(inCache, () => { counter += 1 })

    expect(counter).to.equal(0)

    await pings.refresh()

    expect(counter).to.equal(1)

    await pings.refresh()

    expect(counter).to.equal(1)

    await pings.refresh()

    expect(counter).to.equal(1)
  })

  it("makes sure 'getAll().loading' is reactive", async () => {
    const api = useApiStore()

    const pings = api.cache.getAll('ping')
    const loading = computed(() => pings.loading)
    let counter = 0
    watch(loading, () => { counter += 1 })

    expect(counter).to.equal(0)

    await pings.refresh()

    expect(counter).to.equal(2)

    await pings.refresh()

    expect(counter).to.equal(4)

    await pings.refresh()

    expect(counter).to.equal(6)
  })

  it("makes sure 'getAll().items' is reactive", async () => {
    const api = useApiStore()

    const pings = api.cache.getAll('ping')
    const items = computed(() => pings.items)
    let counter = 0
    watch(items, () => { counter += 1 })

    expect(counter).to.equal(0)

    await pings.refresh()

    expect(counter).to.equal(3)

    await pings.refresh()

    expect(counter).to.equal(6)

    await pings.refresh()

    expect(counter).to.equal(9)
  })
})

describe('ApiStore - Authentication', () => {
  before(console.clear)

  beforeEach(() => {
    cy.request('POST', 'http://fanout:8080/reset-for-tests/yes-im-sure?fixtures=admin-user,test-pings')

    resetApiStores()
  })

  it('logs in and out', async () => {
    const api = useApiStore()

    const loggedOut1 = await api.client.createOne('ping', {}, {})
    expectToBeTrue(loggedOut1.exists)
    expect(loggedOut1.relationships.createdBy).to.be.null

    expect(api.auth.isAuthenticated.value).to.be.false

    expect(await api.auth.login('admin', 'password')).to.be.true

    expect(api.auth.isAuthenticated.value).to.be.true

    const loggedIn = await api.client.createOne('ping', {}, {})
    expectToBeTrue(loggedIn.exists)
    expectToNotBeNull(loggedIn.relationships.createdBy)
    expect(loggedIn.relationships.createdBy.type).to.equal('user')
    expect(loggedIn.relationships.createdBy.id).to.equal('fvirvd')
    expect(loggedIn.relationships.createdBy.inCache).to.be.false

    api.auth.logout()

    expect(api.auth.isAuthenticated.value).to.be.false

    const loggedOut2 = await api.client.createOne('ping', {}, {})
    expectToBeTrue(loggedOut2.exists)
    expect(loggedOut2.relationships.createdBy).to.be.null
  })

  it('sets token and logs out', async () => {
    const api = useApiStore()

    const loggedOut1 = await api.client.createOne('ping', {}, {})
    expectToBeTrue(loggedOut1.exists)
    expect(loggedOut1.relationships.createdBy).to.be.null

    expect(api.auth.isAuthenticated.value).to.be.false

    api.auth.setToken('unused-token')

    expect(api.auth.isAuthenticated.value).to.be.true

    api.auth.logout()

    expect(api.auth.isAuthenticated.value).to.be.false
  })

  it('fails to login', async () => {
    const api = useApiStore()

    expect(await api.auth.login('admin', 'not-the-password')).to.be.false
    expect(api.auth.isAuthenticated.value).to.be.false

    expect(await api.auth.login('not-the-admin', 'password')).to.be.false
    expect(api.auth.isAuthenticated.value).to.be.false
  })

  it('clears items cache on logout', async () => {
    const api = useApiStore()

    await api.auth.login('admin', 'password')

    const before = await api.client.getOne('ping', '1')

    expect(before.inCache).to.be.true

    api.auth.logout()

    expect(before.inCache).to.be.false

    const during = api.cache.getOne('ping', '1')

    expect(during).to.equal(before)

    await before.refresh()

    expect(before.inCache).to.be.true

    await api.auth.login('admin', 'password')

    const after = api.cache.getOne('ping', '1')

    expect(after).to.equal(before)

    expect(before.inCache).to.be.false

    await before.refresh()

    expect(before.inCache).to.be.true
  })

  it('clears lists cache on logout', async () => {
    const api = useApiStore()

    await api.auth.login('admin', 'password')

    const before = await api.client.getAll('ping')

    expect(before.inCache).to.be.true

    api.auth.logout()

    expect(before.inCache).to.be.false

    const during = api.cache.getAll('ping')

    expect(during).to.equal(before)

    await before.refresh()

    expect(before.inCache).to.be.true

    await api.auth.login('admin', 'password')

    const after = api.cache.getAll('ping')

    expect(after).to.equal(before)

    expect(before.inCache).to.be.false

    await before.refresh()

    expect(before.inCache).to.be.true
  })

  it('anticipates token expiration', async () => {
    const api = useApiStore()

    expect(await api.auth.login('admin', 'password', {validity: "PT2S", expiresSoonMargin: 1000, logoutMargin: 500})).to.be.true

    expect(api.auth.isAuthenticated.value).to.be.true
    expect(api.auth.expiresSoon.value).to.be.false

    await new Promise(resolve => setTimeout(resolve, 1100))

    expect(api.auth.isAuthenticated.value).to.be.true
    expect(api.auth.expiresSoon.value).to.be.true

    expect(await api.auth.login('admin', 'password', {validity: "PT2S", expiresSoonMargin: 1000, logoutMargin: 500})).to.be.true

    expect(api.auth.isAuthenticated.value).to.be.true
    expect(api.auth.expiresSoon.value).to.be.false

    await new Promise(resolve => setTimeout(resolve, 1100))

    expect(api.auth.isAuthenticated.value).to.be.true
    expect(api.auth.expiresSoon.value).to.be.true

    await new Promise(resolve => setTimeout(resolve, 500))

    expect(api.auth.isAuthenticated.value).to.be.false
    expect(api.auth.expiresSoon.value).to.be.true
  })

  it('stores authentication token in local storage', async () => {
    const api1 = useApiStore()

    expect(await api1.auth.login('admin', 'password')).to.be.true
    expect(api1.auth.isAuthenticated.value).to.be.true

    resetApiStores()

    const api2 = useApiStore()
    expect(api2.cache).to.not.equal(api1.cache)
    expect(api2.auth.isAuthenticated.value).to.be.true
  })
})

describe('ApiStore - Application - 1', () => {
  before(console.clear)

  beforeEach(() => {
    resetApiStores()
    cy.request('POST', 'http://fanout:8080/reset-for-tests/yes-im-sure?fixtures=test-exercises')
  })

  it('gets all textbooks and sections', async () => {
    const api = useApiStore()
    await api.auth.login('admin', 'password')

    expect(api.cache.getOne('textbook', 'klxufv').inCache).to.be.false

    const textbooks = await api.client.getAll('textbook')
    expect(textbooks.items.length).to.equal(1)
    expectToBeTrue(textbooks.items[0].exists)
    expect(textbooks.items[0].attributes.title).to.equal('Français CE2')

    expect(api.cache.getOne('textbook', '0').inCache).to.be.false
    const textbook = api.cache.getOne('textbook', 'klxufv')
    expectToBeTrue(textbook.inCache)
    expectToBeTrue(textbook.exists)
    expect(textbook.attributes.title).to.equal('Français CE2')
    expect(textbook.relationships.sections[0].inCache).to.be.false

    await api.client.getAll('section')

    expectToBeTrue(textbook.relationships.sections[0].inCache)
    expectToBeTrue(textbook.relationships.sections[0].exists)
    expect(textbook.relationships.sections[0].attributes.textbookStartPage).to.equal(6)
  })

  it('gets one textbook and its sections', async () => {
    const api = useApiStore()
    await api.auth.login('admin', 'password')

    expect(api.cache.getOne('textbook', 'klxufv').inCache).to.be.false

    const textbook = await api.client.getOne('textbook', 'klxufv', {include: ['sections']})
    expectToBeTrue(textbook.exists)
    expect(textbook.attributes.title).to.equal('Français CE2')
    expectToBeTrue(textbook.relationships.sections[0].inCache)
    expectToBeTrue(textbook.relationships.sections[0].exists)
    expect(textbook.relationships.sections[0].attributes.textbookStartPage).to.equal(6)
  })

  it('keeps single included', async () => {
    const api = useApiStore()
    await api.auth.login('admin', 'password')

    await api.client.getAll('textbook', {include: ['sections']})

    const textbook = api.cache.getOne('textbook', 'klxufv')
    expectToBeTrue(textbook.inCache)
    expectToBeTrue(textbook.exists)
    expectToBeTrue(textbook.relationships.sections[0].inCache)
    expectToBeTrue(textbook.relationships.sections[0].exists)
    expect(textbook.relationships.sections[0].attributes.textbookStartPage).to.equal(6)
  })

  it('keeps deep included', async () => {
    const api = useApiStore()
    await api.auth.login('admin', 'password')

    await api.client.getAll('textbook', {include: ['sections.pdfFile.namings']})

    const textbook = api.cache.getOne('textbook', 'klxufv')
    expectToBeTrue(textbook.inCache)
    expectToBeTrue(textbook.exists)
    expectToBeTrue(textbook.relationships.sections[0].inCache)
    expectToBeTrue(textbook.relationships.sections[0].exists)
    expectToBeTrue(textbook.relationships.sections[0].relationships.pdfFile.inCache)
    expectToBeTrue(textbook.relationships.sections[0].relationships.pdfFile.exists)
    expectToBeTrue(textbook.relationships.sections[0].relationships.pdfFile.relationships.namings[0].inCache)
    expectToBeTrue(textbook.relationships.sections[0].relationships.pdfFile.relationships.namings[0].exists)
    expect(textbook.relationships.sections[0].relationships.pdfFile.relationships.namings[0].attributes.name).to.equal('test.pdf')
  })

  it('keeps multiple included', async () => {
    const api = useApiStore()
    await api.auth.login('admin', 'password')

    await api.client.getAll('section', {include: ['textbook', 'pdfFile.namings']})

    const section = api.cache.getOne('section', 'eyjahd')
    expectToBeTrue(section.inCache)
    expectToBeTrue(section.exists)
    expectToBeTrue(section.relationships.textbook.inCache)
    expectToBeTrue(section.relationships.textbook.exists)
    expect(section.relationships.textbook.attributes.title).to.equal('Français CE2')
    expectToBeTrue(section.relationships.pdfFile.inCache)
    expectToBeTrue(section.relationships.pdfFile.exists)
    expectToBeTrue(section.relationships.pdfFile.relationships.namings[0].inCache)
    expectToBeTrue(section.relationships.pdfFile.relationships.namings[0].exists)
    expect(section.relationships.pdfFile.relationships.namings[0].attributes.name).to.equal('test.pdf')
  })

  it('paginates exercises', async () => {
    const api = useApiStore()
    await api.auth.login('admin', 'password')

    const exercises = await api.client.getAll('exercise')

    expect(exercises.items.length).to.equal(6)
  })

  it('filters exercises by textbook and page', async () => {
    const api = useApiStore()
    await api.auth.login('admin', 'password')

    expect((await api.client.getAll('exercise')).items.length).to.equal(6)
    expect((await api.client.getAll('exercise', {filters: {textbook: 'klxufv'}})).items.length).to.equal(3)
    expect((await api.client.getAll('exercise', {filters: {textbook: 'klxufv', textbookPage: 6}})).items.length).to.equal(2)
    expect((await api.client.getAll('exercise', {filters: {textbook: 'klxufv', textbookPage: 7}})).items.length).to.equal(1)
  })

  it('creates a new exercise', async () => {
    const api = useApiStore()
    await api.auth.login('admin', 'password')

    expect((await api.client.getAll('exercise', {filters: {textbook: 'klxufv', textbookPage: 6}})).items.length).to.equal(2)

    expect(api.cache.getOne('textbook', 'klxufv').inCache).to.be.false

    const newExercise = await api.client.createOne(
      'exercise',
      {
        textbookPage: 6, number: '14',
        instructions: 'Do this',
        boundingRectangle: {start: {x: 0, y: 1}, stop: {x: 2, y: 3}},
      },
      {
        project: api.cache.getOne('project', 'xkopqm'),
        textbook: api.cache.getOne('textbook', 'klxufv'),
      },
    )

    expect(newExercise.id).to.equal('vodhqn')
    expectToBeTrue(newExercise.exists)
    expect(newExercise.attributes.instructions).to.equal('Do this')
    expect(newExercise.attributes.boundingRectangle).to.deep.equal({start: {x: 0, y: 1}, stop: {x: 2, y: 3}})

    expect(api.cache.getOne('textbook', 'klxufv').inCache).to.be.false

    expect((await api.client.getAll('exercise', {filters: {textbook: 'klxufv', textbookPage: 6}})).items.length).to.equal(3)
  })

  it('creates a new exercise and retrieves its textbook', async () => {
    const api = useApiStore()
    await api.auth.login('admin', 'password')

    expect((await api.client.getAll('exercise', {filters: {textbook: 'klxufv', textbookPage: 6}})).items.length).to.equal(2)

    const textbook = api.cache.getOne('textbook', 'klxufv')

    expect(textbook.inCache).to.be.false

    const newExercise = await api.client.createOne(
      'exercise',
      {
        textbookPage: 6, number: '14',
        instructions: 'Do that',
      },
      {
        project: api.cache.getOne('project', 'xkopqm'),
        textbook: textbook,
      },
      {
        include: ['textbook']
      },
    )

    expect(newExercise.id).to.equal('vodhqn')
    expectToBeTrue(newExercise.exists)
    expect(newExercise.attributes.instructions).to.equal('Do that')

    expectToBeTrue(textbook.inCache)
    expectToBeTrue(textbook.exists)
    expect(textbook.attributes.title).to.equal('Français CE2')

    expect((await api.client.getAll('exercise', {filters: {textbook: 'klxufv', textbookPage: 6}})).items.length).to.equal(3)
  })

  it('updates an exercise', async () => {
    const api = useApiStore()
    await api.auth.login('admin', 'password')

    const updatedExercise = api.cache.getOne('exercise', 'wbqloc')
    await updatedExercise.patch({instructions: 'Do that'}, {})

    expectToBeTrue(updatedExercise.inCache)
    expectToBeTrue(updatedExercise.exists)
    expect(updatedExercise.attributes.instructions).to.equal('Do that')
  })

  it('updates an exercise and retrieves its textbook', async () => {
    const api = useApiStore()
    await api.auth.login('admin', 'password')

    const textbook = api.cache.getOne('textbook', 'klxufv')
    expect(textbook.inCache).to.be.false

    const updatedExercise = api.cache.getOne('exercise', 'wbqloc')
    await updatedExercise.patch(
      {instructions: 'Do that'},
      {},
      {include: ['textbook']},
    )

    expectToBeTrue(updatedExercise.inCache)
    expectToBeTrue(updatedExercise.exists)
    expect(updatedExercise.attributes.instructions).to.equal('Do that')

    expectToBeTrue(textbook.inCache)
    expectToBeTrue(textbook.exists)
    expect(textbook.attributes.title).to.equal('Français CE2')
  })

  it('deletes an exercise', async () => {
    const api = useApiStore()
    await api.auth.login('admin', 'password')

    const exercise = api.cache.getOne('exercise', 'wbqloc')

    expect(exercise.inCache).to.be.false

    await exercise.delete()

    expectToBeTrue(exercise.inCache)
    expect(exercise.exists).to.be.false
    expect((await api.client.getAll('exercise', {filters: {textbook: 'klxufv', textbookPage: 6}})).items.length).to.equal(1)
  })
})

describe('ApiStore - Application - 2', () => {
  before(console.clear)

  beforeEach(() => {
    resetApiStores()
    const api = useApiStore()

    cy.request('POST', 'http://fanout:8080/reset-for-tests/yes-im-sure?fixtures=more-test-exercises')
      .then(() => api.auth.login('admin', 'password'))
  })

  it('gets an exercise without an adaptation', async () => {
    const api = useApiStore()

    const exercise = await api.client.getOne('exercise', 'bylced', {include: ['adaptation']})

    expectToBeTrue(exercise.exists)
    expect(exercise.attributes.instructions).to.equal('Écris une phrase en respectant l\'ordre des classes grammaticales indiquées.')
    expect(exercise.relationships.adaptation).to.be.null
  })

  it('gets an exercise with "select things" adaptation', async () => {
    const api = useApiStore()

    const exercise = await api.client.getOne('exercise', 'vodhqn', {include: ['adaptation']})

    expectToBeTrue(exercise.exists)
    expect(exercise.attributes.instructions).to.equal('Relève dans le texte trois\n{sel1|déterminants}, un {sel2|nom propre}, quatre\n{sel3|noms communs} et trois {sel4|verbes}.')
    expectToNotBeNull(exercise.relationships.adaptation)
    expect(exercise.relationships.adaptation.type).to.equal('selectThingsAdaptation')
    expect(exercise.relationships.adaptation.id).to.equal('fojjim')
    console.assert(exercise.relationships.adaptation.type === 'selectThingsAdaptation')
    const typed_adaptation = exercise.relationships.adaptation as SelectThingsAdaptation
    expectToBeTrue(typed_adaptation.inCache)
    expectToBeTrue(typed_adaptation.exists)
    expect(typed_adaptation.attributes.colors).to.equal(4)
  })

  it('gets an exercise with "fill with free text" adaptation', async () => {
    const api = useApiStore()

    const exercise = await api.client.getOne('exercise', 'dymwin', {include: ['adaptation']})

    expectToBeTrue(exercise.exists)
    expect(exercise.attributes.instructions).to.equal('Ajoute le suffixe –eur aux verbes.\nIndique la classe des mots fabriqués.')
    expectToNotBeNull(exercise.relationships.adaptation)
    expect(exercise.relationships.adaptation.type).to.equal('fillWithFreeTextAdaptation')
    const typed_adaptation = exercise.relationships.adaptation as FillWithFreeTextAdaptation
    expectToBeTrue(typed_adaptation.inCache)
    expectToBeTrue(typed_adaptation.exists)
    expect(typed_adaptation.attributes.placeholder).to.equal('…')
  })

  it('creates an exercise and its adaptation at once', async () => {
    const api = useApiStore()
    await api.auth.login('admin', 'password')

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
          'project': {type: 'project', id: 'xkopqm'},
          'textbook': {type: 'textbook', id: 'klxufv'},
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
    await exercise.refresh()

    expect(exercise.relationships.adaptation.type).to.equal('selectThingsAdaptation')
    expect(exercise.relationships.adaptation.attributes.colors).to.equal(5)
  })

  it('updates an adaptation', async () => {
    const api = useApiStore()

    const adaptation = api.cache.getOne('selectThingsAdaptation', 'fojjim')
    await adaptation.patch({colors: 17}, {})

    expectToBeTrue(adaptation.inCache)
    expectToBeTrue(adaptation.exists)
    expect(adaptation.attributes.colors).to.equal(17)
  })

  it('changes the type of an adaptation', async () => {
    const api = useApiStore()

    const previous = await api.client.getOne('selectThingsAdaptation', 'fojjim')
    expectToBeTrue(previous.exists)
    expect(previous.relationships.exercise.id).to.equal('vodhqn')

    const adaptation = await api.client.createOne('fillWithFreeTextAdaptation', {placeholder: '...'}, {exercise: previous.relationships.exercise}, {include: ['exercise']})

    expectToBeTrue(adaptation.exists)
    expect(adaptation.attributes.placeholder).to.equal('...')
    expectToBeTrue(adaptation.relationships.exercise.inCache)
    expectToBeTrue(adaptation.relationships.exercise.exists)
    expect(adaptation.relationships.exercise.attributes.instructions).to.equal('Relève dans le texte trois\n{sel1|déterminants}, un {sel2|nom propre}, quatre\n{sel3|noms communs} et trois {sel4|verbes}.')

    await previous.refresh()
    expect(previous.exists).to.be.false
  })
})
