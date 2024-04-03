const { defineConfig } = require('cypress')


module.exports = defineConfig({
  e2e: {
    baseUrl: 'http://fanout:8080/',
    specPattern: '../tests/**/*.{cy,spec}.{js,jsx,ts,tsx}',
    screenshotsFolder: '../tests/screenshots',
    // Disable spellcheck
    // https://docs.cypress.io/api/plugins/browser-launch-api#Changing-browser-preferences
    // https://github.com/electron/electron/blob/main/docs/api/structures/browser-window-options.md
    // https://github.com/electron/electron/blob/main/docs/api/structures/web-preferences.md
    async setupNodeEvents(on) {
      on('before:browser:launch', (browser, launchOptions) => {
        console.assert(browser.family === 'chromium')
        console.assert(browser.name === 'electron')

        launchOptions.preferences.webPreferences.spellcheck = false

        return launchOptions
      })
    },
  },
  component: {
    specPattern: '../{frontend,adapted}/**/*.{cy,spec}.{js,ts,jsx,tsx}',
    devServer: {
      framework: 'vue',
      bundler: 'vite',
    },
  },
})
