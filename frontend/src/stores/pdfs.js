import { reactive, computed } from 'vue'
import { defineStore } from 'pinia'
import * as pdfjs from 'pdfjs-dist/build/pdf'
import shajs from 'sha.js'


export function definePdfsStore(name, options) {
  const weak_ref = (options && options.weak_ref) || ((o) => new WeakRef(o))

  return defineStore(name, () => {
    const infosBySha256 = reactive({})

    async function loadDocument(source) {
      const startTime = performance.now()
      console.info('Loading PDF', source)

      const arg = {}
      if (typeof source === 'string') {
        arg.url = source
      } else {
        arg.data = await source.arrayBuffer()
      }
      try {
        const document = await pdfjs.getDocument(arg).promise
        console.info('Successfully loaded PDF', source, 'in', performance.now() - startTime, 'ms')
        return document
      } catch (e) {
        console.error('Error loading PDF', e)
        throw e
      }
    }

    async function computeSha256(source, document) {
      const startTime = performance.now()
      console.info('Computing sha256 of PDF', source)
      const sha256 = shajs('sha256').update(await document.getData()).digest('hex')
      console.info('Successfully computed sha256 of PDF', source, 'in', performance.now() - startTime, 'ms')
      return sha256
    }

    async function load(source) {
      const document = await loadDocument(source)
      const sha256 = await computeSha256(source, document)

      infosBySha256[sha256] = {
        source, sha256,
        document: weak_ref(document),
      }

      return {source, sha256, document}
    }

    function getSource(sha256) {
      const info = infosBySha256[sha256]
      if (info) {
        return info.source
      } else {
        return null
      }
    }

    async function get(sha256) {
      const info = infosBySha256[sha256]
      if (info) {
        let document = info.document.deref()
        if (!document) {
          console.info('PDF', info.source, 'has been garbage collected, reloading')
          document = await loadDocument(info.source)
          info.document = weak_ref(document)
        }
        return {
          source: info.source,
          sha256: info.sha256,
          document,
        }
      } else {
        return null
      }
    }

    const loaded = computed(() => {
      const loaded = []
      for (const info of Object.values(infosBySha256)) {
        loaded.push({source: info.source, sha256: info.sha256})
      }
      return loaded
    })

    return { load, get, getSource, loaded }
  })
}

export const usePdfsStore = definePdfsStore('pdfs', {})
