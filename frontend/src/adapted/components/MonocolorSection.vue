<script setup lang="ts">
import { computed, watch } from 'vue'
import { nextTick } from 'vue'

import type { Paragraph } from '$adapted/types'
import Renderable from './Renderable.vue'


const props = defineProps<{
  paragraphs: Paragraph[]
  centered: boolean
  first: boolean
}>()

const models = defineModel<Record<string, any/* @todo Type */>>({
  required: true,
})

const emit = defineEmits<{
  layoutChanged: []
}>()

watch(models, () => nextTick(() => emit('layoutChanged')), { deep: true })

const style = computed(() => ({
  textAlign: props.centered ? 'center' as const : 'left' as const,
}))
</script>

<template>
  <p v-for="(paragraph, paragraphIndex) in paragraphs" :style :class="{first: first && paragraphIndex === 0}">
    <Renderable v-for="(node, nodeIndex) in paragraph.contents" :node="node" v-model="models" :nested="false" :modelKey="[paragraphIndex, nodeIndex]" />
  </p>
</template>

<style scoped>
p {
  font-size: 32px;
  line-height: 3;
  margin: 0px;
}

p.first {
  margin-top: -19px;
}
</style>
