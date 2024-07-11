import type { Ref } from 'vue'

import type { InclusionOptions, SelectionOptions } from './interface'


interface Attributes {
  [name: string]: unknown
}

interface ItemRef {
  type: string
  id: string
}

type Relationship = null | ItemRef | ItemRef[]

interface Relationships {
  [name: string]: Relationship
}

interface Item extends ItemRef {
  exists: boolean
  attributes?: Attributes
  relationships?: Relationships
}

export interface RequesterItemResponse {
  main: Item
  included: Item[]
}

export interface RequesterPageResponse {
  items: Item[]
  included: Item[]
  nextPage: string | null
}

export function makeRequester(baseUrl: string, accessToken: Ref<string | null>) {
  function makeItemUrl(type: string, id: string, inclusionOptions: InclusionOptions) {
    console.assert(!baseUrl.endsWith('/'))

    const params = new URLSearchParams()
    if (inclusionOptions.include) {
      params.append('include', typeof inclusionOptions.include === 'string' ? inclusionOptions.include : inclusionOptions.include.join(','))
    }

    if (params.size === 0) {
      return `${baseUrl}/${type}s/${id}`
    } else {
      return `${baseUrl}/${type}s/${id}?${params}`
    }
  }

  function makeListUrl(type: string, selectionOptions: SelectionOptions, inclusionOptions: InclusionOptions) {
    console.assert(!baseUrl.endsWith('/'))

    const params = new URLSearchParams()
    if (inclusionOptions.include) {
      params.append('include', typeof inclusionOptions.include === 'string' ? inclusionOptions.include : inclusionOptions.include.join(','))
    }
    if (selectionOptions.filters) {
      for (const [name, value] of Object.entries(selectionOptions.filters)) {
        params.append(`filter[${name}]`, `${value}`)
      }
    }

    if (params.size === 0) {
      return `${baseUrl}/${type}s`
    } else {
      return `${baseUrl}/${type}s?${params}`
    }
  }

  function extractResponseRelationships(relationships: {[name: string]: { data: Relationship }} | undefined) {
    if (relationships === undefined) {
      return {}
    } else {
      return Object.fromEntries(Object.entries(relationships).map(([name, relationship]) => [name, relationship.data]))
    }
  }

  function makeRequestRelationships(relationships: Relationships) {
    return Object.fromEntries(Object.entries(relationships).map(([name, relationship]) => {
      if (relationship === null) {
        return [name, {data: null}]
      } else if (Array.isArray(relationship)) {
        return [name, {data: relationship.map(related => ({type: related.type, id: related.id}))}]
      } else {
        return [name, {data: {type: relationship.type, id: relationship.id}}]
      }
    }))
  }

  async function makePageResponse(raw_response: Response) {
    const json_response = await raw_response.json()
    const response = {
      items: [] as Item[],
      included: [] as Item[],
      nextPage: json_response.links.next || null,
    }
    for (const item of json_response.data) {
      response.items.push({
        type: item.type,
        id: item.id,
        exists: true,
        attributes: item.attributes,
        relationships: extractResponseRelationships(item.relationships),
      })
    }
    for (const included of json_response.included || []) {
      response.included.push({
        type: included.type,
        id: included.id,
        exists: true,
        attributes: included.attributes,
        relationships: extractResponseRelationships(included.relationships),
      })
    }
    return response
  }

  async function makeItemResponse(raw_response: Response) {
    const json_response = await raw_response.json()
    const response = {
      main: {
        type: json_response.data.type,
        id: json_response.data.id,
        exists: true,
        attributes: json_response.data.attributes,
        relationships: extractResponseRelationships(json_response.data.relationships),
      },
      included: [] as Item[],
    }
    for (const included of json_response.included || []) {
      response.included.push({
        type: included.type,
        id: included.id,
        exists: true,
        attributes: included.attributes,
        relationships: extractResponseRelationships(included.relationships),
      })
    }
    return response
  }

  function makeHeaders(headers: {[name: string]: string}) {
    if (accessToken.value !== null) {
      headers['Authorization'] = `Bearer ${accessToken.value}`
    }
    return headers
  }

  async function postList(type: string, attributes: Attributes, relationships: Relationships, inclusionOptions: InclusionOptions): Promise<RequesterItemResponse> {
    const url = makeListUrl(type, {}, inclusionOptions)
    const raw_response = await fetch(url, {
      method: 'POST',
      headers: makeHeaders({'Content-Type': 'application/vnd.api+json'}),
      body: JSON.stringify({
        data: {
          type,
          attributes,
          relationships: makeRequestRelationships(relationships),
        }
      }),
    })
    if (raw_response.ok) {
      if (raw_response.headers.get('Content-Type') == 'application/vnd.api+json') {
        return await makeItemResponse(raw_response)
      } else {
        throw new Error(`Failed to post ${type}: unexpected Content-Type: ${raw_response.headers.get('Content-Type')}`)
      }
    } else {
      throw new Error(`Failed to post ${type}: ${raw_response.status}`)
    }
  }

  async function getPage(url: string): Promise<RequesterPageResponse> {
    const raw_response = await fetch(url, {headers: makeHeaders({})})
    if (raw_response.ok) {
      if (raw_response.headers.get('Content-Type') == 'application/vnd.api+json') {
        return await makePageResponse(raw_response)
      } else {
        throw new Error(`Failed to get next page: unexpected Content-Type: ${raw_response.headers.get('Content-Type')}`)
      }
    } else {
      throw new Error(`Failed to get next page: ${raw_response.status}`)
    }
  }

  async function getFirstPage(type: string, selectionOptions: SelectionOptions, inclusionOptions: InclusionOptions): Promise<RequesterPageResponse> {
    return getPage(makeListUrl(type, selectionOptions, inclusionOptions))
  }

  async function getItem(type: string, id: string, inclusionOptions: InclusionOptions): Promise<RequesterItemResponse> {
    const url = makeItemUrl(type, id, inclusionOptions)
    const raw_response = await fetch(url, {headers: makeHeaders({})})
    if (raw_response.ok) {
      if (raw_response.headers.get('Content-Type') == 'application/vnd.api+json') {
        return await makeItemResponse(raw_response)
      } else {
        throw new Error(`Failed to get ${type} ${id}: unexpected Content-Type: ${raw_response.headers.get('Content-Type')}`)
      }
    } else if(raw_response.status === 404) {
      return {
        main: {
          type,
          id,
          exists: false,
          attributes: undefined,
          relationships: undefined,
        },
        included: [],
      }
    } else {
      throw new Error(`Failed to get ${type} ${id}: ${raw_response.status}`)
    }
  }

  async function patchItem(type: string, id: string, attributes: Attributes, relationships: Relationships, inclusionOptions: InclusionOptions): Promise<RequesterItemResponse> {
    const url = makeItemUrl(type, id, inclusionOptions)
    const raw_response = await fetch(url, {
      method: 'PATCH',
      headers: makeHeaders({'Content-Type': 'application/vnd.api+json'}),
      body: JSON.stringify({
        data: {
          type,
          id,
          attributes,
          relationships: makeRequestRelationships(relationships),
        }
      }),
    })
    if (raw_response.ok) {
      if (raw_response.headers.get('Content-Type') == 'application/vnd.api+json') {
        return await makeItemResponse(raw_response)
      } else {
        throw new Error(`Failed to patch ${type} ${id}: unexpected Content-Type: ${raw_response.headers.get('Content-Type')}`)
      }
    } else {
      throw new Error(`Failed to patch ${type} ${id}: ${raw_response.status}`)
    }
  }

  async function deleteItem(type: string, id: string): Promise<RequesterItemResponse> {
    const url = makeItemUrl(type, id, {})
    const raw_response = await fetch(url, {method: 'DELETE', headers: makeHeaders({})})
    if (raw_response.ok) {
      return {
        main:{
          type,
          id,
          exists: false,
          attributes: undefined,
          relationships: undefined,
        },
        included: [],
      }
    } else {
      throw new Error(`Failed to delete ${type} ${id}: ${raw_response.status}`)
    }
  }

  async function batch(operations: any/*@todo Type*/): Promise<Item[]> {
    const url = `${baseUrl}/batch`
    
    const json_operations = []
    for (const operation of operations) {
      if (operation[0] == 'add') {
        console.assert(operation.length == 5)
        const [_, type, lid, attributes, relationships] = operation
        json_operations.push({
          op: 'add',
          data: {
            type,
            lid: lid || undefined,
            attributes,
            relationships: Object.fromEntries(Object.entries(relationships).map(([name, relationship]: any/*@todo Type*/) => {
              if (relationship === null) {
                return [name, {data: null}]
              } else if (Array.isArray(relationship)) {
                return [name, {data: relationship.map(related => ({type: related.type, id: related.id, lid: related.lid}))}]
              } else {
                return [name, {data: {type: relationship.type, id: relationship.id, lid: relationship.lid}}]
              }
            })),
          },
        })
      } else {
        console.assert(false)
      }
    }

    const raw_response = await fetch(url, {
      method: 'POST',
      headers: makeHeaders({'Content-Type': 'application/vnd.api+json'}),
      body: JSON.stringify({'atomic:operations': json_operations})
    })
    if (raw_response.ok) {
      if (raw_response.headers.get('Content-Type') == 'application/vnd.api+json') {
        const json_response = await raw_response.json()
        const results = []
        for (const result of json_response['atomic:results']) {

          results.push({
            type: result.data.type,
            id: result.data.id,
            exists: true,
            attributes: result.data.attributes,
            relationships: extractResponseRelationships(result.data.relationships),
          })
        }
        return results
      } else {
        throw new Error(`Failed to batch: unexpected Content-Type: ${raw_response.headers.get('Content-Type')}`)
      }
    } else {
      throw new Error(`Failed to batch: ${raw_response.status}`)
    }
  }

  return {
    postList,
    getFirstPage, getPage,
    getItem,
    patchItem,
    deleteItem,
    batch
  }
}

export type Requester = ReturnType<typeof makeRequester>
