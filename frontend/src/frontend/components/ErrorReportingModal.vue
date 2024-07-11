<script setup lang="ts">
import { ref, watch } from 'vue'
import { useWindowSize } from '@vueuse/core'

import { BModal } from './opinion/bootstrap'
import { app } from '../main'


const gabbyVersion = import.meta.env.VITE_OPINION_APP_VERSION
const userAgent = JSON.stringify((window.navigator as any/* Chromium-specific */).userAgentData || window.navigator.userAgent)
const { width: windowWidth, height: windowHeight } = useWindowSize()
const url = () => window.location.href

type GlobalError = {
  caughtBy: string
  message: string | null
  codeLocation: string | null
}
const globalError = ref<GlobalError | null>(null)

function shortenStack(stack: string | undefined) {
  if (stack === undefined) {
    return null
  } else {
    return stack.split('\n').slice(0, 5).join('\n')
  }
}

// Don't try and patch console.log to get the stack: it's not worth it because
// the second item in the stack is already in the Vue.js framework
// Leave assertions as-is and catch the actual error they are supposed to prevent.

// Never seen an error reach this handler, but it doesn't hurt, and it may catch something one day
window.onerror = (message, source, lineno, colno, _error) => {
  globalError.value ||= {
    caughtBy: 'window.onerror',
    message: `${message}`,
    codeLocation: `${source}:${lineno}:${colno}`,
  }
  return false
}

// Catches promise rejections from the body of (non-async) setup scripts
window.onunhandledrejection = (event) => {
  globalError.value ||= {
    caughtBy: 'window.onunhandledrejection',
    message: `${event.reason}`,
    codeLocation: null,
  }
  return false
}

// Sees everything Vue.js catches
app.config.errorHandler = function (err, _vm, info) {
  globalError.value ||= {
    caughtBy: 'Vue.config.errorHandler',
    message: `${err}\n${info}`,
    codeLocation: err instanceof Error ? shortenStack(err.stack) : null,
  }
}

const modal = ref<InstanceType<typeof BModal> | null>(null)

watch([modal, globalError], ([m, e]) => {
  if (m && e) {
    m.show()
  }
})
</script>

<template>
  <BModal ref="modal" :close="false" backdrop="static" :keyboard="false">
    <template v-slot:header><h1>{{ $t('thereWasABug') }}</h1></template>
    <template v-slot:body>
      <p>{{ $t('thisIsNotYourFault') }}</p>
      <pre style="border: 1px solid black">
Date: {{ new Date().toISOString() }}
Gabby version: {{ gabbyVersion }}
Locale: {{ $i18n.locale }}
User agent: {{ userAgent }}
Window size: {{ windowWidth }}x{{ windowHeight }}
URL: {{ url() }}

Caught by: {{ globalError?.caughtBy }}
{{ globalError?.message ? 'Message: ' + globalError.message : 'No message' }}
{{ globalError?.codeLocation ? 'Code location: ' + globalError.codeLocation : 'No code location' }}
End of details</pre>
    </template>
  </BModal>
</template>
