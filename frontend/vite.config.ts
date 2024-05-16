import { fileURLToPath, URL } from 'node:url'
import { promises as fs } from 'fs'

import { defineConfig, Plugin } from 'vite'
import { viteSingleFile } from "vite-plugin-singlefile"
import vue from '@vitejs/plugin-vue'


const entryPointName = process.env.GABBY_ENTRY_POINT_NAME as string

function renameIndexHtml(name : string) : Plugin {
  return {
    name: 'vite-plugin-rename-index-html',
    transformIndexHtml: {
      order: 'pre',
      async handler() {
        return await fs.readFile(`src/${name}/index.html`, 'utf8');
      },
    },
  }
}

export default defineConfig(({ command, mode, isSsrBuild, isPreview }) => {
  const plugins = [
    renameIndexHtml(entryPointName),
    vue({
      template: {
        compilerOptions: {
          // Fix this problem: https://github.com/vuejs/core/pull/1600#issuecomment-721717095
          whitespace: 'preserve',
        },
      },
    }),
  ]

  if (command === 'build' && entryPointName === 'adapted') {
    // Generate a single HTML file that can be downloaded and opened offline
    // (actually used as a Jinja2 template in the FastAPI app first)
    plugins.push(viteSingleFile() as Plugin)
  }

  return {
    publicDir: `src/${entryPointName}/public`,
    plugins,
    // This section works around the following error when importing pdfjs-dist@4:
    //     "Top-level await is not available in the configured target environment"
    // It's a mix of these solutions:
    // - https://stackoverflow.com/a/77859823/905845
    // - https://stackoverflow.com/a/77643886/905845
    optimizeDeps: {esbuildOptions: {target: 'esnext'}},
    esbuild: {supported: {'top-level-await': true}},
    // End of section
    resolve: {
      alias: {
        '$': fileURLToPath(new URL('./src', import.meta.url)),
        '$adapted': fileURLToPath(new URL('./src/adapted', import.meta.url)),
        '$frontend': fileURLToPath(new URL('./src/frontend', import.meta.url)),
      }
    }
  }
})
