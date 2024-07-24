<script setup lang="ts">
import { ref } from 'vue'

import { BBusy, BLabeledInput } from '$frontend/components/opinion/bootstrap'
import { usePdfsStore } from '$frontend/stores/pdfs'


defineProps<{
  name: string
}>()

const pdfs = usePdfsStore()

const busy = ref(false)
async function loadPdf(source: File) {
  busy.value = true
  await pdfs.open(source)
  busy.value = false
}
</script>

<template>
  <!-- @todo Display all names known for this PDF -->
  <p>{{ $t('pdfNotLoaded', {name}) }}</p>
  <BBusy :busy>
    <BLabeledInput :label="$t('inputFile')" type="file" accept=".pdf" @change="(e: any/* @todo Type */) => loadPdf(e.target.files[0])" />
  </BBusy>
</template>
