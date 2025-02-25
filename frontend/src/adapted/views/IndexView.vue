<script setup lang="ts">
import type { Data } from '$adapted/types'


defineProps<{
  data: Data,
}>()
</script>

<template>
  <ul>
    <li v-for="(exercise, exerciseId) in data.exercises">
      <RouterLink :to="{name: 'exercise', params: {exerciseId, pageletIndex: 0}}">{{ exercise.number }} page {{ exercise.textbook_page }}</RouterLink>
    </li>
  </ul>
</template>
