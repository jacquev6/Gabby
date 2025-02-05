<script lang="ts">
import Quill from 'quill/core'

import { InlineBlot, type Model as Deltas } from './Quill.vue'
import { basicBlots } from './WysiwygEditor.vue'
import ContextMenu from './ContextMenu.vue'


class SelBlot extends InlineBlot {
  static override blotName = 'sel'
  static override tagName = 'sel-blot'

  static override create(s: number) {
    let node = super.create()
    node.setAttribute('data-sel', s.toString())
    return node
  }

  static override formats(node: HTMLElement) {
    const data = node.getAttribute('data-sel')
    console.assert(data !== null)
    return Number.parseInt(data)
  }
}

let model = ref<Model>(null as any/* OK: 'model' is assigned a value in "script setup" below */ as Model)
const choices2ContextMenu = ref<InstanceType<typeof ContextMenu> | null>(null)

class Choices2Blot extends InlineBlot {
  static override blotName = 'choices2'
  static override tagName = 'choices2-blot'

  static override create(settings: {start: string, separator1: string, separator2: string, stop: string, placeholder: string, justCreated?: boolean}) {
    const needsInitialEdit = settings.justCreated
    delete settings.justCreated

    const node = super.create()
    node.setAttribute('data-gabby-settings', JSON.stringify(settings))

    function editSettings(initial: boolean = false) {
      model.value.inProgress = {
        kind: 'multipleChoicesEdition',
        settings: JSON.parse(node.getAttribute('data-gabby-settings')!),
        initial,
        deleted: false,
        delete() {
          this.deleted = true
          const blot = Quill.find(node)
          console.assert(blot !== null && !(blot instanceof Quill))
          let root = blot
          while (root.parent !== undefined) {
            root = root.parent
          }
          const quillNode = root.domNode.parentElement
          console.assert(quillNode !== null)
          const quill = Quill.find(quillNode)
          console.assert(quill instanceof Quill)
          quill.removeFormat(blot.offset(root), blot.length(), 'user')

          console.assert(choices2ContextMenu.value !== null)
          choices2ContextMenu.value.hide()
        },
        stopWatching: watch(
          () => model.value.inProgress.kind === 'multipleChoicesEdition' && model.value.inProgress.settings,
          settings => {
            if (settings !== false) {
              node.setAttribute('data-gabby-settings', JSON.stringify(settings))
            }
          },
          {deep: true},
        ),
      }

      console.assert(choices2ContextMenu.value !== null)
      choices2ContextMenu.value.show(node)
    }

    node.addEventListener('contextmenu', event => {
      event.preventDefault()
      editSettings()
    })

    if (needsInitialEdit) {
      editSettings(true)
    }

    return node
  }

  static override formats(node: HTMLElement) {
    const settings = node.getAttribute('data-gabby-settings')
    console.assert(settings !== null)
    return JSON.parse(settings)
  }
}

function doneEditingChoices2() {
  console.assert(model.value.inProgress.kind === 'multipleChoicesEdition')
  model.value.inProgress.stopWatching()
  const needsReplication =
    model.value.inProgress.initial
    && !model.value.inProgress.deleted
    && model.value.inProgress.settings.start !== ''
    && model.value.inProgress.settings.separator1 !== ''
    && model.value.inProgress.settings.stop !== ''
    // @todo Don't replicate if current selection doesn't match start separator and stop
  if (needsReplication) {
    console.log('Replicating choices')
    const newWording: Deltas = []
    for (const operation of model.value.wording) {
      console.assert(typeof operation.insert === 'string')
      console.assert('attributes' in operation)
      if (Object.keys(operation.attributes).length === 0) {
        let lastProcessedIndex = -1
        let newInsert = ''
        while (true) {
          const startIndex = operation.insert.indexOf(model.value.inProgress.settings.start, lastProcessedIndex + 1)
          if (startIndex === -1) {
            break
          }
          newInsert += operation.insert.slice(lastProcessedIndex + 1, startIndex)
          if (operation.insert[startIndex - 1] === '|') {
            newInsert += model.value.inProgress.settings.start
            lastProcessedIndex = startIndex + model.value.inProgress.settings.start.length - 1
          } else {
            const stopIndex = operation.insert.indexOf(model.value.inProgress.settings.stop, startIndex + model.value.inProgress.settings.start.length)
            const separatorIndex = operation.insert.indexOf(model.value.inProgress.settings.separator1, startIndex + model.value.inProgress.settings.start.length)
            if (stopIndex !== -1 && separatorIndex !== -1 && separatorIndex < stopIndex) {
              console.log('Replicating choices: found choice:', '#' + operation.insert.slice(startIndex, stopIndex + model.value.inProgress.settings.stop.length) + '#')
            }
            newWording.push({insert: newInsert, attributes: operation.attributes})
            newWording.push({insert: operation.insert.slice(startIndex, stopIndex + model.value.inProgress.settings.stop.length), attributes: {choices2: model.value.inProgress.settings}})
            newInsert = ''
            lastProcessedIndex = stopIndex + model.value.inProgress.settings.stop.length - 1
          }
        }
        newInsert += operation.insert.slice(lastProcessedIndex + 1)
        if (newInsert !== '') {
          newWording.push({insert: newInsert, attributes: operation.attributes})
        }
      } else {
        newWording.push(operation)
      }
    }
    console.log('Replicating choices: previous wording:', model.value.wording)
    model.value.wording = newWording
    console.log('Replicating choices: new wording:', newWording)
  }
  model.value.inProgress = {kind: 'nothing'}
}

class ManualItemBlot extends InlineBlot {
  static override blotName = 'manual-item'
  static override tagName = 'manual-item-blot'
}

export const wysiwygBlots = [
  ...basicBlots,
  SelBlot,
  Choices2Blot,
  ManualItemBlot,
]

export const wysiwygContagiousFormats = ['choices2']

export const wysiwygCompatibleFormats = [['bold', 'italic']]
</script>

<script setup lang="ts">
import { computed, reactive, ref, watch } from 'vue'
import deepEqual from 'deep-equal'

import { BRow, BCol, BLabeledInput, BButton, BLabeledCheckbox } from './opinion/bootstrap'
import ExerciseFieldsForm, { type Model, cleanupModel } from './ExerciseFieldsForm.vue'
import FloatingColorPicker from './FloatingColorPicker.vue'
import OptionalInput from './OptionalInput.vue'


defineProps<{
  fields: InstanceType<typeof ExerciseFieldsForm>
}>()

// Colors provided by the client, in display order
const allColorsForSelectableEffect = [
  '#ffff00',  // yellow
  '#ffcf4c',  // orange
  '#ff8084',  // red
  '#ffc0cb',  // pink
  '#d49cff',  // purple
  '#8177ff',  // dark blue
  '#bbbbff',  // light blue
  '#bbffbb',  // light green
  '#68e495',  // dark green
  '#632f2b',  // brown
  '#bbbbbb',  // grey
  '#000000',  // black
]

// Keep the 'style' section below consistent with the length of this array
const defaultColorsForSelectableEffect = [
  allColorsForSelectableEffect[0],
  allColorsForSelectableEffect[3],
  allColorsForSelectableEffect[6],
  allColorsForSelectableEffect[7],
  allColorsForSelectableEffect[10],
]

const model_ = defineModel<Model>({required: true})
model = model_

const fillWithFreeTextPlaceholder = computed({
  get() {
    if (model.value.adaptation.placeholder_for_fill_with_free_text !== null) {
      return model.value.adaptation.placeholder_for_fill_with_free_text
    } else {
      return ''
    }
  },
  set(value: string) {
    if (value === '') {
      model.value.adaptation.placeholder_for_fill_with_free_text = null
    } else {
      model.value.adaptation.placeholder_for_fill_with_free_text = value
    }
  },
})

// Keep settings in memory even when they are not used, so that they are not reset when used again.
const settings = reactive({
  itemized: {
    items: {
      isLetters: false,
      isWords: false,
      isPunctuation: false,
      isSentences: false,
      isManual: false,
      isSeparated: false,
      separator: '',
    },
    effects: {
      isSelectable: false,
      selectable: {
        colorsCount: 2,
        allColors: [...defaultColorsForSelectableEffect],
      },
      isBoxed: false,
      hasMcqBeside: false,
      hasMcqBelow: false,
    },
  },
})

const isLettersProxy = computed({
  get() {
    return settings.itemized.items.isLetters
  },
  set(value: boolean) {
    settings.itemized.items.isLetters = value
    if (value) {
      settings.itemized.items.isWords = false
      settings.itemized.items.isPunctuation = false
      settings.itemized.items.isSentences = false
      settings.itemized.items.isManual = false
      settings.itemized.items.isSeparated = false
    }
  },
})

const isWordsProxy = computed({
  get() {
    return settings.itemized.items.isWords
  },
  set(value: boolean) {
    settings.itemized.items.isWords = value
    if (value) {
      settings.itemized.items.isLetters = false
      settings.itemized.items.isSentences = false
      settings.itemized.items.isManual = false
      settings.itemized.items.isSeparated = false
    }
  },
})

const isPunctuationProxy = computed({
  get() {
    return settings.itemized.items.isPunctuation
  },
  set(value: boolean) {
    settings.itemized.items.isPunctuation = value
    if (value) {
      settings.itemized.items.isLetters = false
      settings.itemized.items.isSentences = false
      settings.itemized.items.isManual = false
      settings.itemized.items.isSeparated = false
    }
  },
})

const isSentencesProxy = computed({
  get() {
    return settings.itemized.items.isSentences
  },
  set(value: boolean) {
    settings.itemized.items.isSentences = value
    if (value) {
      settings.itemized.items.isLetters = false
      settings.itemized.items.isWords = false
      settings.itemized.items.isPunctuation = false
      settings.itemized.items.isManual = false
      settings.itemized.items.isSeparated = false
    }
  },
})

const isManualProxy = computed({
  get() {
    return settings.itemized.items.isManual
  },
  set(value: boolean) {
    settings.itemized.items.isManual = value
    if (value) {
      settings.itemized.items.isLetters = false
      settings.itemized.items.isWords = false
      settings.itemized.items.isPunctuation = false
      settings.itemized.items.isSentences = false
      settings.itemized.items.isSeparated = false
    }
  },
})

const isSeparatedProxy = computed({
  get() {
    return settings.itemized.items.isSeparated
  },
  set(value: boolean) {
    settings.itemized.items.isSeparated = value
    if (value) {
      settings.itemized.items.isLetters = false
      settings.itemized.items.isWords = false
      settings.itemized.items.isPunctuation = false
      settings.itemized.items.isSentences = false
      settings.itemized.items.isManual = false
    }
  },
})

const hasMcqBesideProxy = computed({
  get() {
    return settings.itemized.effects.hasMcqBeside
  },
  set(value: boolean) {
    settings.itemized.effects.hasMcqBeside = value
    if (value) {
      settings.itemized.effects.hasMcqBelow = false
    }
  },
})

const hasMcqBelowProxy = computed({
  get() {
    return settings.itemized.effects.hasMcqBelow
  },
  set(value: boolean) {
    settings.itemized.effects.hasMcqBelow = value
    if (value) {
      settings.itemized.effects.hasMcqBeside = false
    }
  },
})

watch(
  model,
  model => {
    if (model.adaptation.items === null) {
      const hasItems =
        settings.itemized.items.isLetters
        || settings.itemized.items.isWords
        || settings.itemized.items.isPunctuation
        || settings.itemized.items.isSentences
        || settings.itemized.items.isManual
        || (settings.itemized.items.isSeparated && settings.itemized.items.separator !== '')
      const hasEffects =
        settings.itemized.effects.isSelectable
        || settings.itemized.effects.isBoxed
        || settings.itemized.effects.hasMcqBeside
        || settings.itemized.effects.hasMcqBelow

      if (hasItems && hasEffects) {
        settings.itemized.items.isLetters = false
        settings.itemized.items.isWords = false
        settings.itemized.items.isPunctuation = false
        settings.itemized.items.isSentences = false
        settings.itemized.items.isManual = false
        settings.itemized.items.isSeparated = false
        settings.itemized.items.separator = ''
        settings.itemized.effects.isSelectable = false
        settings.itemized.effects.isBoxed = false
        settings.itemized.effects.hasMcqBeside = false
        settings.itemized.effects.hasMcqBelow = false
      }
    } else {
      if (model.adaptation.items.kind === 'characters') {
        settings.itemized.items.isLetters = model.adaptation.items.letters
        settings.itemized.items.isWords = false
        settings.itemized.items.isPunctuation = false
        settings.itemized.items.isSentences = false
        settings.itemized.items.isManual = false
        settings.itemized.items.isSeparated = false
        settings.itemized.items.separator = ''
      } else if (model.adaptation.items.kind === 'tokens') {
        settings.itemized.items.isLetters = false
        settings.itemized.items.isWords = model.adaptation.items.words
        settings.itemized.items.isPunctuation = model.adaptation.items.punctuation
        settings.itemized.items.isSentences = false
        settings.itemized.items.isManual = false
        settings.itemized.items.isSeparated = false
        settings.itemized.items.separator = ''
      } else if (model.adaptation.items.kind === 'manual') {
        settings.itemized.items.isLetters = false
        settings.itemized.items.isWords = false
        settings.itemized.items.isPunctuation = false
        settings.itemized.items.isSentences = false
        settings.itemized.items.isManual = true
        settings.itemized.items.isSeparated = false
        settings.itemized.items.separator = ''
      } else if (model.adaptation.items.kind === 'sentences') {
        settings.itemized.items.isLetters = false
        settings.itemized.items.isWords = false
        settings.itemized.items.isPunctuation = false
        settings.itemized.items.isSentences = true
        settings.itemized.items.isManual = false
        settings.itemized.items.isSeparated = false
        settings.itemized.items.separator = ''
      } else if (model.adaptation.items.kind === 'separated') {
        settings.itemized.items.isLetters = false
        settings.itemized.items.isWords = false
        settings.itemized.items.isPunctuation = false
        settings.itemized.items.isSentences = false
        settings.itemized.items.isManual = false
        settings.itemized.items.isSeparated = true
        settings.itemized.items.separator = model.adaptation.items.separator
      } else {
        console.assert(false, ((items: never) => items)(model.adaptation.items))
      }

      if (model.adaptation.items_are_selectable !== null) {
        settings.itemized.effects.isSelectable = true
        settings.itemized.effects.selectable.colorsCount = model.adaptation.items_are_selectable.colors.length
        settings.itemized.effects.selectable.allColors.splice(
          0,
          model.adaptation.items_are_selectable.colors.length,
          ...model.adaptation.items_are_selectable.colors
        )
      }
      settings.itemized.effects.isBoxed = model.adaptation.items_are_boxed
      settings.itemized.effects.hasMcqBeside = model.adaptation.items_have_mcq_beside
      settings.itemized.effects.hasMcqBelow = model.adaptation.items_have_mcq_below
    }
  },
  {
    deep: true,
    immediate: true,
  },
)

watch(
  settings,
  () => {
    let isBoxed = settings.itemized.effects.isBoxed
    let selectable = (() => {
      if (settings.itemized.effects.isSelectable) {
        return  {
          colors: settings.itemized.effects.selectable.allColors.slice(0, settings.itemized.effects.selectable.colorsCount),
        }
      } else {
        return null
      }
    })()
    let hasMcqBeside = settings.itemized.effects.hasMcqBeside
    let hasMcqBelow = settings.itemized.effects.hasMcqBelow

    const items = (() => {
      if (isBoxed || selectable !== null || hasMcqBeside || hasMcqBelow) {
        if (settings.itemized.items.isLetters) {
          return {kind: 'characters' as const, letters: true}
        } else if (settings.itemized.items.isWords || settings.itemized.items.isPunctuation) {
          return {kind: 'tokens' as const, words: settings.itemized.items.isWords, punctuation: settings.itemized.items.isPunctuation}
        } else if (settings.itemized.items.isSentences) {
          return {kind: 'sentences' as const}
        } else if (settings.itemized.items.isManual) {
          return {kind: 'manual' as const}
        } else if (settings.itemized.items.isSeparated && settings.itemized.items.separator !== '') {
          return {kind: 'separated' as const, separator: settings.itemized.items.separator}
        } else {
          return null
        }
      } else {
        return null
      }
    })()

    if (items === null) {
      isBoxed = false
      selectable = null
      hasMcqBeside = false
      hasMcqBelow = false
    }

    // Break the infinite 'watch' loop by setting the model only if the value has actually changed.
    if (!deepEqual(items, model.value.adaptation.items)) {
      model.value.adaptation.items = items
    }
    if (!deepEqual(selectable, model.value.adaptation.items_are_selectable)) {
      model.value.adaptation.items_are_selectable = selectable
    }
    if (isBoxed !== model.value.adaptation.items_are_boxed) {
      model.value.adaptation.items_are_boxed = isBoxed
    }
    if (hasMcqBeside !== model.value.adaptation.items_have_mcq_beside) {
      model.value.adaptation.items_have_mcq_beside = hasMcqBeside
    }
    if (hasMcqBelow !== model.value.adaptation.items_have_mcq_below) {
      model.value.adaptation.items_have_mcq_below = hasMcqBelow
    }

    cleanupModel(model.value)
  },
  {
    deep: true,
  },
)

const colorPickers = ref<InstanceType<typeof FloatingColorPicker>[]>([])

defineExpose({
  hasManualItems: computed(() => settings.itemized.items.isManual),
})
</script>

<template>
  <ContextMenu ref="choices2ContextMenu" backdropCovers1="#left-col-2" backdropCovers2="#gutter-2" @hidden="doneEditingChoices2">
    <template v-if="model.inProgress.kind === 'multipleChoicesEdition'">
      <div class="container-fluid">
        <BRow>
          <BCol><BLabeledInput :label="$t('choicesSettingsSeparators')" style="width: 8em" v-model="model.inProgress.settings.separator1" /></BCol>
          <BCol><BLabeledInput label="&nbsp;" style="width: 8em" v-model="model.inProgress.settings.separator2" /></BCol>
        </BRow>
        <BRow>
          <BCol><BLabeledInput :label="$t('choicesSettingsStart')" style="width: 8em" v-model="model.inProgress.settings.start" /></BCol>
          <BCol><BLabeledInput :label="$t('choicesSettingsStop')" style="width: 8em" v-model="model.inProgress.settings.stop" /></BCol>
        </BRow>
        <BLabeledInput :label="$t('choicesSettingsPlaceholder')" v-model="model.inProgress.settings.placeholder" />
        <BButton sm secondary @click="() => {console.assert(model.inProgress.kind === 'multipleChoicesEdition'); model.inProgress.delete()}">{{ $t(model.inProgress.initial ? 'choicesSettingsCancel' : 'choicesSettingsDelete') }}</BButton>
        <BButton sm primary v-if="choices2ContextMenu !== null" @click="choices2ContextMenu.hide()">OK</BButton>
      </div>
    </template>
  </ContextMenu>

  <FloatingColorPicker
    v-for="i in settings.itemized.effects.selectable.allColors.length"
    ref="colorPickers"
    v-model="settings.itemized.effects.selectable.allColors[i - 1]"
    :colors="allColorsForSelectableEffect"
    backdropCovers1="#left-col-2"
    backdropCovers2="#gutter-2"
  />

  <BButton primary sm @click="model.inProgress = {kind: 'multipleChoicesCreation'}">{{ $t('multipleChoicesButton') }}</BButton>
  <div style="padding-left: 1em; padding-top: 0.5em;">
    <BLabeledCheckbox :label="$t('alwaysShowMultipleChoices')" v-model="model.adaptation.show_mcq_choices_by_default" />
    <BLabeledCheckbox :label="$t('showArrowBeforeMultipleChoices')" v-model="model.adaptation.show_arrow_before_mcq_fields" />
    <BLabeledCheckbox :label="$t('multipleChoicesBesideEachItem')" v-model="hasMcqBesideProxy" />
    <BLabeledCheckbox :label="$t('multipleChoicesBelowEachItem')" v-model="hasMcqBelowProxy" />
  </div>

  <hr />

  <OptionalInput v-model="fillWithFreeTextPlaceholder" :label="$t('placeholderForFreeText')" />

  <hr />

  <div class="mb-3">
    <p class="form-label">{{ $t('items') }}</p>
    <BLabeledCheckbox v-model="isLettersProxy" :label="$t('itemsLetters')" />
    <BLabeledCheckbox v-model="isWordsProxy" :label="$t('itemsWords')" />
    <BLabeledCheckbox v-model="isPunctuationProxy" :label="$t('itemsPunctuation')" />
    <BLabeledCheckbox v-model="isSentencesProxy" :label="$t('itemsSentences')" />
    <BLabeledCheckbox v-model="isManualProxy" :label="$t('itemsManual')" />
    <BLabeledCheckbox v-model="isSeparatedProxy" :label="$t('itemsSeparated')"><input @click="isSeparatedProxy = true" v-model="settings.itemized.items.separator" style="width: 2em" /></BLabeledCheckbox>
  </div>
  <p>{{ $t('effects') }}</p>
  <BLabeledCheckbox :label="$t('effectsSelectable')" v-model="settings.itemized.effects.isSelectable" />
  <span class="maybe-usable-colors-container">
    <span v-for="i in settings.itemized.effects.selectable.allColors.length" :class="settings.itemized.effects.isSelectable && i - 1 < settings.itemized.effects.selectable.colorsCount ? 'usable-colors-container' : 'unusable-colors-container'">
      <span
        class="usable-colors-button"
        :style="{backgroundColor: settings.itemized.effects.selectable.allColors[i - 1]}"
        :data-cy-colors="i"
        @click="settings.itemized.effects.isSelectable = true; settings.itemized.effects.selectable.colorsCount = i"
        @contextmenu.prevent="(event) => colorPickers[i - 1].show(event.target as HTMLElement)"
      ></span>
    </span>
  </span>
  <BLabeledCheckbox :label="$t('effectsBoxed')" v-model="settings.itemized.effects.isBoxed" />
</template>

<style scoped>
span.maybe-usable-colors-container {
  display: block flow-root;
  line-height: 0;
}

span.usable-colors-container {
  display: inline flow-root;
  background-color: var(--bs-primary);
}

span.unusable-colors-container {
  display: inline flow-root;
  background-color: var(--bs-secondary);
}

span.usable-colors-button {
  display: inline flow-root;
  margin: 0.25em;
  width: 1.25em;
  height: 1.25em;
  cursor: pointer;
}
</style>

<style>
div.ql-editor choice-blot {
  margin: 0;
  padding: 0 0.4em;
  border: 2px solid black;
}

div.ql-editor manual-item-blot {
  margin: 0;
  padding: 0 0.4em;
  border: 2px dotted black;
}

/* Keep this section consistent with the length of 'defaultColors' array above */
/* @todo Could I generate this section? I've not found how Vue could let me do that. */
div.ql-editor sel-blot[data-sel="1"] {
  background: var(--sel-blot-color-1);
}

div.ql-editor sel-blot[data-sel="2"] {
  background: var(--sel-blot-color-2);
}

div.ql-editor sel-blot[data-sel="3"] {
  background: var(--sel-blot-color-3);
}

div.ql-editor sel-blot[data-sel="4"] {
  background: var(--sel-blot-color-4);
}

div.ql-editor sel-blot[data-sel="5"] {
  background: var(--sel-blot-color-5);
}

div.ql-editor choices2-blot {
  margin: 0;
  padding: 0;
  border-top: 2px solid black;
  border-bottom: 2px solid black;
  background-color: lightgray;
}
</style>
