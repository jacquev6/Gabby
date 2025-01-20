<script setup lang="ts">
import { ref, computed, reactive, nextTick } from 'vue'
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { watchPausable } from '@vueuse/core'

import { BButton } from '$frontend/components/opinion/bootstrap'
import bc from '$frontend/components/breadcrumbs'
import ProjectTextbookPageLayout from './ProjectTextbookPageLayout.vue'
import { makeBoundingRectangle, makeBoundingRectangles } from './RectanglesHighlighter.vue'
import { useProjectTextbookPageData } from './ProjectTextbookPageLayout.vue'
import { useExerciseCreationHistoryStore } from './ExerciseCreationHistoryStore'
import { useApiStore } from '$frontend/stores/api'
import { makeModelInTextbook, resetModelInTextbook, modelIsEmpty, create, suggestNextNumber } from '$frontend/components/ExerciseFieldsForm.vue'
import { useGloballyBusyStore } from '$frontend/stores/globallyBusy'
import ConfirmationModal from '$frontend/components/ConfirmationModal.vue'
import ExerciseColumns from './ExerciseColumns.vue'
import ExercisePdfOverlay from './ExercisePdfOverlay.vue'


const props = defineProps<{
  projectId: string
  textbookId: string
  page: number
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

const { project, textbook, exercisesOnPage, exercisesOnDisplayedPage, exercisesOnPageBeforeDisplayed } = useProjectTextbookPageData(projectId, textbookId, page, displayedPage)
globallyBusy.register('loading exercises on page', computed(() => exercisesOnDisplayedPage.value.loading))
globallyBusy.register('loading exercises on previous page', computed(() => exercisesOnPageBeforeDisplayed.value.loading))

function makeGreyRectangles(pdfSha256: string, pdfPage: number) {
  return makeBoundingRectangles(pdfSha256, pdfPage, [...exercisesOnPageBeforeDisplayed.value.existingItems, ...exercisesOnDisplayedPage.value.existingItems])
}

const model = reactive(makeModelInTextbook(page.value))

const matchingExercises = computed(() => {
  if (model.number === '') {
    return null
  } else {
    return api.auto.getAll(
      'exercise',
      {
        filters: {
          textbook: textbook.value.id,
          textbookPage: props.page.toString(),
          number: model.number,
        }
      },
    )
  }
})

const alreadyExists = computed(() => matchingExercises.value !== null && matchingExercises.value.existingItems.length === 1)

async function changeDisplayedPage(newDisplayedPage: number) {
  if (modelIsEmpty(model)) {
    exerciseCreationHistory.reset()
    router.push({name: 'project-textbook-page-new-exercise', params: {page: newDisplayedPage}})
    watcherForModelTextbookPage.pause()
    model.textbookPage = newDisplayedPage
    await nextTick()
    watcherForModelTextbookPage.resume()
  } else {
    router.replace({
      name: 'project-textbook-page-new-exercise',
      params: {},
      query: {displayPage: newDisplayedPage},
    })
  }
}

const watcherForModelTextbookPage = watchPausable(() => model.textbookPage, newTextbookPage => {
  console.assert(newTextbookPage !== null)
  if (newTextbookPage === displayedPage.value) {
    router.replace({
      name: 'project-textbook-page-new-exercise',
      params: {page: newTextbookPage},
      query: {},
    })
  } else {
    router.replace({
      name: 'project-textbook-page-new-exercise',
      params: {
        page: newTextbookPage,
      },
      query: {displayPage: displayedPage.value},
    })
  }
})

const title = computed(() => [i18n.t('create')])

const breadcrumbs = computed(() => bc.last(i18n.t('create')))

function makeSurroundedRectangles(pdfSha256: string, pdfPage: number) {
  const boundingRectangle = makeBoundingRectangle(pdfSha256, pdfPage, model.rectangles)
  if (boundingRectangle === null) {
    return []
  } else {
    return [boundingRectangle]
  }
}

onMounted(() => {
  if (exerciseCreationHistory.suggestedNumber !== null) {
    model.number = exerciseCreationHistory.suggestedNumber
    console.assert(exerciseColumns.value !== null)
    exerciseColumns.value.resetUndoRedo()
  }
})

const fields = computed(() => {
  if (exerciseColumns.value === null) {
    return null
  } else {
    return exerciseColumns.value.fields
  }
})

function skip() {
  const suggestedNextNumber = suggestNextNumber(model.number)
  resetModelInTextbook(model, page.value)
  model.number = suggestedNextNumber
  console.assert(exerciseColumns.value !== null)
  exerciseColumns.value.resetUndoRedo()
}

const pageMismatchConfirmationModal = ref<InstanceType<typeof ConfirmationModal> | null>(null)

async function confirmCreationInCaseOfPageMismatch() {
  const skipConfirmation = model.textbookPage === displayedPage.value
  console.assert(pageMismatchConfirmationModal.value !== null)
  return skipConfirmation || await pageMismatchConfirmationModal.value.show()
}

const busy = ref(false)
async function createThenNext() {
  if (await confirmCreationInCaseOfPageMismatch()) {
    const suggestedNextNumber = suggestNextNumber(model.number)
    busy.value = true
    const exercise = await create(project.value, textbook.value, model)
    busy.value = false

    exerciseCreationHistory.push(exercise.id)

    /* no await */ exercisesOnPage.value.refresh()

    resetModelInTextbook(model, page.value)
    model.number = suggestedNextNumber
    model.textbookPage = displayedPage.value
    exerciseCreationHistory.suggestedNumber = suggestedNextNumber
    console.assert(exerciseColumns.value !== null)
    exerciseColumns.value.resetUndoRedo()
    router.push({name: 'project-textbook-page-new-exercise', params: {page: displayedPage.value}})
  }
}

async function createThenBack() {
  if (await confirmCreationInCaseOfPageMismatch()) {
    busy.value = true
    await create(project.value, textbook.value, model)
    busy.value = false
    /* no await */ exercisesOnPage.value.refresh()
    router.push({name: 'project-textbook-page'})
  }
}

function goToPrevious() {
  const exerciseId = exerciseCreationHistory.previous
  console.assert(exerciseId !== null)
  exerciseCreationHistory.rewind()
  router.push({
    name: 'project-textbook-page-exercise',
    params: {exerciseId},
  })
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
  <ConfirmationModal ref="pageMismatchConfirmationModal">{{ $t('pageMismatchConfirmationMessage') }}</ConfirmationModal>
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

    <template #>
      <ExerciseColumns ref="exerciseColumns" mode="create" :projectId :displayedPage :busy v-model="model">
        <template #exerciseFieldsOverlay>
          <div v-if="alreadyExists" style="position: absolute; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.8);" class="text-center">
            <div style="position: absolute; left: 25%; top: 25%; width: 50%; height: 50%; background-color: white">
              <p>{{ $t('exerciseAlreadyExists', {number: model.number}) }}</p>
              <p>
                <BButton primary @click="skip">{{ $t('skipExercise') }}</BButton>
              </p>
            </div>
          </div>
        </template>

        <template #exerciseFieldsButtons>
          <p>
            <BButton secondary :disabled="exerciseCreationHistory.previous === null" @click="goToPrevious">{{ $t('previous') }}</BButton>
            <BButton primary :disabled="fields === null || fields.saveDisabled || alreadyExists" @click="createThenNext" data-cy="create-then-next">{{ $t('saveThenNext') }}</BButton>
          </p>
          <p>
            <RouterLink class="btn btn-secondary" :to="{name: 'project-textbook-page'}">{{ $t('backToList') }}</RouterLink>
            <BButton secondary :disabled="fields === null || fields.saveDisabled || alreadyExists" @click="createThenBack" data-cy="create-then-back">{{ $t('saveThenBack') }}</BButton>
          </p>
        </template>
      </ExerciseColumns>
    </template>
  </ProjectTextbookPageLayout>
</template>
