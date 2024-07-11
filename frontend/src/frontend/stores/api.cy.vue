<script setup lang="ts">
import Pinger from '$frontend/components/opinion/Pinger.vue'
import { BBusy, BRow, BCol } from '$frontend/components/opinion/bootstrap'
import { useApiStore } from './api'


const api = useApiStore()

const pings = api.auto.getAll('ping')
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
  <b-busy :busy="pings.loading">
    <ul v-if="pings.items.length">
      <li v-for="ping in pings.items" :key="ping.id">
        <template v-if="ping.exists">
          {{ ping.id }} - {{ ping.attributes!.createdAt }}<span v-if="ping.attributes!.message">: {{ ping.attributes!.message }}</span>
          <template v-if="ping.relationships!.prev">Prev: {{ ping.relationships!.prev.id }}</template>
          <template v-if="ping.relationships!.next.length">Next:<template v-for="next in ping.relationships!.next">&nbsp;{{ next.id }}</template></template>
        </template>
        <template v-else>
          {{ ping.id }} - Deleted
        </template>
      </li>
    </ul>
    <p v-else>{{ $t('opinion.noPings') }}</p>
  </b-busy>
</template>
