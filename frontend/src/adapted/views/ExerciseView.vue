<script setup lang="ts">
import { ref, computed } from 'vue'

import { BButton } from '$frontend/components/opinion/bootstrap'
import type { Data, Settings } from '$adapted/types'
import Exercise from '$adapted/components/Exercise.vue'
import { useExercisePagelets } from '$adapted/composables/exercisePagelets'


const props = defineProps<{
  data: Data,
  settings: Settings,
  exerciseId: string,
  pageletIndex: number,
}>()

const exercise = computed(() => {
  return props.data.exercises[props.exerciseId]
})

const { firstWordingParagraph, lastWordingParagraph, pageletsCount } = useExercisePagelets(
  computed(() => exercise.value.wording_paragraphs_per_pagelet),  // @todo Rename to wordingParagraphsPerPagelet
  computed(() => exercise.value.wording.paragraphs.length),
  computed(() => props.pageletIndex),
)

const exerciseComponent = ref<InstanceType<typeof Exercise> | null>(null)
</script>

<template>
  <Exercise
    ref="exerciseComponent"
    :projectId="data.projectId"
    :exerciseId
    :exercise
    :firstWordingParagraph
    :lastWordingParagraph
    :settings
  />
  <p>
    <template v-if="pageletsCount !== 1">
      <RouterLink custom :to="{name: 'exercise', params: {pageletIndex: pageletIndex - 1}}" v-slot="{ navigate }">
        <BButton secondary sm @click="navigate" :disabled="pageletIndex === 0">&lt;&lt;</BButton>
      </RouterLink>
      <span>{{ pageletIndex + 1 }} / {{ pageletsCount }}</span>
      <RouterLink custom :to="{name: 'exercise', params: {pageletIndex: pageletIndex + 1}}" v-slot="{ navigate }">
        <BButton secondary sm @click="navigate" :disabled="pageletIndex === pageletsCount - 1">&gt;&gt;</BButton>
      </RouterLink>
    </template>
    <RouterLink custom :to="{name: 'index'}" v-slot="{ navigate }">
      <BButton secondary sm @click="navigate">{{ $t('back') }}</BButton>
    </RouterLink>
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
