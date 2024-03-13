<script setup>
import { ref, computed } from 'vue'
import { computedAsync } from '@vueuse/core'
import { RouterLink, useRouter } from 'vue-router'

import { useApiStore } from '../stores/api'
import { BBusy, BLabeledInput, BLabeledTextarea, BRow, BCol, BButton } from '../components/opinion/bootstrap'


const router = useRouter()
const api = useApiStore()

const projectsCreated = ref(0)
const loadingProjects = ref(false)
const projects = computedAsync(
  async () => {
    projectsCreated.value  // Dependency for reactivity
    // await new Promise(r => setTimeout(r, 1000))
    return await api.client.getAll('projects')
  },
  [],
  loadingProjects,
)


const newProjectTitle = ref('')
const newProjectDescription = ref('')
const createProjectDisabled = computed(() => !newProjectTitle.value || !newProjectDescription.value)
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
      <h1>Nouveau projet</h1>
      <b-busy :busy="creatingProject">
        <b-labeled-input v-model="newProjectTitle" label="Titre" />
        <b-labeled-textarea v-model="newProjectDescription" label="Description" />
        <b-button primary @click="createProject" :disabled="createProjectDisabled">Créer</b-button>
      </b-busy>
    </b-col>
    <b-col>
      <h1>Projets existants</h1>
      <b-busy :busy="loadingProjects">
        <template v-if="projects.length">
          <ul>
            <li v-for="project in projects" :key="project.id">
              <router-link :to="{name: 'project', params: {projectId: project.id}}">{{ project.attributes.title }}</router-link>
            </li>
          </ul>
        </template>
        <p v-else>Aucun projet pour le moment.</p>
      </b-busy>
    </b-col>
  </b-row>
</template>
