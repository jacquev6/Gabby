<script setup lang="ts">
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'

import { useApiStore } from '$frontend/stores/api'
import LoginModal from '$frontend/components/LoginModal.vue'
import Navbar from '$frontend/components/Navbar.vue'
import ErrorReportingModal from '$frontend/components/ErrorReportingModal.vue'
import type { Breadcrumbs } from '$frontend/components/breadcrumbs'
import { BBusy } from '../components/opinion/bootstrap'
import bc from '$frontend/components/breadcrumbs'
import { useGloballyBusyStore } from '$frontend/stores/globallyBusy'


const props = defineProps<{
  title: string[]
  breadcrumbs: Breadcrumbs
}>()

const api = useApiStore()
const i18n = useI18n()
const globallyBusy = useGloballyBusyStore()

const unavailableUntil = (() => {
  const envVar = import.meta.env.VITE_GABBY_UNAVAILABLE_UNTIL
  if (envVar === undefined) {
    return null
  } else {
    return new Date(envVar)
  }
})()

const title = computed(() => {
  return ['MALIN', ...props.title].join(' - ')
})

const breadcrumbs = computed(() => {
  return bc.prepend(i18n.t('home'), {name: 'new--index'}, props.breadcrumbs)
})
</script>

<template>
  <div class="vh-100 d-flex flex-column overflow-hidden">
    <Navbar :title :breadcrumbs></Navbar>
    <ErrorReportingModal />
    <template v-if="unavailableUntil">
      <div class="alert alert-danger" role="alert">
        <i18n-t keypath="siteUnavailableUntil" #date>
          {{ $d(unavailableUntil, 'long') }}
        </i18n-t>
      </div>
    </template>
    <template v-else>
      <LoginModal />
      <template v-if="api.auth.isAuthenticated.value">
        <BBusy :busy="globallyBusy.busy" size="20rem" class="h-100 flex-fill container-fluid overflow-auto" data-cy="root-container">
          <slot></slot>
        </BBusy>
      </template>
    </template>
  </div>
</template>
