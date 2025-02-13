<template>
  <hr />
  <div @mousedown.stop="">
    <slot></slot>
  </div>
</template>

<style scoped>
div {
  cursor: initial;
}
</style>
