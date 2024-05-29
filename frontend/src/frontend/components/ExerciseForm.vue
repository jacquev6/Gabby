<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import { computedAsync, useDebouncedRefHistory } from '@vueuse/core'
import { nextTick } from 'vue'

import { BBusy, BLabeledInput, BLabeledTextarea, BLabeledCheckbox, BButton, BSelect } from './opinion/bootstrap'
import TextSelectionMenu from './ExerciseFormTextSelectionMenu.vue'
import OptionalTextarea from './OptionalTextarea.vue'
import { useApiStore } from '$frontend/stores/api'
import type { Project, Textbook, Section, Exercise, AdaptedExercise } from '$frontend/types/api'
import type { SelectThingsAdaptationOptions, FillWithFreeTextAdaptationOptions, MultipleChoicesInInstructionsAdaptationOptions, MultipleChoicesInWordingAdaptationOptions } from '$frontend/types/api'


const props = defineProps<{
  project: Project,
  textbook: Textbook | null,
  textbookPage: number | null,
  section: Section | null,
  pdf: {page: {pageNumber: number}} | null,
  number: string,
  automaticNumber: boolean,
  editMode: boolean,
  exercise?: Exercise,
}>()

const emit = defineEmits<{
  created: [exercise: Exercise, suggestedNextExerciseNumber: string],
  saved: [],
}>()

const api = useApiStore()

var extractionEvents: object[] = []

// @todo Automate updating this type when a new adaptation type is added
type AdaptationType = '-' | 'selectThingsAdaptation' | 'fillWithFreeTextAdaptation' | 'multipleChoicesInInstructionsAdaptation' | 'multipleChoicesInWordingAdaptation'
const adaptationTypes: AdaptationType[] = ['selectThingsAdaptation', 'fillWithFreeTextAdaptation', 'multipleChoicesInInstructionsAdaptation', 'multipleChoicesInWordingAdaptation']

interface State {
  number: string,
  boundingRectangle: object | null,
  instructions: string,
  wording: string,
  example: string,
  clue: string,
  adaptationType: AdaptationType,
  selectThingsAdaptationOptions: SelectThingsAdaptationOptions,
  fillWithFreeTextAdaptationOptions: FillWithFreeTextAdaptationOptions,
  multipleChoicesInInstructionsAdaptationOptions: MultipleChoicesInInstructionsAdaptationOptions,
  multipleChoicesInWordingAdaptationOptions: MultipleChoicesInWordingAdaptationOptions,
}

const state = ref<State>({
  number: '',
  boundingRectangle: null,
  instructions: '',
  wording: '',
  example: '',
  clue: '',
  adaptationType: '-',
  selectThingsAdaptationOptions: {
    colors: 1,
    words: true,
    punctuation: true,
  },
  fillWithFreeTextAdaptationOptions: {
    placeholder: '...',
  },
  multipleChoicesInInstructionsAdaptationOptions: {
    placeholder: '...',
  },
  multipleChoicesInWordingAdaptationOptions: {
  },
})
const needsBoundingRectangle = computed(() => {
  if (props.textbook !== null && props.pdf !== null && !props.editMode) {
    return state.value.boundingRectangle === null
  } else {
    return false
  }
})
type FieldName = 'instructions' | 'wording' | 'example' | 'clue'
const fieldNamesForReplace: FieldName[] = ['instructions', 'wording', 'example', 'clue']

function resetAdaptationOptions() {
  state.value.adaptationType = '-'
  state.value.selectThingsAdaptationOptions = {
    colors: 1,
    words: true,
    punctuation: true,
  }
  state.value.fillWithFreeTextAdaptationOptions = {
    placeholder: '...',
  }
  state.value.multipleChoicesInInstructionsAdaptationOptions = {
    placeholder: '...',
  }
  state.value.multipleChoicesInWordingAdaptationOptions = {
  }
}
resetAdaptationOptions()

// @todo Consider using 'useThrottledRefHistory' instead of 'useDebouncedRefHistory'
const history = useDebouncedRefHistory(state, {deep: true, debounce: 1000})
function clearHistory(reset: () => void) {
  // @todo Prevent the creation of a history state even if a change was done during the previous 1000ms
  // Currently, the change is buffered for 1000ms, so an history commit can be created after this function returns
  history.batch(reset)
  history.clear()
}

const alreadyExists = computedAsync(
  async () => {
    if (props.editMode) {
      return true
    } else if (state.value.number === '') {
      return false
    } else if (props.textbook !== null) {
      console.assert(props.textbookPage !== null)
      const exercises = await api.client.getAll(
        'exercises',
        {
          filter: {
            textbook: props.textbook.id,
            textbookPage: props.textbookPage.toString(),
            number: state.value.number,
          }
        },
      )
      console.assert(exercises.length <= 1)
      return exercises.length === 1
    } else {
      // @todo Detect duplicate independent exercise
      return false
    }
  },
  false,
)

watch(
  [() => props.number, () => props.automaticNumber],
  () => {
    clearHistory(() => {
      state.value.number = props.number
    })

    if (props.automaticNumber) {
      extractionEvents.push({kind: 'ExerciseNumberSetAutomatically', value: state.value.number})
    }
  },
  {immediate: true},
)
watch(
  () => props.exercise,
  () => {
    if (props.exercise !== undefined) {
      clearHistory(() => {
        console.assert(props.exercise !== undefined)
        console.assert(props.exercise.attributes !== undefined)
        console.assert(props.exercise.relationships !== undefined)

        state.value.boundingRectangle = props.exercise.attributes.boundingRectangle ?? null

        state.value.instructions = props.exercise.attributes.instructions ?? ''
        state.value.wording = props.exercise.attributes.wording ?? ''
        state.value.example = props.exercise.attributes.example ?? ''
        state.value.clue = props.exercise.attributes.clue ?? ''

        if (props.exercise.relationships.adaptation === null) {
          state.value.adaptationType = '-'
        } else {
          state.value.adaptationType = props.exercise.relationships.adaptation.type as AdaptationType
          console.assert(state.value.adaptationType !== '-')
          switch (state.value.adaptationType) {
            case 'selectThingsAdaptation':
              Object.assign(state.value.selectThingsAdaptationOptions, props.exercise.relationships.adaptation.attributes)
              break
            case 'fillWithFreeTextAdaptation':
              Object.assign(state.value.fillWithFreeTextAdaptationOptions, props.exercise.relationships.adaptation.attributes)
              break
            case 'multipleChoicesInInstructionsAdaptation':
              Object.assign(state.value.multipleChoicesInInstructionsAdaptationOptions, props.exercise.relationships.adaptation.attributes)
              break
            case 'multipleChoicesInWordingAdaptation':
              Object.assign(state.value.multipleChoicesInWordingAdaptationOptions, props.exercise.relationships.adaptation.attributes)
              break
            default:
              ((_1: never) => console.assert(false))(state.value.adaptationType)
          }
        }
      })
    }
  },
  {immediate: true},
)

const disabled = computed(() => (!props.editMode && alreadyExists.value) || !state.value.number)
const busy = ref(false)

const showTextSelectionMenu = ref(false)
const selectedText = ref('')
const selectedRectangle = ref<object | null>(null)
const selectedTextReference = ref<{x: number, y: number}>({x: 0, y: 0})
function textSelected(text: string, point: {clientX: number, clientY: number}, textItems: [], rectangle: object) {
  console.assert(props.section?.relationships?.pdfFile.relationships?.namings[0].attributes !== undefined)
  console.assert(props.pdf !== null)

  if (needsBoundingRectangle.value) {
    extractionEvents.push({
      kind: "BoundingRectangleSelectedInPdf",
      pdf: {
        name: props.section.relationships.pdfFile.relationships.namings[0].attributes.name,
        sha256: props.section.relationships.pdfFile.id,
        page: props.pdf.page.pageNumber,
        rectangle,
      },
    })
    state.value.boundingRectangle = rectangle
  } else {
    extractionEvents.push({
      kind: "TextSelectedInPdf",
      pdf: {
        name: props.section.relationships.pdfFile.relationships.namings[0].attributes.name,
        sha256: props.section.relationships.pdfFile.id,
        page: props.pdf.page.pageNumber,
        rectangle,
      },
      value: text,
      textItems,
    })
    selectedText.value = text
    selectedRectangle.value = rectangle
    selectedTextReference.value = {x: point.clientX, y: point.clientY}
    showTextSelectionMenu.value = true
  }
}

const instructionsTextArea = ref<typeof BLabeledTextarea | null>(null)
const wordingTextArea = ref<typeof BLabeledTextarea | null>(null)
const exampleTextArea = ref<typeof OptionalTextarea | null>(null)
const clueTextArea = ref<typeof OptionalTextarea | null>(null)
const textAreas = {
  instructions: instructionsTextArea,
  wording: wordingTextArea,
  example: exampleTextArea,
  clue: clueTextArea,
}

const noClueNoExample = computed(() => !exampleTextArea.value?.expanded && !clueTextArea.value?.expanded)

const settingSelectionRange = ref(false)
function addTextTo(fieldName: FieldName, text: string) {
  const textArea = textAreas[fieldName].value
  console.assert(textArea !== null)
  const valueBefore = state.value[fieldName]
  if (state.value[fieldName] !== '' && !state.value[fieldName].endsWith('\n')) {
    state.value[fieldName] += '\n'
  }
  const selectionBegin = state.value[fieldName].length
  const selectionEnd = selectionBegin + text.length
  state.value[fieldName] += text  // @todo Double-check this is reactive (assigning to a member of a ref)
  nextTick(() => {
    textArea.focus()
    settingSelectionRange.value = true  // Avoid changing 'selected' when selection doesn't originate from the user
    textArea.setSelectionRange(selectionBegin, selectionEnd)
  })
  extractionEvents.push({kind: `SelectedTextAddedTo${fieldName.charAt(0).toUpperCase()}${fieldName.slice(1)}`, valueBefore, valueAfter: state.value[fieldName]})
}

function skip() {
  clearHistory(() => {
    state.value.boundingRectangle = null
    extractionEvents = []
    state.value.number = tryIncrement(state.value.number)
    state.value.instructions = ''
    state.value.wording = ''
    state.value.example = ''
    state.value.clue = ''

    resetAdaptationOptions()
  })
}

const adaptationOptions = computed(() => {
  switch (state.value.adaptationType) {
    case '-':
      return null
    case 'selectThingsAdaptation':
      return state.value.selectThingsAdaptationOptions
    case 'fillWithFreeTextAdaptation':
      return state.value.fillWithFreeTextAdaptationOptions
    case 'multipleChoicesInInstructionsAdaptation':
      return state.value.multipleChoicesInInstructionsAdaptationOptions
    case 'multipleChoicesInWordingAdaptation':
      return state.value.multipleChoicesInWordingAdaptationOptions
    default:
      ((_1: never) => console.assert(false))(state.value.adaptationType)
      return null
  }
})

async function create() {
  busy.value = true

  // @todo Use a batch request
  const exercise = await api.client.post<Exercise>(
    'exercise',
    {
      textbookPage: props.textbookPage,
      boundingRectangle: state.value.boundingRectangle,
      number: state.value.number,
      instructions: state.value.instructions,
      wording: state.value.wording,
      example: state.value.example,
      clue: state.value.clue,
    },
    {
      project: props.project,
      textbook: props.textbook,
    },
  )
  if (state.value.adaptationType !== '-') {
    console.assert(adaptationOptions.value !== null)
    await api.client.post(
      state.value.adaptationType,
      adaptationOptions.value,
      {exercise: {type: 'exercise', id: exercise.id}},
    )
  }
  for (const event of extractionEvents) {
    await api.client.post(
      'extractionEvent',
      {event: JSON.stringify(event)},
      {exercise: {type: 'exercise', id: exercise.id}},
    )
  }

  clearHistory(() => {
    state.value.boundingRectangle = null
    extractionEvents = []
    state.value.number = ''
    state.value.instructions = ''
    state.value.wording = ''
    state.value.example = ''
    state.value.clue = ''

    resetAdaptationOptions()
  })

  busy.value = false

  emit('created', exercise, tryIncrement(exercise.attributes.number))
}

function tryIncrement(s: string) {
  const n = parseInt(s)
  if (Number.isInteger(n)) {
    return (n + 1).toString()
  } else {
    return ''
  }
}

async function save() {
  console.assert(props.exercise?.relationships !== undefined)

  busy.value = true

  // @todo Use a batch request
  await api.client.patch(
    'exercise',
    props.exercise.id,
    {
      boundingRectangle: state.value.boundingRectangle,
      instructions: state.value.instructions,
      wording: state.value.wording,
      example: state.value.example,
      clue: state.value.clue,
    },
    {},
  )
  if (state.value.adaptationType === '-') {
    if (props.exercise.relationships.adaptation !== null) {
      await api.client.delete(props.exercise.relationships.adaptation.type, props.exercise.relationships.adaptation.id)
    }
  } else {
    console.assert(adaptationOptions.value !== null)
    await api.client.post(
      state.value.adaptationType,
      adaptationOptions.value,
      {exercise: {type: 'exercise', id: props.exercise.id}},
    )
  }
  for (const event of extractionEvents) {
    await api.client.post(
      'extractionEvent',
      {event: JSON.stringify(event)},
      {exercise: {type: 'exercise', id: props.exercise.id}},
    )
  }

  extractionEvents = []

  busy.value = false

  emit('saved')
}

const adaptedDataLoading = ref(false)
const adaptedData = computedAsync(
  async () => {
    if (state.value.adaptationType === '-') {
      return null
    } else {
      const attributes = {
        number: state.value.number,
        textbookPage: props.textbookPage,
        instructions: state.value.instructions,
        wording: state.value.wording,
        type: state.value.adaptationType,
        adaptationOptions: adaptationOptions.value,
      }
      try {
        const adapted = await api.client.post<AdaptedExercise>('adaptedExercise', attributes, {})
        return adapted.attributes.adapted
      } catch (e) {
        console.error(e)
        return null
      }
    }
  },
  null,
  adaptedDataLoading,
)

const highlightedRectangles = computed(() => {
  if (state.value.boundingRectangle) {
    return [state.value.boundingRectangle]
  } else {
    return null
  }
})

const selected = ref([null, ''])

function updateSelected(fieldName: FieldName) {
  const textArea = textAreas[fieldName].value?.textarea
  if (textArea) {
    if (!settingSelectionRange.value) {
      selected.value = [fieldName, textArea.value.substring(textArea.selectionStart, textArea.selectionEnd)]
    }
    settingSelectionRange.value = false
  }
}

function replace(fieldName: FieldName | null, searchValue: string, replaceValue: string) {
  let fieldNames: FieldName[]
  if (fieldName === null) {
    fieldNames = fieldNamesForReplace
  } else {
    fieldNames = [fieldName]
  }
  for (const fieldName of fieldNames) {
    state.value[fieldName] = state.value[fieldName].replaceAll(searchValue, replaceValue)
  }
}

defineExpose({
  textSelected: computed(() => !props.editMode && alreadyExists.value ? null : textSelected),
  adaptedData, adaptedDataLoading,
  highlightedRectangles,
  // Tools
  selected,
  replace,
  fieldNamesForReplace,
  undo: history.undo, redo: history.redo, canUndo: history.canUndo, canRedo: history.canRedo,
})
</script>

<template>
  <TextSelectionMenu
    v-model:show="showTextSelectionMenu"
    :number="state.number"
    :text="selectedText"
    :reference="selectedTextReference"
    @extractionEvent="event => extractionEvents.push(event)"
  >
    <template v-slot="{textToAdd, hide}">
      <p><BButton secondary @click="state.boundingRectangle = selectedRectangle; hide()">{{ $t('setBoundingRect') }}</BButton></p>
      <p>{{ $t('addTo') }}</p>
      <p>
        <BButton primary @click="addTextTo('instructions', textToAdd); hide()">{{ $t('instructions') }}</BButton>
        <BButton primary @click="addTextTo('wording', textToAdd); hide()">{{ $t('wording') }}</BButton>
        <BButton primary @click="addTextTo('example', textToAdd); hide()">{{ $t('example') }}</BButton>
        <BButton primary @click="addTextTo('clue', textToAdd); hide()">{{ $t('clue') }}</BButton>
      </p>
    </template>
  </TextSelectionMenu>

  <BBusy :busy>
    <BLabeledInput :label="$t('exerciseNumber')" v-model="state.number" :disabled="editMode" @change="extractionEvents.push({kind: 'ExerciseNumberSetManually', value: state.number})" />
    
    <div style="position: relative">
      <BLabeledTextarea
        ref="instructionsTextArea"
        :label="$t('exerciseInstructions')"
        v-model="state.instructions"
        @select="updateSelected('instructions')"
        @change="extractionEvents.push({kind: 'InstructionsSetManually', value: state.instructions})"
      />
      <BLabeledTextarea
        ref="wordingTextArea"
        :label="$t('exerciseWording')"
        v-model="state.wording"
        @select="updateSelected('wording')"
        @change="extractionEvents.push({kind: 'WordingSetManually', value: state.wording})"
      />
      <div :class="{'container-fluid': noClueNoExample}">
        <div :class="{row: noClueNoExample}">
          <div :class="{col: noClueNoExample}" style="padding: 0;">
            <OptionalTextarea
              ref="exampleTextArea"
              :label="$t('exerciseExample')"
              v-model="state.example"
              @select="updateSelected('example')"
              @change="extractionEvents.push({kind: 'ExampleSetManually', value: state.example})"
            />
          </div>
          <div :class="{col: noClueNoExample}" style="padding: 0;">
            <OptionalTextarea
              ref="clueTextArea"
              :label="$t('exerciseClue')"
              v-model="state.clue"
              @select="updateSelected('clue')"
              @change="extractionEvents.push({kind: 'ClueSetManually', value: state.clue})"
            />
          </div>
        </div>
      </div>

      <BBusy :busy="adaptedDataLoading">
        <div class="mb-3">
          <label class="form-label" for="abc">{{ $t('adaptationType') }}</label>
            <BSelect
            id="abc"
            v-model="state.adaptationType"
            :options="['-', ...adaptationTypes.map(kind => ({value: kind, label: $t(kind)}))]"
          />
        </div>
        <template v-if="state.adaptationType === '-'">
        </template>
        <template v-else-if="state.adaptationType === 'fillWithFreeTextAdaptation'">
          <BLabeledInput :label="$t('placeholderText')" type="text" v-model="state.fillWithFreeTextAdaptationOptions.placeholder" />
        </template>
        <template v-else-if="state.adaptationType === 'selectThingsAdaptation'">
          <BLabeledInput :label="$t('colorsCount')" type="number" min="1" v-model="state.selectThingsAdaptationOptions.colors" />
          <p class="alert alert-secondary" v-if="state.selectThingsAdaptationOptions.colors > 1">
            <i18n-t keypath="useSel1ToSelN">
              <template v-slot:first>
                <code>{sel1|<em>text</em>}</code>
              </template>
              <template v-slot:last>
                <code>{sel{{ state.selectThingsAdaptationOptions.colors }}|<em>text</em>}</code>
              </template>
            </i18n-t>
          </p>
          <BLabeledCheckbox :label="$t('includePunctuation')" v-model="state.selectThingsAdaptationOptions.punctuation" />
        </template>
        <template v-else-if="state.adaptationType === 'multipleChoicesInInstructionsAdaptation'">
          <p class="alert alert-secondary">
            <i18n-t keypath="useChoice">
              <template v-slot:choice>
                <code>{choice|<em>text</em>}</code>
              </template>
            </i18n-t>
          </p>
          <BLabeledInput :label="$t('placeholderText')" type="text" v-model="state.multipleChoicesInInstructionsAdaptationOptions.placeholder" />
        </template>
        <template v-else-if="state.adaptationType === 'multipleChoicesInWordingAdaptation'">
          <p class="alert alert-secondary">
            <i18n-t keypath="useChoices">
              <template v-slot:choices>
                <code>{choices|<em>text</em>|<em>text</em>|<em>...</em>}</code>
              </template>
            </i18n-t>
          </p>
        </template>
        <template v-else>
          <span>{{ ((t: never) => t)(state.adaptationType) }}</span>
        </template>
      </BBusy>

      <div v-if="!editMode && alreadyExists" style="position: absolute; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.8);" class="text-center">
        <div style="position: absolute; left: 25%; top: 25%; width: 50%; height: 50%; background-color: white">
          <p>{{ $t('exerciseAlreadyExists', {number: state.number}) }}</p>
          <p>
            <BButton primary @click="skip">{{ $t('skipExercise') }}</BButton>
          </p>
        </div>
      </div>
      <div v-else-if="needsBoundingRectangle" style="position: absolute; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.8);" class="text-center">
        <div style="position: absolute; left: 25%; top: 25%; width: 50%; height: 50%; background-color: white">
          <p>{{ $t('drawBoundingRectangle') }}</p>
        </div>
      </div>
    </div>

    <slot :disabled :create :save></slot>
  </BBusy>
</template>
