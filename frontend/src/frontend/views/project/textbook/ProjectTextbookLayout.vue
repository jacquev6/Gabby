<script setup lang="ts">
import { ref, computed } from 'vue'
import { computedAsync } from '@vueuse/core'
import { useI18n } from 'vue-i18n'

import { useApiStore } from '$frontend/stores/api'
import { BBusy } from '$frontend/components/opinion/bootstrap'
import type { Project, Textbook } from '$frontend/types/api'


const props = defineProps<{
  project: Project,
  refreshProject: Function,
  textbookId: string,
}>()

const i18n = useI18n()

const api = useApiStore()

const component = ref<null | { title: string, breadcrumbs: [], handlesScrolling?: boolean }>(null)

const textbookIsLoading = ref(false)
const textbookNeedsRefresh = ref(0)
const textbook = computedAsync(
  async () => {
    textbookNeedsRefresh.value  // Dependency for reactivity
    await new Promise((resolve) => resolve(null))  // @todo Understand why removing this line duplicates the request
    return await api.client.getOne<Textbook>('textbook', props.textbookId, {include: 'sections.pdfFile.namings'})
  },
  null,
  textbookIsLoading,
)

// @todo Move this check (that the textbook belongs to the project) to the backend, probably by adding a *required* query parameter 'filter[project]'
const textbookExists = computed(() => textbook.value?.exists && textbook.value.relationships && textbook.value.relationships.project.id === props.project.id)

const title = computed(() => {
  if (textbookIsLoading.value) {
    return []
  } else if (textbookExists.value) {
    console.assert(textbook.value?.attributes !== undefined)
    const componentTitle = component.value ? component.value.title : []
    return [textbook.value.attributes.title, ...componentTitle]
  } else {
    return [i18n.t('textbookNotFound')]
  }
})

const breadcrumbs = computed(() => {
  if (textbookIsLoading.value) {
    return []
  } else if (textbookExists.value) {
    console.assert(textbook.value?.attributes !== undefined)
    const componentBreadcrumbs = component.value ? component.value.breadcrumbs : []
    return [
      {
        title: textbook.value.attributes.title,
        to: {name: 'textbook', params: {textbookId: props.textbookId}},
      },
      ...componentBreadcrumbs,
    ]
  } else {
    return [{title: i18n.t('textbookNotFound')}]
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
  <BBusy :busy="textbookIsLoading" showWhileBusy="afterNotBusy" size="20em" :class="class_">
    <template v-if="textbookExists">
      <RouterView v-slot="{ Component }">
        <component
          :is="Component" ref="component"
          :project :refreshProject
          :textbook :refreshTextbook="() => { ++textbookNeedsRefresh }"
        />
      </RouterView>
    </template>
    <template v-else>
      <h1>{{ $t('textbookNotFound') }}</h1>
    </template>
  </BBusy>
</template>
