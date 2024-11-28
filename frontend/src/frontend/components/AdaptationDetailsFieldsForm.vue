<script lang="ts">
import Quill from 'quill/core'

import { InlineBlot, type Model as Deltas } from './Quill.vue'
import { basicBlots } from './WysiwygEditor.vue'
import ContextMenu from './ContextMenu.vue'


// Keep the 'style' section below consistent with the length of this array
export const defaultColors = [
  // Colors provided by the client
  "#ffff00",  // yellow
  "#ffc0cb",  // pink (light red)
  "#bbbbff",  // light blue
  "#bbffbb",  // light green
  "#bbbbbb",  // grey
  // Colors suggested by Vincent Jacques on the same pattern
  // "#bbffff",  // light cyan
  // "#ffbbff",  // light magenta
]

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

class SelectableBlot extends InlineBlot {
  static override blotName = 'selectable'
  static override tagName = 'selectable-blot'
}

export const wysiwygBlots = [
  ...basicBlots,
  SelBlot,
  Choices2Blot,
  SelectableBlot,
]
</script>

<script setup lang="ts">
import { computed, reactive, ref, watch } from 'vue'
import deepEqual from 'deep-equal'

import { BRow, BCol, BLabeledInput, BButton, BLabeledCheckbox, BRadio } from './opinion/bootstrap'
import ExerciseFieldsForm, { type Model, cleanupModel } from './ExerciseFieldsForm.vue'
import { defaultColors as defaultColorsForSelectableEffect } from './AdaptationDetailsFieldsForm.vue'
import FloatingColorPicker from './FloatingColorPicker.vue'
import OptionalInput from './OptionalInput.vue'


defineProps<{
  fields: InstanceType<typeof ExerciseFieldsForm>
}>()

type ItemizeEffect = Model['adaptation']['effects'][number] & {kind: 'itemized'}

const model_ = defineModel<Model>({required: true})
model = model_

const fillWithFreeTextPlaceholder = computed({
  get() {
    const fillWithFreeTextEffects = model.value.adaptation.effects.filter(effect => effect.kind === 'fill-with-free-text')
    console.assert(fillWithFreeTextEffects.length <= 1)
    if (fillWithFreeTextEffects.length === 1) {
      return fillWithFreeTextEffects[0].placeholder
    } else {
      return ''
    }
  },
  set(value: string) {
    if (value === '') {
      model.value.adaptation.effects = model.value.adaptation.effects.filter(effect => effect.kind !== 'fill-with-free-text')
    } else {
      const fillWithFreeTextEffects = model.value.adaptation.effects.filter(effect => effect.kind === 'fill-with-free-text')
      console.assert(fillWithFreeTextEffects.length <= 1)
      if (fillWithFreeTextEffects.length === 0) {
        model.value.adaptation.effects.push({kind: 'fill-with-free-text', placeholder: value})
      } else {
        fillWithFreeTextEffects[0].placeholder = value
      }
    }
  },
})

// Keep settings in memory even when they are not used, so that they are not reset when used again.
const settings = reactive({
  itemized: {
    items: {
      kind: 'words' as ItemizeEffect['items']['kind'],
      words: {punctuation: false},
    },
    effects: {
      isSelectable: false,
      selectable: {
        colorsCount: 2,
        allColors: [...defaultColorsForSelectableEffect],
      },
      isBoxed: false,
    },
  },
})

function makeEffect(): ItemizeEffect | null {
  if (settings.itemized.effects.isSelectable || settings.itemized.effects.isBoxed) {
    return {
      kind: 'itemized',
      items: settings.itemized.items.kind === 'words' ? {
        kind: 'words',
        punctuation: settings.itemized.items.words.punctuation,
      } : {
        kind: settings.itemized.items.kind,
      },
      effects: {
        selectable: settings.itemized.effects.isSelectable ? {
          colors: settings.itemized.effects.selectable.allColors.slice(0, settings.itemized.effects.selectable.colorsCount),
        } : null,
        boxed: settings.itemized.effects.isBoxed,
      },
    }
  } else {
    return null
  }
}

watch(
  model,
  () => {
    const itemizedEffects = model.value.adaptation.effects.filter(effect => effect.kind === 'itemized')
    console.assert(itemizedEffects.length <= 1)

    if (itemizedEffects.length === 0) {
      settings.itemized.effects.isSelectable = false
      settings.itemized.effects.isBoxed = false

      console.assert(makeEffect() === null)
    } else {
      const itemizedEffect = itemizedEffects[0]
      settings.itemized.items.kind = itemizedEffect.items.kind
      if (itemizedEffect.items.kind === 'words') {
        settings.itemized.items.words.punctuation = itemizedEffect.items.punctuation
      }
      if (itemizedEffect.effects.selectable !== null) {
        settings.itemized.effects.isSelectable = true
        settings.itemized.effects.selectable.colorsCount = itemizedEffect.effects.selectable.colors.length
        settings.itemized.effects.selectable.allColors.splice(
          0,
          itemizedEffect.effects.selectable.colors.length,
          ...itemizedEffect.effects.selectable.colors
        )
      }
      settings.itemized.effects.isBoxed = itemizedEffect.effects.boxed

      console.assert(deepEqual(makeEffect(), itemizedEffect))
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
    const itemizedEffects = model.value.adaptation.effects.filter(effect => effect.kind === 'itemized')
    console.assert(itemizedEffects.length <= 1)
    const effect = makeEffect()

    // Break the infinite 'watch' loop by setting the model only if the value has actually changed.
    if (effect === null) {
      if (itemizedEffects.length === 1) {
        model.value.adaptation.effects = model.value.adaptation.effects.filter(effect => effect.kind !== 'itemized')
      }
    } else {
      if (itemizedEffects.length === 0) {
        model.value.adaptation.effects.push(effect)
      } else {
        if (!deepEqual(effect, itemizedEffects[0])) {
          model.value.adaptation.effects = model.value.adaptation.effects.filter(effect => effect.kind !== 'itemized')
          model.value.adaptation.effects.push(effect)
        }
      }
    }

    cleanupModel(model.value)
  },
  {
    deep: true,
  },
)

const colorPickers = ref<InstanceType<typeof FloatingColorPicker>[]>([])
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
    :default="defaultColorsForSelectableEffect[i - 1]"
    backdropCovers1="#left-col-2"
    backdropCovers2="#gutter-2"
  />

  <BButton primary sm @click="model.inProgress = {kind: 'multipleChoicesCreation'}">{{ $t('multipleChoicesButton') }}</BButton>

  <hr />

  <OptionalInput v-model="fillWithFreeTextPlaceholder" :label="$t('placeholderForFreeText')" />
  <!-- <template v-if="fillWithFreeTextPlaceholder !== ''">
    <BLabeledInput :label="$t('placeholderForFreeText')" type="text" v-model="fillWithFreeTextPlaceholder" />
  </template>
  <template v-else>
    <p>{{ $t('placeholderForFreeText') }} <BButton sm primary>+</BButton></p>
  </template> -->

  <hr />

  <div class="mb-3">
    <p class="form-label">{{ $t('items') }}</p>
    <BRadio v-model="settings.itemized.items.kind" :label="$t('itemsWords')" value="words" />
    <BLabeledCheckbox :label="$t('itemsPunctuation')" v-model="settings.itemized.items.words.punctuation" :disabled="settings.itemized.items.kind !== 'words'" />
    <BRadio v-model="settings.itemized.items.kind" :label="$t('itemsSentences')" value="sentences" disabled />
    <BRadio v-model="settings.itemized.items.kind" :label="$t('itemsManual')" value="manual" />
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

div.ql-editor selectable-blot {
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
  padding: 0 0.4em;
  border: 2px solid black;
}
</style>
