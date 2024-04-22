<script setup lang="ts">
import { provide } from 'vue'


const params = new URLSearchParams(window.location.search)
const data = JSON.parse(params.get('data') || '{{ data }}')
const isPreview = params.has('preview')

provide('data', data)
provide('isPreview', isPreview)
</script>

<template>
  <router-view />
</template>

<style>
* {
  font-family: sans-serif;
  font-size: 20px;
  line-height: 30px;
}
</style>
