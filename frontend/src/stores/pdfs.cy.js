import { setActivePinia, createPinia } from 'pinia'
import * as pdfjs from 'pdfjs-dist/build/pdf'

import { definePdfsStore, usePdfsStore } from './pdfs.js'


pdfjs.GlobalWorkerOptions.workerSrc = 'http://frontend/pdf.worker.min.js'

describe('PdfsStore', () => {
  before(console.clear)

  beforeEach(() => {
    setActivePinia(createPinia())
  })

  const url = 'http://frontend/test.pdf'
  const sha256 = 'f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c'

  it('opens a PDF from a URL', async () => {
    const pdfs = usePdfsStore()

    const pdf = await pdfs.open({url})
    expect(pdf.info).to.deep.equal({sha256, name: url, size: 484714})
    expect(pdf.document.numPages).to.equal(2)
  })

  it('opens a PDF from a file', () => {
    const pdfs = usePdfsStore()

    cy.fixture('../../../pdf-examples/test.pdf', null)
      .then(async (buffer) => {
        const file = new File([buffer], 'test.pdf', {type: 'application/pdf'})
        const pdf = await pdfs.open(file)
        expect(pdf.info).to.deep.equal({sha256, name: 'test.pdf', size: 484714})
        expect(pdf.document.numPages).to.equal(2)
      })
  })

  it('opens a large PDF from a file', () => {
    const pdfs = usePdfsStore()

    cy.fixture('../../../pdf-examples/large.pdf', null)
      .then(async (buffer) => {
        const file = new File([buffer], 'large.pdf', {type: 'application/pdf'})
        const pdf = await pdfs.open(file)
        // 'pdf-examples/large.pdf' is not in git and made using 'pdf-examples/make_large.sh'
        // that doesn't always produce the same file :-/, so we can't test its sha256 and size.
        expect(pdf.info.name).to.equal('large.pdf')
        expect(pdf.document.numPages).to.equal(64)
      })
  })

  it('gets an already-opened PDF', async () => {
    const pdfs = usePdfsStore()

    expect(pdfs.getInfo(sha256)).to.be.null
    expect(await pdfs.getDocument(sha256)).to.be.null

    await pdfs.open({url})

    expect(pdfs.getInfo(sha256)).to.deep.equal({sha256, name: url, size: 484714})
    expect((await pdfs.getDocument(sha256)).numPages).to.equal(2)
  })

  it('cannot get a closed PDF', async () => {
    const pdfs = usePdfsStore()

    expect(pdfs.getInfo(sha256)).to.be.null
    expect(await pdfs.getDocument(sha256)).to.be.null

    await pdfs.open({url})
    pdfs.close(sha256)

    expect(pdfs.getInfo(sha256)).to.be.null
    expect(await pdfs.getDocument(sha256)).to.be.null
  })

  it('gets an already-opened PDF after garbage collection', async () => {
    let garbage_collections = 0
    let weak_refs_created = 0
    let weak_refs_derefed = 0

    function weak_ref(o) {
      const garbage_collections_on_creation = garbage_collections
      ++weak_refs_created
      return {
        deref() {
          ++weak_refs_derefed
          if (garbage_collections !== garbage_collections_on_creation) {
            return null
          } else {
            return o
          }
        }
      }
    }

    const pdfs = definePdfsStore('pdfs', {weak_ref})()

    await pdfs.open({url})

    expect(weak_refs_created).to.equal(1)
    expect(weak_refs_derefed).to.equal(0)

    expect((await pdfs.getDocument(sha256)).numPages).to.equal(2)

    expect(weak_refs_created).to.equal(1)
    expect(weak_refs_derefed).to.equal(1)

    expect((await pdfs.getDocument(sha256)).numPages).to.equal(2)

    expect(weak_refs_created).to.equal(1)
    expect(weak_refs_derefed).to.equal(2)

    ++garbage_collections

    expect((await pdfs.getDocument(sha256)).numPages).to.equal(2)

    expect(weak_refs_created).to.equal(2)
    expect(weak_refs_derefed).to.equal(3)

    ++garbage_collections

    const doc1Promise = pdfs.getDocument(sha256)
    const doc2Promise = pdfs.getDocument(sha256)

    const doc1 = await doc1Promise
    const doc2 = await doc2Promise

    expect(doc1).to.equal(doc2)
    expect(doc1.numPages).to.equal(2)
    expect(doc2.numPages).to.equal(2)

    expect(weak_refs_created).to.equal(3)
    expect(weak_refs_derefed).to.equal(5)
  })

  it('gets a PDF opened in a previous session or another tab', async () => {
    const pdfs1 = usePdfsStore()
    await pdfs1.open({url})

    setActivePinia(createPinia())
    const pdfs2 = usePdfsStore()

    expect(await pdfs2.getInfo(sha256)).to.deep.equal({sha256, name: url, size: 484714})
    expect((await pdfs2.getDocument(sha256)).numPages).to.equal(2)
    pdfs2.close(sha256)
    expect(await pdfs2.getInfo(sha256)).to.be.null
    expect(await pdfs2.getDocument(sha256)).to.be.null

    setActivePinia(createPinia())
    const pdfs3 = usePdfsStore()
    expect(await pdfs3.getInfo(sha256)).to.be.null
    expect(await pdfs3.getDocument(sha256)).to.be.null
  })

  it('gets a large PDF opened in a previous session or another tab', () => {
    const pdfs1 = usePdfsStore()

    cy.fixture('../../../pdf-examples/large.pdf', null)
      .then(async (buffer) => {
        const file = new File([buffer], 'large.pdf', {type: 'application/pdf'})
        const {sha256, size} = (await pdfs1.open(file)).info

        setActivePinia(createPinia())
        const pdfs2 = usePdfsStore()

        expect(await pdfs2.getInfo(sha256)).to.deep.equal({sha256, name: 'large.pdf', size})
        expect((await pdfs2.getDocument(sha256)).numPages).to.equal(64)
        pdfs2.close(sha256)
        expect(await pdfs2.getInfo(sha256)).to.be.null
        expect(await pdfs2.getDocument(sha256)).to.be.null

        setActivePinia(createPinia())
        const pdfs3 = usePdfsStore()
        expect(await pdfs3.getInfo(sha256)).to.be.null
        expect(await pdfs3.getDocument(sha256)).to.be.null
      })
  })

  it('lists known PDFs from previous sessions or other tabs', async () => {
    const pdfs1 = usePdfsStore()
    await pdfs1.open({url})
    expect(pdfs1.known).to.deep.equal([{sha256, name: url, size: 484714}])

    setActivePinia(createPinia())
    const pdfs2 = usePdfsStore()
    expect(pdfs2.known).to.deep.equal([{sha256, name: url, size: 484714}])
    pdfs2.close(sha256)
    expect(pdfs2.known).to.deep.equal([])

    setActivePinia(createPinia())
    const pdfs3 = usePdfsStore()
    expect(pdfs3.known).to.deep.equal([])
  })
})
