export interface InclusionOptions {
  include?: string[]
  // @todo fields?: {[type: string]: string[]}
}

export interface SelectionOptions {
  filters?: {[name: string]: string | number}
}

export interface GenericAttributes {
  [name: string]: unknown
}

export interface GenericRelationships {
  [name: string]: null | GenericItem | GenericItem[]
}

export interface GenericItem {
  type: string
  id: string

  inCache: boolean  // Whether the item has ever been loaded from the API
  exists?: boolean  // Whether the item exists in the API
  // The following cases are possible:
  // - {inCache: true, exists: true}: e.g. after a successful get
  // - {inCache: true, exists: false}: e.g. after a 404 get or a delete
  // - {inCache: false, exists: undefined}: e.g. after a get from cache of a never-heard-of item
  // - {inCache: false, exists: true}: e.g. after a get that returned this item in 'relationships' but not in 'included'
  // The case {inCache: false, exists: false} is impossible.

  loading: boolean  // Whether the item is currently being loaded from the API
  loaded: Promise<void>  // Resolves when loading the item from the API is done
  refresh(options?: InclusionOptions): Promise<void>  // Load the item from the API again. Returns '.loaded' for convenience.

  attributes?: GenericAttributes
  relationships?: GenericRelationships

  patch(attributes: Partial<GenericAttributes>, relationships: Partial<GenericRelationships>, options?: InclusionOptions): Promise<void>
  delete(): Promise<void>
}

export interface Item<Attributes extends GenericAttributes, RelationShips extends GenericRelationships> extends GenericItem {
  attributes?: Attributes
  relationships?: RelationShips

  patch(attributes: Partial<Attributes>, relationships: Partial<RelationShips>, options?: InclusionOptions): Promise<void>
}

export interface List<ItemType extends GenericItem> {
  inCache: boolean

  loading: boolean
  pageLoaded: Promise<void>  // Resolves when the next page of items is loaded
  // @todo Let user request partial loading (of only first page) and then loading of next page on demand
  fullyLoaded: Promise<void>
  refresh(options?: InclusionOptions): Promise<void>

  items: ItemType[]
}
