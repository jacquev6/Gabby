import { makeStore } from "./glue"


// Multiple, lazy-instantiated singletons, à la Pinia, but handled manually for flexibility.
let stores: {[id: string]: ReturnType<typeof makeStore>} = {}

export function resetApiStores() {
  stores = {}
}

export function defineApiStore(id: string, options: {baseUrl: string}) {
  return function useApiStore() {
    if (stores[id] === undefined) {
      stores[id] = makeStore(options)
    }
    return stores[id]
  }
}

export const useApiStore = defineApiStore('api', {baseUrl: '/api'})
