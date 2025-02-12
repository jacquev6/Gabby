<script lang="ts">
import Quill from 'quill/core'

import { InlineBlot, type Model as Deltas } from '$frontend/components/Quill.vue'
import ContextMenu from '$frontend/components/ContextMenu.vue'
import deepCopy from 'deep-copy'


let model = ref<Model>(null as any/* OK: 'model' is assigned a value in "script setup" below */ as Model)
const choices2ContextMenu = ref<InstanceType<typeof ContextMenu> | null>(null)

export class Choices2Blot extends InlineBlot {
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
</script>

<script setup lang="ts">
import { computed, ref, watch } from 'vue'

import { BRow, BCol, BLabeledInput, BButton, BLabeledCheckbox } from '../../../../components/opinion/bootstrap'
import ExerciseFieldsForm, { defaultAdaptationSettings, type Model } from './ExerciseFieldsForm.vue'
import type { Textbook } from '$frontend/stores/api'


defineProps<{
  textbook: Textbook
  fields: InstanceType<typeof ExerciseFieldsForm>
  hasItems: boolean
}>()

const model_ = defineModel<Model>({required: true})
model = model_

const hasPredefinedMcq = computed(() => model.value.adaptationSettings.itemized.effects.hasGenderMcq || model.value.adaptationSettings.itemized.effects.hasNumberMcq)

const showArrowBeforeMcqFields = computed({
  get() {
    return model.value.adaptationSettings.showArrowBeforeMcqFields || hasPredefinedMcq.value
  },
  set(value: boolean) {
    model.value.adaptationSettings.showArrowBeforeMcqFields = value
  },
})

const hasMcqBeside = computed({
  get() {
    return model.value.adaptationSettings.itemized.effects.hasMcqBeside || hasPredefinedMcq.value
  },
  set(value: boolean) {
    model.value.adaptationSettings.itemized.effects.hasMcqBeside = value
    if (value) {
      model.value.adaptationSettings.itemized.effects.hasMcqBelow = false
    }
  },
})

const hasMcqBelow = computed({
  get() {
    return model.value.adaptationSettings.itemized.effects.hasMcqBelow
  },
  set(value: boolean) {
    model.value.adaptationSettings.itemized.effects.hasMcqBelow = value
    if (value) {
      model.value.adaptationSettings.itemized.effects.hasMcqBeside = false
    }
  },
})

const repeatedWithMcq = computed({
  get() {
    return model.value.adaptationSettings.itemized.effects.repeatedWithMcq
  },
  set(value: boolean) {
    model.value.adaptationSettings.itemized.effects.repeatedWithMcq = value
    if (value) {
      model.value.adaptationSettings.itemized.items = deepCopy(defaultAdaptationSettings.itemized.items)
    }
  },
})
</script>

<template>
  <ContextMenu ref="choices2ContextMenu" backdropCovers1="#left-col-2" backdropCovers2="#gutter-2" @hidden="doneEditingChoices2">
    <template v-if="model.inProgress.kind === 'multipleChoicesEdition'">
      <div class="container-fluid">
        <BRow>
          <BCol><BLabeledInput :label="$t('choicesSettingsSeparators')" style="width: 8em" v-model="model.inProgress.settings.separator1" /></BCol>
          <BCol><BLabeledInput label="&nbsp;" style="width: 8em" v-model="model.inProgress.settings.separator2" data-cy="second-mcq-separator" /></BCol>
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

  <BLabeledCheckbox :label="$t('alwaysShowMultipleChoices')" v-model="model.adaptationSettings.showMcqChoicesByDefault" />
  <BButton primary sm @click="model.inProgress = {kind: 'multipleChoicesCreation'}">{{ $t('multipleChoicesButton') }}</BButton>
  <div style="padding-left: 1em; padding-top: 0.5em;">
    <BLabeledCheckbox :label="$t('showArrowBeforeMultipleChoices')" v-model="showArrowBeforeMcqFields" :disabled="hasPredefinedMcq" />
    <BLabeledCheckbox :label="$t('multipleChoicesBesideEachItem')" v-model="hasMcqBeside" :disabled="!hasItems || hasPredefinedMcq" />
    <BLabeledCheckbox :label="$t('multipleChoicesBelowEachItem')" v-model="hasMcqBelow" :disabled="!hasItems || hasPredefinedMcq" />
    <BLabeledCheckbox :label="$t('multipleChoicesGender')" v-model="model.adaptationSettings.itemized.effects.hasGenderMcq" :disabled="!hasItems" />
    <BLabeledCheckbox :label="$t('multipleChoicesNumber')" v-model="model.adaptationSettings.itemized.effects.hasNumberMcq" :disabled="!hasItems" />
    <BLabeledCheckbox :label="$t('multipleChoicesRepeatedWithMcq')" v-model="repeatedWithMcq" />
  </div>
</template>

<style>
div.ql-editor choice-blot {
  margin: 0;
  padding: 0 0.4em;
  border: 2px solid black;
}

div.ql-editor choices2-blot {
  margin: 0;
  padding: 0;
  border-top: 2px solid black;
  border-bottom: 2px solid black;
  background-color: lightgray;
}

p.separatorSuggestion {
  margin: 0;
  text-align: center;
  cursor: pointer;
}

p.separatorSuggestion:hover {
  background-color: lightblue;
}
</style>
