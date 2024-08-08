<script setup lang="ts">
import type { List } from '$frontend/stores/api'
import { BBusy } from '$frontend/components/opinion/bootstrap'


defineProps<{
  projects: List<'project'>
}>()
</script>

<template>
  <BBusy :busy="projects.loading" size="5em">
    <template v-if="projects.existingItems.length !== 0">
      <ul>
        <li v-for="project in projects.existingItems" :key="project.id">
          <RouterLink :to="{name: 'project', params: {projectId: project.id}}">{{ project.attributes.title }}</RouterLink>
        </li>
      </ul>
    </template>
    <p v-else-if="projects.inCache">{{ $t('noProjectsForNow' )}}</p>
  </BBusy>
</template>
