import { defineStore } from 'pinia'
import {} from 'pinia-shared-state'  // For TypeScript. @todo Remove line when 'main.js' is replaced by 'main.ts'
// @ts-ignore/* Temporary untyped */
import * as untypedPdfjs from 'pdfjs-dist/build/pdf'
import type PdfjsType from 'pdfjs-dist/types/src/pdf'
import type { DocumentInitParameters, PDFDocumentProxy } from 'pdfjs-dist/types/src/display/api'
import shajs from 'sha.js'


const pdfjs = untypedPdfjs as typeof PdfjsType

type Sha256 = string

interface Info {
  sha256: Sha256
  name: string
  size: number
}

export interface InfoDoc {
  info: Info
  document: PDFDocumentProxy
}

function make_weak_ref<T extends object>(o: T) {
  return new WeakRef(o)
}

interface PseudoWeakRef<T extends object> {
  deref(): T | undefined
}

export function definePdfsStore(name: string, options: {weak_ref?: (o: PDFDocumentProxy) => PseudoWeakRef<PDFDocumentProxy>}) {
  const weak_ref = options?.weak_ref ?? make_weak_ref

  async function loadDocument(name: string, arg: DocumentInitParameters) {
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

  function computeSha256(name: string, data: Uint8Array) {
    const startTime = performance.now()
    const sha256 = shajs('sha256').update(data).digest('hex')
    console.info('Computed sha256 of', name, 'in', Math.round(performance.now() - startTime), 'ms')
    return sha256
  }

  // @todo(Project management) Add an end-to-end test for reloading a PDF from local storage
  // (Requires running against localhost or an https server)

  const actualPersistentStore = {
    async save(sha256: Sha256, info: Info, data: Uint8Array) {
      // @todo Rename localStorage keys to '/pdfs-v1/' + sha256
      localStorage.setItem('pdfs/info/' + sha256, JSON.stringify(info))
      const rootStorageDirectory = await navigator.storage.getDirectory()
      // @todo Rename directory to 'pdfs-v1'
      const directoryHandle = await rootStorageDirectory.getDirectoryHandle('pdf', {create: true})
      const fileHandle = await directoryHandle.getFileHandle(sha256, {create: true})
      const writable = await fileHandle.createWritable()
      await writable.write(data)
      await writable.close()
    },
    async load(sha256: Sha256) {
      const infoData = localStorage.getItem('pdfs/info/' + sha256)
      if (!infoData) return null
      const info = JSON.parse(infoData)

      const rootStorageDirectory = await navigator.storage.getDirectory()
      const directoryHandle = await rootStorageDirectory.getDirectoryHandle('pdf', {create: true})
      var fileHandle = null
      try {
        fileHandle = await directoryHandle.getFileHandle(sha256, {create: false})
      } catch (e) {
        if (e instanceof DOMException && e.name === 'NotFoundError') {
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
    async delete(sha256: Sha256) {
      localStorage.removeItem('pdfs/info/' + sha256)
      const rootStorageDirectory = await navigator.storage.getDirectory()
      const directoryHandle = await rootStorageDirectory.getDirectoryHandle('pdf', {create: true})
      directoryHandle.removeEntry(sha256)
    },
  }

  const nullPersistentStore = {
    async save() {},
    async load() { return null },
    list() { return [] },
    async delete() {},
  }

  const persistentStore = navigator.storage ? actualPersistentStore : nullPersistentStore

  return defineStore(name, {
    state: () => {
      const _infosBySha256: {[sha256: Sha256]: Info} = {}
      for (const info of persistentStore.list()) {
        _infosBySha256[info.sha256] = info
      }
      return {
        _infosBySha256,
        _localLoadingPromiseBySha256: {} as {[sha256: Sha256]: Promise<PDFDocumentProxy | null>},
        _documentWeakRefsBySha256: {} as {[sha256: Sha256]: PseudoWeakRef<PDFDocumentProxy>},
      }
    },
    getters: {
      known(): Info[] {
        return Object.values(this._infosBySha256)
      },
    },
    actions: {
      async open(source: {url: string} | File) {
        const {name, document} = await (async () => {
          if ('url' in source) {
            return {name: source.url, document: await loadDocument(source.url, {url: source.url})}
          } else {
            return {name: source.name, document: await loadDocument(source.name, {data: await source.arrayBuffer()})}
          }
        })()
        const data = await document.getData()
        const sha256 = computeSha256(name, data)

        const info = {sha256, name, size: data.length}
        this._infosBySha256[sha256] = info
        this._documentWeakRefsBySha256[sha256] = weak_ref(document)
        await persistentStore.save(sha256, info, data)

        return {info, document}
      },
      async close(sha256: Sha256) {
        delete this._infosBySha256[sha256]
        delete this._documentWeakRefsBySha256[sha256]
        await persistentStore.delete(sha256)
      },
      getInfo(sha256: Sha256) {
        return sha256 in this._infosBySha256 ? this._infosBySha256[sha256] : null
      },
      async getDocument(sha256: Sha256) {
        const document = this._documentWeakRefsBySha256[sha256]?.deref()
        if (document) {
          return document
        } else if (sha256 in this._localLoadingPromiseBySha256) {
          return await this._localLoadingPromiseBySha256[sha256]
        } else {
          const promise = (async () => {
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
          this._localLoadingPromiseBySha256[sha256] = promise
          const document = await promise
          delete this._localLoadingPromiseBySha256[sha256]
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
