<script setup>
import { ref } from 'vue'
import { computedAsync } from '@vueuse/core'

import { useApiStore } from '../../stores/api'


const api = useApiStore()

const created = ref(0)

const loading = ref(false)
const pings = computedAsync(
  async () => {
    created.value  // Dependency for reactivity
    return await api.client.get_all('pings')
  },
  [],
  loading,
)

async function createPing() {
  await api.client.post('ping', {}, {'next': []})
  ++created.value
}
</script>

<template>
  <p v-if="loading">Loading...</p>
  <ul v-else-if="pings.length">
    <li v-for="ping in pings" :key="ping.id">
      {{ ping.id }} - {{ ping.attributes.createdAt }}
    </li>
  </ul>
  <p v-else>No pings.</p>
  <p><button @click="createPing">Ping</button></p>
</template>
