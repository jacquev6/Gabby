<script setup lang="ts">
import { ref, reactive } from 'vue'

import ProjectFieldsForm from '$frontend/components/ProjectFieldsForm.vue'
import { BButton, BBusy } from '$frontend/components/opinion/bootstrap'
import type { Project, InCache, Exists } from '$frontend/stores/api'
import type { Model } from '$frontend/components/ProjectFieldsForm.vue'
import { makeModel, assignModelFrom } from '$frontend/components/ProjectFieldsForm.vue'


const props = defineProps<{
  project: Project & InCache & Exists,
}>()

const fields = ref<InstanceType<typeof ProjectFieldsForm> | null>(null)

  
const editing = ref(false)
const model: Model = reactive(makeModel())

function start() {
  editing.value = true
  assignModelFrom(model, props.project)
}

function cancel() {
  editing.value = false
}

const busy = ref(false)
async function save() {
  busy.value = true
  await props.project.patch({title: model.title, description: model.description}, {})
  busy.value = false
  editing.value = false
}
</script>

<template>
  <template v-if="editing">
    <h1>{{ $t('project') }}</h1>
    <BBusy :busy>
      <ProjectFieldsForm ref="fields" v-model="model" />
      <BButton secondary @click="cancel">{{ $t('cancel') }}</BButton>
      <BButton primary @click="save" :disabled="fields === null || fields.saveDisabled">{{ $t('saveProject') }}</BButton>
    </BBusy>
  </template>
  <template v-else>
    <h1>{{ $t('projectHeader', {title: project.attributes?.title}) }} <BButton sm secondary @click="start">{{ $t('edit') }}</BButton></h1>
    <p>{{ project.attributes?.description }}</p>
  </template>
</template>
