<script setup>
import fr from '../content/fr/help.md?raw'
import en from '../content/en/help.md?raw'

import Markdown from 'vue3-markdown-it';


const content = { en, fr }
</script>

<template>
  <markdown html :source="content[$i18n.locale]" />
</template>
