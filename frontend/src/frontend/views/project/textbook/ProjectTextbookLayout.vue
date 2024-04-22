<script setup lang="ts">
import { ref, computed } from 'vue'
import { computedAsync } from '@vueuse/core'
import { useI18n } from 'vue-i18n'

import { useApiStore } from '../../../stores/api'
import { BBusy } from '../../../components/opinion/bootstrap'

const props = defineProps<{
  project: Object,
  refreshProject: Function,
  textbookId: string,
}>()

const i18n = useI18n()

const api = useApiStore()

const component = ref<null | { title: string, breadcrumbs: [] }>(null)

const textbookIsLoading = ref(false)
const textbookNeedsRefresh = ref(0)
const textbook = computedAsync(
  async () => {
    textbookNeedsRefresh.value  // Dependency for reactivity
    return await api.client.getOne('textbook', props.textbookId, {include: 'sections.pdfFile.namings'})
  },
  null,
  textbookIsLoading,
)

// @todo Move this check (that the textbook belongs to the project) to the backend, probably by adding a *required* query parameter 'filter[project]'
const textbookExists = computed(() => textbook.value?.exists && textbook.value.relationships.project.id === props.project.id)

const title = computed(() => {
  if (textbookIsLoading.value) {
    return []
  } else if (textbookExists.value) {
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

defineExpose({
  title,
  breadcrumbs,
})
</script>

<template>
  <BBusy :busy="textbookIsLoading" showWhileBusy="afterNotBusy" size="20em">
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
