<script setup lang="ts">
import { useI18n } from 'vue-i18n'

const model = defineModel<number | null>({required: true})

const i18n = useI18n()

const possibleValues = [1, 2, 3, 4, 5]

function toggle(v: number) {
  if (model.value === v) {
    model.value = null
  } else {
    model.value = v
  }
}
</script>

<template>
  <p>
    <span v-for="value in possibleValues" class="value" :class="{selected: model === value}" :title="i18n.t('exerciseLinesPerPage', value)" @click="toggle(value)">{{ value }}</span>
  </p>
</template>

<style scoped>
p {
  user-select: none;
}

span.value {
  display: inline flow-root;
  margin: 0.25em;
  padding: 0;
  border: 1px solid black;
  width: 1.5em;
  height: 1.5em;
  text-align: center;
  cursor: pointer;
}

span.value.selected {
  background-color: var(--bs-primary);
  color: white;
}
</style>
