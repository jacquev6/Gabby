<script setup lang="ts">
import { BButton } from '$frontend/components/opinion/bootstrap'
import type ExerciseFieldsForm from '$frontend/components/ExerciseFieldsForm.vue'
import type AdaptationDetailsFieldsForm from '$frontend/components/AdaptationDetailsFieldsForm.vue'
import type { Model } from '$frontend/components/ExerciseFieldsForm.vue'
import { computed } from 'vue'


defineProps<{
  fields: InstanceType<typeof ExerciseFieldsForm>
  adaptationDetails: InstanceType<typeof AdaptationDetailsFieldsForm>
}>()

const model = defineModel<Model>({required: true})

const itemizedEffect = computed(() => {
  const itemizedEffects = model.value.adaptation.effects.filter(effect => effect.kind === 'itemized')
  console.assert(itemizedEffects.length <= 1)
  if (itemizedEffects.length === 0) {
    return null
  } else {
    return itemizedEffects[0]
  }
})
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

  <p v-if="itemizedEffect !== null && itemizedEffect.effects.selectable !== null">
    <template v-for="i in itemizedEffect.effects.selectable.colors.length">
      <BButton
        class="format-color"
        sm secondary
        :disabled="fields.focusedWysiwygField === null || fields.focusedWysiwygField === 'wording'"
        :class="{active: fields.currentWysiwygFormat.sel === i}"
        @click="fields.toggle('sel', i)"
        :style="{lineHeight: 0, padding: '2px'}"
        :data-cy="`format-color-${i}`"
      >
        <span :style="{backgroundColor: itemizedEffect.effects.selectable.colors[i - 1]}"></span>
      </BButton>
      <wbr />
    </template>
  </p>

  <p v-if="adaptationDetails.hasManualItems">
    <BButton
      sm secondary
      :disabled="fields.focusedWysiwygField !== 'wording'"
      :class="{active: fields.currentWysiwygFormat['manual-item']}"
      @click="fields.toggle('manual-item')"
      data-cy="format-manual-item"
    >{{ $t('manualItemButton') }}</BButton>
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
