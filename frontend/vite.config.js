import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'


export default defineConfig({
  plugins: [
    vue({
      template: {
        compilerOptions: {
          // Fix this problem: https://github.com/vuejs/core/pull/1600#issuecomment-721717095
          whitespace: 'preserve',
        },
      },
    }),
  ],
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
  esbuild: {
    supported: {
      'top-level-await': true //browsers can handle top-level-await features
    },
  },
  // End of section
})
