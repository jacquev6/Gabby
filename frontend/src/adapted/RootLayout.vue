<script setup lang="ts">
import type { Data } from './types'


const data = JSON.parse('{{ data }}') as Data
const settings = {
  tricolorWording: true,
  wordingParagraphsPerPagelet: 3,
}
</script>

<template>
  <div class="container-fluid">
    <RouterView v-slot="{ Component }"><component :is="Component" :data :settings /></RouterView>
  </div>
</template>
