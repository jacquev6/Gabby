<script setup lang="ts">
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'

import RootLayout from '../RootLayout.vue'
import bc, { type Breadcrumbs } from '$frontend/components/breadcrumbs'
import type { Project } from '$frontend/stores/api'
import { useGloballyBusyStore } from '$frontend/stores/globallyBusy'


const props = defineProps<{
  project: Project
  title: string[]
  breadcrumbs: Breadcrumbs
}>()

const i18n = useI18n()
const globallyBusy = useGloballyBusyStore()

globallyBusy.register('loading project', computed(() => props.project.loading))

const title = computed(() => {
  if (props.project.loading) {
    return []
  } else if (props.project.inCache && props.project.exists) {
    return [props.project.attributes.title, ...props.title]
  } else {
    return [i18n.t('projectNotFound')]
  }
})

const breadcrumbs = computed(() => {
  if (props.project.loading) {
    return bc.empty
  } else if (props.project.inCache && props.project.exists) {
    return bc.prepend(
      props.project.attributes.title,
      {name: 'project', params: {projectId: props.project.id}},
      props.breadcrumbs,
    )
  } else {
    return bc.last(i18n.t('projectNotFound'))
  }
})
</script>

<template>
  <RootLayout
    :title :breadcrumbs
  >
    <template v-if="project.inCache">
      <template v-if="project.exists">
        <slot :project></slot>
      </template>
      <template v-else>
        <h1>{{ i18n.t('projectNotFound') }}</h1>
      </template>
    </template>
  </RootLayout>
</template>
