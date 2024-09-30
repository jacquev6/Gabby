import { makeStore } from "./glue"
import type { ApiStore, Item, List, InCache, Exists } from "./interface"


// Multiple, lazy-instantiated singletons, à la Pinia, but handled manually for flexibility.
let stores: {[id: string]: ApiStore} = {}

export function resetApiStores() {
  stores = {}
}

export function defineApiStore(id: string, options: {baseUrl: string}): () => ApiStore {
  return function useApiStore() {
    if (stores[id] === undefined) {
      stores[id] = makeStore(options)
    }
    return stores[id]
  }
}

export const useApiStore = defineApiStore('api', {baseUrl: '/api'})

export type { Item, List, InCache, Exists }

export type ParsedExercise = Item<'parsedExercise'>
export type Exercise = Item<'exercise'>
export type PdfFile = Item<'pdfFile'>
export type PdfFileNaming = Item<'pdfFileNaming'>
export type Ping = Item<'ping'>
export type Project = Item<'project'>
export type RecoveryEmailRequest = Item<'recoveryEmailRequest'>
export type Section = Item<'section'>
export type Textbook = Item<'textbook'>
export type User = Item<'user'>
