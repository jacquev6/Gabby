<script setup lang="ts">
import { computed } from 'vue'
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'

import bc from '$frontend/components/breadcrumbs'
import ProjectTextbookPageLayout from './ProjectTextbookPageLayout.vue'
import RectanglesHighlighter, { makeBoundingRectangles } from './RectanglesHighlighter.vue'
import { useProjectTextbookPageData } from './ProjectTextbookPageLayout.vue'
import ExercisesList from './ExercisesList.vue'
import { useExerciseCreationHistoryStore } from './ExerciseCreationHistoryStore'


const props = defineProps<{
  projectId: string
  textbookId: string
  page: number
}>()
const projectId = computed(() => props.projectId)
const textbookId = computed(() => props.textbookId)
const page = computed(() => props.page)

const router = useRouter()
const exerciseCreationHistory = useExerciseCreationHistoryStore()

onMounted(() => {
  exerciseCreationHistory.reset()
})

const { project, textbook, exercises } = useProjectTextbookPageData(projectId, textbookId, page)

const greyRectangles = computed(() => makeBoundingRectangles(exercises.value.existingItems))

function changePage(page: number) {
  router.push({name: 'project-textbook-page', params: {page}})
}
</script>

<template>
  <ProjectTextbookPageLayout
    :project :textbook :page :displayPage="page" @update:displayPage="changePage"
    :title="[]" :breadcrumbs="bc.empty"
  >
    <template #pdfOverlay="{ width, height, transform }">
      <RectanglesHighlighter
        class="img w-100" style="position: absolute; top: 0; left: 0"
        :width :height :transform
        :greyRectangles :surroundedRectangles="[]"
      />
    </template>

    <h1>{{ $t('existingExercises') }}</h1>
    <p style="margin-left: 5em">
      <RouterLink class="btn btn-primary btn-lg" :to="{name: 'project-textbook-page-new-exercise'}" data-cy="new-exercise">
        {{ $t('create') }}
      </RouterLink>
    </p>
    <ExercisesList :exercises />
  </ProjectTextbookPageLayout>
</template>
