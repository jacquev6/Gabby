<script setup>
import { ref } from 'vue'

import PdfPicker from './components/PdfPicker.vue'
import FloatingModal from './components/FloatingModal.vue'

const selectedText = ref(null)
const showTextSelectionMenu = ref(false)
const textSelectionMenuReference = ref({x: 0, y: 0})

function text_selected(text, point) {
  selectedText.value = text
  showTextSelectionMenu.value = true
  textSelectionMenuReference.value = {x: point.clientX, y: point.clientY}
}

const wording = ref('')
const directives = ref('')
</script>

<template>
  <div class="container-fluid">
    <h1>Gabby</h1>
    <div class="row">
      <div class="col">
        <h2>PDF</h2>
        <PdfPicker src="/test.pdf" :page="1" @text-selected="text_selected" />
        <FloatingModal
          v-if="showTextSelectionMenu"
          title="Selected text"
          :reference="textSelectionMenuReference"
          @dismissed="showTextSelectionMenu=false"
        >
          <pre>{{ selectedText }}</pre>
          <p>Add to:</p>
          <div class="row">
            <div class="col">
              <p><button class="btn btn-primary" @click="wording += selectedText; showTextSelectionMenu=false">Wording</button></p>
            </div>
            <div class="col">
              <p><button class="btn btn-primary" @click="directives += selectedText; showTextSelectionMenu=false">Directives</button></p>
              </div>
          </div>
        </FloatingModal>
      </div>
      <div class="col">
        <h2>Form</h2>
        <h3>Wording</h3>
        <pre>{{ wording }}</pre>
        <h3>Directives</h3>
        <pre>{{ directives }}</pre>
      </div>
    </div>
  </div>
</template>
