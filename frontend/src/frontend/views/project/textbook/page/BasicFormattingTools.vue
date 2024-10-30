<script setup lang="ts">
import { BButton } from '$frontend/components/opinion/bootstrap'
import type ExerciseFieldsForm from '$frontend/components/ExerciseFieldsForm.vue'
import type { Model } from '$frontend/components/ExerciseFieldsForm.vue'


defineProps<{
  fields: InstanceType<typeof ExerciseFieldsForm>
}>()

const model = defineModel<Model>({required: true})
</script>

<template v-if="fields !== null">
  <p>
    <BButton
      sm secondary
      :disabled="fields.focusedWysiwygField == null"
      :class="{active: fields.currentWysiwygFormat.bold}"
      @click="fields.toggle('bold')"
      data-cy="format-bold"
    ><img :style="{height: '1.25em'}" src="/bold.svg" /></BButton>
    <BButton
      sm secondary
      :disabled="fields.focusedWysiwygField == null"
      :class="{active: fields.currentWysiwygFormat.italic}"
      @click="fields.toggle('italic')"
      data-cy="format-italic"
    ><img :style="{height: '1.25em'}" src="/italic.svg" /></BButton>
  </p>

  <p v-if="model.adaptationKind === 'select-things'">
    <template v-for="i in model.adaptationEffects['select-things'].colors.length">
      <BButton
        class="format-color"
        sm secondary
        :disabled="fields.focusedWysiwygField === null || fields.focusedWysiwygField === 'wording'"
        :class="{active: fields.currentWysiwygFormat.sel === i}"
        @click="fields.toggle('sel', i)"
        :style="{lineHeight: 0, padding: '2px'}"
        :data-cy="`format-color-${i}`"
      >
        <span :style="{backgroundColor: model.adaptationEffects['select-things'].colors[i - 1]}"></span>
      </BButton>
      <wbr />
    </template>
  </p>

  <template v-if="model.adaptationKind === 'items-and-effects-attempt-1' && model.adaptationEffects['items-and-effects-attempt-1'].effects.selectable !== null">
    <p>
      <template v-for="i in model.adaptationEffects['items-and-effects-attempt-1'].effects.selectable.colors.length">
        <BButton
          class="format-color"
          sm secondary
          :disabled="fields.focusedWysiwygField === null || fields.focusedWysiwygField === 'wording'"
          :class="{active: fields.currentWysiwygFormat.sel === i}"
          @click="fields.toggle('sel', i)"
          :style="{lineHeight: 0, padding: '2px'}"
          :data-cy="`format-color-${i}`"
        >
          <span :style="{backgroundColor: model.adaptationEffects['items-and-effects-attempt-1'].effects.selectable.colors[i - 1]}"></span>
        </BButton>
        <wbr />
      </template>
    </p>

    <p v-if="model.adaptationEffects['items-and-effects-attempt-1'].items.kind === 'manual'">
      <BButton
        sm secondary
        :disabled="fields.focusedWysiwygField !== 'wording'"
        :class="{active: fields.currentWysiwygFormat.selectable}"
        @click="fields.toggle('selectable')"
        data-cy="format-selectable"
      >{{ $t('selectableButton') }}</BButton>
    </p>
  </template>

  <p v-if="model.adaptationKind === 'multiple-choices-in-instructions'">
    <BButton
      sm secondary
      :disabled="fields.focusedWysiwygField === null || fields.focusedWysiwygField !== 'instructions'"
      :class="{active: fields.currentWysiwygFormat.choice}"
      @click="fields.toggle('choice')"
      data-cy="format-choice"
    >{{ $t('choiceButton') }}</BButton>
  </p>
</template>

<style scoped>
button.format-color > span {
  display: inline flow-root;
  margin: 0.25em;
  width: 1.25em;
  height: 1.25em;
  cursor: pointer;
}
</style>
