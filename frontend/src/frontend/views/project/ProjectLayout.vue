<script setup lang="ts">
import { ref, computed } from 'vue'
import { useI18n } from 'vue-i18n'

import { useApiStore } from '$frontend/stores/api'
import { BBusy } from '$frontend/components/opinion/bootstrap'
import type { Breadcrumbs } from '$frontend/components/breadcrumbs'
import bc from '$frontend/components/breadcrumbs'


const props = defineProps<{
  projectId: string,
}>()

const i18n = useI18n()

const api = useApiStore()

const component = ref<null | { title: string, breadcrumbs: Breadcrumbs, handlesScrolling?: boolean }>(null)

const project = computed(() => api.auto.getOne('project', props.projectId, {include: ['textbooks', 'exercises.textbook']}))

function refreshProject() {
  // @todo Remove 'options' from '.refresh()' (use those from '.getOne'). The remove 'refreshProject' and have sub-components simply call 'project.value.refresh()'
  project.value.refresh({include: ['textbooks', 'exercises.textbook']})
}

const title = computed(() => {
  if (project.value.loading) {
    return []
  } else if (project.value.inCache && project.value.exists) {
    console.assert(project.value.attributes !== undefined)
    const componentTitle = component.value ? component.value.title : []
    return [project.value.attributes.title, ...componentTitle]
  } else {
    return [i18n.t('projectNotFound')]
  }
})

const breadcrumbs = computed(() => {
  if (project.value.loading) {
    return bc.empty
  } else if (project.value.inCache && project.value.exists) {
    console.assert(project.value.attributes !== undefined)
    const componentBreadcrumbs = component.value ? component.value.breadcrumbs : bc.empty
    return bc.prepend(
      project.value.attributes.title,
      {name: 'project', params: {projectId: props.projectId}},
      componentBreadcrumbs,
    )
  } else {
    return bc.last(i18n.t('projectNotFound'))
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
  <BBusy :busy="project.loading" showWhileBusy="afterNotBusy" size="20em" :class="class_">
    <template v-if="project.inCache && project.exists"> <!-- @todo Start loading the textbook earlier (currently, it has to wait until the project is loaded) -->
      <RouterView v-slot="{ Component }">
        <component
          :is="Component" ref="component"
          :project :refreshProject
        />
      </RouterView>
    </template>
    <template v-else>
      <h1>{{ $t('projectNotFound') }}</h1>
    </template>
  </BBusy>
</template>
