<script setup lang="ts">
import { ref } from 'vue'

import { BBusy, BLabeledInput } from '$frontend/components/opinion/bootstrap'
import { usePdfsStore } from '$frontend/stores/pdfs'


const props = defineProps<{
  name: string
  sha256: string
}>()

const pdfs = usePdfsStore()

const busy = ref(false)
async function loadPdf(source: File) {
  busy.value = true
  const pdf = await pdfs.open(source)
  busy.value = false
  return pdf
}

const wrongSha = ref(false)
const loaded = ref<string | null>(null)
async function change(event: Event) {
  console.assert(event.target !== null)
  const input = event.target as HTMLInputElement
  if (input.files !== null && input.files.length !== 0) {
    loaded.value = input.files[0].name
    const pdf = await loadPdf(input.files[0])
    wrongSha.value = pdf.info.sha256 !== props.sha256
  }
}
</script>

<template>
  <p class="alert alert-warning" v-if="wrongSha">{{ $t('wrongPdfLoaded', {loaded, name}) }}</p>
  <!-- @todo Display all names known for this PDF -->
  <p v-else>{{ $t('pdfNotLoaded', {name}) }}</p>
  <BBusy :busy>
    <BLabeledInput :label="$t('inputFile')" type="file" accept=".pdf" @change="change" />
  </BBusy>
</template>
