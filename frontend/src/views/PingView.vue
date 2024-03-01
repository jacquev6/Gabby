<script setup>
import { ref } from 'vue'
import { computedAsync } from '@vueuse/core'

import { useApiStore } from '../stores/api'


const api = useApiStore()

const pingsCreated = ref(0)

const pingsLoading = ref(false)
const pings = computedAsync(
  async () => {
    pingsCreated.value  // Dependency for reactivity
    return await api.client.get_all('pings')
  },
  [],
  pingsLoading,
)

function createPing() {
  api.client.post('ping', {}, {})
  ++pingsCreated.value
}
</script>

<template>
  <h1>Pings</h1>
  <p v-if="pingsLoading">Loading...</p>
  <ul v-else-if="pings.length">
    <li v-for="ping in pings" :key="ping.id">
      {{ ping.id }} - {{ ping.attributes.createdAt }}
    </li>
  </ul>
  <p v-else>No pings.</p>
  <p><button @click="createPing">Ping</button></p>
</template>
