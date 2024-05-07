<script setup lang="ts">
import { inject } from 'vue'

import { type Data } from '../types'


const data = inject('data') as Data
</script>

<template>
  <ul>
    <li v-for="(exercise, exerciseId) in data.exercises">
      <router-link :to="{name: 'exercise', params: {exerciseId}}">{{ exercise.number }} page {{ exercise.textbook_page }}</router-link>
    </li>
  </ul>
</template>
