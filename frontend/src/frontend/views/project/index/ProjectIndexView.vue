<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

import { BRow, BCol } from '$frontend/components/opinion/bootstrap'
import EditableProjectHeader from './EditableProjectHeader.vue'
import CreateTextbookForm from './CreateTextbookForm.vue'
import CreateExerciseForm from './CreateExerciseForm.vue'
import ExercisesList from './ExercisesList.vue'
import PdfPreview from '$frontend/components/PdfPreview.vue'
import type { Project } from '$frontend/types/api'
import type { InfoDoc } from '$frontend/stores/pdfs'


const router = useRouter()

const props = defineProps<{
  project: Project
  refreshProject: any/* @todo Type */
}>()

function goToTextbook(textbookId: string) {
  router.push({name: 'project-textbook-page-list-exercises', params: {projectId: props.project.id, textbookId, page: 1}})
}

const pdfToPreview = ref<InfoDoc | null>(null)

defineExpose({
  title: [],
  breadcrumbs: [],
})
</script>

<template>
  <EditableProjectHeader :project />
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
          <PdfPreview :pdf="pdfToPreview.document as any/* @todo Understand and fix typing issue*/" />
        </BCol>
      </BRow>
    </BCol>
    <BCol v-if="pdfToPreview === null">
      <h2>{{ $t('newIndependentExercise') }}</h2>
      <CreateExerciseForm :project @created="refreshProject" />
    </BCol>
    <BCol :w="4">
      <h2>{{ $t('existingTextbooksAndExercises') }}</h2>
      <ExercisesList :project />
    </BCol>
  </BRow>
</template>
