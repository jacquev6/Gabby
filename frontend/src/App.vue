<script setup>
import { ref, reactive, watch } from 'vue'

import PdfPicker from './components/PdfPicker.vue'
import FloatingModal from './components/FloatingModal.vue'

const pdf = ref('/test.pdf')
const pdfName = ref(null)
const pageNumber = ref(1)
const pagesCount = ref(null)

function pdfLoaded(name, numPages) {
  pdfName.value = name
  pagesCount.value = numPages
  pageNumber.value = 1
}

watch(pageNumber, () => {
  if (pageNumber.value < 1) {
    pageNumber.value = 1
  } else if (pageNumber.value > pagesCount.value) {
    pageNumber.value = pagesCount.value
  }
})

const selectedText = ref(null)
const showTextSelectionMenu = ref(false)
const textSelectionMenuReference = ref({x: 0, y: 0})

function textSelected(text, point) {
  selectedText.value = text
  showTextSelectionMenu.value = true
  textSelectionMenuReference.value = {x: point.clientX, y: point.clientY}
}

const sections = reactive({
  // French vocabulary used here to avoid a translation roundtrip from the specs in French
  consignes: '',
  exemple: '',
  indice: '',
  énoncé: '',
})

const wording = ref('')
const directives = ref('')
</script>

<template>
  <PdfPicker style="float: left" :pdf="pdf" :page="pageNumber" @text-selected="textSelected" @pdf-loaded="pdfLoaded" />

  <FloatingModal
    v-if="showTextSelectionMenu"
    :title="$t('headers.selectedText')"
    :reference="textSelectionMenuReference"
    @dismissed="showTextSelectionMenu=false"
  >
    <pre>{{ selectedText }}</pre>
    <hr/>
    <p>{{ $t('headers.addTo') }}</p>
    <template v-for="(_, section, index) in sections">
      <template v-if="index !== 0">&nbsp;</template>
      <button class="btn btn-primary" @click="sections[section] += selectedText; showTextSelectionMenu=false">{{ $t('headers.' + section) }}</button>
    </template>
  </FloatingModal>

  <div class="container-fluid">
    <div class="row">
      <div class="col">
        <h1>Gabby</h1>
        <select v-model="$i18n.locale">
          <option v-for="locale in $i18n.availableLocales" :key="locale" :value="locale">{{ {'en': '🇺🇸', 'fr': '🇫🇷'}[locale] }}</option>
        </select>
        <p>Page <input type="number" v-model="pageNumber" /> of {{ pagesCount }} in {{ pdfName }}</p>
        <p><input type="file" @change="(e) => { pdf = e.target.files[0] }" /></p>
        <h2>{{ $t('headers.form') }}</h2>
        <template v-for="(content, section) in sections">
          <h3>{{ $t('headers.' + section) }}</h3>
          <pre>{{ content }}</pre>
        </template>
      </div>
    </div>
  </div>
</template>
