import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  // This section works around the following error when importing pdfjs-dist@4:
  //     "Top-level await is not available in the configured target environment"
  // It's a mix of these solutions:
  // - https://stackoverflow.com/a/77859823/905845
  // - https://stackoverflow.com/a/77643886/905845
  optimizeDeps: {
    esbuildOptions: {
      target: 'esnext'
    }
  },
  build: {
    target: 45
  },
  esbuild: {
    supported: {
      'top-level-await': true //browsers can handle top-level-await features
    },
  },
  // End of section
})
