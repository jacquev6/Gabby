<script setup lang="ts">
import { ref, computed, watch } from 'vue'

import { BButton } from '$frontend/components/opinion/bootstrap'
import Exercise from '$adapted/components/Exercise.vue'
import { useExercisePagelets } from '$/adapted/composables/exercisePagelets'


const props = defineProps<{
  projectId: string,
  exerciseId: string,
  exercise: any,
}>()

const settings = {
  tricolorWording: true,
  wordingParagraphsPerPagelet: 3,
}

const pageletIndex = ref(0)

const { firstWordingParagraph, lastWordingParagraph, pageletsCount } = useExercisePagelets(
  computed(() => settings.wordingParagraphsPerPagelet),
  computed(() => props.exercise.wording.paragraphs.length),
  pageletIndex,
)

watch(pageletsCount, () => {
  if (pageletIndex.value >= pageletsCount.value) {
    pageletIndex.value = pageletsCount.value - 1
  }
})

const exerciseComponent = ref<InstanceType<typeof Exercise> | null>(null)
</script>

<template>
  <Exercise
    ref="exerciseComponent"
    :projectId="props.projectId"
    :exerciseId="props.exerciseId"
    :exercise
    :firstWordingParagraph
    :lastWordingParagraph
    :settings
    :isPreview="true"
  />
  <p>
    <template v-if="pageletsCount !== 1">
      <BButton secondary sm @click="pageletIndex -= 1" :disabled="pageletIndex === 0">&lt;&lt;</BButton>
      <span>{{ pageletIndex + 1 }} / {{ pageletsCount }}</span>
      <BButton secondary sm @click="pageletIndex += 1" :disabled="pageletIndex === pageletsCount - 1">&gt;&gt;</BButton>
    </template>
    <BButton
      data-cy="erase-responses"
      secondary sm
      @click="exerciseComponent?.reinitModels"
      :disabled="exerciseComponent?.disabledReinitModels"
    >
      {{ $t('eraseAnswers') }}
    </BButton>
  </p>
</template>
