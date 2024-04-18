<script setup lang="ts">
import { inject } from 'vue'

import { type Data } from '../types'


const data = inject('data') as Data
</script>

<template>
  <ul>
    <li v-for="(exercise, exerciseIndex) in data.exercises">
      <router-link :to="{name: 'exercise', params: {exerciseIndex}}">{{ exercise.number }} page {{ exercise.textbookPage }}</router-link>
    </li>
  </ul>
</template>
