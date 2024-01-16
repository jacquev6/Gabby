<script setup>
import { ref } from 'vue'

import PdfPicker from './components/PdfPicker.vue'

const lastSelectedText = ref(null)

function text_selected(text, point) {
  lastSelectedText.value = text
}
</script>

<template>
  <div class="container-fluid">
    <h1>Gabby</h1>
    <div class="row">
      <div class="col">
        <h2>PDF</h2>
        <PdfPicker src="/test.pdf" :page="1" @text-selected="text_selected" />
      </div>
      <div class="col">
        <h2>Form</h2>
        <p>Last selected text:</p><pre>{{ lastSelectedText }}</pre>
      </div>
    </div>
  </div>
</template>
