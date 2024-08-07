import { ref } from 'vue'
import type { Ref } from 'vue'
import { pauseTracking, resetTracking } from '@vue/reactivity'


import { makeItems } from './items'
import { makeLists } from './lists'
import { makeRequester } from './requester'
import type { InclusionOptions, SelectionOptions, InclusionAndSelectionOptions, Operations } from './interface'
import type { Items } from './items'
import type { Lists } from './lists'
import type { ItemTypes, List, Item, InCache } from './interface'


function makeAuth(baseUrl: string, token: Ref<string | null>, items: Items, lists: Lists) {
  const defaultExpiresSoonMargin = 15 * 60 * 1000
  const defaultLogoutMargin = 5 * 60 * 1000
  let expiresSoonTimeout: ReturnType<typeof setTimeout> | null = null
  let logoutTimeout: ReturnType<typeof setTimeout> | null = null

  const auth = {
    async login(
      username: string,
      password: string,
      options = {
        validity: null as null | string,
        expiresSoonMargin: defaultExpiresSoonMargin,
        logoutMargin: defaultLogoutMargin,
      },
    ) {
      const body = new FormData()
      body.append('username', username)
      body.append('password', password)
      if (options.validity !== null) {
        body.append('options', JSON.stringify({validity: options.validity}))
      }
      const response = await fetch(`${baseUrl}/token`, {method: 'POST', body})
      if (response.ok) {
        const json_response = await response.json()
        this._setAuth(json_response.access_token, new Date(json_response.valid_until), options.expiresSoonMargin, options.logoutMargin)
        items.clearCache()
        lists.clearCache()
        return true
      } else {
        this.logout()
        return false
      }
    },
    logout() {
      this.token.value = null
      this.isAuthenticated.value = false
      localStorage.removeItem('auth-v1')
      items.clearCache()
      lists.clearCache()
    },
    setToken(accessToken: string) {
      this.token.value = accessToken
      this.isAuthenticated.value = true
      this.expiresSoon.value = false
    },
    _setAuth(accessToken: string, validUntil: Date, expiresSoonMargin: number, logoutMargin: number) {
      this.token.value = accessToken
      this.isAuthenticated.value = true
      localStorage.setItem('auth-v1', JSON.stringify({accessToken, validUntil}))
      this.expiresSoon.value = false
      if (expiresSoonTimeout !== null) {
        clearTimeout(expiresSoonTimeout)
      }
      if (logoutTimeout !== null) {
        clearTimeout(logoutTimeout)
      }
      const validFor = (validUntil.getTime() - Date.now())
      expiresSoonTimeout = setTimeout(() => { this.expiresSoon.value = true }, validFor - expiresSoonMargin)
      logoutTimeout = setTimeout(() => { this.logout() }, validFor - logoutMargin)
    },
    token,
    isAuthenticated: ref(false),  // I tried 'computed(() => token.value !== null)' but a test failed. I couldn't figure out why.
    expiresSoon: ref(false),
  }

  const stored = localStorage.getItem('auth-v1')
  if (stored !== null) {
    const {accessToken, validUntil} = JSON.parse(stored)
    auth._setAuth(accessToken, new Date(validUntil), defaultExpiresSoonMargin, defaultLogoutMargin)
  }

  return auth
}

function makeCache(items: Items, lists: Lists) {
  return {
    getOne<ItemType extends ItemTypes>(type: ItemType, id: string, inclusionOptions?: InclusionOptions) {
      return items.get(type, id, inclusionOptions || {})[0]
    },
    getAll(type: string, selectionOptions?: SelectionOptions) {
      return lists.get(type, selectionOptions || {})[0]
    },
  }
}

function makeAuto(items: Items, lists: Lists) {
  return {
    getOne<ItemType extends ItemTypes>(type: ItemType, id: string, inclusionOptions?: InclusionOptions) {
      const [item, needsRefresh] = items.get(type, id, inclusionOptions || {})
      pauseTracking()
      const needsLoad = !item.inCache && !item.loading
      resetTracking()
      if (needsLoad || needsRefresh) {
        item.refresh()
      }
      return item
    },
    getAll(type: string, inclusionAndSelectionOptions?: InclusionAndSelectionOptions) {
      const [list, needsRefresh] = lists.get(type, inclusionAndSelectionOptions || {})
      pauseTracking()
      const needsLoad = !list.inCache && !list.loading
      resetTracking()
      if (needsLoad || needsRefresh) {
        list.refresh()
      }
      return list
    },
  }
}

function makeClient(items: Items, lists: Lists) {
  return {
    async createOne<ItemType extends ItemTypes>(type: ItemType, attributes: Operations<ItemType>['creatableAttributes'], relationships: Operations<ItemType>['creatableRelationships'], inclusionOptions?: InclusionOptions) {
      const item = await items.create(type, attributes, relationships, inclusionOptions)
      return item as Item<ItemType> & InCache
    },
    async getOne<ItemType extends ItemTypes>(type: ItemType, id: string, inclusionOptions?: InclusionOptions) {
      const item = items.get(type, id, inclusionOptions || {})[0]
      await item.refresh()
      return item as Item<ItemType> & InCache
    },
    async getAll<ItemType extends ItemTypes>(type: ItemType, inclusionAndSelectionOptions?: InclusionAndSelectionOptions) {
      const list = lists.get(type, inclusionAndSelectionOptions || {})[0]
      await list.refresh()
      return list as List<ItemType> & InCache
    },
    async batch(...operations: any/* @todo Type */) {
      return items.batch(operations)
    },
  }
}

// @todo Pass a type annotation to 'defineApiStore' containing a mapping of the known types.
// Then remove the individual type annotations from the 'getOne' and 'getAll' methods.
// (while keeping full type safety: 'getOne("ping")' should still return a 'Ping', not a 'GenericItem'.)
export function makeStore(storeOptions: {baseUrl: string}) {
  const baseUrl = storeOptions.baseUrl
  const accessToken = ref<string | null>(null)

  const requester = makeRequester(baseUrl, accessToken)
  const items = makeItems(requester)
  const lists = makeLists(requester, items)

  return {
    auth: makeAuth(baseUrl, accessToken, items, lists),
    cache: makeCache(items, lists),
    auto: makeAuto(items, lists),
    client: makeClient(items, lists),
  }
}
