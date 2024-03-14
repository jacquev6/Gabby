<script setup>
import { usePdfsStore } from '../stores/pdfs'


const pdfs = usePdfsStore()
</script>

<template>
  <h1>PDFs</h1>
  <ul>
    <li v-for="pdf in pdfs.known">
      {{ pdf.sha256.slice(0, 16) }} ({{ pdf.name }}) <button @click="pdfs.close(pdf.sha256)">Close</button>
    </li>
  </ul>
</template>
