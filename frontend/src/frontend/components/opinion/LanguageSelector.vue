<script setup>
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'

import { BSelect } from './bootstrap'


const i18n = useI18n()

const options = computed(() => i18n.availableLocales.map(locale => ({
  value: locale,
  label: i18n.t('opinion.languageLabel', null, {locale})  // https://github.com/kazupon/vue-i18n/issues/491#issuecomment-984864601
})))
</script>

<template>
  <BSelect v-model="$i18n.locale" :options="options" />
</template>
