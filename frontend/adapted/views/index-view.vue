<script setup>
import { inject } from 'vue'


const data = inject('data')
</script>

<template>
  <ul>
    <li v-for="(exercise, exerciseIndex) in data.exercises">
      <router-link :to="{name: 'exercise', params: {exerciseIndex}}">{{ exercise.number }} page {{ exercise.textbookPage }}</router-link>
    </li>
  </ul>
</template>
