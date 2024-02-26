<script setup>
import { useApiStore } from '../api.js'

const api = useApiStore()
</script>

<template>
  <p>Textbook title: [{{ api.cache.get('textbook', '1')?.attributes.title }}]</p>
  <p>Section start page: [{{ api.cache.get('section', '1')?.attributes.textbookStartPage }}]</p>
  <p>Textbook section start page: [{{ api.cache.get('textbook', '1')?.relationships.sections[0]?.attributes.textbookStartPage }}]</p>
  <button @click="api.client.get('textbooks')">Fetch textbooks</button>
  <button @click="api.client.get('sections')">Fetch sections</button>
</template>
