<script setup lang="ts">
defineProps<{
  pageletsCount: number,
}>()

const model = defineModel<number>({required: true})
</script>

<!-- Arrow characters copy-pasted from https://fsymbols.com/signs/arrow/ -->
<template>
  <div class="root">
    <div class="control" :class="{disabled: model === 0}" @click="model = Math.max(0, model - 1)"><div class="arrow arrowLeft"><div>🡸</div></div></div>
    <div style="overflow-x: hidden;"><slot></slot></div>
    <div class="control" :class="{disabled: model === pageletsCount - 1}" @click="model = Math.min(pageletsCount - 1, model + 1)"><div class="arrow arrowRight"><div :style="model === 0 ? {} : {}">🡺</div></div></div>
  </div>
</template>


<style scoped>
.root {
  --control-width: 35px;
  display: grid;
  grid-template-columns: var(--control-width) 1fr var(--control-width);
  height: 100%;
}

div.control {
  height: 100%;
  background: grey;
  font-size: calc(.9 * var(--control-width));
  line-height: 0;
  font-family: Arial,sans-serif;
  font-weight: 400;
  cursor: pointer;
  user-select: none;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

div.arrow {
  height: calc(2 * var(--control-width));
  width: 100%;
  background: lightgray;
  display: flex;
  flex-direction: column;
  justify-content: center;
  color: black;
}

div.arrowLeft {
  border-top-right-radius: var(--control-width);
  border-bottom-right-radius: var(--control-width);
}

div.arrowLeft >div {
  padding-left: calc(0.1 * var(--control-width));
  text-align: left;
}

div.arrowRight {
  border-top-left-radius: var(--control-width);
  border-bottom-left-radius: var(--control-width);
}

div.arrowRight >div {
  padding-right: calc(0.1 * var(--control-width));
  text-align: right;
}

div.control.disabled {
  cursor: not-allowed;
}

div.control.disabled div.arrow {
  color: grey;
}
</style>
