<script setup lang="ts">
import { ref, computed } from 'vue'
import { computedAsync } from '@vueuse/core'
import { useI18n } from 'vue-i18n'

import { useApiStore } from '../../stores/api'
import { BBusy } from '../../components/opinion/bootstrap'

const props = defineProps<{
  projectId: string,
}>()

const i18n = useI18n()

const api = useApiStore()

const component = ref<null | { title: string, breadcrumbs: [] }>(null)

const projectIsLoading = ref(false)
const projectNeedsRefresh = ref(0)
const project = computedAsync(
  async () => {
    projectNeedsRefresh.value  // Dependency for reactivity
    return await api.client.getOne('project', props.projectId, {include: ['textbooks', 'exercises.textbook']})
  },
  null,
  projectIsLoading,
)

const projectExists = computed(() => project.value?.exists)

const title = computed(() => {
  if (projectIsLoading.value) {
    return []
  } else if (projectExists.value) {
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

defineExpose({
  title,
  breadcrumbs,
})
</script>

<template>
  <BBusy :busy="projectIsLoading" showWhileBusy="afterNotBusy" size="20em">
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
