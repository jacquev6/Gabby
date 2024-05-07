<script setup lang="ts">
import { provide } from 'vue'

import type { Data, Settings } from './types'


const params = new URLSearchParams(window.location.search)
const data = JSON.parse(params.get('data') || '{{ data }}') as Data
const isPreview = params.has('preview')
const defaultSettings: Settings = {
  tricolorWording: true,
}
const settings: Settings = params.has('settings') ? JSON.parse(params.get('settings')!) as Settings : defaultSettings

provide('data', data)
provide('isPreview', isPreview)
provide('settings', settings)
</script>

<template>
  <RouterView />
</template>

<style>
* {
  font-family: sans-serif;
  font-size: 20px;
  line-height: 30px;
}
</style>
