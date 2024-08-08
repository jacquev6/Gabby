<script setup lang="ts">
import { ref, computed, type Ref } from 'vue'

import { BBusy, BLabeledInput, BButton, BRow, BCol, BModal } from '$frontend/components/opinion/bootstrap'
import { useApiStore } from '$frontend/stores/api'


const sectionId = ref<string | null>(null)

const labelId = `modal-${ Math.floor(Math.random() * 4000000000) }`

const api = useApiStore()

const pdfFileFirstPage = ref(0)
const pdfFileLastPage = ref(0)
const textbookFirstPage = ref(0)
const textbookLastPage = computed(() => textbookFirstPage.value + pdfFileLastPage.value - pdfFileFirstPage.value)

const disabled = computed(() => {
  function isValid(n: Ref<number>) {
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

const modal = ref<InstanceType<typeof BModal> | null>(null)
const saving = ref(false)
async function save() {
  console.assert(sectionId.value !== null)

  try {
    saving.value = true
    await api.cache.getOne('section', sectionId.value).patch(
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

function show(id: string) {
  console.assert(modal.value !== null)

  sectionId.value = id
  const section = api.cache.getOne('section', id)
  console.assert(section.inCache && section.exists)

  pdfFileFirstPage.value = section.attributes.pdfFileStartPage
  pdfFileLastPage.value = section.attributes.pdfFileStartPage + section.attributes.pagesCount - 1
  textbookFirstPage.value = section.attributes.textbookStartPage
  modal.value.show()
}

function hide() {
  console.assert(modal.value !== null)

  modal.value.hide()
}

const active = computed(() => modal.value?.active)

defineExpose({
  show,
  active,
})
</script>

<template>
  <BModal ref="modal" :aria-labelledby="labelId">
    <template #header>
      <h1 class="modal-title" :id="labelId">Lien entre PDF et manuel</h1>
    </template>
    <template #body>
      <BBusy :busy="saving">
        <BRow>
          <BCol>
            <BLabeledInput label="Début dans le PDF" v-model="pdfFileFirstPage" type="number" min="1" />
          </BCol>
          <BCol>
            <BLabeledInput label="Fin dans le PDF" v-model="pdfFileLastPage" type="number" min="1" />
          </BCol>
        </BRow>
        <BRow>
          <BCol>
            <BLabeledInput label="Début dans le manuel" v-model="textbookFirstPage" type="number" min="1" />
          </BCol>
          <BCol>
            <BLabeledInput label="Fin dans le manuel" v-model="textbookLastPage" type="number" min="1" disabled />
          </BCol>
        </BRow>
        <hr>
        <p>
          Les pages {{ pdfFileFirstPage }} à {{ pdfFileLastPage }} du PDF
          correspondent aux pages {{ textbookFirstPage }} à {{ textbookLastPage }} du manuel.
        </p>
      </BBusy>
    </template>
    <template #footer>
      <BBusy :busy="saving">
        <BButton secondary @click="hide" :disabled="!active">Annuler</BButton>
        <BButton primary @click="save().then(hide)" :disabled="!active || disabled">Enregistrer</BButton>
      </BBusy>
    </template>
  </BModal>
</template>
