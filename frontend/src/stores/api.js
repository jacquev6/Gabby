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
      const attributes = attributesCache[itemId.type]?.[itemId.id]
      if (!attributes) {
        return null
      } else {
        return {
          ...itemId,
          attributes,
          get relationships() {
            const relationships = {}
            for (const relationship of Object.keys(relationshipsCache[itemId.type][itemId.id])) {
              const data = relationshipsCache[itemId.type][itemId.id][relationship].data
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
        get: async function(path, options) {
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
          let url = baseUrl + path + '?' + params.toString()

          const got = []
          // @todo(Project management, later) Handle pagination more... subtly
          // This is just getting all pages so the name of the function should reflect that,
          // and this store should also provide functions that paginate explicitly
          while (url) {
            const response = await (await fetch(url, {headers: {'Content-Type': 'application/vnd.api+json'}})).json()
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
