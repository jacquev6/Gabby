<script setup lang="ts">
import { ref, computed, watch } from 'vue'

import type { Exercise } from '$adapted/types'
import { BButton } from '$frontend/components/opinion/bootstrap'
import ExerciseComponent, { useExercisePagelets } from '$adapted/components/Exercise.vue'
import PageletsNavigationControls from '$adapted/components/PageletsNavigationControls.vue'


const props = defineProps<{
  projectId: string,
  exerciseId: string,
  exercise: Exercise,
}>()

const settings = {
  centeredInstructions: true,
  tricolorWording: true,
}

const pageletIndex = ref(0)

const { firstWordingParagraph, lastWordingParagraph, pageletsCount } = useExercisePagelets(
  computed(() => props.exercise.wording_paragraphs_per_pagelet),  // @todo Rename to wordingParagraphsPerPagelet
  computed(() => props.exercise.wording.paragraphs.length),
  pageletIndex,
)

watch(pageletsCount, () => {
  if (pageletIndex.value >= pageletsCount.value) {
    pageletIndex.value = pageletsCount.value - 1
  }
})

const exerciseComponent = ref<InstanceType<typeof ExerciseComponent> | null>(null)
</script>

<template>
  <div style="border: 1px solid black">
    <PageletsNavigationControls :pageletsCount v-model="pageletIndex">
      <ExerciseComponent
        ref="exerciseComponent"
        :projectId="props.projectId"
        :exerciseId="props.exerciseId"
        :exercise
        :firstWordingParagraph
        :lastWordingParagraph
        :settings
        :isPreview="true"
      />
      <div style="height: 10em"></div>
    </PageletsNavigationControls>
  </div>
  <p>
    Page {{ pageletIndex + 1 }} / {{ pageletsCount }}
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
