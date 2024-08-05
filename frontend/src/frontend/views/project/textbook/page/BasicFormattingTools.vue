<script setup lang="ts">
import { BButton } from '$frontend/components/opinion/bootstrap'
import type ExerciseFieldsForm from '$frontend/components/ExerciseFieldsForm.vue'


defineProps<{
  fields: InstanceType<typeof ExerciseFieldsForm>
}>()
</script>

<template v-if="fields !== null">
  <div>
    <BButton sm primary :disabled="!fields.wysiwygInstructionsHasFocus" @click="fields.toggle('bold')" data-cy="bold">{{ $t('boldButton') }}</BButton>
    <BButton sm primary :disabled="!fields.wysiwygInstructionsHasFocus" @click="fields.toggle('italic')" data-cy="italic">{{ $t('italicButton') }}</BButton>
  </div>
</template>
