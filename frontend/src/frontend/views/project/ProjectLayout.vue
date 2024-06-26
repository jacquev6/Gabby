<script setup lang="ts">
import { ref, computed } from 'vue'
import { computedAsync } from '@vueuse/core'
import { useI18n } from 'vue-i18n'

import { useApiStore } from '$frontend/stores/api'
import { BBusy } from '$frontend/components/opinion/bootstrap'
import type { Project } from '$frontend/types/api'


const props = defineProps<{
  projectId: string,
}>()

const i18n = useI18n()

const api = useApiStore()

const component = ref<null | { title: string, breadcrumbs: [], handlesScrolling?: boolean }>(null)

const projectIsLoading = ref(false)
const projectNeedsRefresh = ref(0)
const project = computedAsync(
  async () => {
    projectNeedsRefresh.value  // Dependency for reactivity
    await new Promise((resolve) => resolve(null))  // @todo Understand why removing this line duplicates the request
    return await api.client.getOne<Project>('project', props.projectId, {include: ['textbooks', 'exercises.textbook']})
  },
  null,
  projectIsLoading,
)

const projectExists = computed(() => project.value?.exists)

const title = computed(() => {
  if (projectIsLoading.value) {
    return []
  } else if (projectExists.value) {
    console.assert(project.value?.attributes !== undefined)
    const componentTitle = component.value ? component.value.title : []
    return [project.value.attributes.title, ...componentTitle]
  } else {
    return [i18n.t('projectNotFound')]
  }
})

const breadcrumbs = computed(() => {
  if (projectIsLoading.value) {
    return []
  } else if (projectExists.value) {
    console.assert(project.value?.attributes !== undefined)
    const componentBreadcrumbs = component.value ? component.value.breadcrumbs : []
    return [
      {
        title: project.value.attributes.title,
        to: {name: 'project', params: {projectId: props.projectId}},
      },
      ...componentBreadcrumbs,
    ]
  } else {
    return [{title: i18n.t('projectNotFound')}]
  }
})

const componentHandlesScrolling = computed(() => component.value?.handlesScrolling ?? false)

const class_ = computed(() => componentHandlesScrolling.value ? ['h-100', 'overflow-hidden'] : [])

defineExpose({
  title,
  breadcrumbs,
  handlesScrolling: componentHandlesScrolling,
})
</script>

<template>
  <BBusy :busy="projectIsLoading" showWhileBusy="afterNotBusy" size="20em" :class="class_">
    <template v-if="projectExists">
      <RouterView v-slot="{ Component }">
        <component
          :is="Component" ref="component"
          :project :refreshProject="() => { ++projectNeedsRefresh }"
        />
      </RouterView>
    </template>
    <template v-else>
      <h1>{{ $t('projectNotFound') }}</h1>
    </template>
  </BBusy>
</template>
