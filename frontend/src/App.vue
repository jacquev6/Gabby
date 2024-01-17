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
    <select v-model="$i18n.locale">
      <option v-for="locale in $i18n.availableLocales" :key="locale" :value="locale">{{ {'en': '🇺🇸', 'fr': '🇫🇷'}[locale] }}</option>
    </select>
    <div class="row">
      <div class="col">
        <h2>PDF</h2>
        <PdfPicker @text-selected="text_selected" />
        <FloatingModal
          v-if="showTextSelectionMenu"
          :title="$t('headers.selectedText')"
          :reference="textSelectionMenuReference"
          @dismissed="showTextSelectionMenu=false"
        >
          <pre>{{ selectedText }}</pre>
          <p>{{ $t('headers.addTo') }}</p>
          <div class="row">
            <div class="col">
              <p><button class="btn btn-primary" @click="wording += selectedText; showTextSelectionMenu=false">{{ $t('headers.wording') }}</button></p>
            </div>
            <div class="col">
              <p><button class="btn btn-primary" @click="directives += selectedText; showTextSelectionMenu=false">{{ $t('headers.directives') }}</button></p>
              </div>
          </div>
        </FloatingModal>
      </div>
      <div class="col">
        <h2>{{ $t('headers.form') }}</h2>
        <h3>{{ $t('headers.wording') }}</h3>
        <pre>{{ wording }}</pre>
        <h3>{{ $t('headers.directives') }}</h3>
        <pre>{{ directives }}</pre>
      </div>
    </div>
  </div>
</template>
