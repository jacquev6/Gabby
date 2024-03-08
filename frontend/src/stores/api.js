import { reactive } from 'vue'
import { defineStore } from 'pinia'


export function defineApiStore(name, options) {
  const baseUrl = (options && options.baseUrl) || '/api/'
  const headers = {'Content-Type': 'application/vnd.api+json'}

  return defineStore(name, () => {
    const attributesCache = reactive({})
    const relationshipsCache = reactive({})

    function makeUrl(path, options) {
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
      return `${baseUrl}${path}?${params.toString()}`
    }

    function makeRelationships(relationships_) {
      const relationships = {}
      for (const [key, value] of Object.entries(relationships_)) {
        if (value) {
          if (Array.isArray(value)) {
            relationships[key] = {data: value.map(item => ({type: item.type, id: item.id}))}
          } else {
            relationships[key] = {data: {type: value.type, id: value.id}}
          }
        } else {
          relationships[key] = {data: null}
        }
      }
      return relationships
    }

    async function request(method, url, json_body) {
      const body = json_body ? JSON.stringify(json_body) : null
      const raw_response = await fetch(url, {method, headers, body})
      const json_response = raw_response.headers.get('Content-Type') == 'application/vnd.api+json' ? await raw_response.json() : null
      if (raw_response.ok) {
        if (json_response) {
          return handle_response(json_response)
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
    }

    function handle_response(response) {
      if (Array.isArray(response.data)) {
        for (const item of response.data) {
          update_item(item)
        }
      } else {
        update_item(response.data)
      }
      if (Array.isArray(response.included)) {
        for (const item of response.included) {
          update_item(item)
        }
      }
      return response
    }

    function update_item(item) {
      if (!attributesCache[item.type]) {
        attributesCache[item.type] = {}
        relationshipsCache[item.type] = {}
      }
      attributesCache[item.type][item.id] = item.attributes
      relationshipsCache[item.type][item.id] = item.relationships
    }

    function cacheHas(type, id) {
      return !!attributesCache[type]?.[id]
    }

    function get(itemId) {
      const type = itemId.type
      const id = itemId.id
      return {
        type,
        id,
        get attributes() {
          if (cacheHas(type, id)) {
            return attributesCache[type][id]
          } else {
            throw new Error(`${type} ${id} not in cache`)
          }
        },
        get relationships() {
          if (cacheHas(type, id)) {
            const relationships = {}
            for (const relationship of Object.keys(relationshipsCache[type][id])) {
              const data = relationshipsCache[type][id][relationship].data
              if (data === null) {
                relationships[relationship] = null
              } else if (Array.isArray(data)) {
                relationships[relationship] = []
                for (const relationId of data) {
                  relationships[relationship].push(get(relationId))
                }
              } else {
                relationships[relationship] = get(data)
              }
            }
            return relationships
          } else {
            throw new Error(`${type} ${id} not in cache`)
          }
        },
      }
    }

    return {
      client: {
        get_all: async function(path, options) {
          let url = makeUrl(path, options)
          const got = []
          while (url) {
            const response = await request('GET', url)
            for (const item of response.data) {
              got.push(get(item))
            }
            url = response.links?.next
          }
          return got
        },
        get_one: async function(type, id, options) {
          const response = await request('GET', makeUrl(`${type}s/${id}`, options))
          if (response) {
            return get(response.data)
          } else {
            throw new Error(`${type} ${id} does not exist`)
          }
        },
        try_get_one: async function(type, id, options) {
          const response = await request('GET', makeUrl(`${type}s/${id}`, options))
          if (response) {
            return get(response.data)
          } else {
            return null
          }
        },
        post: async function(type, attributes, relationships, options) {
          const payload = {data: {
            type,
            attributes,
            relationships: makeRelationships(relationships)
          }}
          const response = await request('POST', makeUrl(`${type}s`, options), payload)
          return get(response.data)
        },
        patch: async function(type, id, attributes, relationships, options) {
          const payload = {data: {
            type,
            id,
            attributes,
            relationships: makeRelationships(relationships),
          }}
          const response = await request('PATCH', makeUrl(`${type}s/${id}`, options), payload)
          return get(response.data)
        },
        delete: async function(type, id) {
          await request('DELETE', makeUrl(`${type}s/${id}`))
          if (attributesCache[type]) {
            attributesCache[type][id] = null
          }
        }
      },
      cache: {
        try_get_one: function(type, id) {
          if (cacheHas(type, id)) {
            return get({type, id})
          } else {
            return null
          }
        },
        get_one: function(type, id) {
          if (cacheHas(type, id)) {
            return get({type, id})
          } else {
            throw new Error(`${type} ${id} not in cache`)
          }
        },
      },
    }
  })
}

export const useApiStore = defineApiStore('api')
