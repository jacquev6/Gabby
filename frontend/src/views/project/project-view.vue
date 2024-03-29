<script setup>
import { ref, computed } from 'vue'
import { computedAsync } from '@vueuse/core'
import { useRouter } from 'vue-router'

import { useApiStore } from '../../stores/api'
import Layout from '../../components/layout.vue'
import { BBusy, BRow, BCol } from '../../components/opinion/bootstrap'
import EditableProjectHeader from './editable-project-header.vue'
import CreateTextbookForm from './create-textbook-form.vue'
import CreateExerciseForm from './create-exercise-form.vue'
import ExercisesList from './exercises-list.vue'
import PdfPreview from '../../components/pdf-preview.vue'


const api = useApiStore()
const router = useRouter()

const props = defineProps({
  projectId: {type: String, required: true},
})

function goToTextbook(textbookId) {
  router.push({name: 'project-textbook-page', params: {projectId: props.projectId, textbookId, page: 1}})
}

const exercisesCreated = ref(0)
const projectLoading = ref(false)
const project = computedAsync(
  async () => {
    ++exercisesCreated.value  // Dependency for reactivity
    return await api.client.getOne('project', props.projectId, {include: ['textbooks', 'exercises.textbook']})
  },
  null,
  projectLoading,
)

const breadcrumbs = computed(() => {
  if (project.value?.exists) {
    return [
      {title: project.value.attributes.title},
    ]
  } else {
    return []
  }
})

const title = computed(() => {
  if (project.value?.exists) {
    return `MALIN - ${project.value.attributes.title}`
  } else {
    return 'MALIN'
  }
})

const pdfToPreview = ref(null)
</script>

<template>
  <layout :title="title" :breadcrumbs="breadcrumbs">
    <b-busy :busy="projectLoading">
      <template v-if="project?.exists">
        <editable-project-header :project="project" />
        <p>{{ $t('download') }} <a :href="`/api/project-${project.id}-extraction-report.json`">{{ $t('theExtractionReport') }}</a>.</p>
        <b-row>
          <b-col>
            <h2>{{ $t('newTextbook') }}</h2>
            <b-row>
              <b-col>
                <create-textbook-form
                  :projectId="project.id"
                  @loadedPdf="pdf => pdfToPreview = pdf"
                  @unloadedPdf="pdfToPreview = null"
                  @created="goToTextbook"
                />
              </b-col>
              <b-col v-if="pdfToPreview !== null" :w="6">
                <pdf-preview :pdf="pdfToPreview.document" />
              </b-col>
            </b-row>
          </b-col>
          <b-col v-if="pdfToPreview === null">
            <h2>{{ $t('newIndependentExercise') }}</h2>
            <create-exercise-form :project="project" @created="++exercisesCreated" />
          </b-col>
          <b-col :w="4">
            <h2>{{ $t('existingTextbooksAndExercises') }}</h2>
            <exercises-list :project="project" />
          </b-col>
        </b-row>
      </template>
      <template v-else>
        <h1>{{ $t('projectNotFound') }}</h1>
      </template>
    </b-busy>
  </layout>
</template>
