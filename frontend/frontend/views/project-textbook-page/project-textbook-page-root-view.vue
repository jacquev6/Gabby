<script setup>
import { ref } from 'vue'
import { computedAsync } from '@vueuse/core'

import { useApiStore } from '../../stores/api'
import { BBusy } from '../../components/opinion/bootstrap'


const props = defineProps({
  projectId: {type: String, required: true},
  textbookId: {type: String, required: true},
  page: {type: Number, required: true},
})

const api = useApiStore()

const projectLoading = ref(false)
const project = computedAsync(
  async () => {
    return await api.client.getOne('project', props.projectId)
  },
  null,
  projectLoading,
)

const textbookLoading = ref(false)
const textbook = computedAsync(
  async () => {
    const textbook = await api.client.getOne('textbook', props.textbookId, {include: 'sections.pdfFile.namings'})
    if (textbook.relationships.project.id === props.projectId) {
      return textbook
    } else {
      return null
    }
  },
  null,
  textbookLoading,
)
</script>

<template>
  <b-busy size="11rem" :busy="projectLoading || textbookLoading">
    <template v-if="!project?.exists">
      <h1>{{ $t('projectNotFound') }}</h1>
    </template>
    <template v-else-if="!textbook?.exists">
      <h1>{{ $t('textbookNotFound') }}</h1>
    </template>
    <template v-else>
      <router-view name="main" :project :textbook :page></router-view>
    </template>
  </b-busy>
</template>
