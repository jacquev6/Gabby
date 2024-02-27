import { reactive } from 'vue'
import { defineStore } from 'pinia'

export function defineApiStore(name, options) {
  const baseUrl = (options && options.baseUrl) || '/api/'

  return defineStore(name, () => {
    const attributesCache = reactive({})
    const relationshipsCache = reactive({})

    function update(item) {
      if (!attributesCache[item.type]) {
        attributesCache[item.type] = {}
        relationshipsCache[item.type] = {}
      }
      attributesCache[item.type][item.id] = item.attributes
      relationshipsCache[item.type][item.id] = item.relationships
    }

    function get(itemId) {
      const type = itemId.type
      const id = itemId.id
      const attributes = attributesCache[type]?.[id]
      if (!attributes) {
        return null
      } else {
        return {
          type,
          id,
          attributes,
          get relationships() {
            const relationships = {}
            for (const relationship of Object.keys(relationshipsCache[type][id])) {
              const data = relationshipsCache[type][id][relationship].data
              if (Array.isArray(data)) {
                relationships[relationship] = []
                for (const relationId of data) {
                  relationships[relationship].push(get(relationId))
                }
              } else {
                relationships[relationship] = get(data)
              }
            }
            return relationships
          },
        }
      }
    }

    return {
      client: {
        // @todo(Project management, soon) Factorize common parts in these functions
        get_all: async function(path, options) {
          const params = new URLSearchParams();
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
          let url = `${baseUrl}${path}?${params.toString()}`

          const got = []
          // @todo(Project management, later) Handle pagination more... subtly
          // This is just getting all pages so the name of the function should reflect that,
          // and this store should also provide functions that paginate explicitly
          while (url) {
            const raw_response = await fetch(
              url,
              {
                headers: {'Content-Type': 'application/vnd.api+json'},
              },
            )
            const response = await raw_response.json()
            for (const item of response.data) {
              update(item)
              got.push(get(item))
            }
            if (response.included) {
              for (const item of response.included) {
                update(item)
              }
            }
            url = response.links?.next
          }
          return got
        },
        get_one: async function(type, id, options) {
          const params = new URLSearchParams();
          if (options?.include) {
            params.append('include', options.include)
          }
          const url = `${baseUrl}${type}s/${id}?${params.toString()}`
          const raw_response = await fetch(
            url,
            {
              headers: {'Content-Type': 'application/vnd.api+json'},
            },
          )
          const response = await raw_response.json()
          update(response.data)
          if (response.included) {
            for (const item of response.included) {
              update(item)
            }
          }
          return get(response.data)
        },
        post: async function(type, attributes, relationships_, options) {
          const params = new URLSearchParams();
          if (options?.include) {
            params.append('include', options.include)
          }
          const url = `${baseUrl}${type}s?${params.toString()}`

          const relationships = {}
          for (const [key, value] of Object.entries(relationships_)) {
            if (Array.isArray(value)) {
              relationships[key] = {data: value.map(item => ({type: item.type, id: item.id}))}
            } else {
              relationships[key] = {data: {type: value.type, id: value.id}}
            }
          }
          const data = {
            type,
            attributes,
            relationships,
          }
          const raw_response = await fetch(
            url,
            {
              method: 'POST',
              headers: {'Content-Type': 'application/vnd.api+json'},
              body: JSON.stringify({data}),
            },
          )
          const response = await raw_response.json()
          update(response.data)
          if (response.included) {
            for (const item of response.included) {
              update(item)
            }
          }
          return get(response.data)
        },
        patch: async function(type, id, attributes, relationships_, options) {
          const params = new URLSearchParams();
          if (options?.include) {
            params.append('include', options.include)
          }
          const url = `${baseUrl}${type}s/${id}?${params.toString()}`

          const relationships = {}
          for (const [key, value] of Object.entries(relationships_)) {
            if (Array.isArray(value)) {
              relationships[key] = {data: value.map(item => ({type: item.type, id: item.id}))}
            } else {
              relationships[key] = {data: {type: value.type, id: value.id}}
            }
          }
          const data = {
            type,
            id,
            attributes,
            relationships,
          }
          const raw_response = await fetch(
            url,
            {
              method: 'PATCH',
              headers: {'Content-Type': 'application/vnd.api+json'},
              body: JSON.stringify({data}),
            },
          )
          const response = await raw_response.json()
          update(response.data)
          if (response.included) {
            for (const item of response.included) {
              update(item)
            }
          }
          return get(response.data)
        },
        delete: async function(type, id) {
          const url = `${baseUrl}${type}s/${id}`
          await fetch(
            url,
            {
              method: 'DELETE',
              headers: {'Content-Type': 'application/vnd.api+json'},
            },
          )
          if (attributesCache[type]) {
            attributesCache[type][id] = null
          }
        }
      },
      cache: {
        get: function(type, id) {
          return get({type, id})
        }
      },
    }
  })
}

export const useApiStore = defineApiStore('api')
