<script lang="ts">
import { InlineBlot } from './Quill.vue'
import { basicFormats } from './WysiwygEditor.vue'


class ChoiceBlot extends InlineBlot {
  static override blotName = 'choice'
  static override tagName = 'choice-blot'
}

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

const selectThingsFormats = {
  ...basicFormats,
  sel: {
    make: (text: string, value: unknown) => `{sel${value}|${text}}`,
    blot: SelBlot,
  },
}

export const wysiwygFormats = {
  '-': {
    instructions: basicFormats,
    wording: basicFormats,
    example: basicFormats,
    clue: basicFormats,
  },
  fillWithFreeTextAdaptation: {
    instructions: basicFormats,
    wording: basicFormats,
    example: basicFormats,
    clue: basicFormats,
  },
  selectThingsAdaptation: {
    instructions: selectThingsFormats,
    wording: basicFormats,
    example: selectThingsFormats,
    clue: selectThingsFormats,
  },
  multipleChoicesInInstructionsAdaptation: {
    instructions: {
      ...basicFormats,
      choice: {
        make: (text: string) => `{choice|${text}}`,
        blot: ChoiceBlot,
      },
    },
    wording: basicFormats,
    example: basicFormats,
    clue: basicFormats,
  },
  multipleChoicesInWordingAdaptation: {
    instructions: basicFormats,
    wording: basicFormats,
    example: basicFormats,
    clue: basicFormats,
  },
}
</script>

<script setup lang="ts">
import { BLabeledInput, BLabeledCheckbox } from './opinion/bootstrap'

import { BButton } from './opinion/bootstrap'
import type { Model } from './ExerciseFieldsForm.vue'
import type ExerciseFieldsForm from './ExerciseFieldsForm.vue'
import { colors } from '$adapted/components/SelectedText.vue'


defineProps<{
  wysiwyg: boolean
  fields: InstanceType<typeof ExerciseFieldsForm>
}>()

const model = defineModel<Model>({required: true})
</script>

<template>
  <template v-if="model.adaptationType === '-'">
  </template>
  <template v-else-if="model.adaptationType === 'fillWithFreeTextAdaptation'">
    <BLabeledInput :label="$t('placeholderText')" type="text" v-model="model.fillWithFreeTextAdaptationOptions.placeholder" />
  </template>
  <template v-else-if="model.adaptationType === 'selectThingsAdaptation'">
    <template v-if="wysiwyg">
      <div class="mb-3">
        <label class="form-label" for="blah">{{ $t('usableColors' )}}</label>
        <span class="maybe-usable-colors-container">
          <template v-for="i in colors.length">
            <span :class="i <= model.selectThingsAdaptationOptions.colors ? 'usable-colors-container' : 'unusable-colors-container'">
              <span
                class="usable-colors-button"
                :style="{backgroundColor: colors[i - 1]}"
                :data-cy-colors="i"
                @click="model.selectThingsAdaptationOptions.colors = i"
              ></span>
            </span>
          </template>
        </span>
      </div>
      <div class="mb-3">
        <label class="form-label" for="blah">{{ $t('formatWithColor' )}}</label>
        <p><template v-for="i in model.selectThingsAdaptationOptions.colors">
          <BButton
            sm primary
            :disabled="fields.focusedWysiwygField === null || fields.focusedWysiwygField === 'wording'"
            @click="fields.toggle('sel', i)" :style="{lineHeight: 0, padding: '2px'}"
          >
            <span class="usable-colors-button" :data-cy-colors="i" :style="{backgroundColor: colors[i - 1]}"></span>
          </BButton>
          <wbr>
        </template></p>
      </div>
    </template>
    <template v-else>
      <BLabeledInput :label="$t('colorsCount')" type="number" min="1" v-model="model.selectThingsAdaptationOptions.colors" />
      <p class="alert alert-secondary">
        <i18n-t keypath="useSel1ToSelN" v-if="model.selectThingsAdaptationOptions.colors > 1">
          <template v-slot:first>
            <code>{sel1|<em>text</em>}</code>
          </template>
          <template v-slot:last>
            <code>{sel{{ model.selectThingsAdaptationOptions.colors }}|<em>text</em>}</code>
          </template>
        </i18n-t>
        <i18n-t keypath="useSel1" v-else>
          <template v-slot:first>
            <code>{sel1|<em>text</em>}</code>
          </template>
        </i18n-t>
      </p>
    </template>
    <BLabeledCheckbox :label="$t('includePunctuation')" v-model="model.selectThingsAdaptationOptions.punctuation" />
  </template>
  <template v-else-if="model.adaptationType === 'multipleChoicesInInstructionsAdaptation'">
    <template v-if="wysiwyg">
      <p><BButton sm primary :disabled="fields.focusedWysiwygField !== 'instructions'" @click="fields.toggle('choice')">{{ $t('choiceButton') }}</BButton></p>
    </template>
    <p v-else class="alert alert-secondary">
      <i18n-t keypath="useChoice">
        <template v-slot:choice>
          <code>{choice|<em>text</em>}</code>
        </template>
      </i18n-t>
    </p>
    <BLabeledInput :label="$t('placeholderText')" type="text" v-model="model.multipleChoicesInInstructionsAdaptationOptions.placeholder" />
  </template>
  <template v-else-if="model.adaptationType === 'multipleChoicesInWordingAdaptation'">
    <p class="alert alert-secondary">
      <i18n-t keypath="useChoices">
        <template v-slot:choices>
          <code>{choices|<em>text</em>|<em>text</em>|<em>...</em>}</code>
        </template>
      </i18n-t>
    </p>
  </template>
  <template v-else>
    <span>{{ ((t: never) => t)(model.adaptationType) }}</span>
  </template>
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

/* Keep this section consistent with the 'colors' array in 'SeletctedText.vue' */
/* @todo Could I generate this section? I've not found how Vue could let me do that. */
div.ql-editor sel-blot[data-sel="1"] {
  background: #ffff00;
}

div.ql-editor sel-blot[data-sel="2"] {
  background: #ffc0cb;
}

div.ql-editor sel-blot[data-sel="3"] {
  background: #bbbbff;
}

div.ql-editor sel-blot[data-sel="4"] {
  background: #bbffbb;
}

div.ql-editor sel-blot[data-sel="5"] {
  background: #bbbbbb;
}

div.ql-editor sel-blot[data-sel="6"] {
  background: #bbffff;
}

div.ql-editor sel-blot[data-sel="7"] {
  background: #ffbbff;
}
</style>
