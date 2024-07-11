import { reactive } from 'vue'
import type { InclusionOptions, SelectionOptions } from './interface'
import type { Items } from './items'
import type { Requester, RequesterPageResponse } from './requester'


export interface CachedList {
  inCache: boolean

  loading: boolean
  _loadingPromise: Promise<void> | null
  _needsRefresh: boolean
  fullyLoaded: Promise<void>
  _pageLoadingPromise: Promise<RequesterPageResponse> | null
  pageLoaded: Promise<void>
  refresh(inclusionOptions?: InclusionOptions): Promise<void>

  items: any/* @todo Type */[]
  _reactive: {
    inCache: boolean
    loading: boolean
    items: any/* @todo Type */[]
  }
}

export function makeLists(requester: Requester, items: Items) {
  const cache: {[type: string]: {[selection: string]: CachedList}} = {}

  function getList(type: string, selectionOptions: SelectionOptions) {
    const selection = (() => {
      const filters = selectionOptions.filters
      if (filters) {
        return JSON.stringify(filters)
      } else {
        return ''
      }
    })()
    if (!cache[type]) {
      cache[type] = {}
    }
    if (!cache[type][selection]) {
      cache[type][selection] = makeList(type, selectionOptions, selection)
    }
    return cache[type][selection]
  }

  function makeList(type: string, selectionOptions: SelectionOptions, selection: string) {
    return {
      // Attributes to reset in 'resetList' below
      _loadingPromise: null as Promise<void> | null,
      _needsRefresh: false,
      _pageLoadingPromise: null as Promise<RequesterPageResponse> | null,
      _reactive: reactive({
        inCache: false,
        loading: false,
        items: [] as any/* @todo Type */[],
      }),
      // Methods and getters
      get inCache() { return this._reactive.inCache },
      get loading() { return this._reactive.loading },  
      get fullyLoaded() {
        if (this._loadingPromise !== null) {
          return this._loadingPromise
        } else if(this.inCache) {
          return Promise.resolve()
        } else {
          return Promise.reject(new Error('Never refreshed'))
        }
      },
      get pageLoaded () {
        if (this._pageLoadingPromise !== null) {
          return this._pageLoadingPromise as unknown as Promise<void>
        } else {
          return Promise.reject(new Error('Never refreshed'))
        }
      },
      async refresh(inclusionOptions?: InclusionOptions) {
        console.assert(cache[type]?.[selection] === this, 'List detached from store')

        this._needsRefresh = true
        if (this._loadingPromise === null) {
          this._reactive.loading = true
          this._loadingPromise = (async () => {
            while(this._needsRefresh) {
              this._needsRefresh = false
              this._pageLoadingPromise = requester.getFirstPage(type, selectionOptions, inclusionOptions || {})
              const firstPage = await this._pageLoadingPromise
              this._reactive.items = []
              processResponse(firstPage)
              for (const item of firstPage.items) {
                this._reactive.items.push({type: item.type, id: item.id})
              }
              let next = firstPage.nextPage
              while (next !== null) {
                if (this._needsRefresh) {
                  // Cancel getting more pages; we're going to start over anyway
                  break
                }
                this._pageLoadingPromise = requester.getPage(next)
                const page = await this._pageLoadingPromise
                processResponse(page)
                for (const item of page.items) {
                  this._reactive.items.push({type: item.type, id: item.id})
                }
                next = page.nextPage
              }
            }
            this._reactive.inCache = true
            this._reactive.loading = false
            this._loadingPromise = null
          })()
        }
        return this._loadingPromise
      },
      get items() {
        return this._reactive.items.map(ref => items.get(ref.type, ref.id))
      },
    }
  }

  function resetList(list: CachedList) {
    list._reactive.inCache = false
    list._reactive.loading = false
    list._loadingPromise = null
    list._needsRefresh = false
    list._pageLoadingPromise = null
    list._reactive.items = []
  }

  function clearCache() {
    for (const type in cache) {
      for (const selection in cache[type]) {
        resetList(cache[type][selection])
      }
    }
  }

  function processResponse(response: RequesterPageResponse) {
    for (const item of response.items) {
      items.processItemInResponse(item)
    }
    for (const item of response.included) {
      items.processItemInResponse(item)
    }
  }

  return {
    get: getList,
    clearCache,
  }
}

export type Lists = ReturnType<typeof makeLists>
