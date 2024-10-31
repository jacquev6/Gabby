<script setup lang="ts">
import { ref, computed, reactive, watch } from 'vue'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'

import { BButton } from '$frontend/components/opinion/bootstrap'
import bc from '$frontend/components/breadcrumbs'
import ProjectTextbookPageLayout from './ProjectTextbookPageLayout.vue'
import { makeBoundingRectangle, makeBoundingRectangles } from './RectanglesHighlighter.vue'
import { useProjectTextbookPageData } from './ProjectTextbookPageLayout.vue'
import { useExerciseCreationHistoryStore } from './ExerciseCreationHistoryStore'
import { useApiStore } from '$frontend/stores/api'
import { makeModelInTextbook, assignModelFrom, save } from '$frontend/components/ExerciseFieldsForm.vue'
import { useGloballyBusyStore } from '$frontend/stores/globallyBusy'
import ExerciseColumns from './ExerciseColumns.vue'
import ExercisePdfOverlay from './ExercisePdfOverlay.vue'


const props = defineProps<{
  projectId: string
  textbookId: string
  page: number
  exerciseId: string
  displayedPage?: number
}>()
const projectId = computed(() => props.projectId)
const textbookId = computed(() => props.textbookId)
const page = computed(() => props.page)
const displayedPage = computed(() => props.displayedPage ?? props.page)

const router = useRouter()
const api = useApiStore()
const i18n = useI18n()
const globallyBusy = useGloballyBusyStore()
const exerciseCreationHistory = useExerciseCreationHistoryStore()

const { project, textbook, exercisesOnDisplayedPage, exercisesOnPageBeforeDisplayed } = useProjectTextbookPageData(projectId, textbookId, page, displayedPage)
globallyBusy.register('loading exercises on page', computed(() => exercisesOnDisplayedPage.value.loading))
globallyBusy.register('loading exercises on previous page', computed(() => exercisesOnPageBeforeDisplayed.value.loading))

function makeGreyRectangles(pdfSha256: string, pdfPage: number) {
  const otherExercises = [...exercisesOnPageBeforeDisplayed.value.existingItems,  ...exercisesOnDisplayedPage.value.existingItems].filter(exercise => exercise.id !== props.exerciseId)
  return makeBoundingRectangles(pdfSha256, pdfPage, otherExercises)
}

function changeDisplayedPage(newDisplayedPage: number) {
  if (newDisplayedPage === props.page) {
    router.replace({
      name: 'project-textbook-page-exercise',
      params: {},
    })
  } else {
    router.replace({
      name: 'project-textbook-page-exercise',
      params: {},
      query: {displayPage: newDisplayedPage},
    })
  }
}

const title = computed(() => {
  if (exercise.value.inCache && exercise.value.exists) {
    return [`Exercise ${exercise.value.attributes.number}`]
  } else {
    return [i18n.t('exerciseNotFound')]
  }
})

const breadcrumbs = computed(() => {
  if (exercise.value.inCache && exercise.value.exists) {
    return bc.last(
      `Exercise ${exercise.value.attributes.number}`,
      {name: 'project-textbook-page-exercise', params: {exerciseId: exercise.value.id}},
    )
  } else {
    return bc.last(i18n.t('exerciseNotFound'))
  }
})

const model = reactive(makeModelInTextbook(props.page))

const exercise = computed(() => api.auto.getOne('exercise', props.exerciseId))

const exerciseBelongsToTextbookPage = computed(() =>
  exercise.value.inCache && exercise.value.exists && exercise.value.relationships.textbook === textbook.value && exercise.value.attributes.textbookPage === props.page
)

function makeSurroundedRectangles(pdfSha256: string, pdfPage: number) {
  const boundingRectangle = makeBoundingRectangle(pdfSha256, pdfPage, model.rectangles)
  if (boundingRectangle === null) {
    return []
  } else {
    return [boundingRectangle]
  }
}

watch(
  [
    computed(() => exercise.value.inCache && exercise.value.exists ? exercise.value.attributes.number : null),
  ],
  () => {
    if (exercise.value.inCache && exercise.value.exists) {
      assignModelFrom(model, exercise.value)
      if (exerciseColumns.value !== null) {
        exerciseColumns.value.resetUndoRedo()
      }
    }
  },
  {immediate: true},
)

const fields = computed(() => {
  if (exerciseColumns.value === null) {
    return null
  } else {
    return exerciseColumns.value.fields
  }
})

function goToPrevious() {
  const exerciseId = exerciseCreationHistory.previous
  console.assert(exerciseId !== null)
  exerciseCreationHistory.rewind()
  router.push({
    name: 'project-textbook-page-exercise',
    params: {exerciseId},
  })
}

const busy = ref(false)
async function saveThenBack() {
  busy.value = true
  console.assert(exercise.value.inCache && exercise.value.exists)
  await save(exercise.value, model)
  busy.value = false

  router.push({
    name: 'project-textbook-page',
  })
}

async function saveThenNext() {
  busy.value = true
  console.assert(exercise.value.inCache && exercise.value.exists)
  await save(exercise.value, model)
  busy.value = false

  const exerciseId = exerciseCreationHistory.next
  exerciseCreationHistory.forward()
  if(exerciseId === null) {
    router.push({
      name: 'project-textbook-page-new-exercise',
    })
  } else {
    router.push({
      name: 'project-textbook-page-exercise',
      params: {exerciseId},
    })
  }
}

const exerciseColumns = ref<InstanceType<typeof ExerciseColumns> | null>(null)
const parsedExercise = computed(() => {
  if (exerciseColumns.value === null) {
    return null
  } else {
    return exerciseColumns.value.parsedExercise
  }
})
</script>

<template>
  <ProjectTextbookPageLayout
    :project :textbook :page :displayedPage @update:displayedPage="changeDisplayedPage"
    :title :breadcrumbs
  >
    <template #pdfOverlay="{ pdfFile, pdf, width, height, transform }">
      <ExercisePdfOverlay
        v-if="pdfFile.inCache && pdfFile.exists && fields !== null && parsedExercise !== null"
        :pdfFile :width :height :transform
        :greyRectangles="makeGreyRectangles(pdfFile.attributes.sha256, pdf.page.pageNumber)"
        :surroundedRectangles="makeSurroundedRectangles(pdfFile.attributes.sha256, pdf.page.pageNumber)"
        :pdf :fields :parsedExercise
        v-model="model"
      />
    </template>

    <template # v-if="exercise.inCache">
      <template v-if="exercise.exists && exerciseBelongsToTextbookPage">
        <ExerciseColumns ref="exerciseColumns" mode="edit" :projectId :displayedPage :busy v-model="model">
          <template #exerciseFieldsButtons>
            <template v-if="exerciseCreationHistory.current === null">
              <p>
                <RouterLink class="btn btn-secondary" :to="{name: 'project-textbook-page'}">{{ $t('backToList') }}</RouterLink>
                <BButton primary :disabled="fields === null || fields.saveDisabled" @click="saveThenBack" data-cy="save-then-back">{{ $t('saveThenBack') }}</BButton>
              </p>
            </template>
            <template v-else>
              <p>
                <BButton secondary :disabled="exerciseCreationHistory.previous === null" @click="goToPrevious">{{ $t('previous') }}</BButton>
                <BButton primary :disabled="fields === null || fields.saveDisabled" @click="saveThenNext" data-cy="save-then-next">{{ $t('saveThenNext') }}</BButton>
              </p>
              <p>
                <RouterLink class="btn btn-secondary" :to="{name: 'project-textbook-page'}">{{ $t('backToList') }}</RouterLink>
                <BButton secondary :disabled="fields === null || fields.saveDisabled" @click="saveThenBack" data-cy="save-then-back">{{ $t('saveThenBack') }}</BButton>
              </p>
            </template>
          </template>
        </ExerciseColumns>
      </template>
      <template v-else>
        <h1>{{ $t('exerciseNotFound') }}</h1>
      </template>
    </template>
  </ProjectTextbookPageLayout>
</template>
