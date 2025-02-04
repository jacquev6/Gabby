import TricolorSection from './OldTricolorSection.vue'

describe('TricolorSection for MultipleChoicesInInstructionsAdaptationTestCase', () => {
  beforeEach(() => {
    cy.viewport(1000, 100)
  })

  it('renders gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2 pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "Choose"}, {"type": "whitespace"}, {"type": "boxedText", "text": "a"}, {"type": "whitespace"}, {"type": "plainText", "text": "ou"}, {"type": "whitespace"}, {"type": "boxedText", "text": "b"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2.0.instructions')
  })

  it('renders gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2 pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "A"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["a", "b"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "plainText", "text": "B"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["a", "b"], "show_choices_by_default": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2.0.wording')
  })

  it('renders gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_empty_separator pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "Choose"}, {"type": "whitespace"}, {"type": "boxedText", "text": "a b"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_empty_separator.0.instructions')
  })

  it('renders gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_empty_separator pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "A"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["a b"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "plainText", "text": "B"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["a b"], "show_choices_by_default": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_empty_separator.0.wording')
  })

  it('renders gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_oxford_comma pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "Choose"}, {"type": "whitespace"}, {"type": "boxedText", "text": "a"}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "boxedText", "text": "b"}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "boxedText", "text": "c"}, {"type": "whitespace"}, {"type": "plainText", "text": "ou"}, {"type": "whitespace"}, {"type": "boxedText", "text": "d"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_oxford_comma.0.instructions')
  })

  it('renders gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_oxford_comma pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "A"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["a", "b", "c", "d"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "plainText", "text": "B"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["a", "b", "c", "d"], "show_choices_by_default": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_oxford_comma.0.wording')
  })

  it('renders gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_successive_separators pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "Choose"}, {"type": "whitespace"}, {"type": "boxedText", "text": "a"}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "boxedText", "text": "b"}, {"type": "whitespace"}, {"type": "plainText", "text": "ou"}, {"type": "whitespace"}, {"type": "boxedText", "text": "c"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_successive_separators.0.instructions')
  })

  it('renders gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_successive_separators pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "A"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["a", "b", "c"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "plainText", "text": "B"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["a", "b", "c"], "show_choices_by_default": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_successive_separators.0.wording')
  })

  it('renders gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_chose_a_single_letter_to_complete_a_word pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "Compl\u00e8te"}, {"type": "whitespace"}, {"type": "plainText", "text": "les"}, {"type": "whitespace"}, {"type": "plainText", "text": "mots"}, {"type": "whitespace"}, {"type": "plainText", "text": "avec"}, {"type": "whitespace"}, {"type": "boxedText", "text": "m"}, {"type": "whitespace"}, {"type": "plainText", "text": "ou"}, {"type": "whitespace"}, {"type": "boxedText", "text": "n"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_chose_a_single_letter_to_complete_a_word.0.instructions')
  })

  it('renders gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_chose_a_single_letter_to_complete_a_word pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "i"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["m", "n"], "show_choices_by_default": false}, {"type": "plainText", "text": "mense"}, {"type": "whitespace"}, {"type": "plainText", "text": "i"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["m", "n"], "show_choices_by_default": false}, {"type": "plainText", "text": "juste"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_chose_a_single_letter_to_complete_a_word.0.wording')
  })

  it('renders gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_example_and_clue pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "Choose"}, {"type": "whitespace"}, {"type": "boxedText", "text": "a"}, {"type": "whitespace"}, {"type": "plainText", "text": "ou"}, {"type": "whitespace"}, {"type": "boxedText", "text": "b"}, {"type": "plainText", "text": "."}]}, {"tokens": [{"type": "plainText", "text": "This"}, {"type": "whitespace"}, {"type": "plainText", "text": "{"}, {"type": "plainText", "text": "choices2"}, {"type": "plainText", "text": "|"}, {"type": "plainText", "text": "|"}, {"type": "plainText", "text": "/"}, {"type": "plainText", "text": "|"}, {"type": "plainText", "text": "|"}, {"type": "plainText", "text": "|"}, {"type": "plainText", "text": "|"}, {"type": "plainText", "text": "is"}, {"type": "plainText", "text": "}"}, {"type": "whitespace"}, {"type": "plainText", "text": "the"}, {"type": "whitespace"}, {"type": "plainText", "text": "@"}, {"type": "whitespace"}, {"type": "plainText", "text": "example"}, {"type": "plainText", "text": "."}]}, {"tokens": [{"type": "plainText", "text": "This"}, {"type": "whitespace"}, {"type": "plainText", "text": "is"}, {"type": "whitespace"}, {"type": "plainText", "text": "{"}, {"type": "plainText", "text": "choices2"}, {"type": "plainText", "text": "|"}, {"type": "plainText", "text": "|"}, {"type": "plainText", "text": "/"}, {"type": "plainText", "text": "|"}, {"type": "plainText", "text": "|"}, {"type": "plainText", "text": "|"}, {"type": "plainText", "text": "|"}, {"type": "plainText", "text": "the"}, {"type": "plainText", "text": "}"}, {"type": "whitespace"}, {"type": "plainText", "text": "@"}, {"type": "whitespace"}, {"type": "plainText", "text": "clue"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_example_and_clue.0.instructions')
  })

  it('renders gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_two_choices2 pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "Choose"}, {"type": "whitespace"}, {"type": "boxedText", "text": "a"}, {"type": "whitespace"}, {"type": "plainText", "text": "ou"}, {"type": "whitespace"}, {"type": "boxedText", "text": "b"}, {"type": "whitespace"}, {"type": "plainText", "text": "and"}, {"type": "whitespace"}, {"type": "boxedText", "text": "c"}, {"type": "whitespace"}, {"type": "plainText", "text": "ou"}, {"type": "whitespace"}, {"type": "boxedText", "text": "d"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_two_choices2.0.instructions')
  })

  it('renders gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_two_choices2 pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "A"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["a", "b"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["c", "d"], "show_choices_by_default": false}]}, {"tokens": [{"type": "plainText", "text": "B"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["a", "b"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["c", "d"], "show_choices_by_default": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_two_choices2.0.wording')
  })
})
