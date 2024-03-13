<script setup>
import { ref, computed } from 'vue'
import { RouterLink, useRouter } from 'vue-router'

import { useApiStore } from '../stores/api'
import { BBusy, BLabeledInput, BLabeledTextarea, BRow, BCol, BButton } from '../components/opinion/bootstrap'


const router = useRouter()
const api = useApiStore()

const projects = api.auto.getAll('projects')

const newProjectTitle = ref('')
const newProjectDescription = ref('')
const createProjectDisabled = computed(() => !newProjectTitle.value)
const creatingProject = ref(false)
async function createProject() {
  creatingProject.value = true
  const project = await api.client.post(
    'project',
    {title: newProjectTitle.value, description: newProjectDescription.value},
    {textbooks: [], exercises: []},
  )
  creatingProject.value = false
  newProjectTitle.value = ''
  newProjectDescription.value = ''
  router.push({name: 'project', params: {projectId: project.id}})
}
</script>

<template>
  <b-row>
    <b-col>
      <h1>{{ $t('newProject') }}</h1>
      <b-busy :busy="creatingProject">
        <b-labeled-input v-model="newProjectTitle" :label="$t('title')" />
        <b-labeled-textarea v-model="newProjectDescription" :label="$t('description')" />
        <b-button primary @click="createProject" :disabled="createProjectDisabled">{{ $t('createProject' )}}</b-button>
      </b-busy>
    </b-col>
    <b-col>
      <h1>{{ $t('existingProjects' )}}</h1>
      <b-busy :busy="projects.loading">
        <template v-if="projects.length">
          <ul>
            <li v-for="project in projects" :key="project.id">
              <router-link :to="{name: 'project', params: {projectId: project.id}}">{{ project.attributes.title }}</router-link>
            </li>
          </ul>
        </template>
        <p v-else>{{ $t('noProjectsForNow' )}}</p>
      </b-busy>
    </b-col>
  </b-row>
</template>
