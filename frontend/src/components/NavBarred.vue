<script setup>
import NavBar from './NavBar.vue'
</script>

<template>
  <div class="container-fluid">
    <nav-bar><slot name="navbar"></slot></nav-bar>
    <slot></slot>
  </div>
</template>
