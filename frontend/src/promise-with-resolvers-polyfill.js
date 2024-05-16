// Polyfill required for Electron 118, still used by Cypress 13.9.0
if (Promise.withResolvers === undefined) {
  Promise.withResolvers = function() {
    let resolve, reject
    const promise = new Promise((res, rej) => {resolve = res; reject = rej})
    return {promise, resolve, reject}
  }
}
