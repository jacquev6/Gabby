<script setup lang="ts">
import { ref, computed, reactive, watch } from 'vue'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'

import { BButton, BBusy, BLabeledRadios } from '$frontend/components/opinion/bootstrap'
import bc from '$frontend/components/breadcrumbs'
import ProjectTextbookPageLayout from './ProjectTextbookPageLayout.vue'
import { makeBoundingRectangle, makeBoundingRectangles } from './RectanglesHighlighter.vue'
import { useProjectTextbookPageData } from './ProjectTextbookPageLayout.vue'
import ExerciseFieldsForm from '$frontend/components/ExerciseFieldsForm.vue'
import { useExerciseCreationHistoryStore } from './ExerciseCreationHistoryStore'
import { useApiStore } from '$frontend/stores/api'
import ToolsGutter from './ToolsGutter.vue'
import UndoRedoTool from './UndoRedoTool.vue'
import AdaptationDetailsFieldsForm from '$frontend/components/AdaptationDetailsFieldsForm.vue'
import { makeModelInTextbook, assignModelFrom, save } from '$frontend/components/ExerciseFieldsForm.vue'
import BasicFormattingTools from './BasicFormattingTools.vue'
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
const wantWysiwyg = ref(true)
const wysiwyg = computed(() => wantWysiwyg.value)

const resetUndoRedo = ref(0)

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
      resetUndoRedo.value++
    }
  },
  {immediate: true},
)

const fields = ref<InstanceType<typeof ExerciseFieldsForm> | null>(null)

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

const deltas = computed(() => {
  if (exerciseColumns.value === null) {
    return null
  } else {
    return exerciseColumns.value.deltas
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
        <ExerciseColumns ref="exerciseColumns" :projectId v-model="model">
          <template #left>
            <div class="h-100 overflow-auto position-relative" id="left-col-2" data-cy="left-col-2">
              <h1>{{ $t('edition') }}  <span style="font-size: small">(<label>WYSIWYG: <input type="checkbox" v-model="wantWysiwyg" /></label>)</span></h1>
              <BBusy :busy>
                <ExerciseFieldsForm ref="fields"
                  v-model="model" :displayedPage
                  :fixedNumber="true" :wysiwyg :deltas
                >
                </ExerciseFieldsForm>
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
              </BBusy>
            </div>
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
                        <AdaptationDetailsFieldsForm v-if="fields !== null" v-model="model" :wysiwyg :fields />
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
      <template v-else>
        <h1>{{ $t('exerciseNotFound') }}</h1>
      </template>
    </template>
  </ProjectTextbookPageLayout>
</template>
