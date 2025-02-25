<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

import type { Data } from '$adapted/types'
import Exercise from '$adapted/components/Exercise.vue'
import PageletsNavigationControls from '$adapted/components/PageletsNavigationControls.vue'


const props = defineProps<{
  data: Data,
  blah: string
  exerciseId: string,
  pageletIndex: number,
}>()

const router = useRouter()

const exercise = computed(() => {
  return props.data.exercises[props.exerciseId]
})

const pageletsCount = computed(() => exercise.value.pagelets.length)

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
      :pageletIndex
    />
  </PageletsNavigationControls>
</template>
