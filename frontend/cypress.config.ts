import { defineConfig } from 'cypress'


export default defineConfig({
  e2e: {
    baseUrl: 'http://fanout:8080/',
    specPattern: '../tests/**/*.{cy,spec}.{js,jsx,ts,tsx}',
    screenshotsFolder: '../tests/screenshots',
    async setupNodeEvents(on) {
      on('before:browser:launch', (browser, launchOptions) => {
        console.assert(browser.family === 'chromium')
        console.assert(browser.name === 'electron')

        // Disable spellcheck
        // https://docs.cypress.io/api/plugins/browser-launch-api#Changing-browser-preferences
        // https://github.com/electron/electron/blob/main/docs/api/structures/browser-window-options.md
        // https://github.com/electron/electron/blob/main/docs/api/structures/web-preferences.md
        launchOptions.preferences.webPreferences.spellcheck = false

        // Enable high-resolution snapshots
        // https://github.com/cypress-io/cypress/issues/19505#issuecomment-1003740653
        // https://www.cypress.io/blog/2021/03/01/generate-high-resolution-videos-and-screenshots#the-window-size-on-ci
        if (browser.isHeadless) {
          launchOptions.preferences.width = 1600
          launchOptions.preferences.height = 1200
        }

        return launchOptions
      })
    },
  },
  component: {
    specPattern: 'src/**/*.{cy,spec}.{js,ts,jsx,tsx}',
    devServer: {
      framework: 'vue',
      bundler: 'vite',
    },
  },
})
