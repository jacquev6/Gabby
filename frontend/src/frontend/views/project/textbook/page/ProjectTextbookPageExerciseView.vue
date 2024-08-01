<script setup lang="ts">
import { ref, computed, reactive, watch, toRaw } from 'vue'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { computedAsync } from '@vueuse/core'

import { BButton, BBusy } from '$/frontend/components/opinion/bootstrap'
import { useApiStore } from '$frontend/stores/api'
import bc from '$frontend/components/breadcrumbs'
import ProjectTextbookPageLayout from './ProjectTextbookPageLayout.vue'
import RectanglesHighlighter from './RectanglesHighlighter.vue'
import { useProjectTextbookPageData } from './ProjectTextbookPageLayout.vue'
import TwoResizableColumns from '$frontend/components/TwoResizableColumns.vue'
import ExerciseFieldsForm from '$/frontend/components/ExerciseFieldsForm.vue'
import AdaptedExercise from './AdaptedExercise.vue'
import ToolsGutter from './ToolsGutter.vue'
import ReplaceTool from './ReplaceTool.vue'
import UndoRedoTool from './UndoRedoTool.vue'
import { useExerciseCreationHistoryStore } from './ExerciseCreationHistoryStore'
import { makeModel, assignModelFrom, getParsed, save } from '$frontend/components/ExerciseFieldsForm.vue'
import TextSelectionModal from './TextSelectionModal.vue'
import type { Rectangle, TextualFieldName, Selection } from '$/frontend/components/ExerciseFieldsForm.vue'
import type { TextItem } from './TextPicker.vue'
import AdaptationDetailsFieldsForm from '$/frontend/components/AdaptationDetailsFieldsForm.vue'
import TextPicker from './TextPicker.vue'
import type { PdfFile } from '$/frontend/stores/api'
import type { PDFPageProxy } from 'pdfjs-dist'


const props = defineProps<{
  projectId: string
  textbookId: string
  page: number
  exerciseId: string
  displayPage?: number
}>()
const projectId = computed(() => props.projectId)
const textbookId = computed(() => props.textbookId)
const page = computed(() => props.page)
const displayPage = computed(() => props.displayPage ?? props.page)

const api = useApiStore()
const router = useRouter()
const i18n = useI18n()
const exerciseCreationHistory = useExerciseCreationHistoryStore()


function changeDisplayPage(newDisplayPage: number) {
  if (newDisplayPage === props.page) {
    router.replace({
      name: 'project-textbook-page-exercise',
      params: {},
    })
  } else {
    router.replace({
      name: 'project-textbook-page-exercise',
      params: {},
      query: {displayPage: newDisplayPage},
    })
  }
}

const { project, textbook, exercises } = useProjectTextbookPageData(projectId, textbookId, displayPage)

const greyRectangles = computed(() =>
  exercises.value.existingItems
    .filter(exercise => exercise.id !== props.exerciseId)
    .map(exercise => exercise.attributes.boundingRectangle)
    .filter((x): x is Rectangle => x !== null)
)

const exercise = computed(() => api.auto.getOne('exercise', props.exerciseId, {include: ['adaptation']}))

const exerciseBelongsToTextbookPage = computed(() =>
  exercise.value.inCache && exercise.value.exists && exercise.value.relationships.textbook === textbook.value && exercise.value.attributes.textbookPage === props.page
)

const surroundedRectangles = computed(() => {
  if (exercise.value.inCache && exercise.value.exists) {
    if (exercise.value.attributes.textbookPage === displayPage.value) {
      if (exercise.value.attributes.boundingRectangle !== null) {
        return [exercise.value.attributes.boundingRectangle]
      }
    }
  }
  return []
})

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

const model = reactive(makeModel())
const wysiwyg = ref(true)
const extractionEvents: object[] = []

const resetUndoRedo = ref(0)

watch(
  [
    computed(() => exercise.value.inCache && exercise.value.exists ? exercise.value.attributes.number : null),
    computed(() => exercise.value.inCache && exercise.value.exists && exercise.value.relationships.adaptation !== null && exercise.value.relationships.adaptation.inCache),
  ],
  () => {
    if (exercise.value.inCache && exercise.value.exists) {
      assignModelFrom(model, exercise.value, extractionEvents)
      resetUndoRedo.value++
    }
  },
  {immediate: true},
)

const fields = ref<InstanceType<typeof ExerciseFieldsForm> | null>(null)

const textSelectionModal = ref<InstanceType<typeof TextSelectionModal> | null>(null)

function textSelected(pdfFile: PdfFile, pdf: {page: PDFPageProxy}, text: string, point: {clientX: number, clientY: number}, textItems: TextItem[], rectangle: Rectangle) {
  console.assert(pdfFile.inCache && pdfFile.exists)
  console.assert(pdfFile.relationships.namings.length > 0)
  console.assert(pdfFile.relationships.namings[0].inCache && pdfFile.relationships.namings[0].exists)
  console.assert(textSelectionModal.value !== null)
  extractionEvents.push({
    kind: "TextSelectedInPdf",
    pdf: {
      name: pdfFile.relationships.namings[0].attributes.name,
      sha256: pdfFile.id,
      page: pdf.page.pageNumber,
      rectangle,
    },
    value: text,
    textItems,
  })
  textSelectionModal.value.show(text, {x: point.clientX, y: point.clientY})
}

function highlightSuffix(fieldName: TextualFieldName, text: string) {
  console.assert(fields.value !== null)
  fields.value.highlightSuffix(fieldName, text)
}

const lastSelection = ref<Selection | null>(null)

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
  await save(exercise.value, model, extractionEvents)
  busy.value = false

  router.push({
    name: 'project-textbook-page',
  })
}

async function saveThenNext() {
  busy.value = true
  console.assert(exercise.value.inCache && exercise.value.exists)
  await save(exercise.value, model, extractionEvents)
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

const parsedExerciseLoading = ref(false)
const parsedExercise = computedAsync(
  () => getParsed(model),
  null,
  parsedExerciseLoading,
)

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
    console.log('Instructions delta:', toRaw(parsedExercise.value.attributes.delta.instructions))
    return parsedExercise.value.attributes.delta
  }
})
</script>

<template>
  <TextSelectionModal ref="textSelectionModal" v-model="model" :extractionEvents @textAdded="highlightSuffix" />
  <ProjectTextbookPageLayout
    :project :textbook :page :displayPage @update:displayPage="changeDisplayPage"
    :title :breadcrumbs
  >
    <template #pdfOverlay="{ pdfFile, pdf, width, height, transform }">
      <RectanglesHighlighter
        class="img w-100" style="position: absolute; top: 0; left: 0"
        :width :height :transform
        :greyRectangles :surroundedRectangles
      />
      <TextPicker
        class="img w-100" style="position: absolute; top: 0; left: 0"
        :width :height :transform
        :textContent="pdf.textContent"
        @textSelected="(text, point, items, rectangle) => textSelected(pdfFile, pdf, text, point, items, rectangle)"
      />
    </template>

    <template v-if="exercise.inCache">
      <template v-if="exercise.exists && exerciseBelongsToTextbookPage">
        <TwoResizableColumns saveKey="projectTextbookPage-2" :snap="150" class="h-100" gutterWidth="200px">
          <template #left>
            <div class="h-100 overflow-auto" data-cy="left-col-2">
              <h1>{{ $t('edition') }} <span style="font-size: small">(<label>WYSIWYG: <input type="checkbox" v-model="wysiwyg" /></label>)</span></h1>
              <BBusy :busy>
                <ExerciseFieldsForm ref="fields"
                  v-model="model"
                  :fixedNumber="true" :extractionEvents :wysiwyg :deltas
                  @selected="selection => { lastSelection = selection }"
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
                <ToolsGutter>
                  <template #undoRedo>
                    <UndoRedoTool v-model="model" :reset="resetUndoRedo" />
                  </template>
                  <template #adaptationDetails>
                    <template v-if="fields !== null">
                      <AdaptationDetailsFieldsForm v-model="model" :wysiwyg :fields />
                    </template>
                  </template>
                  <template #replace>
                    <ReplaceTool v-model="model" :lastSelection />
                  </template>
                </ToolsGutter>
              </div>
              <div class="handle"></div>
            </div>
          </template>

          <template #right>
            <div class="h-100 overflow-auto" data-cy="right-col-2">
              <h1>{{ $t('adaptation') }}</h1>
              <BBusy :busy="parsedExerciseLoading">
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
