<script setup lang="ts">
import { ref, computed, reactive, watch, nextTick } from 'vue'
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { computedAsync } from '@vueuse/core'

import { BButton, BBusy } from '$/frontend/components/opinion/bootstrap'
import bc from '$frontend/components/breadcrumbs'
import ProjectTextbookPageLayout from './ProjectTextbookPageLayout.vue'
import RectanglesHighlighter, { makeBoundingRectangle, makeBoundingRectangles, type Rectangle } from './RectanglesHighlighter.vue'
import TextPicker from './TextPicker.vue'
import { useProjectTextbookPageData } from './ProjectTextbookPageLayout.vue'
import TwoResizableColumns from '$frontend/components/TwoResizableColumns.vue'
import ExerciseFieldsForm from '$/frontend/components/ExerciseFieldsForm.vue'
import { useExerciseCreationHistoryStore } from './ExerciseCreationHistoryStore'
import { useApiStore } from '$/frontend/stores/api'
import type { PdfFile } from '$/frontend/stores/api'
import AdaptedExercise from './AdaptedExercise.vue'
import ToolsGutter from './ToolsGutter.vue'
import UndoRedoTool from './UndoRedoTool.vue'
import type { TextualFieldName } from '$/frontend/components/ExerciseFieldsForm.vue'
import AdaptationDetailsFieldsForm from '$/frontend/components/AdaptationDetailsFieldsForm.vue'
import TextSelectionModal from './TextSelectionModal.vue'
import { makeModel, resetModel, getParsed, create, suggestNextNumber } from '$frontend/components/ExerciseFieldsForm.vue'
import type { PDFPageProxy } from 'pdfjs-dist'
import BasicFormattingTools from './BasicFormattingTools.vue'


const props = defineProps<{
  projectId: string
  textbookId: string
  page: number
}>()
const projectId = computed(() => props.projectId)
const textbookId = computed(() => props.textbookId)
const page = computed(() => props.page)

const router = useRouter()
const api = useApiStore()
const i18n = useI18n()
const exerciseCreationHistory = useExerciseCreationHistoryStore()

const { project, textbook, exercises } = useProjectTextbookPageData(projectId, textbookId, page)

const greyRectangles = computed(() => makeBoundingRectangles(exercises.value.existingItems))

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

function changePage(page: number) {
  exerciseCreationHistory.reset()
  router.push({name: 'project-textbook-page-new-exercise', params: {page}})
}

const title = computed(() => [i18n.t('create')])

const breadcrumbs = computed(() => bc.last(i18n.t('create')))

const model = reactive(makeModel())
const canWysiwyg = computed(() => model.adaptationType !== 'multipleChoicesInWordingAdaptation')
const wantWysiwyg = ref(true)
const wysiwyg = computed(() => canWysiwyg.value && wantWysiwyg.value)

const resetUndoRedo = ref(0)

onMounted(() => {
  if (exerciseCreationHistory.suggestedNumber !== null) {
    model.number = exerciseCreationHistory.suggestedNumber
    resetUndoRedo.value++
  }
})

const surroundedRectangles = computed(() => {
  const boundingRectangle = makeBoundingRectangle(model.rectangles)
  if (boundingRectangle === null) {
    return []
  } else {
    return [boundingRectangle]
  }
})

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

function skip() {
  const suggestedNextNumber = suggestNextNumber(model.number)
  resetModel(model)
  model.number = suggestedNextNumber
  resetUndoRedo.value++
}

const busy = ref(false)
async function createThenNext() {
  const suggestedNextNumber = suggestNextNumber(model.number)
  busy.value = true
  const exercise = await create(project.value, textbook.value, page.value, model)
  busy.value = false

  exerciseCreationHistory.push(exercise.id)

  /* no await */ exercises.value.refresh()

  resetModel(model)
  model.number = suggestedNextNumber
  exerciseCreationHistory.suggestedNumber = suggestedNextNumber
  resetUndoRedo.value++
}

async function createThenBack() {
  busy.value = true
  await create(project.value, textbook.value, page.value, model)
  busy.value = false
  /* no await */ exercises.value.refresh()
  router.push({name: 'project-textbook-page'})
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
  const names = ['undoRedo']
  if (wysiwyg.value) {
    names.push('basicFormatting')
  }
  if (model.adaptationType !== '-') {
    names.push('adaptationDetails')
  }
  return names
})
</script>

<template>
  <TextSelectionModal ref="textSelectionModal" v-model="model" @textAdded="highlightSuffix" />
  <ProjectTextbookPageLayout
    :project :textbook :page :displayPage="page" @update:displayPage="changePage"
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
        @textSelected="(text, point, rectangle) => textSelected(pdfFile, pdf, text, point, rectangle)"
      />
    </template>

    <template #>
      <TwoResizableColumns saveKey="projectTextbookPage-2" :snap="150" class="h-100" gutterWidth="200px">
        <template #left>
          <div class="h-100 overflow-auto" data-cy="left-col-2">
            <h1>{{ $t('edition') }}<template v-if="canWysiwyg">  <span style="font-size: small">(<label>WYSIWYG: <input type="checkbox" v-model="wantWysiwyg" /></label>)</span></template></h1>
            <BBusy :busy>
              <ExerciseFieldsForm ref="fields"
                v-model="model"
                :fixedNumber="false" :wysiwyg :deltas
              >
                <template #overlay>
                  <div v-if="alreadyExists" style="position: absolute; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.8);" class="text-center">
                    <div style="position: absolute; left: 25%; top: 25%; width: 50%; height: 50%; background-color: white">
                      <p>{{ $t('exerciseAlreadyExists', {number: model.number}) }}</p>
                      <p>
                        <BButton primary @click="skip">{{ $t('skipExercise') }}</BButton>
                      </p>
                    </div>
                  </div>
                </template>
              </ExerciseFieldsForm>
              <p>
                <BButton secondary :disabled="exerciseCreationHistory.previous === null" @click="goToPrevious">{{ $t('previous') }}</BButton>
                <BButton primary :disabled="fields === null || fields.saveDisabled || alreadyExists" @click="createThenNext" data-cy="create-then-next">{{ $t('saveThenNext') }}</BButton>
              </p>
              <p>
                <RouterLink class="btn btn-secondary" :to="{name: 'project-textbook-page'}">{{ $t('backToList') }}</RouterLink>
                <BButton secondary :disabled="fields === null || fields.saveDisabled || alreadyExists" @click="createThenBack" data-cy="create-then-back">{{ $t('saveThenBack') }}</BButton>
              </p>
            </BBusy>
          </div>
        </template>

        <template #gutter>
          <div class="h-100 overflow-hidden d-flex flex-row">
            <div class="handle"></div>
            <div class="h-100 overflow-auto flex-fill" data-cy="gutter-2">
              <ToolsGutter :slotNames="toolSlotNames">
                <template #undoRedo>
                  <UndoRedoTool v-model="model" :reset="resetUndoRedo" />
                </template>
                <template #basicFormatting>
                  <BasicFormattingTools v-if="fields !== null" :fields />
                </template>
                <template #adaptationDetails>
                  <AdaptationDetailsFieldsForm v-if="fields !== null" v-model="model" :wysiwyg :fields/>
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
  </ProjectTextbookPageLayout>
</template>
