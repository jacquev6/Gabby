<script setup lang="ts">
import { useApiStore } from '$frontend/stores/api'
import { BBusy } from '$frontend/components/opinion/bootstrap'


const api = useApiStore()

const projects = api.auto.getAll('project')
</script>

<template>
  <BBusy :busy="projects.loading">
    <template v-if="projects.existingItems.length">
      <ul>
        <li v-for="project in projects.existingItems" :key="project.id">
          <RouterLink :to="{name: 'project', params: {projectId: project.id}}">{{ project.attributes.title }}</RouterLink>
        </li>
      </ul>
    </template>
    <p v-else>{{ $t('noProjectsForNow' )}}</p>
  </BBusy>
</template>
