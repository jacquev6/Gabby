<script setup>
import { ref, watch } from 'vue'

import PdfPicker from './components/PdfPicker.vue'
import FloatingModal from './components/FloatingModal.vue'

const windowHeight = ref(null)
function onResize() {
  windowHeight.value = window.innerHeight
}
onResize()
window.addEventListener('resize', onResize);

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

const sections = {
  // French vocabulary used here to avoid a translation roundtrip from the specs in French
  consignes: ref(''),
  exemple: ref(''),
  indice: ref(''),
  énoncé: ref(''),
}

const wording = ref('')
const directives = ref('')
</script>

<template>
  <PdfPicker style="float: left" :pdf="pdf" :page="pageNumber" :targetHeight="windowHeight" @text-selected="textSelected" @pdf-loaded="pdfLoaded" />

  <FloatingModal
    v-if="showTextSelectionMenu"
    :title="$t('selectedText')"
    :reference="textSelectionMenuReference"
    @dismissed="showTextSelectionMenu=false"
  >
    <pre>{{ selectedText }}</pre>
    <hr/>
    <p>{{ $t('addTo') }}</p>
    <template v-for="(_, section, index) in sections">
      <template v-if="index !== 0">&nbsp;</template>
      <button class="btn btn-primary" @click="sections[section].value += selectedText; showTextSelectionMenu=false">{{ $t(section) }}</button>
    </template>
  </FloatingModal>

  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand"><img src="/favicon.ico" alt="Logo" width="30" height="24" class="d-inline-block align-text-top">Gabby</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0"></ul>
        <form>
          <select class="form-control" v-model="$i18n.locale">
            <option v-for="locale in $i18n.availableLocales" :key="locale" :value="locale">{{ {'en': '🇺🇸 English (US)', 'fr': '🇫🇷 Français'}[locale] }}</option>
          </select>
        </form>
      </div>
    </div>
  </nav>

  <div class="container-fluid">
    <div class="row">
      <div class="col">
        <h2>{{ $t('edition') }}</h2>
        <form>
          <div class="mb-3">
            <label class="form-label">{{ $t('inputFile') }}</label>
            <input class="form-control" type="file" @change="(e) => { pdf = e.target.files[0] }" />
          </div>

          <div class="mb-3">
            <label class="form-label">Page (sur {{ pagesCount }})</label>
            <input class="form-control" type="number" v-model="pageNumber" />
          </div>

          <div v-for="(content, section) in sections" class="mb-3">
            <label class="form-label">{{ $t(section) }}</label>
            <textarea class="form-control" rows="3" v-model="sections[section].value"></textarea>
          </div>
        </form>
      </div>
      <div class="col">
        <h2>{{ $t('visualization') }}</h2>
        <p v-for="(content) in sections" class="mb-3">{{ content.value }}</p>
      </div>
    </div>
  </div>
</template>
