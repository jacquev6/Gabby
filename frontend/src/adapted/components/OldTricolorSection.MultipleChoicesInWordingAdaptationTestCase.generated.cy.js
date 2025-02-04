import TricolorSection from './OldTricolorSection.vue'

describe('TricolorSection for MultipleChoicesInWordingAdaptationTestCase', () => {
  beforeEach(() => {
    cy.viewport(1000, 100)
  })

  it('renders gabby.adaptation.MultipleChoicesInWordingAdaptationTestCase.test_choices2_with_empty_separator pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "Choose"}, {"type": "whitespace"}, {"type": "plainText", "text": "wisely"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInWordingAdaptationTestCase.test_choices2_with_empty_separator.0.instructions')
  })

  it('renders gabby.adaptation.MultipleChoicesInWordingAdaptationTestCase.test_choices2_with_empty_separator pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "A"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["blah / blih"], "show_choices_by_default": false}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInWordingAdaptationTestCase.test_choices2_with_empty_separator.0.wording')
  })

  it('renders gabby.adaptation.MultipleChoicesInWordingAdaptationTestCase.test_choices2_with_empty_start_and_stop pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "A"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["blah", "blih"], "show_choices_by_default": false}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInWordingAdaptationTestCase.test_choices2_with_empty_start_and_stop.0.wording')
  })

  it('renders gabby.adaptation.MultipleChoicesInWordingAdaptationTestCase.test_choices2_with_placeholder_after pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "The"}, {"type": "whitespace"}, {"type": "plainText", "text": "sky"}, {"type": "whitespace"}, {"type": "plainText", "text": "is"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["blue", "red"], "show_choices_by_default": false}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInWordingAdaptationTestCase.test_choices2_with_placeholder_after.0.wording')
  })

  it('renders gabby.adaptation.MultipleChoicesInWordingAdaptationTestCase.test_choices2_with_two_placeholders pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "The"}, {"type": "whitespace"}, {"type": "plainText", "text": "sky"}, {"type": "whitespace"}, {"type": "plainText", "text": "is"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["blue", "yellow"], "show_choices_by_default": false}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "plainText", "text": "the"}, {"type": "whitespace"}, {"type": "plainText", "text": "sun"}, {"type": "whitespace"}, {"type": "plainText", "text": "is"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["blue", "yellow"], "show_choices_by_default": false}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInWordingAdaptationTestCase.test_choices2_with_two_placeholders.0.wording')
  })

  it('renders gabby.adaptation.MultipleChoicesInWordingAdaptationTestCase.test_simple pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "A"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["a", "b", "c"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "plainText", "text": "B"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["d", "e"], "show_choices_by_default": false}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInWordingAdaptationTestCase.test_simple.0.wording')
  })

  it('renders gabby.adaptation.MultipleChoicesInWordingAdaptationTestCase.test_two_choices2_with_identical_placeholders pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "The"}, {"type": "whitespace"}, {"type": "plainText", "text": "sky"}, {"type": "whitespace"}, {"type": "plainText", "text": "is"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["blue", "red"], "show_choices_by_default": false}, {"type": "plainText", "text": "."}]}, {"tokens": [{"type": "plainText", "text": "The"}, {"type": "whitespace"}, {"type": "plainText", "text": "sun"}, {"type": "whitespace"}, {"type": "plainText", "text": "is"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["green", "yellow"], "show_choices_by_default": false}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInWordingAdaptationTestCase.test_two_choices2_with_identical_placeholders.0.wording')
  })

  it('renders gabby.adaptation.MultipleChoicesInWordingAdaptationTestCase.test_two_choices2_with_matching_placeholders pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "The"}, {"type": "whitespace"}, {"type": "plainText", "text": "sky"}, {"type": "whitespace"}, {"type": "plainText", "text": "is"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["blue", "red"], "show_choices_by_default": false}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "plainText", "text": "the"}, {"type": "whitespace"}, {"type": "plainText", "text": "sun"}, {"type": "whitespace"}, {"type": "plainText", "text": "is"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["green", "yellow"], "show_choices_by_default": false}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInWordingAdaptationTestCase.test_two_choices2_with_matching_placeholders.0.wording')
  })
})
