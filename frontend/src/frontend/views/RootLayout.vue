<script setup lang="ts">
import { ref, computed } from 'vue'
import { useI18n } from 'vue-i18n'

import LoginModal from '$frontend/components/LoginModal.vue'
import Navbar from '$frontend/components/Navbar.vue'
import ErrorReportingModal from '$frontend/components/ErrorReportingModal.vue'
import { useApiStore } from '../stores/api'
import type { Breadcrumbs } from '$frontend/components/breadcrumbs'
import bc from '$frontend/components/breadcrumbs'


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
  breadcrumbs: Breadcrumbs,
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
  const componentBreadcrumbs = component.value ? component.value.breadcrumbs : bc.empty
  return bc.prepend(i18n.t('home'), '/', componentBreadcrumbs)
})

const componentHandlesScrolling = computed(() => component.value?.handlesScrolling ?? false)

const class_ = computed(() => componentHandlesScrolling.value ? 'overflow-hidden' : 'overflow-auto')
</script>

<template>
  <div class="vh-100 d-flex flex-column overflow-hidden">
    <Navbar :title :breadcrumbs></Navbar>
    <ErrorReportingModal />
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
