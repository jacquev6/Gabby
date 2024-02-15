import { defineConfig } from 'cypress'

export default defineConfig({
  e2e: {
    specPattern: 'cypress/e2e/**/*.{cy,spec}.{js,jsx,ts,tsx}',
    // Disable spellcheck
    // https://docs.cypress.io/api/plugins/browser-launch-api#Changing-browser-preferences
    // https://github.com/electron/electron/blob/main/docs/api/structures/browser-window-options.md
    // https://github.com/electron/electron/blob/main/docs/api/structures/web-preferences.md
    setupNodeEvents : async (on, config) => {
      on('before:browser:launch', (browser, launchOptions) => {
        console.assert(browser.family === 'chromium')
        console.assert(browser.name === 'electron')

        launchOptions.preferences.webPreferences.spellcheck = false

        return launchOptions
      })
    },
  },
  component: {
    specPattern: 'src/**/__tests__/*.{cy,spec}.{js,ts,jsx,tsx}',
    devServer: {
      framework: 'vue',
      bundler: 'vite'
    }
  }
})
