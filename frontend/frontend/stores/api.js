import { defineStore } from 'pinia'
import _ from 'lodash'


// item.inCache: whether the item has ever been retrieved from the API
// item.exists: whether the item exists in the API
// The following cases are possible:
// - {inCache: true, exists: true}: e.g. after a successful get
// - {inCache: true, exists: false}: e.g. after a 404 get or a delete
// - {inCache: false, exists: undefined}: e.g. after a get from cache of a never-heard-of item
// - {inCache: false, exists: true}: e.g. after a get that returned this item in 'relationships' but not in 'included'
// The case {inCache: false, exists: false} is impossible.

export function defineApiStore(name, options) {
  const promises = {}
  const refreshQueued = {}

  const useCache = defineStore(name, {
    state: () => ({
      _items: {},
      _lists: {},
      _baseUrl: (options && options.baseUrl) || '/api/',
    }),
    getters: {},
    actions: {
      getAll(path, options) {
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
                  refreshQueued[mainUrl] = false
                  const got = []
                  let url = mainUrl
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
                promises[mainUrl] = null
              })()
            }
            await promises[mainUrl]
          }
        }
        return this._lists[mainUrl]
      },
      getOne(type, id) {
        this._items[type] = this._items[type] ?? {}
        if (!this._items[type][id]) {
          const cache = this
          this._items[type][id] = {
            type,
            id,
            inCache: false,
            get relationships() {
              if (this._relationships) {
                const relationships = {}
                for (const [name, relationship] of Object.entries(this._relationships)) {
                  if (relationship.data === null) {
                    relationships[name] = null
                  } else if (Array.isArray(relationship.data)) {
                    relationships[name] = []
                    for (const relation of relationship.data) {
                      relationships[name].push(cache.getOne(relation.type, relation.id))
                    }
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
      _updateOne({type, id, attributes, relationships}) {
        const item = this.getOne(type, id)
        item.inCache = true
        item.exists = true
        item.attributes = attributes
        item._relationships = relationships
        for (const relationship of Object.values(relationships)) {
          if (Array.isArray(relationship.data)) {
            for (const relation of relationship.data) {
              this.getOne(relation.type, relation.id).exists = true
            }
          } else if (relationship.data) {
            this.getOne(relationship.data.type, relationship.data.id).exists = true
          }
        }
      },
      _deleteOne(type, id) {
        const item = this.getOne(type, id)
        item.inCache = true
        item.exists = false
        item.attributes = undefined
        item._relationships = undefined
        for (const list of Object.values(this._lists)) {
          _.remove(list, item => item.type == type && item.id == id)
        }
      },
      _makeUrl(path, options) {
        const params = new URLSearchParams()
        if (options?.include) {
          // This obviously works for a single string,
          // and fortunately for a list of strings: it adds them comma-separated
          params.append('include', options.include)
        }
        if (options?.filter) {
          for (const [key, value] of Object.entries(options.filter)) {
            params.append(`filter[${key}]`, value)
          }
        }
        return `${this._baseUrl}${path}?${params.toString()}`
      },
      _makeRelationships(relationships_) {
        const relationships = {}
        for (const [key, value] of Object.entries(relationships_)) {
          if (value) {
            if (Array.isArray(value)) {
              relationships[key] = {data: value.map(item => ({type: item.type, id: item.id, lid: item.lid}))}
            } else {
              relationships[key] = {data: {type: value.type, id: value.id, lid: value.lid}}
            }
          } else {
            relationships[key] = {data: null}
          }
        }
        return relationships
      },
      async _request(method, url, json_body) {
        const body = json_body ? JSON.stringify(json_body) : null
        const raw_response = await fetch(url, {method, headers: {'Content-Type': 'application/vnd.api+json'}, body})
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
      _handleResponse(response) {
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

    const client = {
      async getAll(path, options) {
        const ret = cache.getAll(path, options)
        await ret.refresh()
        return ret
      },
      async getOne(type, id, options) {
        const response = await cache._request('GET', cache._makeUrl(`${type}s/${id}`, options))
        if (!response) {
          cache._deleteOne(type, id)
        }
        return cache.getOne(type, id)
      },
      async post(type, attributes, relationships, options) {
        const payload = {data: {
          type,
          attributes,
          relationships: cache._makeRelationships(relationships)
        }}
        const response = await cache._request('POST', cache._makeUrl(`${type}s`, options), payload)
        return cache.getOne(type, response.data.id)
      },
      async patch(type, id, attributes, relationships, options) {
        const payload = {data: {
          type,
          id,
          attributes,
          relationships: cache._makeRelationships(relationships),
        }}
        await cache._request('PATCH', cache._makeUrl(`${type}s/${id}`, options), payload)
        return cache.getOne(type, id)
      },
      async delete(type, id) {
        await cache._request('DELETE', cache._makeUrl(`${type}s/${id}`))
        cache._deleteOne(type, id)
      },
      async batch() {
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

        const raw_response = await fetch(url, {method: 'POST', headers: {'Content-Type': 'application/vnd.api+json'}, body: JSON.stringify({'atomic:operations': operations})})
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
          console.error({request: {method, url, json_body, body}, response})
          throw new Error('API request failed', {cause: response})
        }
      },
    }

    const auto = {
      getAll(path, options) {
        const ret = cache.getAll(path, options)
        ret.refresh()
        return ret
      },
      // @todo api.auto.getOne
    }

    return {cache, client, auto}
  }
}

export const useApiStore = defineApiStore('api')
