<script setup lang="ts">
import { BButton } from '$frontend/components/opinion/bootstrap'
import ProjectForm from '$frontend/components/ProjectForm.vue'
</script>

<template>
  <ProjectForm v-slot="{ disabled, create }">
    <BButton primary :disabled @click="create" data-cy="create-project">{{ $t('createProject' )}}</BButton>
  </ProjectForm>
</template>
