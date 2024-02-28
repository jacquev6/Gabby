import { setActivePinia, createPinia } from 'pinia'
import * as pdfjs from 'pdfjs-dist/build/pdf'

import { definePdfsStore, usePdfsStore } from '../pdfs.js'


pdfjs.GlobalWorkerOptions.workerSrc = 'http://frontend/pdf.worker.min.js'

describe('PdfsStore', () => {
  beforeEach(() => {
    setActivePinia(createPinia())
  })

  const url = 'http://frontend/test.pdf'
  const sha256 = 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c'

  it('loads a PDF', async () => {
    const pdfs = usePdfsStore()

    const info = await pdfs.load(url)
    expect(info.source).to.equal(url)
    expect(info.sha256).to.equal(sha256)
    expect(info.document.numPages).to.equal(2)
  })

  it('gets a loaded PDF', async () => {
    const pdfs = usePdfsStore()

    expect(pdfs.loaded.length).to.equal(0)
    expect(await pdfs.getSource(sha256)).to.be.null
    expect(await pdfs.get(sha256)).to.be.null

    await pdfs.load(url)

    expect(pdfs.loaded.length).to.equal(1)
    expect(pdfs.loaded[0].source).to.equal(url)
    expect(pdfs.loaded[0].sha256).to.equal(sha256)
    expect(await pdfs.getSource(sha256)).to.equal(url)
    const info = await pdfs.get(sha256)
    expect(info.source).to.equal(url)
    expect(info.sha256).to.equal(sha256)
    expect(info.document.numPages).to.equal(2)
  })

  it('reloads a PDF after garbage collection', async () => {
    let garbage_collected = false
    let weak_refs_created = 0
    let weak_refs_derefed = 0

    function weak_ref(o) {
      ++weak_refs_created
      return {
        deref() {
          ++weak_refs_derefed
          if (garbage_collected) {
            return null
          } else {
            return o
          }
        }
      }
    }

    const pdfs = definePdfsStore('pdfs', {weak_ref})()

    await pdfs.load(url)

    expect(weak_refs_created).to.equal(1)
    expect(weak_refs_derefed).to.equal(0)

    expect((await pdfs.get(sha256)).document.numPages).to.equal(2)

    expect(weak_refs_created).to.equal(1)
    expect(weak_refs_derefed).to.equal(1)

    expect((await pdfs.get(sha256)).document.numPages).to.equal(2)

    expect(weak_refs_created).to.equal(1)
    expect(weak_refs_derefed).to.equal(2)

    garbage_collected = true

    expect((await pdfs.get(sha256)).document.numPages).to.equal(2)

    expect(weak_refs_created).to.equal(2)
    expect(weak_refs_derefed).to.equal(3)
  })
})
