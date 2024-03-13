<script setup>
import { ref, computed } from 'vue'

import { BBusy, BLabeledInput, BLabeledTextarea, BButton } from '../../components/opinion/bootstrap'
import { useApiStore } from '../../stores/api'


const emit = defineEmits([
  'created',  // (projectId: string) => void
])

const api = useApiStore()

const title = ref('')
const description = ref('')
const disabled = computed(() => !title.value)
const creating = ref(false)
async function create() {
  creating.value = true
  const project = await api.client.post(
    'project',
    {title: title.value, description: description.value},
    {textbooks: [], exercises: []},
  )
  creating.value = false
  title.value = ''
  description.value = ''
  emit('created', project.id)
}
</script>

<template>
  <b-busy :busy="creating">
    <b-labeled-input v-model="title" :label="$t('projectTitle')" />
    <b-labeled-textarea v-model="description" :label="$t('projectDescription')" />
    <b-button primary @click="create" :disabled="disabled">{{ $t('createProject' )}}</b-button>
  </b-busy>
</template>
