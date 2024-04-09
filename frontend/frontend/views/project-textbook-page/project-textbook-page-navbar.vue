<script setup>
import { computed } from 'vue'

import Navbar from '../../components/navbar.vue'
import { useApiStore } from '../../stores/api'


const props = defineProps({
  projectId: {type: String, required: true},
  textbookId: {type: String, required: true},
  page: {type: Number, required: true},
})

const api = useApiStore()

const project = computed(() => api.cache.getOne('project', props.projectId))

const projectTitle = computed(() => {
  if (project.value.inCache && project.value.exists) {
    return project.value.attributes.title
  } else {
    return null
  }
})

const textbook = computed(() => {
  const textbook = api.cache.getOne('textbook', props.textbookId)
  if (textbook.inCache && textbook.exists && textbook.relationships.project.id === props.projectId) {
    return textbook
  } else {
    return null
  }
})

const textbookTitle = computed(() => {
  if (textbook.value && textbook.value.inCache && textbook.value.exists) {
    return textbook.value.attributes.title
  } else {
    return null
  }
})

const title = computed(() => {
  if (projectTitle.value && textbookTitle.value) {
    return `MALIN - ${projectTitle.value} - ${textbookTitle.value} - Page ${props.page}`
  } else {
    return 'MALIN'
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
</script>

<template>
  <navbar :title :breadcrumbs></navbar>
</template>
