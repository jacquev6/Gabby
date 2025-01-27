import { type Model } from './Quill.vue'
import WysiwygEditor from './WysiwygEditor.vue'

describe('WysiwygEditor', () => {
  before(console.clear)

  it("updates its model", () => {
    let modelValue: Model = [{insert: 'hell\n\n', attributes: {}}]
    cy.mount(WysiwygEditor, {props: {
      label: 'Test',
      blots: [],
      compatibleFormats: [],
      contagiousFormats: [],
      modelValue,
      'onUpdate:modelValue': (m: Model) => {modelValue = m},
    }})
    cy.get('div.ql-editor').type('o').then(() => {
      expect(modelValue).to.deep.equal([{insert: 'hell\no\n', attributes: {}}])
    })
  })

  it("adds characters before the trailing line end when typing at the end", () => {
    let modelValue: Model = [{insert: 'hell\n', attributes: {}}]
    cy.mount(WysiwygEditor, {props: {
      label: 'Test',
      blots: [],
      compatibleFormats: [],
      contagiousFormats: [],
      modelValue,
      'onUpdate:modelValue': (m: Model) => {modelValue = m},
    }})
    cy.get('div.ql-editor').type('o')
    cy.wait(0).then(() => {
      expect(modelValue).to.deep.equal([{insert: 'hello\n', attributes: {}}])
    })
  })

  it("add characters at the start when typing at the start", () => {
    let modelValue: Model = [{insert: 'ello\n', attributes: {}}]
    cy.mount(WysiwygEditor, {props: {
      label: 'Test',
      blots: [],
      compatibleFormats: [],
      contagiousFormats: [],
      modelValue,
      'onUpdate:modelValue': (m: Model) => {modelValue = m},
    }})
    cy.get('div.ql-editor').type('{moveToStart}h').then(() => {
      expect(modelValue).to.deep.equal([{insert: 'hello\n', attributes: {}}])
    })
  })

  it("keeps a freshly-added trailing line end", () => {
    let modelValue: Model = [{insert: 'hello\n', attributes: {}}]
    cy.mount(WysiwygEditor, {props: {
      label: 'Test',
      blots: [],
      compatibleFormats: [],
      contagiousFormats: [],
      modelValue,
      'onUpdate:modelValue': (m: Model) => {modelValue = m},
    }})
    cy.get('div.ql-editor').type('\n').then(() => {
      expect(modelValue).to.deep.equal([{insert: 'hello\n\n', attributes: {}}])
    })
  })

  it("keeps an ever-present trailing line end", () => {
    let modelValue: Model = [{insert: 'ello\n\n', attributes: {}}]
    cy.mount(WysiwygEditor, {props: {
      label: 'Test',
      blots: [],
      compatibleFormats: [],
      contagiousFormats: [],
      modelValue,
      'onUpdate:modelValue': (m: Model) => {modelValue = m},
      delta: [{insert: modelValue, attributes: {}}],
    }})
    cy.get('div.ql-editor').type('{moveToStart}h').then(() => {
      expect(modelValue).to.deep.equal([{insert: 'hello\n\n', attributes: {}}])
    })
  })

  it("removes an ever-present trailing line end when deleting all", () => {
    let modelValue: Model = [{insert: 'hello\n\n', attributes: {}}]
    cy.mount(WysiwygEditor, {props: {
      label: 'Test',
      blots: [],
      compatibleFormats: [],
      contagiousFormats: [],
      modelValue,
      'onUpdate:modelValue': (m: Model) => {modelValue = m},
      delta: [{insert: modelValue, attributes: {}}],
    }})
    cy.get('div.ql-editor').type('{selectAll}{del}').then(() => {
      expect(modelValue).to.deep.equal([{insert: '\n', attributes: {}}])
    })
  })
})
