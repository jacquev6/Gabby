import { computed, ref } from 'vue'

import { defineStore } from 'pinia'
import _ from 'lodash'


interface GenericAttributes {
  [key: string]: any/* Type depends on actual server API. @todo Use 'unknown' instead. */
}

interface ItemId {
  type: string
  id: string
}

interface ItemLid {
  type: string
  lid: string
}

interface CachedItem {
  inCache: boolean  // Whether the item has ever been retrieved from the API
  exists?: boolean  // Whether the item exists in the API
  // The following cases are possible:
  // - {inCache: true, exists: true}: e.g. after a successful get
  // - {inCache: true, exists: false}: e.g. after a 404 get or a delete
  // - {inCache: false, exists: undefined}: e.g. after a get from cache of a never-heard-of item
  // - {inCache: false, exists: true}: e.g. after a get that returned this item in 'relationships' but not in 'included'
  // The case {inCache: false, exists: false} is impossible.
}

interface GenericInterfaceRelationships<T> {
  [key: string]: null | T | T[]
}

interface GenericItem extends ItemId, CachedItem {
  attributes?: GenericAttributes
  relationships?: GenericInterfaceRelationships<GenericItem>
}

export interface Item<
  Attributes extends GenericAttributes,
  RelationShips extends GenericInterfaceRelationships<GenericItem>
> extends GenericItem {
  attributes?: Attributes
  relationships?: RelationShips
}

// @todo Do not extend 'Array': we just want a read-only, iterable and indexable object
interface List<ItemType> extends Array<Required<ItemType>> {
  loading: boolean
  refresh: () => Promise<void>
}

interface WireRequestRelationships {
  [key: string]: {data: null | ItemId | ItemLid | (ItemId | ItemLid)[]}
}

interface WireResponseRelationships {
  [key: string]: {data: null | ItemId | ItemId[]}
}

interface ItemInCache extends GenericItem {
  _relationships?: WireResponseRelationships
}

interface ItemListInCache extends Array<ItemInCache> {
  loading?: boolean
  refresh?: () => Promise<void>
}

type Path = string

type Url = string

interface Options {
  include?: string | string[]
  filter?: {[key: string]: string}
}

export function defineApiStore(name: string, options?: {baseUrl?: string}) {
  const promises: {[url: Url]: Promise<void> | undefined} = {}
  const refreshQueued: {[url: Url]: true | undefined} = {}

  const useCache = defineStore(name, {
    state: () => ({
      _items: {} as {[type: string]: {[id: string]: ItemInCache}},
      _lists: {} as {[url: Url]: ItemListInCache},
      _baseUrl: (options && options.baseUrl) || '/api/',
      _authentication: null as null | {
        header: string,
        validUntil: Date | null,
      }
    }),
    getters: {},
    actions: {
      getAll<ItemType extends GenericItem=GenericItem>(path: Path, options?: Options) {
        return this._getAll(path, options) as List<ItemType>
      },
      _getAll(path: Path, options?: Options) {
        const mainUrl = this._makeUrl(path, options)
        if (!this._lists[mainUrl]) {
          this._lists[mainUrl] = []
          const ret = this._lists[mainUrl]
          ret.loading = false
          ret.refresh = async () => {
            refreshQueued[mainUrl] = true  // Ensure the last call to .refresh() is honored
            if (!promises[mainUrl]) {
              promises[mainUrl] = (async () => {
                ret.loading = true
                while (refreshQueued[mainUrl]) {
                  delete refreshQueued[mainUrl]
                  const got = []
                  let url: Url | null = mainUrl
                  while (url) {
                    const response = await this._request('GET', url)
                    if (response) {
                      for (const item of response?.data) {
                        got.push(this.getOne(item.type, item.id))
                      }
                      url = response.links.next
                    } else {
                      // Previous response.links.next was invalid (maybe because items were deleted concurrently?)
                      url = null
                    }
                  }
                  // await new Promise(r => setTimeout(r, 1000))
                  ret.splice(0, ret.length, ...got)
                }
                ret.loading = false
                delete promises[mainUrl]
              })()
            }
            await promises[mainUrl]
          }
        }
        return this._lists[mainUrl]
      },
      getOne<ItemType extends GenericItem=GenericItem>(type: string, id: string) {
        return this._getOne(type, id) as ItemType
      },
      _getOne(type: string, id: string) {
        this._items[type] = this._items[type] ?? {}
        if (!this._items[type][id]) {
          const cache = this
          this._items[type][id] = {
            type,
            id,
            inCache: false,
            get relationships() {
              if (this._relationships) {
                const relationships: GenericInterfaceRelationships<GenericItem> = {}
                for (const [name, relationship] of Object.entries(this._relationships)) {
                  if (relationship.data === null) {
                    relationships[name] = null
                  } else if (Array.isArray(relationship.data)) {
                    const rel = []
                    for (const relation of relationship.data) {
                      rel.push(cache.getOne(relation.type, relation.id))
                    }
                    relationships[name] = rel
                  } else {
                    relationships[name] = cache.getOne(relationship.data.type, relationship.data.id)
                  }
                }
                return relationships
              } else {
                return undefined
              }
            },
          }
        }
        return this._items[type][id]
      },
      _updateOne({type, id, attributes, relationships}: {type: string, id: string, attributes: GenericAttributes, relationships: WireResponseRelationships}) {
        const item = this._getOne(type, id)
        item.inCache = true
        item.exists = true
        item.attributes = attributes
        item._relationships = relationships
        for (const relationship of Object.values(relationships ?? {})) {
          if (Array.isArray(relationship.data)) {
            for (const relation of relationship.data) {
              this.getOne(relation.type, relation.id).exists = true
            }
          } else if (relationship.data) {
            this.getOne(relationship.data.type, relationship.data.id).exists = true
          }
        }
      },
      _deleteOne(type: string, id: string) {
        const item = this._getOne(type, id)
        item.inCache = true
        item.exists = false
        item.attributes = undefined
        item._relationships = undefined
        for (const list of Object.values(this._lists)) {
          _.remove(list, item => item.type == type && item.id == id)
        }
      },
      _makeUrl(path: string, options?: Options) {
        const params = new URLSearchParams()
        if (options?.include) {
          params.append('include', typeof options.include === 'string' ? options.include : options.include.join(','))
        }
        if (options?.filter) {
          for (const [key, value] of Object.entries(options.filter)) {
            params.append(`filter[${key}]`, value)
          }
        }
        return `${this._baseUrl}${path}?${params.toString()}`
      },
      _makeRelationships(relationships_: GenericInterfaceRelationships<ItemId | ItemLid>) {
        const relationships: WireRequestRelationships = {}
        function make_id(item: ItemId | ItemLid) {
          return 'id' in item ? {type: item.type, id: item.id} : {type: item.type, lid: item.lid}
        }
        for (const [key, value] of Object.entries(relationships_)) {
          if (value) {
            if (Array.isArray(value)) {
              relationships[key] = {data: value.map(make_id)}
            } else {
              relationships[key] = {data: make_id(value)}
            }
          } else {
            relationships[key] = {data: null}
          }
        }
        return relationships
      },
      async _request(method: 'POST' | 'GET' | 'PATCH' | 'DELETE', url: Url, json_body?: object) {
        const body = json_body ? JSON.stringify(json_body) : null
        const headers: {[name: string]: string} = {'Content-Type': 'application/vnd.api+json'}
        if (this._authentication !== null) {
          headers['Authorization'] = this._authentication.header
        }
        const raw_response = await fetch(url, {method, headers, body})
        const json_response = raw_response.headers.get('Content-Type') == 'application/vnd.api+json' ? await raw_response.json() : null
        if (raw_response.ok) {
          if (json_response) {
            return this._handleResponse(json_response)
          } else {
            return null
          }
        } else if (raw_response.status == 404) {
          return null
        } else {
          const response = json_response ?? raw_response
          console.error({request: {method, url, json_body, body}, response})
          throw new Error('API request failed', {cause: response})
        }
      },
      _handleResponse(response: any/* @todo Type*/) {
        if (Array.isArray(response.data)) {
          for (const item of response.data) {
            this._updateOne(item)
          }
        } else {
          this._updateOne(response.data)
        }
        if (Array.isArray(response.included)) {
          for (const item of response.included) {
            this._updateOne(item)
          }
        }
        return response
      },
    },
  })

  return function() {
    const cache = useCache()

    const expiresSoon = ref(false)
    let expiresSoonTimeout: ReturnType<typeof setTimeout> | null = null
    const defaultExpiresSoonMargin = 15 * 60 * 1000
    let logoutTimeout: ReturnType<typeof setTimeout> | null = null
    const defaultLogoutMargin = 5 * 60 * 1000

    const auth = {
      isAuthenticated: computed(() => cache._authentication !== null),
      expiresSoon,
      async login(
        username: string,
        password: string,
        options = {
          validity: null as null | string,
          expiresSoonMargin: defaultExpiresSoonMargin,
          logoutMargin: defaultLogoutMargin,
        },
      ) {
        const body = new FormData()
        body.append('username', username)
        body.append('password', password)
        if (options.validity !== null) {
          body.append('options', JSON.stringify({validity: options.validity}))
        }
        const response = await fetch(cache._makeUrl('token'), {method: 'POST', body})
        if (response.ok) {
          const json_response = await response.json()
          this._setAuth(json_response.access_token, new Date(json_response.valid_until), options.expiresSoonMargin, options.logoutMargin)
          return true
        } else {
          this.logout()
          return false
        }
      },
      _setAuth(accessToken: string, validUntil: Date, expiresSoonMargin: number, logoutMargin: number) {
        cache._authentication = {header: 'Bearer ' + accessToken, validUntil}
        localStorage.setItem('auth-v1', JSON.stringify({accessToken, validUntil}))
        expiresSoon.value = false
        if (expiresSoonTimeout !== null) {
          clearTimeout(expiresSoonTimeout)
        }
        if (logoutTimeout !== null) {
          clearTimeout(logoutTimeout)
        }
        const validFor = (validUntil.getTime() - Date.now())
        expiresSoonTimeout = setTimeout(() => { expiresSoon.value = true }, validFor - expiresSoonMargin)
        logoutTimeout = setTimeout(() => { this.logout() }, validFor - logoutMargin)
      },
      setToken(accessToken: string) {
        cache._authentication = {header: 'Bearer ' + accessToken, validUntil: new Date(0)}
      },
      logout() {
        cache._authentication = null
        localStorage.removeItem('auth-v1')
        // Clear cache to avoid accessing data got while logged-in
        cache._items = {}
        cache._lists = {}
      },
    }

    const stored = localStorage.getItem('auth-v1')
    if (stored !== null) {
      const {accessToken, validUntil} = JSON.parse(stored)
      auth._setAuth(accessToken, new Date(validUntil), defaultExpiresSoonMargin, defaultLogoutMargin)
    }

    const client = {
      async getAll<ItemType extends GenericItem=GenericItem>(path: string, options?: Options) {
        const ret = cache.getAll<ItemType>(path, options)
        await ret.refresh()
        return ret
      },
      async getOne<ItemType extends GenericItem=GenericItem>(type: string, id: string, options?: Options) {
        const response = await cache._request('GET', cache._makeUrl(`${type}s/${id}`, options))
        if (!response) {
          cache._deleteOne(type, id)
        }
        return cache.getOne<ItemType>(type, id)
      },
      async post<ItemType extends GenericItem=GenericItem>(type: string, attributes: GenericAttributes, relationships: GenericInterfaceRelationships<ItemId>, options?: Options) {
        const payload = {data: {
          type,
          attributes,
          relationships: cache._makeRelationships(relationships)
        }}
        const response = await cache._request('POST', cache._makeUrl(`${type}s`, options), payload)
        return cache.getOne<Required<ItemType>>(type, response.data.id)
      },
      async patch<ItemType extends GenericItem=GenericItem>(type: string, id: string, attributes: GenericAttributes, relationships: GenericInterfaceRelationships<ItemId>, options?: Options) {
        const payload = {data: {
          type,
          id,
          attributes,
          relationships: cache._makeRelationships(relationships),
        }}
        await cache._request('PATCH', cache._makeUrl(`${type}s/${id}`, options), payload)
        return cache.getOne<Required<ItemType>>(type, id)
      },
      async delete(type: string, id: string) {
        await cache._request('DELETE', cache._makeUrl(`${type}s/${id}`))
        cache._deleteOne(type, id)
      },
      async batch() {  // @todo Type
        const url = `${cache._baseUrl}batch`
        const operations = []

        for (const arg of arguments) {
          if (arg[0] == 'add') {
            console.assert(arg.length == 5)
            const [_, type, lid, attributes, relationships] = arg
            operations.push({
              op: 'add',
              data: {
                type,
                lid: lid || undefined,
                attributes,
                relationships: cache._makeRelationships(relationships),
              },
            })
          } else {
            console.assert(false)
          }
        }

        const json_body = {'atomic:operations': operations}
        const headers: {[name: string]: string} = {'Content-Type': 'application/vnd.api+json'}
        if (cache._authentication !== null) {
          headers['Authorization'] = cache._authentication.header
        }
        const raw_response = await fetch(url, {method: 'POST', headers, body: JSON.stringify(json_body)})
        const json_response = raw_response.headers.get('Content-Type') == 'application/vnd.api+json' ? await raw_response.json() : null
        if (raw_response.ok) {
          const results = []
          for (const result of json_response['atomic:results']) {
            cache._updateOne(result.data)
            results.push(cache.getOne(result.data.type, result.data.id))
          }
          return results
        } else {
          const response = json_response ?? raw_response
          console.error({request: {url, json_body}, response})
          throw new Error('API request failed', {cause: response})
        }
      },
    }

    const auto = {
      getAll<ItemType extends GenericItem=GenericItem>(path: string, options?: Options) {
        const ret = cache.getAll<ItemType>(path, options)
        ret.refresh()
        return ret
      },
      // @todo api.auto.getOne
    }

    return {auth, cache, client, auto}
  }
}

export const useApiStore = defineApiStore('api')
