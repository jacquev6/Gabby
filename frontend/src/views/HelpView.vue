<script setup>
import { reactive } from 'vue'

import fr from '../content/fr/help.md?raw'
import en from '../content/en/help.md?raw'

import Markdown from 'vue3-markdown-it';


const content = reactive({ en, fr })
</script>

<template>
  <div class="markdown">
    <markdown html :source="content[$i18n.locale]" />
  </div>
</template>

<style>
  div.markdown img {
    border: 1px solid black;
  }
</style>
