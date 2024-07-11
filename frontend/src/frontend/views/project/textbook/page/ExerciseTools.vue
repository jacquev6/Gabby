<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import { watchPausable, useMagicKeys } from '@vueuse/core'
import { useI18n } from 'vue-i18n'

import { BLabeledInput, BLabeledSelect, BButton } from '$frontend/components/opinion/bootstrap'
import type ExerciseForm from '$/frontend/components/ExerciseForm.vue'


const props = defineProps<{
  exerciseForm: typeof ExerciseForm,
}>()

const i18n = useI18n()

const { Ctrl_Z, Ctrl_Y } = useMagicKeys()
watch(Ctrl_Z, (v) => {
  if (v && props.exerciseForm.canUndo) {
    props.exerciseForm.undo()
  }
})
watch(Ctrl_Y, (v) => {
  if (v && props.exerciseForm.canRedo) {
    props.exerciseForm.redo()
  }
})

const search = ref('')
const searchHasBeenModified = ref(false)
const { pause: pauseSearchWatch, resume: resumeSearchWatch } = watchPausable(
  search,
  (s) => (searchHasBeenModified.value = s !== ''),
  {flush: 'sync'},
)
const replace = ref('')
const where = ref('everywhere')
watch(() => props.exerciseForm.selected, ([fieldName, selected]) => {
  if (selected !== '' && !searchHasBeenModified.value) {
    pauseSearchWatch()
    where.value = fieldName
    search.value = selected
    resumeSearchWatch()
  }
})

const whereOptions = computed(() => {
  return ['everywhere', ...props.exerciseForm.fieldNamesForReplace].map((option) => ({value: option, label: i18n.t(`replaceIn.${option}`)}))
})

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

function unescape(ss: string) {
  let s = ss
  for (const {escape, replacement} of escapes) {
    s = s.replaceAll(escape, replacement)
  }
  return s
}

const searchValue = computed(() => unescape(search.value))
const replaceValue = computed(() => unescape(replace.value))

function applyReplace() {
  const fieldName = where.value === 'everywhere' ? null : where.value
  props.exerciseForm.replace(fieldName, searchValue.value, replaceValue.value)
  search.value = ''
  searchHasBeenModified.value = false
  replace.value = ''
}
</script>

<template>
  <h1>{{ $t('tools') }}</h1>
  <hr/>
  <div @mousedown="e => e.stopPropagation()" @touchstart="e => e.stopPropagation()" style="cursor: initial">
    <BButton primary sm @click="exerciseForm.undo" :disabled="!exerciseForm.canUndo" title="Ctrl+Z">{{ $t('undo') }}</BButton>
    <BButton primary sm @click="exerciseForm.redo" :disabled="!exerciseForm.canRedo" title="Ctrl+Y">{{ $t('redo') }}</BButton>
  </div>
  <hr/>
  <div id="teleportTargetForAdaptationDetails" @mousedown="e => e.stopPropagation()" @touchstart="e => e.stopPropagation()" style="cursor: initial"></div>
  <hr/>
  <div @mousedown="e => e.stopPropagation()" @touchstart="e => e.stopPropagation()" style="cursor: initial">
    <BLabeledInput :label="$t('replace')" v-model="search" list="escapes"/>
    <BLabeledInput :label="$t('replaceWith')" v-model="replace" list="escapes"/>
    <datalist id="escapes">
      <option v-for="{name, escape} in escapes" :value="escape">{{ escape }} ({{ $t(name) }})</option>
    </datalist>
    <BLabeledSelect :label="$t('replaceWhere')" v-model="where" :options="whereOptions"/>
    <p><BButton primary data-cy="apply-replace" @click="applyReplace" :disabled="searchValue === ''">{{ $t('apply') }}</BButton></p>
  </div>
  <hr/>
</template>
