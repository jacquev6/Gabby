import TricolorSection from './TricolorSection.vue'

describe('TricolorSection for ManualMcqFieldsAdaptationTestCase', () => {
  beforeEach(() => {
    cy.viewport(1000, 100)
  })

  it('renders gabby.adaptation.ManualMcqFieldsAdaptationTestCase.test_simplest pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "alpha"}], "boxed": true}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": ","}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "bravo"}], "boxed": true}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "ou"}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "charlie"}], "boxed": true}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ManualMcqFieldsAdaptationTestCase.test_simplest.0.instructions')
  })

  it('renders gabby.adaptation.ManualMcqFieldsAdaptationTestCase.test_simplest pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "multipleChoicesInput", "show_arrow_before": false, "choices": [[{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "alpha"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "bravo"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "charlie"}]], "show_choices_by_default": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ManualMcqFieldsAdaptationTestCase.test_simplest.0.wording')
  })
})
