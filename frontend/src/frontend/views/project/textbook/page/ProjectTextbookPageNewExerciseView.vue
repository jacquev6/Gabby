<script setup lang="ts">
import { ref, computed, reactive } from 'vue'
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'

import { BButton, BLabeledRadios } from '$frontend/components/opinion/bootstrap'
import bc from '$frontend/components/breadcrumbs'
import ProjectTextbookPageLayout from './ProjectTextbookPageLayout.vue'
import { makeBoundingRectangle, makeBoundingRectangles } from './RectanglesHighlighter.vue'
import { useProjectTextbookPageData } from './ProjectTextbookPageLayout.vue'
import { useExerciseCreationHistoryStore } from './ExerciseCreationHistoryStore'
import { useApiStore } from '$frontend/stores/api'
import ToolsGutter from './ToolsGutter.vue'
import UndoRedoTool from './UndoRedoTool.vue'
import AdaptationDetailsFieldsForm from '$frontend/components/AdaptationDetailsFieldsForm.vue'
import { makeModelInTextbook, resetModelInTextbook, modelIsEmpty, create, suggestNextNumber } from '$frontend/components/ExerciseFieldsForm.vue'
import BasicFormattingTools from './BasicFormattingTools.vue'
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

function changeDisplayedPage(newDisplayedPage: number) {
  if (modelIsEmpty(model)) {
    exerciseCreationHistory.reset()
    router.push({name: 'project-textbook-page-new-exercise', params: {page: newDisplayedPage}})
    model.textbookPage = newDisplayedPage
  } else {
    router.replace({
      name: 'project-textbook-page-new-exercise',
      params: {},
      query: {displayPage: newDisplayedPage},
    })
  }
}

const title = computed(() => [i18n.t('create')])

const breadcrumbs = computed(() => bc.last(i18n.t('create')))

const model = reactive(makeModelInTextbook(page.value))
const wysiwyg = computed(() => {
  if (exerciseColumns.value === null) {
    return false
  } else {
    return exerciseColumns.value.wysiwyg
  }
})

const resetUndoRedo = ref(0)

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
    resetUndoRedo.value++
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
  resetUndoRedo.value++
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
    resetUndoRedo.value++
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

const toolSlotNames = computed(() => {
  const names = []
  names.push('undoRedo')
  if (model.adaptationKind !== 'null') {
    names.push('adaptationDetails')
  }
  if (wysiwyg.value) {
    names.push('basicFormatting')
  }
  names.push('repartition')
  return names
})

const wordingParagraphsPerPageletOptions = [1, 2, 3, 4, 5].map(value => ({
  label: i18n.t('exerciseLinesPerPage', {lines: value}),
  value,
}))
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

        <template #gutter>
          <div class="h-100 overflow-hidden d-flex flex-row position-relative" id="gutter-2">
            <div class="handle"></div>
            <div class="h-100 overflow-auto flex-fill" data-cy="gutter-2">
              <div style="position: relative">
                <div>
                  <ToolsGutter :slotNames="toolSlotNames">
                    <template #undoRedo>
                      <UndoRedoTool v-model="model" :reset="resetUndoRedo" />
                    </template>
                    <template #adaptationDetails>
                      <AdaptationDetailsFieldsForm v-if="fields !== null" v-model="model" :wysiwyg :fields/>
                    </template>
                    <template #basicFormatting>
                      <BasicFormattingTools v-if="fields !== null" v-model="model" :fields />
                    </template>
                    <template #repartition>
                      <BLabeledRadios :label="$t('exerciseRepartition')" v-model="model.wordingParagraphsPerPagelet" :options="wordingParagraphsPerPageletOptions" />
                    </template>
                  </ToolsGutter>
                </div>
                <div
                  v-if="model.inProgress.kind === 'multipleChoicesCreation'"
                  style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.5); cursor: initial;"
                  @mousedown="e => e.stopPropagation()" @touchstart="e => e.stopPropagation()"
                >
                  <div style="position: absolute; top: 50%; left: 10%; width: 80%; transform: translate(0, -50%); background-color: white; padding: 1em;">
                    {{ $t('multipleChoicesInstructions') }}
                    <BButton secondary sm @click="model.inProgress = {kind: 'nothing'}">{{ $t('choicesSettingsCancel') }}</BButton>
                  </div>
                </div>
              </div>
            </div>
            <div class="handle"></div>
          </div>
        </template>
      </ExerciseColumns>
    </template>
  </ProjectTextbookPageLayout>
</template>
