<script setup>
import { useRouter } from 'vue-router'

import Layout from '../../components/layout.vue'
import { BRow, BCol } from '../../components/opinion/bootstrap'
import CreateProjectForm from './create-project-form.vue'
import ProjectsList from './projects-list.vue'


const router = useRouter()

function goToProject(project) {
  router.push({name: 'project', params: {projectId: project.id}})
}
</script>

<template>
  <layout title="MALIN">
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
  </layout>
</template>
