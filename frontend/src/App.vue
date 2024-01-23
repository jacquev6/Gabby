<script setup>
import { ref, watch } from 'vue'

import AboutModal from './components/AboutModal.vue'
import FloatingModal from './components/FloatingModal.vue'
import PdfPicker from './components/PdfPicker.vue'


const pdfMaxWidth = ref(null)
const pdfMaxHeight = ref(null)
function onResize() {
  pdfMaxWidth.value = window.innerWidth * 0.4
  pdfMaxHeight.value = window.innerHeight
}
onResize()
window.addEventListener('resize', onResize);

const pdf = ref('/test.pdf')
const pdfName = ref(null)
const pdfSha1 = ref(null)
const pdfPageNumber = ref(null)
const pdfPagesCount = ref(null)

function pdfDisplayed(name, sha1, pagesCount, page) {
  pdfName.value = name
  pdfSha1.value = sha1
  pdfPagesCount.value = pagesCount
  pdfPageNumber.value = page
}

// The PdfPicker doesn't rely on this clamping logic:
// this is just to avoid a flash when the user selects an out-of-range page number.
watch(pdfPageNumber, () => {
  if (pdfPageNumber.value < 1) {
    pdfPageNumber.value = 1
  } else if (pdfPageNumber.value > pdfPagesCount.value) {
    pdfPageNumber.value = pdfPagesCount.value
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

const exerciseNumber = ref('')
// @todo Use a single 'reactive' object instead of several 'ref's
const sections = {
  instructions: ref(''),
  example: ref(''),
  clue: ref(''),
  wording: ref(''),
}



async function save() {
  fetch('/api/exercises', {
    method: 'POST',
    headers: {
      'content-type': 'application/vnd.api+json',
    },
    body: JSON.stringify({
      data: {
        type: 'exercise',
        id: null,
        attributes: {
          pdfSha1: pdfSha1.value,
          pdfPage: pdfPageNumber.value,
          number: exerciseNumber.value,
          ...Object.fromEntries(Object.entries(sections).map(([k, v]) => [k, v.value]))
        },
      },
    }),
  })
}
</script>

<template>
  <PdfPicker style="float: left" :pdf="pdf" :page="pdfPageNumber" :maxWidth="pdfMaxWidth" :maxHeight="pdfMaxHeight" @displayed="pdfDisplayed" @text-selected="textSelected" />

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
        <div class="d-flex">
          <button class="btn form-control btn-secondary" data-bs-toggle="modal" data-bs-target="#aboutModal">{{ $t('about') }}</button>
          <select class="form-control" v-model="$i18n.locale">
            <option v-for="locale in $i18n.availableLocales" :key="locale" :value="locale">{{ {'en': '🇺🇸 English (US)', 'fr': '🇫🇷 Français'}[locale] }}</option>
          </select>
        </div>
      </div>
    </div>
  </nav>

  <div class="container-fluid">
    <div class="row">
      <div class="col">
        <h2>{{ $t('exercise') }}</h2>
        <form>
          <div class="mb-3">
            <label class="form-label">{{ $t('inputFile') }}</label>
            <input class="form-control" type="file" @change="(e) => { pdf = e.target.files[0] }" />
            <p>(SHA-1: {{ pdfSha1 }})</p>
          </div>

          <div class="mb-3">
            <label class="form-label">{{ $t('pageOver', {count : pdfPagesCount}) }}</label>
            <input class="form-control" type="number" v-model="pdfPageNumber" />
          </div>

          <div class="mb-3">
            <label class="form-label">{{ $t('exerciseNumber') }}</label>
            <input class="form-control" type="text" v-model="exerciseNumber" />
          </div>
        </form>

        <h2>{{ $t('edition') }}</h2>
        <form>
          <div v-for="(content, section) in sections" class="mb-3">
            <label class="form-label">{{ $t(section) }}</label>
            <textarea class="form-control" rows="3" v-model="sections[section].value"></textarea>
          </div>

          <div class="mb-3">
            <button class="btn btn-primary" type="text" @click.prevent="save">{{ $t('save') }}</button>
          </div>
        </form>
      </div>
      <div class="col">
        <h2>{{ $t('visualization') }}</h2>
        <p>({{ $t('not-yet-implemented') }})</p>
        <p v-for="(content) in sections" class="mb-3">{{ content.value }}</p>
      </div>
    </div>
  </div>

  <AboutModal id="aboutModal" />
</template>
