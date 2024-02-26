<script setup>
import { computed } from 'vue'
import { computedAsync } from '@vueuse/core'
import { useApiStore } from '@/stores/api'
import { usePdfsStore } from '@/stores/pdfs'


const props = defineProps({
  textbookId: {
    type: String,
    required: true,
  },
  page: {
    type: Number,
    required: true,
  },
})

const api = useApiStore()
const pdfs = usePdfsStore()

const textbook = computed(() => {
  return api.cache.get('textbook', props.textbookId)
})

const section = computed(() => {
  for (const section of textbook.value?.relationships.sections || []) {
    if (props.page >= section.attributes.textbookStartPage && props.page < section.attributes.textbookStartPage + section.attributes.pagesCount) {
      return section
    }
  }
  return null
})

const pdfPage = computed(() => {
  if (section.value) {
    return section.value.attributes.pdfFileStartPage + props.page - section.value.attributes.textbookStartPage
  } else {
    return null
  }
})

const pdfDocument = computedAsync(async () => {
  if (section.value) {
    return (await pdfs.get(section.value.relationships.pdfFile.id)).document
  } else {
    return null
  }
})

if (api.cache.get('textbook', props.textbookId) === null) {
  // @todo(Project management, soon) Load only one textbook
  api.client.get(`textbooks`, {include: 'sections.pdfFile'})
}
</script>

<template>
  <p><button @click="pdfs.load('/test.pdf')">Load test.pdf</button></p>
  <p>textbookId: {{ textbookId }}, page: {{ page }}</p>
  <p>textbook?.attributes: {{ textbook?.attributes }}</p>
  <p>section: {{ section !== null }}</p>
  <p>pdfPage: {{ pdfPage }} / pdf?.document.numPages: {{ pdfDocument?.numPages }}</p>
  <p>
    <router-link :to="{name: 'textbook-page', params: {textbookId, page: page - 1}}">&lt;</router-link>
    <router-link :to="{name: 'textbook-page', params: {textbookId, page: page + 1}}">&gt;</router-link>
  </p>
</template>
