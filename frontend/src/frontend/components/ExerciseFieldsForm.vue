<script lang="ts">
import { useApiStore } from '$frontend/stores/api'
import type { Project, Textbook, Exercise, InCache, Exists } from '$frontend/stores/api'
import deepEqual from 'deep-equal'
import { type Model as Deltas } from '$frontend/components/Quill.vue'
import { Delta } from 'quill/core'

const api = useApiStore()

type Adaptation = (Exercise & InCache & Exists)['attributes']['adaptation']
type PdfRectangle = (Exercise & InCache & Exists)['attributes']['rectangles'][number]

const emptyDeltas: Deltas = [{insert: '\n', attributes: {}}]

export const adaptationKinds: Adaptation['kind'][] = ['generic', 'fill-with-free-text', 'multiple-choices']

export const textualFieldNames = ['instructions', 'wording', 'example', 'clue', 'textReference'] as const
export type TextualFieldName = typeof textualFieldNames[number]

export type Model = {
  inTextbook: boolean
  number: string
  textbookPage: number | null
  instructions: Deltas
  wording: Deltas
  example: Deltas
  clue: Deltas
  textReference: Deltas
  wordingParagraphsPerPagelet: number | null
  rectangles: PdfRectangle[]
  adaptation: Adaptation
  inProgress:
    {
      kind: 'nothing'
    } | {
      kind: 'multipleChoicesCreation'
    } | {
      kind: 'multipleChoicesEdition'
      initial: boolean
      stopWatching(): void
      deleted: boolean
      delete(): void
      settings: {
        start: string
        stop: string
        separator1: string
        separator2: string
        placeholder: string
      }
    }
}

type MakeModelOptions  = {
  inTextbook: true
  textbookPage: number
} | {
  inTextbook: false
  textbookPage: null
}

function makeModel({inTextbook, textbookPage}: MakeModelOptions): Model {
  return {
    inTextbook,
    number: '',
    textbookPage,
    instructions: [{insert: '\n', attributes: {}}],
    wording: [{insert: '\n', attributes: {}}],
    example: [{insert: '\n', attributes: {}}],
    clue: [{insert: '\n', attributes: {}}],
    textReference: [{insert: '\n', attributes: {}}],
    wordingParagraphsPerPagelet: null,
    rectangles: [],
    adaptation: {kind: 'generic', effects: []},
    inProgress: {
      kind: 'nothing',
    },
  }
}

export function makeModelInTextbook(textbookPage: number): Model {
  return makeModel({inTextbook: true, textbookPage})
}

export function makeModelNotInTextbook(): Model {
  return makeModel({inTextbook: false, textbookPage: null})
}

export function assignModelFrom(model: Model, exercise: Exercise & InCache & Exists) {
  model.number = exercise.attributes.number
  model.instructions = exercise.attributes.instructions
  model.wording = exercise.attributes.wording
  model.example = exercise.attributes.example
  model.clue = exercise.attributes.clue
  model.textReference = exercise.attributes.textReference
  model.wordingParagraphsPerPagelet = exercise.attributes.wordingParagraphsPerPagelet
  model.adaptation = deepCopy(exercise.attributes.adaptation)
  model.rectangles = deepCopy(exercise.attributes.rectangles)
  model.inProgress = {
    kind: 'nothing',
  }
}

function resetModel(model: Model, options: MakeModelOptions) {
  Object.assign(model, makeModel(options))
}

export function resetModelInTextbook(model: Model, textbookPage: number) {
  resetModel(model, {inTextbook: true, textbookPage})
}

export function resetModelNotInTextbook(model: Model) {
  resetModel(model, {inTextbook: false, textbookPage: null})
}

export function modelIsEmpty(model: Model) {
  return  deepEqual(model.instructions, emptyDeltas)
    && deepEqual(model.wording, emptyDeltas)
    && deepEqual(model.example, emptyDeltas)
    && deepEqual(model.clue, emptyDeltas)
    && deepEqual(model.textReference, emptyDeltas)
    && deepEqual(model.adaptation, {kind: 'generic', effects: []})
}

export function cleanupModel(model: Model) {
  let usableColorsCount = 0
  const itemizedEffects = model.adaptation.effects.filter(effect => effect.kind === 'itemized')
  if (itemizedEffects.length === 1) {
    const itemizedEffect = itemizedEffects[0]
    if (itemizedEffect.effects.selectable !== null) {
      usableColorsCount = itemizedEffect.effects.selectable.colors.length
    }
  }
  for (const fieldName of ['instructions', 'wording', 'example'] as const) {
    const newOps = new Delta()
    for (const delta of downgradeDeltas(model[fieldName])) {
      if ('sel' in delta.attributes && (delta.attributes.sel as number) > usableColorsCount) {
        newOps.insert(delta.insert, {})
      } else {
        newOps.insert(delta.insert, delta.attributes)
      }
    }
    model[fieldName] = newOps.ops.map(op => {
      console.assert(typeof op.insert === 'string')
      return {insert: op.insert, attributes: op.attributes ?? {}}
    })
  }
}

function downgradeDeltas(deltas: Deltas) {
  return deltas.map(operation => {
    console.assert(typeof operation.insert === 'string')
    console.assert('attributes' in operation)
    return operation
  })
}

export async function getParsed(model: Model) {
  const parsed = await api.client.createOne(
    'parsedExercise', {
      number: model.number,
      instructions: downgradeDeltas(model.instructions),
      wording: downgradeDeltas(model.wording),
      example: downgradeDeltas(model.example),
      clue: downgradeDeltas(model.clue),
      textReference: downgradeDeltas(model.textReference),
      wordingParagraphsPerPagelet: model.wordingParagraphsPerPagelet,
      adaptation: model.adaptation,
    },
    {},
  )
  console.assert(parsed.exists)
  return parsed
}

export async function create(project: Project, textbook: Textbook | null, model: Model) {
  return await api.client.createOne(
    'exercise',
    {
      number: model.number,
      textbookPage: model.textbookPage,
      instructions: downgradeDeltas(model.instructions),
      wording: downgradeDeltas(model.wording),
      example: downgradeDeltas(model.example),
      clue: downgradeDeltas(model.clue),
      textReference: downgradeDeltas(model.textReference),
      wordingParagraphsPerPagelet: model.wordingParagraphsPerPagelet,
      adaptation: model.adaptation,
      rectangles: model.rectangles,
    },
    {
      project,
      textbook,
    },
  )
}

export async function save(exercise: Exercise & InCache & Exists, model: Model) {
  await exercise.patch(
    {
      instructions: downgradeDeltas(model.instructions),
      wording: downgradeDeltas(model.wording),
      example: downgradeDeltas(model.example),
      clue: downgradeDeltas(model.clue),
      textReference: downgradeDeltas(model.textReference),
      wordingParagraphsPerPagelet: model.wordingParagraphsPerPagelet,
      adaptation: model.adaptation,
      rectangles: model.rectangles,
    },
    {},
  )
}

export function suggestNextNumber(number: string) {
  const n = parseInt(number)
  if (Number.isInteger(n)) {
    return (n + 1).toString()
  } else {
    return ''
  }
}
</script>

<script setup lang="ts">
import { ref, computed } from 'vue'
import deepCopy from 'deep-copy'
import { useI18n } from 'vue-i18n'

import { BRow, BCol, BLabeledInput, BLabeledSelect } from './opinion/bootstrap'
import WysiwygEditor from './WysiwygEditor.vue'
import { wysiwygBlots } from './AdaptationDetailsFieldsForm.vue'
import OptionalWysiwygEditor from './OptionalWysiwygEditor.vue'


defineProps<{
  fixedNumber: boolean
  displayedPage: number | null
}>()

const model = defineModel<Model>({required: true})

const i18n = useI18n()

const instructionsEditor = ref<InstanceType<typeof WysiwygEditor> | null>(null)
const wordingEditor = ref<InstanceType<typeof WysiwygEditor> | null>(null)
const exampleEditor = ref<InstanceType<typeof OptionalWysiwygEditor> | null>(null)
const clueEditor = ref<InstanceType<typeof OptionalWysiwygEditor> | null>(null)
const textReferenceEditor = ref<InstanceType<typeof OptionalWysiwygEditor> | null>(null)
const editors = {
  instructions: instructionsEditor,
  wording: wordingEditor,
  example: exampleEditor,
  clue: clueEditor,
  textReference: textReferenceEditor,
}

const allOptionalsAreCollapsed = computed(() => {
  return !exampleEditor.value?.expanded && !clueEditor.value?.expanded && !textReferenceEditor.value?.expanded
})

const saveDisabled = computed(() => model.value.number === '')

function highlightSuffix(fieldName: TextualFieldName, suffix: string) {
  const editor = editors[fieldName].value
  console.assert(editor !== null)
  editor.focus()
  editor.setSelection(editor.getLength() - suffix.length - 1, suffix.length)
}

function toggle(format: string, value: unknown = true) {
  if (focusedWysiwygField.value !== null) {
    const editor = editors[focusedWysiwygField.value]
    console.assert(editor.value !== null)
    editor.value.toggle(format, value)
  }
}

const focusedWysiwygField = computed(() => {
  if (instructionsEditor.value?.hasFocus) {
    return 'instructions'
  } else if (wordingEditor.value?.hasFocus) {
    return 'wording'
  } else if (exampleEditor.value?.hasFocus) {
    return 'example'
  } else if (clueEditor.value?.hasFocus) {
    return 'clue'
  } else if (textReferenceEditor.value?.hasFocus) {
    return 'textReference'
  } else {
    return null
  }
})

const currentWysiwygFormat = computed(() => {
  if (instructionsEditor.value?.hasFocus) {
    return instructionsEditor.value.currentFormat
  } else if (wordingEditor.value?.hasFocus) {
    return wordingEditor.value.currentFormat
  } else if (exampleEditor.value?.hasFocus) {
    return exampleEditor.value.currentFormat
  } else if (clueEditor.value?.hasFocus) {
    return clueEditor.value.currentFormat
  } else if (textReferenceEditor.value?.hasFocus) {
    return textReferenceEditor.value.currentFormat
  } else {
    return {}
  }
})


const selBlotColors = computed(() => {
  const selectableEffects = model.value.adaptation.effects.filter(effect => effect.kind === 'itemized' && effect.effects.selectable !== null)
  console.assert(selectableEffects.length <= 1)
  if (selectableEffects.length === 0) {
    return {}
  } else {
    const effect = selectableEffects[0]
    console.assert(effect.kind === 'itemized')
    console.assert(effect.effects.selectable !== null)
    return Object.fromEntries(effect.effects.selectable.colors.map((color, i) => [`--sel-blot-color-${i + 1}`, color]))
  }
})

function selectionChangeInInstructionsOrWording(fieldName: 'instructions' | 'wording', range: {index: number, length: number}) {
  if (model.value.inProgress.kind === 'multipleChoicesCreation') {
    const selected = downgradeDeltas(model.value[fieldName]).map(delta => delta.insert).join('').slice(range.index, range.index + range.length)

    const [start, stop] = (() => {
      for (const [start, stop] of [['(', ')'], ['[', ']']]) {
        if (selected.startsWith(start) && selected.endsWith(stop)) {
          return [start, stop]
        }
      }
      return ['', '']
    })()

    const separator1 = (() => {
      for (const separator of ['/', '|', ',', '*', 'ou', 'or']) {
        if (selected.includes(separator)) {
          return separator
        }
      }
      return ''
    })()

    const separator2 = (() => {
      for (const separator of [i18n.t('multipleChoicesSeparator2'), 'ou', 'or']) {
        if (selected.includes(' ' + separator + ' ')) {
          return separator
        }
      }
      return ''
    })()

    const settings = {
      start,
      stop,
      separator1,
      separator2,
      placeholder: '',
      justCreated: true,
    }

    toggle('choices2', settings)
  }
}

function selectionChangeInInstructions(range: {index: number, length: number}) {
  selectionChangeInInstructionsOrWording('instructions', range)
}

function selectionChangeInWording(range: {index: number, length: number}) {
  selectionChangeInInstructionsOrWording('wording', range)
}

defineExpose({
  saveDisabled,
  highlightSuffix,
  toggle,
  focusedWysiwygField,
  currentWysiwygFormat,
})
</script>

<template>
  <div class="overflow-x-hidden">
    <BRow>
      <BCol>
        <BLabeledInput :label="$t('exerciseNumber')" v-model="model.number" data-cy-exercise-field="number" :disabled="fixedNumber" />
      </BCol>
      <BCol v-if="model.inTextbook">
        <!-- @todo Add warning icon when different from displayed page -->
        <BLabeledInput :label="$t( model.textbookPage === displayedPage ? 'exercisePage' : 'exercisePageWithWarning')" v-model="model.textbookPage" data-cy-exercise-field="page" :disabled="fixedNumber" />
      </BCol>
    </BRow>
  </div>
  <div :style="{position: 'relative', ...selBlotColors}">
    <BLabeledSelect
      :label="$t('adaptationType')" v-model="model.adaptation.kind"
      :options="adaptationKinds.map(kind => ({value: kind, label: $t(kind)}))"
    />
    <WysiwygEditor
      ref="instructionsEditor"
      :label="$t('exerciseInstructions')"
      :blots="wysiwygBlots"
      v-model="model.instructions"
      @selectionChange="selectionChangeInInstructions"
    />
    <WysiwygEditor
      ref="wordingEditor"
      :label="$t('exerciseWording')"
      :blots="wysiwygBlots"
      v-model="model.wording"
      @selectionChange="selectionChangeInWording"
    />
    <div :class="{'container-fluid': allOptionalsAreCollapsed}">
      <div :class="{row: allOptionalsAreCollapsed}">
        <div :class="{col: allOptionalsAreCollapsed}" style="padding: 0;">
          <OptionalWysiwygEditor
            ref="exampleEditor"
            :label="$t('exerciseExample')"
            :blots="wysiwygBlots"
            v-model="model.example"
          />
        </div>
        <div :class="{col: allOptionalsAreCollapsed}" style="padding: 0;">
          <OptionalWysiwygEditor
            ref="clueEditor"
            :label="$t('exerciseClue')"
            :blots="wysiwygBlots"
            v-model="model.clue"
          />
        </div>
        <div :class="{col: allOptionalsAreCollapsed}" style="padding: 0;">
          <OptionalWysiwygEditor
            ref="textReferenceEditor"
            :label="$t('exerciseTextReference')"
            :blots="wysiwygBlots"
            v-model="model.textReference"
          />
        </div>
      </div>
    </div>

    <slot name="overlay"></slot>
  </div>
</template>
