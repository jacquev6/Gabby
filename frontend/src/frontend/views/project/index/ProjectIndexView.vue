<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

import { BRow, BCol } from '../../../components/opinion/bootstrap'
import EditableProjectHeader from './EditableProjectHeader.vue'
import CreateTextbookForm from './CreateTextbookForm.vue'
import CreateExerciseForm from './CreateExerciseForm.vue'
import ExercisesList from './ExercisesList.vue'
import PdfPreview from '../../../components/PdfPreview.vue'


const router = useRouter()

const props = defineProps({
  project: {
    type: Object,
    required: true,
  },
  refreshProject: {
    type: Function,
    required: true,
  },
})

function goToTextbook(textbookId) {
  router.push({name: 'project-textbook-page-list-exercises', params: {projectId: props.projectId, textbookId, page: 1}})
}

const pdfToPreview = ref(null)

defineExpose({
  title: [],
  breadcrumbs: [],
})
</script>

<template>
  <EditableProjectHeader :project="project" />
  <p>{{ $t('download') }} <a :href="`/api/project-${project.id}.html`">{{ $t('theExportedHtml') }}</a>.</p>
  <p>{{ $t('download') }} <a :href="`/api/project-${project.id}-extraction-report.json`" download>{{ $t('theExtractionReport') }}</a>.</p>
  <BRow>
    <BCol>
      <h2>{{ $t('newTextbook') }}</h2>
      <BRow>
        <BCol>
          <CreateTextbookForm
            :projectId="project.id"
            @loadedPdf="pdf => pdfToPreview = pdf"
            @unloadedPdf="pdfToPreview = null"
            @created="goToTextbook"
          />
        </BCol>
        <BCol v-if="pdfToPreview !== null" :w="6">
          <PdfPreview :pdf="pdfToPreview.document" />
        </BCol>
      </BRow>
    </BCol>
    <BCol v-if="pdfToPreview === null">
      <h2>{{ $t('newIndependentExercise') }}</h2>
      <CreateExerciseForm :project="project" @created="refreshProject" />
    </BCol>
    <BCol :w="4">
      <h2>{{ $t('existingTextbooksAndExercises') }}</h2>
      <ExercisesList :project="project" />
    </BCol>
  </BRow>
</template>
