<script setup lang="ts">
import { computed } from 'vue'

import { useApiStore } from '$frontend/stores/api'
import { BBusy } from '$frontend/components/opinion/bootstrap'
import type { Project, InCache, Exists } from '$frontend/stores/api'


const api = useApiStore()

const allProjects = api.auto.getAll('project')

const existingProjects = computed(() => allProjects.items.filter((project): project is Project & InCache & Exists => project.inCache && project.exists))
</script>

<template>
  <BBusy :busy="allProjects.loading">
    <template v-if="existingProjects.length">
      <ul>
        <li v-for="project in existingProjects" :key="project.id">
          <RouterLink :to="{name: 'project', params: {projectId: project.id}}">{{ project.attributes.title }}</RouterLink>
        </li>
      </ul>
    </template>
    <p v-else>{{ $t('noProjectsForNow' )}}</p>
  </BBusy>
</template>
