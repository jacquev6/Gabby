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
    // @todo Use https://www.npmjs.com/package/vite-plugin-singlefile to create a single distributable file
  ],
})
