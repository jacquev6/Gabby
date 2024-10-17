<script setup lang="ts">
import { ref, computed, reactive, watch, nextTick } from 'vue'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import deepCopy from 'deep-copy'
import deepEqual from 'deep-equal'

import { BButton, BBusy, BLabeledRadios } from '$frontend/components/opinion/bootstrap'
import { useApiStore } from '$frontend/stores/api'
import bc from '$frontend/components/breadcrumbs'
import ProjectTextbookPageLayout from './ProjectTextbookPageLayout.vue'
import RectanglesHighlighter, { makeBoundingRectangle, makeBoundingRectangles, type Rectangle } from './RectanglesHighlighter.vue'
import { useProjectTextbookPageData } from './ProjectTextbookPageLayout.vue'
import TwoResizableColumns from '$frontend/components/TwoResizableColumns.vue'
import ExerciseFieldsForm from '$frontend/components/ExerciseFieldsForm.vue'
import AdaptedExercise from './AdaptedExercise.vue'
import ToolsGutter from './ToolsGutter.vue'
import UndoRedoTool from './UndoRedoTool.vue'
import { useExerciseCreationHistoryStore } from './ExerciseCreationHistoryStore'
import { makeModelInTextbook, assignModelFrom, getParsed, save } from '$frontend/components/ExerciseFieldsForm.vue'
import TextSelectionModal from './TextSelectionModal.vue'
import type { TextualFieldName } from '$frontend/components/ExerciseFieldsForm.vue'
import AdaptationDetailsFieldsForm from '$frontend/components/AdaptationDetailsFieldsForm.vue'
import TextPicker from './TextPicker.vue'
import type { Exists, InCache, ParsedExercise, PdfFile } from '$frontend/stores/api'
import type { PDFPageProxy } from 'pdfjs-dist'
import BasicFormattingTools from './BasicFormattingTools.vue'
import { useGloballyBusyStore } from '$frontend/stores/globallyBusy'


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

const api = useApiStore()
const router = useRouter()
const i18n = useI18n()
const globallyBusy = useGloballyBusyStore()
const exerciseCreationHistory = useExerciseCreationHistoryStore()


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

const { project, textbook, exercisesOnDisplayedPage, exercisesOnPageBeforeDisplayed } = useProjectTextbookPageData(projectId, textbookId, page, displayedPage)
globallyBusy.register('loading exercises on page', computed(() => exercisesOnDisplayedPage.value.loading))
globallyBusy.register('loading exercises on previous page', computed(() => exercisesOnPageBeforeDisplayed.value.loading))

function makeGreyRectangles(pdfSha256: string, pdfPage: number) {
  const otherExercises = [...exercisesOnPageBeforeDisplayed.value.existingItems,  ...exercisesOnDisplayedPage.value.existingItems].filter(exercise => exercise.id !== props.exerciseId)
  return makeBoundingRectangles(pdfSha256, pdfPage, otherExercises)
}

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

const textSelectionModal = ref<InstanceType<typeof TextSelectionModal> | null>(null)

function textSelected(pdfFile: PdfFile, pdf: {page: PDFPageProxy}, selectedText: string, point: {clientX: number, clientY: number}, rectangle: Rectangle) {
  console.assert(pdfFile.inCache && pdfFile.exists)
  console.assert(pdfFile.relationships.namings.length > 0)
  console.assert(pdfFile.relationships.namings[0].inCache && pdfFile.relationships.namings[0].exists)
  console.assert(textSelectionModal.value !== null)
  textSelectionModal.value.show({
    selectedText,
    at: {x: point.clientX, y: point.clientY},
    pdfSha256: pdfFile.attributes.sha256,
    pdfPage: pdf.page.pageNumber,
    rectangle,
  })
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

const parsedExercise = ref<ParsedExercise & InCache & Exists | null>(null)
const parsedExerciseIsLoading = ref(false)
const parsedExerciseNeedsLoading = ref(true)
watch(model, () => { parsedExerciseNeedsLoading.value = true })
watch(parsedExerciseNeedsLoading, async () => {
  while (parsedExerciseNeedsLoading.value) {
    const modelBefore = deepCopy(model)
    parsedExerciseIsLoading.value = true
    const parsed = await getParsed(model)
    if (deepEqual(model, modelBefore)) {
      parsedExercise.value = parsed
      parsedExerciseIsLoading.value = false
      parsedExerciseNeedsLoading.value = false
    }
  }
}, {immediate: true})

const adaptedExercise = computed(() => {
  if (parsedExercise.value === null) {
    return null
  } else {
    return parsedExercise.value.attributes.adapted
  }
})

const deltas = computed(() => {
  if (parsedExercise.value === null) {
    return null
  } else {
    return parsedExercise.value.attributes.delta
  }
})

const suffixToHighlight = ref<{fieldName: TextualFieldName, text: string} | null>(null)
function highlightSuffix(fieldName: TextualFieldName, text: string) {
  suffixToHighlight.value = {fieldName, text}
}

watch(parsedExercise, () => {
  if (suffixToHighlight.value !== null) {
    const {fieldName, text} = suffixToHighlight.value
    suffixToHighlight.value = null
    nextTick(() => {
      console.assert(fields.value !== null)
      fields.value.highlightSuffix(fieldName, text)
    })
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

function confirmInProgressMultipleChoices() {
  console.assert(model.awaiting.multipleChoices !== null)
  const settings = model.awaiting.multipleChoices.settings
  console.assert(settings !== null)
  const prefix = `{choices2|${settings.start}|${settings.separator}|${settings.stop}|${settings.placeholder}|`
  const suffix = '}'
  const range = model.awaiting.multipleChoices.range
  console.assert(range !== null)
  model.wording = model.wording.slice(0, range.index) + prefix + model.wording.slice(range.index, range.index + range.length) + suffix + model.wording.slice(range.index + range.length)
  model.awaiting.multipleChoices = null
}
</script>

<template>
  <TextSelectionModal ref="textSelectionModal" v-model="model" @textAdded="highlightSuffix" />
  <ProjectTextbookPageLayout
    :project :textbook :page :displayedPage @update:displayedPage="changeDisplayedPage"
    :title :breadcrumbs
  >
    <template #pdfOverlay="{ pdfFile, pdf, width, height, transform }">
      <RectanglesHighlighter
        v-if="pdfFile.inCache && pdfFile.exists"
        class="img w-100" style="position: absolute; top: 0; left: 0"
        :width :height :transform
        :greyRectangles="makeGreyRectangles(pdfFile.attributes.sha256, pdf.page.pageNumber)"
        :surroundedRectangles="makeSurroundedRectangles(pdfFile.attributes.sha256, pdf.page.pageNumber)"
      />
      <TextPicker
        class="img w-100" style="position: absolute; top: 0; left: 0"
        :width :height :transform
        :textContent="pdf.textContent"
        @textSelected="(text, point, rectangle) => textSelected(pdfFile, pdf, text, point, rectangle)"
      />
    </template>

    <template v-if="exercise.inCache">
      <template v-if="exercise.exists && exerciseBelongsToTextbookPage">
        <TwoResizableColumns saveKey="projectTextbookPage-2" :snap="150" class="h-100" gutterWidth="200px">
          <template #left>
            <div class="h-100 overflow-auto" data-cy="left-col-2">
              <h1>{{ $t('edition') }}  <span style="font-size: small">(<label>WYSIWYG: <input type="checkbox" v-model="wantWysiwyg" /></label>)</span></h1>
              <BBusy :busy>
                <ExerciseFieldsForm ref="fields"
                  v-model="model" :displayedPage
                  :fixedNumber="true" :wysiwyg :deltas
                />
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
            <div class="h-100 overflow-hidden d-flex flex-row">
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
                    v-if="model.awaiting.multipleChoices !== null && !model.awaiting.multipleChoices.editing"
                    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.5); cursor: initial;"
                    @mousedown="e => e.stopPropagation()" @touchstart="e => e.stopPropagation()"
                  >
                    <div style="position: absolute; top: 50%; left: 10%; width: 80%; transform: translate(0, -50%); background-color: white; padding: 1em;">
                      <div v-if="model.awaiting.multipleChoices.globalSelection">
                        Select a set of choices in the "Wording" field in the "Edition" column.
                        Include start, stop and separator characters.
                      </div>
                      <div v-else-if="model.awaiting.multipleChoices.confirmation">
                        Settings.
                        <BButton primary sm @click="confirmInProgressMultipleChoices">Confirm</BButton>
                      </div>
                      <div v-else>
                        This is a bug. Please let Vincent Jacques know you've seen this message.
                      </div>
                      <BButton secondary sm @click="model.awaiting.multipleChoices = null">Cancel</BButton>
                    </div>
                  </div>
                </div>
              </div>
              <div class="handle"></div>
            </div>
          </template>

          <template #right>
            <div class="h-100 overflow-auto" data-cy="right-col-2">
              <h1>{{ $t('adaptation') }}</h1>
              <BBusy :busy="parsedExerciseIsLoading">
                <AdaptedExercise
                  v-if="adaptedExercise !== null"
                  :projectId="projectId"
                  exerciseId="unused @todo Compute storageKey in an independent composable, and let AdaptedExercise load and save iif the key is not null"
                  :exercise="adaptedExercise"
                />
              </BBusy>
            </div>
          </template>
        </TwoResizableColumns>
      </template>
      <template v-else>
        <h1>{{ $t('exerciseNotFound') }}</h1>
      </template>
    </template>
  </ProjectTextbookPageLayout>
</template>
