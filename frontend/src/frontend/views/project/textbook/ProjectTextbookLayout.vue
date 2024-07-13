<script setup lang="ts">
import { ref, computed } from 'vue'
import { useI18n } from 'vue-i18n'

import { useApiStore } from '$frontend/stores/api'
import { BBusy } from '$frontend/components/opinion/bootstrap'
import type { Project, InCache, Exists } from '$frontend/stores/api'
import type { Breadcrumbs } from '$frontend/components/breadcrumbs'
import bc from '$frontend/components/breadcrumbs'


const props = defineProps<{
  project: Project & InCache & Exists,
  refreshProject(): void,
  textbookId: string,
}>()

const i18n = useI18n()

const api = useApiStore()

const component = ref<null | { title: string, breadcrumbs: Breadcrumbs, handlesScrolling?: boolean }>(null)

const textbook = computed(() => api.auto.getOne('textbook', props.textbookId, {include: ['sections.pdfFile.namings']}))

function refreshTextbook() {
  // @todo Remove 'refreshTextbook' and have sub-components simply call 'textbook.refresh()'
  textbook.value.refresh()
}

// @todo Move this check (that the textbook belongs to the project) to the backend, probably by adding a *required* query parameter 'filter[project]'
const textbookBelongsToProject = computed(() => textbook.value.inCache && textbook.value.exists && textbook.value.relationships && textbook.value.relationships.project.id === props.project.id)

const title = computed(() => {
  if (textbook.value.loading) {
    return []
  } else if (textbook.value.inCache && textbook.value.exists && textbookBelongsToProject.value) {
    const componentTitle = component.value ? component.value.title : []
    return [textbook.value.attributes.title, ...componentTitle]
  } else {
    return [i18n.t('textbookNotFound')]
  }
})

const breadcrumbs = computed(() => {
  if (textbook.value.loading) {
    return bc.empty
  } else if (textbook.value.inCache && textbook.value.exists && textbookBelongsToProject.value) {
    const componentBreadcrumbs = component.value ? component.value.breadcrumbs : bc.empty
    return bc.prepend(
      textbook.value.attributes.title,
      {name: 'textbook', params: {textbookId: props.textbookId}},
      componentBreadcrumbs,
    )
  } else {
    return bc.last(i18n.t('textbookNotFound'))
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
    <template v-if="textbookBelongsToProject">
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
