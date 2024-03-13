<script setup>
import { ref, computed } from 'vue'
import { computedAsync } from '@vueuse/core'
import { RouterLink, useRouter } from 'vue-router'

import { useApiStore } from '../stores/api'
import { usePdfsStore } from '../stores/pdfs'
import { BBusy, BLabeledInput, BRow, BCol, BButton } from '../components/opinion/bootstrap'


const pdfs = usePdfsStore()
const api = useApiStore()
const router = useRouter()

const props = defineProps({
  projectId: {type: String, required: true},
})


const newTextbookPdf = ref(null)
const loadingPdf = ref(false)
async function loadPdf(source) {
  loadingPdf.value = true
  newTextbookPdf.value = await pdfs.open(source)
  loadingPdf.value = false
}
const newTextbookTitle = ref('')
const newTextbookPublisher = ref('')
const newTextbookYear = ref('')
const newTextbookIsbn = ref('')
const createTextbookDisabled = computed(() => !newTextbookPdf.value || !newTextbookTitle.value || !newTextbookPublisher.value || !newTextbookYear.value || !newTextbookIsbn.value)
const creatingTextbook = ref(false)
async function createTextbook() {
  creatingTextbook.value = true
  const pdfFile = await api.client.post(
    'pdfFile',
    {sha256: newTextbookPdf.value.info.sha256, bytesCount: 0, pagesCount: newTextbookPdf.value.document.numPages},
    {namings: [], sections: []},
  )
  await api.client.post(
    'pdfFileNaming',
    {name: newTextbookPdf.value.info.name},
    {pdfFile},
  )
  const textbook = await api.client.post(
    'textbook',
    {title: newTextbookTitle.value, publisher: newTextbookPublisher.value, year: newTextbookYear.value, isbn: newTextbookIsbn.value},
    {project: {type: 'project', id: props.projectId}, exercises: [], sections: []}
  )
  await api.client.post(
    'section',
    {pdfFileStartPage: 1, pagesCount: newTextbookPdf.value.document.numPages, textbookStartPage: 1},
    {pdfFile, textbook},
  )
  creatingTextbook.value = false
  router.push({name: 'project-textbook-page', params: {projectId: props.projectId, textbookId: textbook.id, page: 1}})
}


const projectLoading = ref(false)
const project = computedAsync(
  async () => {
    return await api.client.getOne('project', props.projectId, {include: ['textbooks', 'exercises.textbook']})
  },
  null,
  projectLoading,
)

const exercisesByTextbookAndPage = computed(() => {
  const textbooks = {}
  for (const exercise of project.value?.relationships.exercises) {
    const textbook = exercise.relationships.textbook
    if (textbook) {
      textbooks[textbook.id] = textbooks[textbook.id] ?? { textbook, pages: [] }
      const page = exercise.attributes.textbookPage
      textbooks[textbook.id].pages[page] = textbooks[textbook.id].pages[page] ?? []
      textbooks[textbook.id].pages[page].push(exercise)
    }
  }
  return textbooks
})

const independentExercises = computed(() => {
  const exercises = []
  for (const exercise of project.value?.relationships.exercises) {
    if (!exercise.relationships.textbook) {
      exercises.push(exercise)
    }
  }
  return exercises
})

function ellipsis(s) {
  return s.length > 25 ? s.slice(0, 25) + '…' : s
}
</script>

<template>
  <b-busy :busy="projectLoading">
    <h1>Projet "{{ project?.attributes.title }}"</h1>
    <p>{{ project?.attributes.description }}</p>
    <p>Téléchargez <a :href="`/api/project-${props.projectId}-extraction-report.json`">le rapport d'extraction</a>.</p>
    <b-row>
      <b-col>
        <h2>Nouveau manuel</h2>
        <b-busy :busy="creatingTextbook">
          <b-busy :busy="loadingPdf">
            <b-labeled-input :label="$t('inputFile')" type="file" accept=".pdf" @change="(e) => loadPdf(e.target.files[0])" />
          </b-busy>
          <b-labeled-input label="Titre" v-model="newTextbookTitle"/>
          <b-labeled-input label="Éditeur" v-model="newTextbookPublisher"/>
          <b-labeled-input label="Année" type="number" v-model="newTextbookYear"/>
          <b-labeled-input label="ISBN" v-model="newTextbookIsbn"/>
          <b-button primary @click="createTextbook" :disabled="createTextbookDisabled">Créer</b-button>
        </b-busy>
      </b-col>
      <b-col>
        <h2>Nouvel exercice indépendant</h2>
        <p>({{ $t('not-yet-implemented') }})</p>
      </b-col>
      <b-col>
        <h2>Exercices existants</h2>
        <template v-if="project?.relationships.textbooks.length || project?.relationships.exercises.length">
          <template v-if="independentExercises.length">
            <h3>Indépendants</h3>
            <ul>
              <li v-for="exercise in independentExercises">
                <strong>{{ exercise.attributes.number }}</strong> : {{ ellipsis(exercise.attributes.instructions) }}
              </li>
            </ul>
          </template>
          <template v-for="textbook in project.relationships.textbooks">
            <h3><router-link :to="{name: 'project-textbook-page', params: {projectId, textbookId: textbook.id, page: 1}}">{{ textbook.attributes.title }}</router-link>, {{ textbook.attributes.publisher }} ({{ textbook.attributes.year }})</h3>
            <template v-if="exercisesByTextbookAndPage[textbook.id]">
              <ul v-for="[page, exercises] of Object.entries(exercisesByTextbookAndPage[textbook.id]?.pages)">
                <li>
                  <router-link :to="{name: 'project-textbook-page', params: {projectId, textbookId: textbook.id, page}}">Page {{ page }}</router-link>
                  <ul>
                    <li v-for="exercise in exercises">
                    <strong>{{ exercise.attributes.number }}</strong> : {{ ellipsis(exercise.attributes.instructions) }}
                  </li>
                  </ul>
                </li>
              </ul>
            </template>
          </template>
        </template>
        <p v-else>Aucun exercice pour le moment.</p>
      </b-col>
    </b-row>
  </b-busy>
</template>
