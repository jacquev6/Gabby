<script lang="ts">
import { InlineBlot } from './Quill.vue'
import { basicFormats } from './WysiwygEditor.vue'


class ChoiceBlot extends InlineBlot {
  static override blotName = 'choice'
  static override tagName = 'choice-blot'
}

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

const selectThingsFormats = {
  ...basicFormats,
  sel: {
    make: (text: string, value: unknown) => `{sel${value}|${text}}`,
    blot: SelBlot,
  },
}

class SelectableBlot extends InlineBlot {
  static override blotName = 'selectable'
  static override tagName = 'selectable-blot'
}

const itemsAndEffectsWordingFormats = {
  ...basicFormats,
  selectable: {
    make: (text: string) => `{selectable|${text}}`,
    blot: SelectableBlot,
  },
}

export const wysiwygFormats = {
  'null': {
    instructions: basicFormats,
    wording: basicFormats,
    example: basicFormats,
    clue: basicFormats,
  },
  'fill-with-free-text': {
    instructions: basicFormats,
    wording: basicFormats,
    example: basicFormats,
    clue: basicFormats,
  },
  'items-and-effects-attempt-1': {
    instructions: selectThingsFormats,
    wording: itemsAndEffectsWordingFormats,
    example: selectThingsFormats,
    clue: selectThingsFormats,
  },
  'select-things': {
    instructions: selectThingsFormats,
    wording: basicFormats,
    example: selectThingsFormats,
    clue: selectThingsFormats,
  },
  'multiple-choices-in-instructions': {
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
  'multiple-choices-in-wording': {
    instructions: basicFormats,
    wording: basicFormats,
    example: basicFormats,
    clue: basicFormats,
  },
}
</script>

<script setup lang="ts">
import { computed, reactive, ref } from 'vue'

import { BLabeledInput, BLabeledCheckbox } from './opinion/bootstrap'
import type { Model } from './ExerciseFieldsForm.vue'
import type ExerciseFieldsForm from './ExerciseFieldsForm.vue'
import FloatingColorPicker from './FloatingColorPicker.vue'
import AdaptationDetailsFieldsFormForItemsAndEffectsAttempt1 from './AdaptationDetailsFieldsFormForItemsAndEffectsAttempt1.vue'


defineProps<{
  wysiwyg: boolean
  fields: InstanceType<typeof ExerciseFieldsForm>
}>()

const model = defineModel<Model>({required: true})

const colorPickers = ref<InstanceType<typeof FloatingColorPicker>[]>([])

const allColors = reactive([...defaultColors])
const colors = allColors.map((_color, i) => computed({
  get() {
    if (i < model.value.adaptations['select-things'].colors.length) {
      return model.value.adaptations['select-things'].colors[i]
    } else {
      return allColors[i]
    }
  },
  set(value) {
    allColors[i] = value
    if (i < model.value.adaptations['select-things'].colors.length) {
      model.value.adaptations['select-things'].colors[i] = value
    }
  },
}))

const colorsCount = computed({
  get: () => model.value.adaptations['select-things'].colors.length,
  set: (value) => {
    const prev = model.value.adaptations['select-things'].colors.length
    if (value > prev) {
      for (let k = prev; k !== value; ++k) {
        model.value.adaptations['select-things'].colors.push(allColors[k])
      }
    } else {
      model.value.adaptations['select-things'].colors.length = value
    }
  },
})
</script>

<template>
  <template v-if="model.adaptationKind === 'null'">
  </template>
  <template v-else-if="model.adaptationKind === 'fill-with-free-text'">
    <BLabeledInput :label="$t('placeholderText')" type="text" v-model="model.adaptations['fill-with-free-text'].placeholder" />
  </template>
  <template v-else-if="model.adaptationKind === 'items-and-effects-attempt-1'">
    <AdaptationDetailsFieldsFormForItemsAndEffectsAttempt1 v-model="model" />
  </template>
  <template v-else-if="model.adaptationKind === 'select-things'">
    <template v-if="wysiwyg">
      <FloatingColorPicker
        v-for="i in colors.length"
        ref="colorPickers"
        v-model="colors[i - 1].value"
        :default="defaultColors[i - 1]"
      />
      <div class="mb-3">
        <label class="form-label" for="blah">{{ $t('usableColors' )}}</label>
        <span class="maybe-usable-colors-container">
          <span v-for="i in colors.length" :class="i - 1 < model.adaptations['select-things'].colors.length ? 'usable-colors-container' : 'unusable-colors-container'">
            <span
              class="usable-colors-button"
              :style="{backgroundColor: colors[i - 1].value}"
              :data-cy-colors="i"
              @click="colorsCount = i"
              @contextmenu.prevent="(event) => colorPickers[i - 1].show(event.target as HTMLElement)"
            ></span>
          </span>
        </span>
      </div>
      <BLabeledCheckbox :label="$t('includePunctuation')" v-model="model.adaptations['select-things'].punctuation" />
    </template>
    <template v-else>
      <BLabeledInput :label="$t('colorsCount')" type="number" min="1" v-model="colorsCount" />
      <BLabeledCheckbox :label="$t('includePunctuation')" v-model="model.adaptations['select-things'].punctuation" />
      <p class="alert alert-secondary">
        <i18n-t keypath="useSel1ToSelN" v-if="model.adaptations['select-things'].colors.length > 1">
          <template v-slot:first>
            <code>{sel1|<em>text</em>}</code>
          </template>
          <template v-slot:last>
            <code>{sel{{ model.adaptations['select-things'].colors.length }}|<em>text</em>}</code>
          </template>
        </i18n-t>
        <i18n-t keypath="useSel1" v-else>
          <template v-slot:first>
            <code>{sel1|<em>text</em>}</code>
          </template>
        </i18n-t>
      </p>
    </template>
  </template>
  <template v-else-if="model.adaptationKind === 'multiple-choices-in-instructions'">
    <BLabeledInput :label="$t('placeholderText')" type="text" v-model="model.adaptations['multiple-choices-in-instructions'].placeholder" />
    <p v-if="!wysiwyg" class="alert alert-secondary">
      <i18n-t keypath="useChoice">
        <template v-slot:choice>
          <code>{choice|<em>text</em>}</code>
        </template>
      </i18n-t>
    </p>
  </template>
  <template v-else-if="model.adaptationKind === 'multiple-choices-in-wording'">
    <p class="alert alert-secondary">
      <i18n-t keypath="useChoices">
        <template v-slot:choices>
          <code>{choices|<em>text</em>|<em>text</em>|<em>...</em>}</code>
        </template>
      </i18n-t>
    </p>
  </template>
  <template v-else>
    <span>{{ ((t: never) => t)(model.adaptationKind) }}</span>
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
</style>
