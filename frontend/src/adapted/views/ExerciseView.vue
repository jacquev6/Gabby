<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

import type { Data, Settings } from '$adapted/types'
import Exercise, { useExercisePagelets } from '$adapted/components/Exercise.vue'
import PageletsNavigationControls from '$adapted/components/PageletsNavigationControls.vue'


const props = defineProps<{
  data: Data,
  settings: Settings,
  exerciseId: string,
  pageletIndex: number,
}>()

const router = useRouter()

const exercise = computed(() => {
  return props.data.exercises[props.exerciseId]
})

const { firstWordingParagraph, lastWordingParagraph, pageletsCount } = useExercisePagelets(
  computed(() => exercise.value.wording_paragraphs_per_pagelet),  // @todo Rename to wordingParagraphsPerPagelet
  computed(() => exercise.value.wording.paragraphs.length),
  computed(() => props.pageletIndex),
)

const exerciseComponent = ref<InstanceType<typeof Exercise> | null>(null)

function changePagelet(newPageletIndex: number) {
  if (newPageletIndex >= 0 && newPageletIndex < pageletsCount.value) {
    router.push({name: 'exercise', params: {exerciseId: props.exerciseId, pageletIndex: newPageletIndex.toString()}})
  }
}
</script>

<template>
  <PageletsNavigationControls :pageletsCount :modelValue="pageletIndex" @update:modelValue="changePagelet">
    <Exercise
      ref="exerciseComponent"
      :projectId="data.projectId"
      :exerciseId
      :exercise
      :firstWordingParagraph
      :lastWordingParagraph
      :settings
    />
  </PageletsNavigationControls>
</template>
