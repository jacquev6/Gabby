import { defineConfig } from 'vite'
import { viteSingleFile } from "vite-plugin-singlefile"
import makeVue from '@vitejs/plugin-vue'


export default defineConfig(({ command, mode, isSsrBuild, isPreview }) => {
  // Use https://vitejs.dev/config/#conditional-config because 'viteSingleFile' overwrites '--base' even in 'serve' mode

  const vue = makeVue({
    template: {
      compilerOptions: {
        // Fix this problem: https://github.com/vuejs/core/pull/1600#issuecomment-721717095
        whitespace: 'preserve',
      },
    },
  })

  if (command === 'serve') {
    return {
      plugins: [vue],
    }
  } else {
    // command === 'build'
    return {
      plugins: [
        vue,
        viteSingleFile(),  // Generate a single HTML file that can be downloaded and opened offline (actually used as a Jinja2 template in the FastAPI app first)
      ],
    }
  }
})
