<script setup lang="ts">
import { useRouter } from 'vue-router'

import { BRow, BCol } from '$frontend/components/opinion/bootstrap'
import CreateProjectForm from './CreateProjectForm.vue'
import ProjectsList from './ProjectsList.vue'
import type { Project } from '$frontend/types/api'


const router = useRouter()

function goToProject(project: Project) {
  router.push({name: 'project', params: {projectId: project.id}})
}

defineExpose({
  title: [],
  breadcrumbs: [],
})
</script>

<template>
  <BRow>
    <BCol>
      <h1>{{ $t('newProject') }}</h1>
      <CreateProjectForm @created="goToProject" />
    </BCol>
    <BCol>
      <h1>{{ $t('existingProjects' )}}</h1>
      <ProjectsList />
    </BCol>
  </BRow>
</template>
