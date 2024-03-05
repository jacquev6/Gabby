import { defineStore } from 'pinia'
import * as pdfjs from 'pdfjs-dist/build/pdf'
import shajs from 'sha.js'


// @todo(Bug, now) Fix opening 03581037_nouvel_explorons_int_complet.pdf

export function definePdfsStore(name, options) {
  const weak_ref = options?.weak_ref ?? ((o) => new WeakRef(o))

  async function loadDocument(name, arg) {
    const startTime = performance.now()
    try {
      const document = await pdfjs.getDocument(arg).promise
      console.info('Loaded', name, 'in', Math.round(performance.now() - startTime), 'ms')
      return document
    } catch (e) {
      console.error('Failed to load', name, ':', e)
      throw e
    }
  }

  function computeSha256(name, data) {
    const startTime = performance.now()
    const sha256 = shajs('sha256').update(data).digest('hex')
    console.info('Computed sha256 of', name, 'in', Math.round(performance.now() - startTime), 'ms')
    return sha256
  }

  const persistentStore = {
    async save(sha256, info, data) {
      localStorage.setItem('pdfs/info/' + sha256, JSON.stringify(info))
      const rootStorageDirectory = await navigator.storage.getDirectory()
      const directoryHandle = await rootStorageDirectory.getDirectoryHandle('pdf', {create: true})
      const fileHandle = await directoryHandle.getFileHandle(sha256, {create: true})
      const writable = await fileHandle.createWritable()
      await writable.write(data)
      await writable.close()
    },
    async load(sha256) {
      const info = JSON.parse(localStorage.getItem('pdfs/info/' + sha256))
      if (!info) return null

      const rootStorageDirectory = await navigator.storage.getDirectory()
      const directoryHandle = await rootStorageDirectory.getDirectoryHandle('pdf', {create: true})
      var fileHandle = null
      try {
        fileHandle = await directoryHandle.getFileHandle(sha256, {create: false})
      } catch (e) {
        if (e.name === 'NotFoundError') {
          localStorage.removeItem('pdfs/info/' + sha256)
          return null
        } else {
          throw e
        }
      }
      console.assert(fileHandle)
      const file = await fileHandle.getFile()
      const data = await file.arrayBuffer()

      return {info, data}
    },
    list() {
      const l = []
      for (const [key, info] of Object.entries(localStorage)) {
        if (key.startsWith('pdfs/info/')) {
          l.push(JSON.parse(info))
        }
      }
      return l
    },
    async delete(sha256) {
      localStorage.removeItem('pdfs/info/' + sha256)
      const rootStorageDirectory = await navigator.storage.getDirectory()
      const directoryHandle = await rootStorageDirectory.getDirectoryHandle('pdf', {create: true})
      directoryHandle.removeEntry(sha256)
    },
  }

  return defineStore(name, {
    state: () => {
      const _infosBySha256 = {}
      for (const info of persistentStore.list()) {
        _infosBySha256[info.sha256] = info
      }
      return {
        _infosBySha256,
        _localLoadingPromiseBySha256: {},
        _documentWeakRefsBySha256: {},
      }
    },
    getters: {
      known() {
        const known = []
        for (const info of Object.values(this._infosBySha256)) {
          if (info) {
            const {sha256, name, size} = info
            known.push({sha256, name, size})
          }
        }
        return known
      },
    },
    actions: {
      async open(source) {
        const name = source.url ?? source.name
        const document = await loadDocument(
          name,
          source.url ? {url: source.url} : {data: await source.arrayBuffer()},
        )
        const data = await document.getData()
        const sha256 = computeSha256(name, data)
        
        const info = {sha256, name, size: data.length}
        this._infosBySha256[sha256] = info
        this._documentWeakRefsBySha256[sha256] = weak_ref(document)
        await persistentStore.save(sha256, info, data)

        return {info, document}
      },
      async close(sha256) {
        this._infosBySha256[sha256] = null
        this._documentWeakRefsBySha256[sha256] = null
        await persistentStore.delete(sha256)
      },
      getInfo(sha256) {
        return this._infosBySha256[sha256] ?? null
      },
      async getDocument(sha256) {
        const document = this._documentWeakRefsBySha256[sha256]?.deref()
        if (document) {
          return document
        } else if (this._localLoadingPromiseBySha256[sha256]) {
          return await this._localLoadingPromiseBySha256[sha256]
        } else {
          this._localLoadingPromiseBySha256[sha256] = (async () => {
            const stored = await persistentStore.load(sha256)
            if(stored) {
              const {info: {name}, data} = stored
              const document = await loadDocument(name + ' (from local storage)', {data})
              this._documentWeakRefsBySha256[sha256] = weak_ref(document)
              return document
            } else {
              return null
            }
          })()
          const document = await this._localLoadingPromiseBySha256[sha256]
          this._localLoadingPromiseBySha256[sha256] = null
          return document
        }
      },
    },
    share: {
      enable: true,
      omit: ['_documentWeakRefsBySha256', '_localLoadingPromiseBySha256'],
    },
  })
}

export const usePdfsStore = definePdfsStore('pdfs', {})
