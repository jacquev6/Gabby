<script setup>
import { ref } from 'vue'
import { useFloating, shift, flip, offset } from '@floating-ui/vue'
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle.min.js'

import PdfPicker from './components/PdfPicker.vue'

const selectedText = ref(null)
const floatingModal = ref(null)
const floatingModalDialog = ref(null)
const floatingModalReference = ref(null)
const {floatingStyles: floatingModalDialogStyle} = useFloating(floatingModalReference, floatingModalDialog, { placement: 'top', middleware: [offset(-40), flip(), shift()] })

function text_selected(text, point) {
  selectedText.value = text
  bootstrap.Modal.getOrCreateInstance(floatingModal.value).show()

  floatingModalReference.value = {
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
        <div ref="floatingModal" class="modal">
          <div ref="floatingModalDialog" class="modal-dialog modal-xl" :style="{...floatingModalDialogStyle, margin: 0}">
            <div class="modal-content">
              <div class="modal-header">
                <h3 class="modal-title">Selected text</h3>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <pre>{{ selectedText }}</pre>
                <p>Add to:</p>
                <div class="row">
                  <div class="col">
                    <p><button class="btn btn-primary" @click="wording += selectedText" data-bs-dismiss="modal">Wording</button></p>
                  </div>
                  <div class="col">
                    <p><button class="btn btn-primary" @click="directives += selectedText" data-bs-dismiss="modal">Directives</button></p>
                    </div>
                </div>
              </div>
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
