import TricolorSection from './TricolorSection.vue'

describe('TricolorSection for FillWithFreeTextAdaptationTestCase', () => {
  beforeEach(() => {
    cy.viewport(1000, 100)
  })

  it('renders gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_example_and_clue pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "instructions"}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "This"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "@"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "is"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "the"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "example"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "This"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "@"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "is"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "the"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "clue"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_example_and_clue.0.instructions')
  })

  it('renders gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_example_and_clue pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "This"}, {"kind": "whitespace"}, {"kind": "freeTextInput"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "is"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "the"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wording"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_example_and_clue.0.wording')
  })

  it('renders gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_multiple_lines_in_instructions pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "instructions"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "are"}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "on"}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "multiple"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "lines"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_multiple_lines_in_instructions.0.instructions')
  })

  it('renders gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_multiple_lines_in_instructions pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wording"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_multiple_lines_in_instructions.0.wording')
  })

  it('renders gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_multiple_lines_in_wording pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "instructions"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_multiple_lines_in_wording.0.instructions')
  })

  it('renders gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_multiple_lines_in_wording pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "foo"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "toto"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": ":"}, {"kind": "whitespace"}, {"kind": "freeTextInput"}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "bar"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": ":"}, {"kind": "whitespace"}, {"kind": "freeTextInput"}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "baz"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": ":"}, {"kind": "whitespace"}, {"kind": "freeTextInput"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_multiple_lines_in_wording.0.wording')
  })

  it('renders gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_single_sentence pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "The"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wording"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "of"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "this"}, {"kind": "whitespace"}, {"kind": "freeTextInput"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "is"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "a"}, {"kind": "whitespace"}, {"kind": "freeTextInput"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "sentence"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_single_sentence.0.wording')
  })

  it('renders gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_start_and_end_with_placeholder pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "freeTextInput"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "a"}, {"kind": "whitespace"}, {"kind": "freeTextInput"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_start_and_end_with_placeholder.0.wording')
  })

  it('renders gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_strip_whitespace pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "abc"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_strip_whitespace.0.instructions')
  })

  it('renders gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_strip_whitespace pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "def"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_strip_whitespace.0.wording')
  })

  it('renders gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_unknown_tags pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "{"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "tag"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "|"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "abc"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "}"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_unknown_tags.0.instructions')
  })

  it('renders gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_unknown_tags pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "{"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "tag"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "|"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "def"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "}"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_unknown_tags.0.wording')
  })
})
