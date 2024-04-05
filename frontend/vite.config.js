import { promises as fs } from 'fs'

import { defineConfig } from 'vite'
import { viteSingleFile } from "vite-plugin-singlefile"
import vue from '@vitejs/plugin-vue'


const entryPointName = process.env.GABBY_ENTRY_POINT_NAME

// @todo Avoid adding contents of 'public' in all entry points; change 'publicDir' according to entry point

function renameIndexHtml(name) {
  return {
    name: 'vite-plugin-rename-index-html',
    transformIndexHtml: {
      order: 'pre',
      async handler() {
        return await fs.readFile(`./${name}.html`, 'utf8');
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
    plugins.push(viteSingleFile())
  }

  return {
    plugins,
    // This section works around the following error when importing pdfjs-dist@4:
    //     "Top-level await is not available in the configured target environment"
    // It's a mix of these solutions:
    // - https://stackoverflow.com/a/77859823/905845
    // - https://stackoverflow.com/a/77643886/905845
    optimizeDeps: {esbuildOptions: {target: 'esnext'}},
    esbuild: {supported: {'top-level-await': true}},
    // End of section
  }
})
