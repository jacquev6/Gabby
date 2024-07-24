<script setup lang="ts">
import { ref, watch, computed } from 'vue'
import { watchPausable } from '@vueuse/core'
import { useI18n } from 'vue-i18n'

import { BButton, BLabeledInput, BLabeledSelect } from '$/frontend/components/opinion/bootstrap'
import { textualFieldNames } from '$/frontend/components/ExerciseFieldsForm.vue'
import type { Model, TextualFieldName, Selection } from '$/frontend/components/ExerciseFieldsForm.vue'


const props = defineProps<{
  lastSelection: Selection | null
}>()

const model = defineModel<Model>({required: true})

const i18n = useI18n()

const escapes = [
  {
    name: 'lineEnd',
    escape: '{line-end}',
    replacement: '\n',
  },
  {
    name: 'paragraphEnd',
    escape: '{paragraph-end}',
    replacement: '\n\n',
  },
]

const search = ref('')
const searchHasBeenModified = ref(false)
const { pause: pauseSearchWatch, resume: resumeSearchWatch } = watchPausable(
  search,
  (s) => (searchHasBeenModified.value = s !== ''),
  {flush: 'sync'},
)
const replace = ref('')
const where = ref<TextualFieldName | 'everywhere'>('everywhere')
watch(
  () => props.lastSelection,
  (lastSelection) => {
    if (lastSelection !== null && lastSelection.text !== '' && !searchHasBeenModified.value) {
      pauseSearchWatch()
      where.value = lastSelection.fieldName
      search.value = lastSelection.text
      resumeSearchWatch()
    }
  },
)

function unescape(ss: string) {
  let s = ss
  for (const {escape, replacement} of escapes) {
    s = s.replaceAll(escape, replacement)
  }
  return s
}

const searchValue = computed(() => unescape(search.value))
const replaceValue = computed(() => unescape(replace.value))

const whereOptions = computed(() => {
  return ['everywhere', ...textualFieldNames].map((option) => ({value: option, label: i18n.t(`replaceIn.${option}`)}))
})

function applyReplace() {
  const fieldNames = where.value === 'everywhere' ? textualFieldNames : [where.value]
  for (const fieldName of fieldNames) {
    model.value[fieldName] = model.value[fieldName].replaceAll(searchValue.value, replaceValue.value)
  }
  search.value = ''
  searchHasBeenModified.value = false
  replace.value = ''
}</script>

<template>
  <BLabeledInput :label="$t('replace')" v-model="search" list="escapes"/>
  <BLabeledInput :label="$t('replaceWith')" v-model="replace" list="escapes"/>
  <datalist id="escapes">
    <option v-for="{name, escape} in escapes" :value="escape">{{ escape }} ({{ $t(name) }})</option>
  </datalist>
  <BLabeledSelect :label="$t('replaceWhere')" v-model="where" :options="whereOptions"/>
  <p><BButton primary data-cy="apply-replace" @click="applyReplace" :disabled="searchValue === ''">{{ $t('apply') }}</BButton></p>
</template>
