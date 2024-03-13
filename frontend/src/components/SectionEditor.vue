<script setup>
import { ref, computed } from 'vue'

import { BLabeledInput, BButton, BRow, BCol, BModal } from './opinion/bootstrap'
import Loading from './Loading.vue'
import { useApiStore } from '../stores/api'


const sectionId = ref(null)

const labelId = `modal-${ Math.floor(Math.random() * 4000000000) }`

const api = useApiStore()

const pdfFileFirstPage = ref(null)
const pdfFileLastPage = ref(null)
const textbookFirstPage = ref(null)
const textbookLastPage = computed(() => textbookFirstPage.value + pdfFileLastPage.value - pdfFileFirstPage.value)

const disabled = computed(() => {
  function isValid(n) {
    return Number.isInteger(n.value) && n.value >= 1
  }
  return (
    !isValid(pdfFileFirstPage)
    || !isValid(pdfFileLastPage)
    || !isValid(textbookFirstPage)
    || !isValid(textbookLastPage)
    || pdfFileFirstPage.value > pdfFileLastPage.value
  )
})

const modal = ref(null)
const saving = ref(false)
async function save() {
  try {
    saving.value = true
    await api.client.patch(
      'section',
      sectionId.value,
      {
        pdfFileStartPage: pdfFileFirstPage.value,
        textbookStartPage: textbookFirstPage.value,
        pagesCount: pdfFileLastPage.value - pdfFileFirstPage.value + 1,
      },
      {},
    )
  } finally {
    saving.value = false
  }
}

function show(id) {
  sectionId.value = id
  const section = api.cache.getOne('section', id)
  pdfFileFirstPage.value = section.attributes.pdfFileStartPage
  pdfFileLastPage.value = section.attributes.pdfFileStartPage + section.attributes.pagesCount - 1
  textbookFirstPage.value = section.attributes.textbookStartPage
  modal.value.show()
}

function hide() {
  modal.value.hide()
}

const active = computed(() => modal.value.active)

defineExpose({
  show,
  active,
})
</script>

<template>
  <b-modal ref="modal" :aria-labelledby="labelId">
    <template #header>
      <h1 class="modal-title" :id="labelId">Lien entre PDF et manuel</h1>
    </template>
    <template #body>
      <loading :loading="saving">
        <b-row>
          <b-col>
            <b-labeled-input label="Début dans le PDF" v-model="pdfFileFirstPage" type="number" min="1" />
          </b-col>
          <b-col>
            <b-labeled-input label="Fin dans le PDF" v-model="pdfFileLastPage" type="number" min="1" />
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <b-labeled-input label="Début dans le manuel" v-model="textbookFirstPage" type="number" min="1" />
          </b-col>
          <b-col>
            <b-labeled-input label="Fin dans le manuel" v-model="textbookLastPage" type="number" min="1" disabled />
          </b-col>
        </b-row>
        <hr>
        <p>
          Les pages {{ pdfFileFirstPage }} à {{ pdfFileLastPage }} du PDF
          correspondent aux pages {{ textbookFirstPage }} à {{ textbookLastPage }} du manuel.
        </p>
      </loading>
    </template>
    <template #footer>
      <loading :loading="saving">
        <b-button secondary @click="hide" :disabled="!active">Annuler</b-button>
        <b-button primary @click="save().then(hide)" :disabled="!active || disabled">Enregistrer</b-button>
      </loading>
    </template>
  </b-modal>
</template>
