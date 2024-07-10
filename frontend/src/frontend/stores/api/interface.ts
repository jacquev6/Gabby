import type { Ref } from 'vue'

import type { paths } from '../../../openapi'


export type InclusionOptions = {
  include?: string[]
  // @todo fields?: {[type: string]: string[]}
}

export type SelectionOptions = {
  filters?: {[name: string]: string | number}
  // @todo sort?: string
}

export type InclusionAndSelectionOptions = InclusionOptions & SelectionOptions

// @todo make 'ItemTypes' and 'Paths' generic arguments to everything, so that they can be specified by the client

export const itemTypes = [
  'adaptedExercise',
  'exercise',
  'extractionEvent',
  'fillWithFreeTextAdaptation',
  'multipleChoicesInInstructionsAdaptation',
  'multipleChoicesInWordingAdaptation',
  'pdfFile',
  'pdfFileNaming',
  'ping',
  'project',
  'recoveryEmailRequest',
  'section',
  'selectThingsAdaptation',
  'textbook',
  'user',
] as const

export type ItemTypes = typeof itemTypes[number]

export type Paths = paths

type ListPath<ItemType extends string> = `/api/${ItemType}s`

type ItemPath<ItemType extends string> = `/api/${ItemType}s/{id}`

type GenericPath = {
  post: {
    requestBody: {
      content: {
        'application/json': {
          data: {}
        }
      }
    }
  }
  patch: {
    requestBody: {
      content: {
        'application/json': {
          data: {}
        }
      }
    }
  }
}

type ExtractAttributes<T> = Required<T> extends {attributes: unknown} ? Required<T>['attributes'] : never

type ConvertRelationships<T> = {
  [name in keyof T]:
    [T[name]] extends [{data: {type: ItemTypes}[]}] ? Item<T[name]['data'][number]['type']>[] :
    [T[name]] extends [{data: {type: ItemTypes}}] ? Item<T[name]['data']['type']> :
    [T[name]] extends [{data: {type: ItemTypes} | null}] ? Item<NonNullable<T[name]['data']>['type']> | null :
    never
}

type ExtractRelationships<T> = Required<T> extends {relationships: unknown} ? ConvertRelationships<Required<Required<T>['relationships']>> : never

export type Operations<ItemType extends ItemTypes> = {
  creatableAttributes: Paths extends {[K in ListPath<ItemType>]: {post: GenericPath['post']}} ? ExtractAttributes<Paths[ListPath<ItemType>]['post']['requestBody']['content']['application/json']['data']> : never
  creatableRelationships: Paths extends {[K in ListPath<ItemType>]: {post: GenericPath['post']}} ? Partial/* @todo Remove this 'Partial': the information of which relationship is required should come from 'Paths'. This makes createOne fragile because one can forget a required relationship */<ExtractRelationships<Paths[ListPath<ItemType>]['post']['requestBody']['content']['application/json']['data']>> : never
  gettableAttributes: ExtractAttributes<Paths[ItemPath<ItemType>]['get']['responses'][200]['content']['application/vnd.api+json']['data']>
  gettableRelationships: ExtractRelationships<Paths[ItemPath<ItemType>]['get']['responses'][200]['content']['application/vnd.api+json']['data']>
  patchable: Paths extends {[K in ItemPath<ItemType>]: {patch: {}}} ? true : false
  patchableAttributes: Paths extends {[K in ItemPath<ItemType>]: {patch: GenericPath['patch']}} ? ExtractAttributes<Paths[ItemPath<ItemType>]['patch']['requestBody']['content']['application/json']['data']> : never
  patchableRelationships: Paths extends {[K in ItemPath<ItemType>]: {patch: GenericPath['patch']}} ? Partial/* @todo Remove this 'Partial': the information of which relationship is required should come from 'Paths', even if for now nothing is required */<ExtractRelationships<Paths[ItemPath<ItemType>]['patch']['requestBody']['content']['application/json']['data']>> : never
  deletable: Paths extends {[K in ItemPath<ItemType>]: {delete: {}}} ? true : false
}

export type Item<ItemType extends ItemTypes> = ({
  type: ItemType
  id: string
  inCache: boolean
  exists?: boolean
  relationships?: Readonly<Operations<ItemType>['gettableRelationships']>
  attributes?: Readonly<Operations<ItemType>['gettableAttributes']>

  busy: boolean
  loading: boolean
  loaded: Promise<void>
  refresh(inclusionOptions?: InclusionOptions): Promise<void>
}) & (Operations<ItemType>['patchable'] extends false ? {} : {
  patching: boolean
  patch(attributes: Operations<ItemType>['patchableAttributes'], relationships: Operations<ItemType>['patchableRelationships'], inclusionOptions?: InclusionOptions): Promise<void>
}) & (Operations<ItemType>['deletable'] extends false ? {} : {
  deleting: boolean
  delete(): Promise<void>
})

export type List<ItemType extends ItemTypes> = {
  inCache: boolean

  items: Item<ItemType>[]  // @todo Maybe List<> should extend ArrayLike<> instead of having an 'items' property?

  loading: boolean
  fullyLoaded: Promise<void>
  pageLoaded: Promise<void>
  refresh(inclusionOptions?: InclusionOptions): Promise<void>
}

export type ApiStore = {
  auth: {
    login(username: string, password: string, options?: {validity: string | null,expiresSoonMargin: number, logoutMargin: number}): Promise<boolean>
    logout(): void
    setToken(accessToken: string): void
    readonly isAuthenticated: Ref<boolean>
    readonly token: Ref<string | null>
    readonly expiresSoon: Ref<boolean>
  }
  cache: {
    getOne<ItemType extends ItemTypes>(type: ItemType, id: string, inclusionOptions?: InclusionOptions): Item<ItemType>
    getAll<ItemType extends ItemTypes>(type: ItemType, selectionOptions?: SelectionOptions): List<ItemType>
  }
  auto: {
    getOne<ItemType extends ItemTypes>(type: ItemType, id: string, inclusionOptions?: InclusionOptions): Item<ItemType>
    getAll<ItemType extends ItemTypes>(type: ItemType, inclusionAndSelectionOptions?: InclusionAndSelectionOptions): List<ItemType>
  }
  client: {
    createOne<ItemType extends ItemTypes>(type: ItemType, attributes: Operations<ItemType>['creatableAttributes'], relationships: Operations<ItemType>['creatableRelationships'], inclusionOptions?: InclusionOptions): Promise<Item<ItemType>>
    getOne<ItemType extends ItemTypes>(type: ItemType, id: string, inclusionOptions?: InclusionOptions): Promise<Item<ItemType>>
    getAll<ItemType extends ItemTypes>(type: ItemType, inclusionAndSelectionOptions?: InclusionAndSelectionOptions): Promise<List<ItemType>>
    batch(...operations: any/* @todo Type */): Promise<any/* @todo Type */>
  }
}
