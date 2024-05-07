<script setup lang="ts">
import { inject } from 'vue'

import { type Data } from '../types'


const data = inject('data') as Data
</script>

<template>
  <ul>
    <li v-for="(exercise, exerciseIndex) in data.exercises">
      <router-link :to="{name: 'exercise', params: {exerciseIndex}}">{{ exercise.adapted.number }} page {{ exercise.adapted.textbook_page }}</router-link>
    </li>
  </ul>
</template>
