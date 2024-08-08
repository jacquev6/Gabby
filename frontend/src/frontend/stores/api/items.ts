import { reactive } from 'vue'
import type { Requester, RequesterItemResponse } from './requester'
import { itemTypes } from './interface'
import type { ItemTypes, Operations, Item } from './interface'
import type { InclusionOptions } from './interface'


type GettableAttributes<ItemType extends ItemTypes> = Operations<ItemType>['gettableAttributes']
type GettableRelationships<ItemType extends ItemTypes> = Operations<ItemType>['gettableRelationships']

type GenericGettableRelationship = Item<ItemTypes>[] | Item<ItemTypes> | null

type CachedAttributes<ItemType extends ItemTypes> = GettableAttributes<ItemType>
type CachedRelationships<ItemType extends ItemTypes> = {
  [name in keyof GettableRelationships<ItemType>]:
    [GettableRelationships<ItemType>[name]] extends [Item<infer ItemType extends ItemTypes>[]] ? {type: ItemType, id: string}[] :
    [GettableRelationships<ItemType>[name]] extends [Item<infer ItemType extends ItemTypes>] ? {type: ItemType, id: string} :
    [GettableRelationships<ItemType>[name]] extends [Item<infer ItemType extends ItemTypes> | null] ? {type: ItemType, id: string} | null :
    never
}

type GenericCachedRelationship = {type: ItemTypes, id: string}[] | {type: ItemTypes, id: string} | null

type PatchableAttributes<ItemType extends ItemTypes> = Operations<ItemType>['patchableAttributes']
type PatchableRelationships<ItemType extends ItemTypes> = Operations<ItemType>['patchableRelationships']

type CachedItem<ItemType extends ItemTypes> = Item<ItemType> & {
  _reactive: {
    inCache: boolean
    loading: boolean
    patching: boolean
    deleting: boolean
    exists?: boolean
    attributes?: CachedAttributes<ItemType>
    relationships?: CachedRelationships<ItemType>
  }
  _include: Record<string, true>
  _loadingPromise: Promise<void> | null
  _needsRefresh: boolean
  _reset(): void
}

type Cache = {
  [ItemType in ItemTypes]?: {[id: string]: CachedItem<ItemType>}
}

export function makeItems(requester: Requester) {
  const cache: Cache = Object.fromEntries(itemTypes.map((type: ItemTypes) => [type, {}]))

  function clearCache() {
    for (const type of itemTypes) {
      const items = cache[type]
      console.assert(items !== undefined)
      for (const id in items) {
        const item = items[id]
        item._reset()
      }
    }
  }

  async function createItem<ItemType extends ItemTypes>(type: ItemType, attributes: Operations<ItemType>['creatableAttributes'], relationships: Operations<ItemType>['creatableRelationships'], inclusionOptions?: InclusionOptions) {
    const response = await requester.postList(type, attributes as any/* @todo Type */, relationships as any/* @todo Type */, inclusionOptions || {})
    return processResponse(response) as any/* @todo Type */ as Item<ItemType>
  }

  function getItem<ItemType extends ItemTypes>(type: ItemType, id: string): CachedItem<ItemType> {
    const items = cache[type]
    console.assert(items !== undefined)
    if (items[id] === undefined) {
      items[id] = makeItem(type, id)
    }
    return items[id]
  }

  function makeGettableRelationships<ItemType extends ItemTypes>(cached: CachedRelationships<ItemType> | undefined) {
    if (cached === undefined) {
      return undefined
    } else {
      // @todo Read more about TypeScript to decide whether we can do better than this.
      const relationships: Record<string, GenericGettableRelationship> = {}
      for (const name in cached) {
        const relationship: GenericCachedRelationship = cached[name]
        if (relationship === null) {
          relationships[name] = null
        } else if (Array.isArray(relationship)) {
          relationships[name] = relationship.map(related => getItem(related.type, related.id))
        } else {
          relationships[name] = getItem(relationship.type, relationship.id)
        }
      }
      return relationships as GettableRelationships<ItemType>
    }
  }

  function makeItem<ItemType extends ItemTypes>(type: ItemType, id: string): CachedItem<ItemType> {
    return {
      // Constant attributes
      type,
      id,
      // Attributes to reset in method '_reset' below
      _reactive: reactive({
        inCache: false,
        loading: false,
        patching: false,
        deleting: false,
        exists: undefined,
        attributes: undefined,
        relationships: undefined,
      }),
      _include: {},
      _loadingPromise: null,
      _needsRefresh: false,
      // Methods and getters
      get inCache() { return this._reactive.inCache },
      get loading() { return this._reactive.loading },
      get patching() { return this._reactive.patching },
      get deleting() { return this._reactive.deleting },
      get busy() { return this._reactive.loading || this._reactive.patching || this._reactive.deleting },
      get exists() { return this._reactive.exists },
      get attributes() { return this._reactive.attributes },
      get relationships() { return makeGettableRelationships(this._reactive.relationships) },
      get loaded() {
        if (this._loadingPromise !== null) {
          return this._loadingPromise
        } else if(this.inCache) {
          return Promise.resolve()
        } else {
          return Promise.reject(new Error('Never refreshed'))
        }
      },
      _reset() {
        this._reactive.inCache = false
        this._reactive.loading = false
        this._reactive.exists = undefined
        this._reactive.attributes = undefined
        this._reactive.relationships = undefined
        this._include = {}
        this._loadingPromise = null
        this._needsRefresh = false
      },
      refresh() {
        console.assert(cache[this.type]?.[this.id] === this, 'Item detached from store')

        this._needsRefresh = true
        if (this._loadingPromise === null) {
          this._reactive.loading = true
          this._loadingPromise = (async () => {
            while(this._needsRefresh) {
              this._needsRefresh = false
              const include = Object.keys(this._include)
              processResponse(await requester.getItem(this.type, this.id, include.length === 0 ? {} : {include}))
            }
            this._reactive.loading = false
            this._loadingPromise = null
          })()
        }
        return this._loadingPromise
      },
      async delete() {
        this._reactive.deleting = true
        processResponse(await requester.deleteItem(this.type, this.id))
        this._reactive.deleting = false
      },
      async patch(attributes: PatchableAttributes<ItemType>, relationships: PatchableRelationships<ItemType>, inclusionOptions?: InclusionOptions) {
        this._reactive.patching = true
        processResponse(await requester.patchItem(this.type, this.id, attributes as any/* @todo Type */, relationships as any/* @todo Type */, inclusionOptions || {}))
        this._reactive.patching = false
      },
    } as CachedItem<ItemType>  // Type assertion required because of dynamic relation between 'inCache', 'exists', and 'attributes'/'relationships'
  }

  function processResponse(response: RequesterItemResponse) {
    for (const item of response.included) {
      processItemInResponse(item)
    }
    return processItemInResponse(response.main)
  }

  function processItemInResponse(item: RequesterItemResponse['main']) {
    const cached = getItem(item.type as any/* @todo Type */, item.id)
    cached._reactive.inCache = true
    cached._reactive.exists = item.exists
    cached._reactive.attributes = item.attributes as any/* @todo Type */
    cached._reactive.relationships = item.relationships as any/* @todo Type */
    if (item.relationships) {
      for (const relationship of Object.values(item.relationships)) {
        if (Array.isArray(relationship)) {
          for (const related of relationship) {
            getItem(related.type as any/* @todo Type */, related.id)._reactive.exists = true
          }
        } else if (relationship !== null) {
          getItem(relationship.type as any/* @todo Type */, relationship.id)._reactive.exists = true
        }
      }
    }
    return cached
  }

  async function batch(operations: any/* @todo Type*/[]) {
    const results = await requester.batch(operations)
    return results.map(processItemInResponse) as any/* @todo Type*/[]
  }

  function get<ItemType extends ItemTypes>(type: ItemType, id: string, inclusionOptions: InclusionOptions): [CachedItem<ItemType>, boolean] {
    const item = getItem(type, id)
    let needsRefresh = false
    for (const include of inclusionOptions.include || []) {
      if (!item._include[include]) {
        item._include[include] = true
        needsRefresh = true
      }
    }
    return [item, needsRefresh]
  }

  return {
    create: createItem,
    clearCache,
    get,
    batch,
    processItemInResponse,
  }
}

export type Items = ReturnType<typeof makeItems>
