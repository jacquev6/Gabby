<script setup>
import { ref, reactive } from 'vue'

import PdfPicker from './components/PdfPicker.vue'

const selectedText = ref(null)
const menuStyle = reactive({
  'position': 'absolute',
  'left': '0px',
  'top': '0px',
  'background-color': 'white',
  'z-index': '1000',
  'display': 'none',
  'border': '1px solid black',
  'padding': '5px',
})

function text_selected(text, point) {
  selectedText.value = text
  menuStyle.left = point.clientX + 'px'
  menuStyle.top = point.clientY + 'px'
  menuStyle.display = 'block'
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
        <div :style="menuStyle">
          <p>Selection:</p>
          <pre>{{ selectedText }}</pre>
          <p>Add to:</p>
          <div class="row">
            <div class="col">
              <p><button @click="wording += selectedText; menuStyle.display='none'">Wording</button></p>
            </div>
            <div class="col">
              <p><button @click="directives += selectedText; menuStyle.display='none'">Directives</button></p>
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
