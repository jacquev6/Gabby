import { reactive } from 'vue'
import type { Requester, RequesterItemResponse } from './requester'
import type { GenericAttributes, GenericRelationships, GenericItem, InclusionOptions } from './interface'


interface CachedAttributes {
  [name: string]: unknown
}

export interface ItemReference {
  type: string
  id: string
}

type CachedRelationship = null | ItemReference | ItemReference[]

interface CachedRelationships {
  [name: string]: CachedRelationship
}

export interface CachedItem {
  type: string
  id: string

  _reactive: {
    inCache: boolean
    loading: boolean
    exists?: boolean
    attributes?: CachedAttributes
    relationships?: CachedRelationships
  }

  inCache: boolean
  exists?: boolean
  attributes?: CachedAttributes
  relationships?: GenericRelationships

  loading: boolean
  _loadingPromise: Promise<void> | null
  _needsRefresh: boolean
  loaded: Promise<void>
  refresh(inclusionOptions?: InclusionOptions): Promise<void>

  patch(attributes: Partial<CachedAttributes>, relationships: Partial<CachedRelationships>, inclusionOptions?: InclusionOptions): Promise<void>
  delete(): Promise<void>
}

export function makeItems(requester: Requester) {
  const cache: {[type: string]: {[id: string]: CachedItem}} = {}

  async function createItem(type: string, attributes: GenericAttributes, relationships: GenericRelationships, inclusionOptions?: InclusionOptions) {
    const response = await requester.postList(type, attributes, relationships, inclusionOptions || {})
    return processResponse(response)
  }

  function getItem(type: string, id: string) {
    if (!cache[type]) {
      cache[type] = {}
    }
    if (!cache[type][id]) {
      cache[type][id] = makeItem(type, id)
    }
    return cache[type][id]
  }

  function makeRelationships(_relationships: CachedRelationships | undefined) {
    if (_relationships === undefined) {
      return undefined
    } else {
      const relationships: GenericItem['relationships'] = {}
      for (const [name, relationship] of Object.entries(_relationships)) {
        if (relationship === null) {
          relationships[name] = null
        } else if (Array.isArray(relationship)) {
          const rel = []
          for (const related of relationship) {
            rel.push(getItem(related.type, related.id))
          }
          relationships[name] = rel
        } else {
          relationships[name] = getItem(relationship.type, relationship.id)
        }
      }
      return relationships
    }
  }

  function makeItem(type: string, id: string): CachedItem {
    return {
      // Constant attributes
      type,
      id,
      // Attributes to reset in 'resetItem' below
      _reactive: reactive({
        inCache: false,
        loading: false,
        exists: undefined,
        attributes: undefined,
        relationships: undefined,
      }),
      _loadingPromise: null as Promise<void> | null,
      _needsRefresh: false,
      // Methods and getters
      get inCache() { return this._reactive.inCache },
      get loading() { return this._reactive.loading },  
      get exists() { return this._reactive.exists },
      get attributes() { return this._reactive.attributes },
      get relationships() { return makeRelationships(this._reactive.relationships) },
      get loaded() {
        if (this._loadingPromise !== null) {
          return this._loadingPromise
        } else if(this.inCache) {
          return Promise.resolve()
        } else {
          return Promise.reject(new Error('Never refreshed'))
        }
      },
      refresh(inclusionOptions?: InclusionOptions) {
        console.assert(cache[this.type]?.[this.id] === this, 'Item detached from store')

        this._needsRefresh = true
        if (this._loadingPromise === null) {
          this._reactive.loading = true
          this._loadingPromise = (async () => {
            while(this._needsRefresh) {
              this._needsRefresh = false
              processResponse(await requester.getItem(this.type, this.id, inclusionOptions || {}))
            }
            this._reactive.loading = false
            this._loadingPromise = null
          })()
        }
        return this._loadingPromise
      },
      async delete() {
        this._reactive.loading = true
        processResponse(await requester.deleteItem(this.type, this.id))
        this._reactive.loading = false
      },
      async patch(attributes: GenericRelationships, relationships: CachedRelationships, inclusionOptions?: InclusionOptions) {
        this._reactive.loading = true
        processResponse(await requester.patchItem(this.type, this.id, attributes, relationships, inclusionOptions || {}))
        this._reactive.loading = false
      },
    }
  }

  function resetItem(item: CachedItem) {
    item._reactive.inCache = false
    item._reactive.loading = false
    item._reactive.exists = undefined
    item._reactive.attributes = undefined
    item._reactive.relationships = undefined
    item._loadingPromise = null
    item._needsRefresh = false
  }

  function clearCache() {
    for (const type in cache) {
      for (const id in cache[type]) {
        resetItem(cache[type][id])
      }
    }
  }

  function processResponse(response: RequesterItemResponse) {
    for (const item of response.included) {
      processItemInResponse(item)
    }
    return processItemInResponse(response.main)
  }

  function processItemInResponse(item: RequesterItemResponse['main']) {
    const cached = getItem(item.type, item.id)
    cached._reactive.inCache = true
    cached._reactive.exists = item.exists
    cached._reactive.attributes = item.attributes
    cached._reactive.relationships = item.relationships
    return cached
  }

  async function batch(operations: any/* @todo Type*/[]) {
    const results = await requester.batch(operations)
    return results.map(processItemInResponse) as any/* @todo Type*/[]
  }

  return {
    create: createItem,
    clearCache,
    get: getItem,
    batch,
    processItemInResponse,
  }
}

export type Items = ReturnType<typeof makeItems>
