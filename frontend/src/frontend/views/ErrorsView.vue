<script setup lang="ts">
import { useApiStore } from '../stores/api'
import bc from '$frontend/components/breadcrumbs'


const api = useApiStore()

const undef: any/* Voluntarily untyped */ = undefined
const nul: any/* Same */ = null

const errors: [string, () => void][] = [
  ['Assert without message (not caught, by design)', () => console.assert(false)],
  ['Assert with message (not caught, by design)', () => console.assert(false, 'This is the message')],
  ['Dereference undefined', () => undef.foo],
  ['Dereference null', () => nul.foo],
  ['Unhandled rejection', () => Promise.reject('This is the reason')],
  ['Throw exception', () => { throw new Error('This is the error') }],
  ['Generate a 422 response', () => api.client.getOne('syntheticError', '422')],
  ['Generate a 404 response (not caught, by design)', () => api.client.getOne('syntheticError', '404')],
  ['Generate a 500 response', () => api.client.getOne('syntheticError', '500')],
]

defineExpose({
  title: ['Errors'],
  breadcrumbs: bc.last('Errors', '/errors'),
})

if (window.location.search.includes('reject')) {
  Promise.reject('This is the reason')
}
</script>

<template>
  <p v-for="[title, f] of errors"><button @click="f">{{ title }}</button></p>
</template>
