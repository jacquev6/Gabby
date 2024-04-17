<script setup>
import { BButton } from '../../components/opinion/bootstrap'
import ProjectForm from '../../components/project-form.vue'
</script>

<template>
  <project-form v-slot="{ disabled, create }">
    <b-button primary :disabled @click="create">{{ $t('createProject' )}}</b-button>
  </project-form>
</template>
