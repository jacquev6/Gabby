<script setup>
import { ref, computed, watch } from 'vue'

import { BBusy, BLabeledInput, BLabeledTextarea } from './opinion/bootstrap'
import { useApiStore } from '../stores/api'


const props = defineProps({
  project: {type: Object, required: false},
})

const emit = defineEmits([
  'created',  // (project: Object) => void
  'saved',  // () => void
])

const api = useApiStore()

const title = ref('')
const description = ref('')

watch(
  () => props.project,
  () => {
    title.value = props.project?.attributes.title ?? ''
    description.value = props.project?.attributes.description ?? ''
  },
  {immediate: true},
)

const disabled = computed(() => !title.value)
const busy = ref(false)

async function create() {
  busy.value = true
  const project = await api.client.post(
    'project',
    {title: title.value, description: description.value},
    {},
  )
  busy.value = false
  title.value = ''
  description.value = ''
  emit('created', project)
}

async function save() {
  busy.value = true
  await api.client.patch(
    'project',
    props.project.id,
    {title: title.value, description: description.value},
    {},
  )
  busy.value = false
  emit('saved')
}
</script>

<template>
  <b-busy :busy>
    <b-labeled-input v-model="title" :label="$t('projectTitle')" />
    <b-labeled-textarea v-model="description" :label="$t('projectDescription')" />
    <slot :disabled :create :save></slot>
  </b-busy>
</template>
