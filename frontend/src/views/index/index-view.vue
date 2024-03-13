<script setup>
import { useRouter } from 'vue-router'

import { BRow, BCol } from '../../components/opinion/bootstrap'
import CreateProjectForm from './create-project-form.vue'
import ProjectsList from './projects-list.vue'


const router = useRouter()

function goToProject(projectId) {
  router.push({name: 'project', params: {projectId}})
}
</script>

<template>
  <b-row>
    <b-col>
      <h1>{{ $t('newProject') }}</h1>
      <create-project-form @created="goToProject" />
    </b-col>
    <b-col>
      <h1>{{ $t('existingProjects' )}}</h1>
      <projects-list />
    </b-col>
  </b-row>
</template>
