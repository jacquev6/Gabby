<script setup>
import { ref, computed } from 'vue'
import { computedAsync } from '@vueuse/core'

import { useApiStore } from '../../stores/api'
import { BBusy } from '../../components/opinion/bootstrap'


const props = defineProps({
  projectId: {type: String, required: true},
  textbookId: {type: String, required: true},
  page: {type: Number, required: true},
})

const api = useApiStore()

const projectLoading = ref(false)
const project = computedAsync(
  async () => {
    return await api.client.getOne('project', props.projectId)
  },
  null,
  projectLoading,
)

const projectTitle = computed(() => {
  if (project.value?.inCache && project.value?.exists) {
    return project.value.attributes.title
  } else {
    return null
  }
})

const textbookLoading = ref(false)
const textbook = computedAsync(
  async () => {
    const textbook = await api.client.getOne('textbook', props.textbookId, {include: 'sections.pdfFile.namings'})
    if (textbook.relationships.project.id === props.projectId) {
      return textbook
    } else {
      return null
    }
  },
  null,
  textbookLoading,
)

const textbookTitle = computed(() => {
  if (textbook.value?.inCache && textbook.value?.exists) {
    return textbook.value.attributes.title
  } else {
    return null
  }
})

const title = computed(() => {
  if (projectTitle.value && textbookTitle.value) {
    return ['MALIN', projectTitle.value, textbookTitle.value, `Page ${props.page}`]
  } else {
    return ['MALIN']
  }
})

const breadcrumbs = computed(() => {
  if (projectTitle.value && textbookTitle.value) {
    return [
      {title: projectTitle.value, to: {name: 'project', params: {projectId: props.projectId}}},
      {title: textbookTitle.value},
    ]
  } else {
    return []
  }
})

defineExpose({
  title,
  breadcrumbs,
})
</script>

<template>
  <b-busy size="11rem" :busy="projectLoading || textbookLoading">
    <template v-if="!project?.exists">
      <h1>{{ $t('projectNotFound') }}</h1>
    </template>
    <template v-else-if="!textbook?.exists">
      <h1>{{ $t('textbookNotFound') }}</h1>
    </template>
    <template v-else>
      <router-view :project :textbook :page></router-view>
    </template>
  </b-busy>
</template>
