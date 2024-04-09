<script setup>
import { computed } from 'vue'

import Navbar from '../../components/navbar.vue'
import { useApiStore } from '../../stores/api'


const props = defineProps({
  projectId: {type: String, required: true},
})

const api = useApiStore()

const project = computed(() => api.cache.getOne('project', props.projectId))

const title = computed(() => {
  if (project.value?.exists) {
    return `MALIN - ${project.value.attributes.title}`
  } else {
    return 'MALIN'
  }
})

const breadcrumbs = computed(() => {
  if (project.value?.exists) {
    return [
      {title: project.value.attributes.title},
    ]
  } else {
    return []
  }
})
</script>

<template>
  <navbar :title :breadcrumbs></navbar>
</template>
