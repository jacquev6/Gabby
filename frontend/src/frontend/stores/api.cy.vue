<script setup lang="ts">
import { ref } from 'vue'
import { computedAsync } from '@vueuse/core'

import Pinger from '../components/opinion/Pinger.vue'
import { BBusy, BRow, BCol } from '../components/opinion/bootstrap'
import { useApiStore } from './api'
import type { Ping } from '../types/api'


const api = useApiStore()

const loadingPings = ref(false)
const pings = computedAsync(
  async () => {
    return await api.client.getAll<Ping>('pings')
  },
  [] as Required<Ping>[],
  loadingPings,
)
</script>

<template>
  <b-row>
    <b-col>
      <pinger />
    </b-col>
    <b-col>
      <pinger />
    </b-col>
  </b-row>
  <b-busy :busy="loadingPings">
    <ul v-if="pings.length">
      <li v-for="ping in pings" :key="ping.id">
        {{ ping.id }} - {{ ping.attributes.createdAt }}<span v-if="ping.attributes.message">: {{ ping.attributes.message }}</span>
        <template v-if="ping.relationships.prev">Prev: {{ ping.relationships.prev.id }}</template>
        <template v-if="ping.relationships.next.length">Next:<template v-for="next in ping.relationships.next">&nbsp;{{ next.id }}</template></template>
      </li>
    </ul>
    <p v-else>{{ $t('opinion.noPings') }}</p>
  </b-busy>
</template>
