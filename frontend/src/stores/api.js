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
        get: async function(path) {
          const url = baseUrl + path
          const response = await (await fetch(url, {headers: {'Content-Type': 'application/vnd.api+json'}})).json()
          const got = []
          for (const item of response.data) {
            update(item)
            got.push(get(item))
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
