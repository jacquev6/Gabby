<script setup>
import { ref } from 'vue'

import { BBusy, BLabeledInput } from '../../../../components/opinion/bootstrap'
import { usePdfsStore } from '../../../../stores/pdfs'


const props = defineProps({
  name: {type: String, required: true},
})

const pdfs = usePdfsStore()

const busy = ref(false)
async function loadPdf(source) {
  busy.value = true
  await pdfs.open(source)
  busy.value = false
}

</script>

<template>
  <!-- @todo Display all names known for this PDF -->
  <p>{{ $t('pdfNotLoaded', {name}) }}</p>
  <BBusy :busy>
    <BLabeledInput :label="$t('inputFile')" type="file" accept=".pdf" @change="(e) => loadPdf(e.target.files[0])" />
  </BBusy>
</template>
