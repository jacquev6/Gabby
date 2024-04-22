<script setup>
import { useApiStore } from '../../stores/api'
import { BBusy } from '../../components/opinion/bootstrap'


const api = useApiStore()

const projects = api.auto.getAll('projects')
</script>

<template>
  <BBusy :busy="projects.loading">
    <template v-if="projects.length">
      <ul>
        <li v-for="project in projects" :key="project.id">
          <RouterLink :to="{name: 'project', params: {projectId: project.id}}">{{ project.attributes.title }}</RouterLink>
        </li>
      </ul>
    </template>
    <p v-else>{{ $t('noProjectsForNow' )}}</p>
  </BBusy>
</template>
