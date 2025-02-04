import TricolorSection from './OldTricolorSection.vue'

describe('TricolorSection for FillWithFreeTextAdaptationTestCase', () => {
  beforeEach(() => {
    cy.viewport(1000, 100)
  })

  it('renders gabby.adaptation.FillWithFreeTextAdaptationTestCase.test_example_and_clue pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "instructions"}]}, {"tokens": [{"type": "plainText", "text": "This"}, {"type": "whitespace"}, {"type": "plainText", "text": "@"}, {"type": "whitespace"}, {"type": "plainText", "text": "is"}, {"type": "whitespace"}, {"type": "plainText", "text": "the"}, {"type": "whitespace"}, {"type": "plainText", "text": "example"}, {"type": "plainText", "text": "."}]}, {"tokens": [{"type": "plainText", "text": "This"}, {"type": "whitespace"}, {"type": "plainText", "text": "@"}, {"type": "whitespace"}, {"type": "plainText", "text": "is"}, {"type": "whitespace"}, {"type": "plainText", "text": "the"}, {"type": "whitespace"}, {"type": "plainText", "text": "clue"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.FillWithFreeTextAdaptationTestCase.test_example_and_clue.0.instructions')
  })

  it('renders gabby.adaptation.FillWithFreeTextAdaptationTestCase.test_example_and_clue pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "This"}, {"type": "whitespace"}, {"type": "freeTextInput"}, {"type": "whitespace"}, {"type": "plainText", "text": "is"}, {"type": "whitespace"}, {"type": "plainText", "text": "the"}, {"type": "whitespace"}, {"type": "plainText", "text": "wording"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.FillWithFreeTextAdaptationTestCase.test_example_and_clue.0.wording')
  })

  it('renders gabby.adaptation.FillWithFreeTextAdaptationTestCase.test_multiple_lines_in_instructions pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "instructions"}, {"type": "whitespace"}, {"type": "plainText", "text": "are"}]}, {"tokens": [{"type": "plainText", "text": "on"}]}, {"tokens": [{"type": "plainText", "text": "multiple"}, {"type": "whitespace"}, {"type": "plainText", "text": "lines"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.FillWithFreeTextAdaptationTestCase.test_multiple_lines_in_instructions.0.instructions')
  })

  it('renders gabby.adaptation.FillWithFreeTextAdaptationTestCase.test_multiple_lines_in_instructions pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "wording"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.FillWithFreeTextAdaptationTestCase.test_multiple_lines_in_instructions.0.wording')
  })

  it('renders gabby.adaptation.FillWithFreeTextAdaptationTestCase.test_multiple_lines_in_wording pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "instructions"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.FillWithFreeTextAdaptationTestCase.test_multiple_lines_in_wording.0.instructions')
  })

  it('renders gabby.adaptation.FillWithFreeTextAdaptationTestCase.test_multiple_lines_in_wording pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "foo"}, {"type": "whitespace"}, {"type": "plainText", "text": "toto"}, {"type": "whitespace"}, {"type": "plainText", "text": ":"}, {"type": "whitespace"}, {"type": "freeTextInput"}]}, {"tokens": [{"type": "plainText", "text": "bar"}, {"type": "whitespace"}, {"type": "plainText", "text": ":"}, {"type": "whitespace"}, {"type": "freeTextInput"}]}, {"tokens": [{"type": "plainText", "text": "baz"}, {"type": "whitespace"}, {"type": "plainText", "text": ":"}, {"type": "whitespace"}, {"type": "freeTextInput"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.FillWithFreeTextAdaptationTestCase.test_multiple_lines_in_wording.0.wording')
  })

  it('renders gabby.adaptation.FillWithFreeTextAdaptationTestCase.test_single_sentence pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "The"}, {"type": "whitespace"}, {"type": "plainText", "text": "wording"}, {"type": "whitespace"}, {"type": "plainText", "text": "of"}, {"type": "whitespace"}, {"type": "plainText", "text": "this"}, {"type": "whitespace"}, {"type": "freeTextInput"}, {"type": "whitespace"}, {"type": "plainText", "text": "is"}, {"type": "whitespace"}, {"type": "plainText", "text": "a"}, {"type": "whitespace"}, {"type": "freeTextInput"}, {"type": "whitespace"}, {"type": "plainText", "text": "sentence"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.FillWithFreeTextAdaptationTestCase.test_single_sentence.0.wording')
  })

  it('renders gabby.adaptation.FillWithFreeTextAdaptationTestCase.test_start_and_end_with_placeholder pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "freeTextInput"}, {"type": "whitespace"}, {"type": "plainText", "text": "a"}, {"type": "whitespace"}, {"type": "freeTextInput"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.FillWithFreeTextAdaptationTestCase.test_start_and_end_with_placeholder.0.wording')
  })

  it('renders gabby.adaptation.FillWithFreeTextAdaptationTestCase.test_strip_whitespace pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "abc"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.FillWithFreeTextAdaptationTestCase.test_strip_whitespace.0.instructions')
  })

  it('renders gabby.adaptation.FillWithFreeTextAdaptationTestCase.test_strip_whitespace pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "def"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.FillWithFreeTextAdaptationTestCase.test_strip_whitespace.0.wording')
  })

  it('renders gabby.adaptation.FillWithFreeTextAdaptationTestCase.test_unknown_tags pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "{"}, {"type": "plainText", "text": "tag"}, {"type": "plainText", "text": "|"}, {"type": "plainText", "text": "abc"}, {"type": "plainText", "text": "}"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.FillWithFreeTextAdaptationTestCase.test_unknown_tags.0.instructions')
  })

  it('renders gabby.adaptation.FillWithFreeTextAdaptationTestCase.test_unknown_tags pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "{"}, {"type": "plainText", "text": "tag"}, {"type": "plainText", "text": "|"}, {"type": "plainText", "text": "def"}, {"type": "plainText", "text": "}"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.FillWithFreeTextAdaptationTestCase.test_unknown_tags.0.wording')
  })
})
