<script setup lang="ts">
import { ref, computed } from 'vue'
import { useI18n } from 'vue-i18n'

import { useApiStore } from '$frontend/stores/api'
import { BBusy } from '$frontend/components/opinion/bootstrap'
import type { Project } from '$frontend/stores/api'


const props = defineProps<{
  project: Project,
  refreshProject(): void,
  textbookId: string,
}>()

const i18n = useI18n()

const api = useApiStore()

const component = ref<null | { title: string, breadcrumbs: [], handlesScrolling?: boolean }>(null)

const textbook = api.auto.getOne('textbook', props.textbookId, {include: ['sections.pdfFile.namings']})

function refreshTextbook() {
  // @todo Remove 'options' from '.refresh()' (use those from '.getOne'). The remove 'refreshTextbook' and have sub-components simply call 'textbook.refresh()'
  textbook.refresh({include: ['sections.pdfFile.namings']})
}

// @todo Move this check (that the textbook belongs to the project) to the backend, probably by adding a *required* query parameter 'filter[project]'
const textbookExists = computed(() => textbook.exists && textbook.relationships && textbook.relationships.project.id === props.project.id)

const title = computed(() => {
  if (textbook.loading) {
    return []
  } else if (textbookExists.value) {
    console.assert(textbook.attributes !== undefined)
    const componentTitle = component.value ? component.value.title : []
    return [textbook.attributes.title, ...componentTitle]
  } else {
    return [i18n.t('textbookNotFound')]
  }
})

const breadcrumbs = computed(() => {
  if (textbook.loading) {
    return []
  } else if (textbookExists.value) {
    console.assert(textbook.attributes !== undefined)
    const componentBreadcrumbs = component.value ? component.value.breadcrumbs : []
    return [
      {
        title: textbook.attributes.title,
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
  <BBusy :busy="textbook.loading" showWhileBusy="afterNotBusy" size="20em" :class="class_">
    <template v-if="textbookExists">
      <RouterView v-slot="{ Component }">
        <component
          :is="Component" ref="component"
          :project :refreshProject
          :textbook :refreshTextbook
        />
      </RouterView>
    </template>
    <template v-else>
      <h1>{{ $t('textbookNotFound') }}</h1>
    </template>
  </BBusy>
</template>
