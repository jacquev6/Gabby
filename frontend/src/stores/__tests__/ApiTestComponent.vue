<script setup>
import { defineApiStore } from '../api.js'


const api = defineApiStore('api', {baseUrl: 'http://fanout:8080/api/'})()
</script>

<template>
  <p>Textbook title: [{{ api.cache.getOne('textbook', '1').attributes?.title }}]</p>
  <p>Section start page: [{{ api.cache.getOne('section', '1').attributes?.textbookStartPage }}]</p>
  <p>Textbook section start page: [{{ api.cache.getOne('textbook', '1').relationships?.sections[0].attributes?.textbookStartPage }}]</p>
  <button @click="api.client.getAll('textbooks')">Fetch textbooks</button>
  <button @click="api.client.getAll('sections')">Fetch sections</button>
</template>
