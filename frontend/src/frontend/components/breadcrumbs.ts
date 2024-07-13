import type { RouteLocationRaw } from 'vue-router'


const tag: unique symbol = Symbol()

export type Breadcrumbs = {
  [tag]: 'breadcrumb'
  intermediate: {title: string, to: RouteLocationRaw}[]
  last: string | null
}

function make(intermediate: {title: string, to: RouteLocationRaw}[], last: string | null) {
  return {intermediate, last} as Breadcrumbs
}

export function prepend(title: string, to: RouteLocationRaw, breadcrumbs: Breadcrumbs) {
  return make(
    [{title, to}, ...breadcrumbs.intermediate],
    breadcrumbs.last,
  )
}

export function last(title: string) {
  return make([], title)
}

export const empty = make([], null)


export function normalize(breadcrumbs: Breadcrumbs) {
  if (breadcrumbs.intermediate.length === 0 && breadcrumbs.last === null) {
    return null
  } else if (breadcrumbs.last === null) {
    return make(
      breadcrumbs.intermediate.slice(0, -1),
      breadcrumbs.intermediate[breadcrumbs.intermediate.length - 1].title,
    )
  } else {
    return breadcrumbs
  }
}


export default {
  prepend,
  last,
  empty,
  normalize,
}
