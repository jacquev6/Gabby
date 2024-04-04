const { defineConfig } = require('cypress')


module.exports = defineConfig({
  component: {
    specPattern: 'src/**/*.{cy,spec}.{js,ts,jsx,tsx}',
    devServer: {
      framework: 'vue',
      bundler: 'vite',
    },
  },
})
