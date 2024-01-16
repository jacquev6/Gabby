<script setup>
import { ref, reactive } from 'vue'
import { useFloating, autoPlacement } from '@floating-ui/vue';

import PdfPicker from './components/PdfPicker.vue'

const selectedText = ref(null)
const showFloatingMenu = ref(false)
const floatingMenuReference = ref(null);
const floatingMenu = ref(null);
const {floatingStyles} = useFloating(floatingMenuReference, floatingMenu, { middleware: [autoPlacement()] });

function text_selected(text, point) {
  selectedText.value = text
  showFloatingMenu.value = true
  floatingMenuReference.value = {
    getBoundingClientRect() {
      const { clientX, clientY } = point
      return {
        width: 0,
        height: 0,
        x: clientX,
        y: clientY,
        top: clientY,
        left: clientX,
        right: clientX,
        bottom: clientY,
      }
    }
  }
}

var wording = ref('')
var directives = ref('')
</script>

<template>
  <div class="container-fluid">
    <h1>Gabby</h1>
    <div class="row">
      <div class="col">
        <h2>PDF</h2>
        <PdfPicker src="/test.pdf" :page="1" @text-selected="text_selected" />
        <div v-if="showFloatingMenu" ref="floatingMenu" :style="{...floatingStyles, zIndex: 1000, padding: '5px', border: '1px solid black', background: 'white'}">
          <p>Selection:</p>
          <pre>{{ selectedText }}</pre>
          <p>Add to:</p>
          <div class="row">
            <div class="col">
              <p><button @click="wording += selectedText; showFloatingMenu = false">Wording</button></p>
            </div>
            <div class="col">
              <p><button @click="directives += selectedText; showFloatingMenu = false">Directives</button></p>
              </div>
          </div>
        </div>
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
