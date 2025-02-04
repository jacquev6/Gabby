import TricolorSection from './OldTricolorSection.vue'

describe('TricolorSection for LenientParagraphTestCase', () => {
  beforeEach(() => {
    cy.viewport(1000, 100)
  })

  it('renders gabby.adaptation.LenientParagraphTestCase.test_bold_and_italic pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "This"}, {"type": "whitespace"}, {"type": "plainText", "text": "is"}, {"type": "whitespace"}, {"type": "plainText", "text": "a"}, {"type": "whitespace"}, {"type": "passiveFormattedText", "text": "strict", "bold": true, "italic": false}, {"type": "whitespace"}, {"type": "plainText", "text": "instructions"}, {"type": "whitespace"}, {"type": "passiveFormattedText", "text": "paragraph", "bold": false, "italic": true}, {"type": "plainText", "text": "."}]}, {"tokens": [{"type": "plainText", "text": "And"}, {"type": "whitespace"}, {"type": "plainText", "text": "this"}, {"type": "whitespace"}, {"type": "plainText", "text": "is"}, {"type": "whitespace"}, {"type": "plainText", "text": "a"}, {"type": "whitespace"}, {"type": "passiveFormattedText", "text": "lenient", "bold": true, "italic": false}, {"type": "whitespace"}, {"type": "plainText", "text": "instructions"}, {"type": "whitespace"}, {"type": "passiveFormattedText", "text": "paragraph", "bold": false, "italic": true}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.LenientParagraphTestCase.test_bold_and_italic.0.instructions')
  })

  it('renders gabby.adaptation.LenientParagraphTestCase.test_bold_and_italic pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "This"}, {"type": "whitespace"}, {"type": "plainText", "text": "is"}, {"type": "whitespace"}, {"type": "plainText", "text": "a"}, {"type": "whitespace"}, {"type": "passiveFormattedText", "text": "strict", "bold": true, "italic": false}, {"type": "whitespace"}, {"type": "plainText", "text": "wording"}, {"type": "whitespace"}, {"type": "passiveFormattedText", "text": "paragraph", "bold": false, "italic": true}, {"type": "plainText", "text": "."}]}, {"tokens": [{"type": "plainText", "text": "And"}, {"type": "whitespace"}, {"type": "plainText", "text": "this"}, {"type": "whitespace"}, {"type": "plainText", "text": "is"}, {"type": "whitespace"}, {"type": "plainText", "text": "a"}, {"type": "whitespace"}, {"type": "passiveFormattedText", "text": "lenient", "bold": true, "italic": false}, {"type": "whitespace"}, {"type": "plainText", "text": "wording"}, {"type": "whitespace"}, {"type": "passiveFormattedText", "text": "paragraph", "bold": false, "italic": true}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.LenientParagraphTestCase.test_bold_and_italic.0.wording')
  })

  it('renders gabby.adaptation.LenientParagraphTestCase.test_fill_with_free_text pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "instructions"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.LenientParagraphTestCase.test_fill_with_free_text.0.instructions')
  })

  it('renders gabby.adaptation.LenientParagraphTestCase.test_fill_with_free_text pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "This"}, {"type": "whitespace"}, {"type": "plainText", "text": "is"}, {"type": "whitespace"}, {"type": "plainText", "text": "a"}, {"type": "whitespace"}, {"type": "freeTextInput"}, {"type": "whitespace"}, {"type": "plainText", "text": "strict"}, {"type": "whitespace"}, {"type": "plainText", "text": "paragraph"}, {"type": "plainText", "text": "."}, {"type": "whitespace"}, {"type": "plainText", "text": "With"}, {"type": "whitespace"}, {"type": "plainText", "text": "some"}, {"type": "whitespace"}, {"type": "plainText", "text": "punctuation"}, {"type": "plainText", "text": "."}]}, {"tokens": [{"type": "plainText", "text": "And"}, {"type": "whitespace"}, {"type": "plainText", "text": "this"}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "plainText", "text": "is"}, {"type": "whitespace"}, {"type": "plainText", "text": "a"}, {"type": "whitespace"}, {"type": "freeTextInput"}, {"type": "whitespace"}, {"type": "plainText", "text": "lenient"}, {"type": "whitespace"}, {"type": "plainText", "text": "paragraph"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.LenientParagraphTestCase.test_fill_with_free_text.0.wording')
  })

  it('renders gabby.adaptation.LenientParagraphTestCase.test_multiple_choices pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "Choose"}, {"type": "whitespace"}, {"type": "boxedText", "text": "alpha"}, {"type": "whitespace"}, {"type": "plainText", "text": "ou"}, {"type": "whitespace"}, {"type": "boxedText", "text": "bravo"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.LenientParagraphTestCase.test_multiple_choices.0.instructions')
  })

  it('renders gabby.adaptation.LenientParagraphTestCase.test_multiple_choices pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "This"}, {"type": "whitespace"}, {"type": "plainText", "text": "is"}, {"type": "whitespace"}, {"type": "plainText", "text": "a"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "plainText", "text": "strict"}, {"type": "whitespace"}, {"type": "plainText", "text": "paragraph"}, {"type": "plainText", "text": "."}, {"type": "whitespace"}, {"type": "plainText", "text": "With"}, {"type": "whitespace"}, {"type": "plainText", "text": "some"}, {"type": "whitespace"}, {"type": "plainText", "text": "punctuation"}, {"type": "plainText", "text": "."}]}, {"tokens": [{"type": "plainText", "text": "And"}, {"type": "whitespace"}, {"type": "plainText", "text": "this"}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "plainText", "text": "is"}, {"type": "whitespace"}, {"type": "plainText", "text": "a"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "plainText", "text": "lenient"}, {"type": "whitespace"}, {"type": "plainText", "text": "paragraph"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.LenientParagraphTestCase.test_multiple_choices.0.wording')
  })

  it('renders gabby.adaptation.LenientParagraphTestCase.test_select_words_with_punctuation pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "selectableText", "text": "This", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "is", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "a", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "strict", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "paragraph", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": ",", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "with", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": "...", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "some", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "punctuation", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": ".", "colors": ["red"], "boxed": false}]}, {"tokens": [{"type": "selectableText", "text": "And", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "this", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": ",", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "is", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "a", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": "...", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "lenient", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "paragraph", "colors": ["red"], "boxed": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.LenientParagraphTestCase.test_select_words_with_punctuation.0.wording')
  })

  it('renders gabby.adaptation.LenientParagraphTestCase.test_select_words_without_punctuation pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "selectableText", "text": "This", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "is", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "a", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "strict", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "paragraph", "colors": ["red"], "boxed": false}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "selectableText", "text": "with", "colors": ["red"], "boxed": false}, {"type": "plainText", "text": "..."}, {"type": "whitespace"}, {"type": "selectableText", "text": "some", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "punctuation", "colors": ["red"], "boxed": false}, {"type": "plainText", "text": "."}]}, {"tokens": [{"type": "selectableText", "text": "And", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "this", "colors": ["red"], "boxed": false}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "selectableText", "text": "is", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "a", "colors": ["red"], "boxed": false}, {"type": "plainText", "text": "..."}, {"type": "whitespace"}, {"type": "selectableText", "text": "lenient", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "paragraph", "colors": ["red"], "boxed": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.LenientParagraphTestCase.test_select_words_without_punctuation.0.wording')
  })
})
