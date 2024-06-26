<script setup lang="ts">
import { ref, computed } from 'vue'
import { useI18n } from 'vue-i18n'
import type { RouteLocationRaw } from 'vue-router'

import LoginModal from '$frontend/components/LoginModal.vue'
import Navbar from '$frontend/components/Navbar.vue'
import { useApiStore } from '../stores/api'


const api = useApiStore()
const i18n = useI18n()

const unavailableUntil = (() => {
  const envVar = import.meta.env.VITE_GABBY_UNAVAILABLE_UNTIL
  if (envVar === undefined) {
    return null
  } else {
    return new Date(envVar)
  }
})()

const component = ref<{
  title?: string,
  breadcrumbs: {title: string, to: RouteLocationRaw}[],
  handlesScrolling?: boolean,
} | null>(null)

const title = computed(() => {
  if (component.value) {
    if (component.value.title === undefined) {
      console.error('component.value.title is undefined')
      return i18n.t('thisIsABug')
    } else {
      console.assert(component.value.title !== null)
      return ['MALIN', ...component.value.title].join(' - ')
    }
  } else {
    return 'MALIN'
  }
})

const breadcrumbs = computed(() => {
  const home = {title: i18n.t('home'), to: '/'}
  if (component.value) {
    if (component.value.breadcrumbs === undefined) {
      console.error('component.value.breadcrumbs is undefined')
      return [{title: i18n.t('thisIsABug'), to: ''}]
    } else {
      console.assert(component.value.breadcrumbs !== null)
      return [home, ...component.value.breadcrumbs]
    }
  } else {
    return [home]
  }
})

const componentHandlesScrolling = computed(() => component.value?.handlesScrolling ?? false)

const class_ = computed(() => componentHandlesScrolling.value ? 'overflow-hidden' : 'overflow-auto')
</script>

<template>
  <div class="vh-100 d-flex flex-column overflow-hidden">
    <Navbar :title :breadcrumbs></Navbar>
    <template v-if="unavailableUntil">
      <div class="alert alert-danger" role="alert">
        <i18n-t keypath="siteUnavailableUntil">
          <template v-slot:date>
            {{ $d(unavailableUntil, 'long') }}
          </template>
        </i18n-t>
      </div>
    </template>
    <template v-else>
      <LoginModal />
      <template v-if="api.auth.isAuthenticated.value">
        <div class="h-100 flex-fill container-fluid" data-cy="root-container" :class="class_">
          <RouterView v-slot="{ Component }">
            <component :is="Component" ref="component" />
          </RouterView>
        </div>
      </template>
    </template>
    </div>
</template>
