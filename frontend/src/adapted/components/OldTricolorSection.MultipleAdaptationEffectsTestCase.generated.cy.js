import TricolorSection from './OldTricolorSection.vue'

describe('TricolorSection for MultipleAdaptationEffectsTestCase', () => {
  beforeEach(() => {
    cy.viewport(1000, 100)
  })

  it('renders gabby.adaptation.MultipleAdaptationEffectsTestCase.test_fill_with_free_text_and_multiple_choices_in_instructions pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "instructions"}, {"type": "whitespace"}, {"type": "boxedText", "text": "short"}, {"type": "whitespace"}, {"type": "plainText", "text": "ou"}, {"type": "whitespace"}, {"type": "boxedText", "text": "long"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleAdaptationEffectsTestCase.test_fill_with_free_text_and_multiple_choices_in_instructions.0.instructions')
  })

  it('renders gabby.adaptation.MultipleAdaptationEffectsTestCase.test_fill_with_free_text_and_multiple_choices_in_instructions pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "The"}, {"type": "whitespace"}, {"type": "plainText", "text": "wording"}, {"type": "whitespace"}, {"type": "plainText", "text": "of"}, {"type": "whitespace"}, {"type": "plainText", "text": "this"}, {"type": "whitespace"}, {"type": "freeTextInput"}, {"type": "whitespace"}, {"type": "plainText", "text": "is"}, {"type": "whitespace"}, {"type": "plainText", "text": "a"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["short", "long"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "plainText", "text": "sentence"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleAdaptationEffectsTestCase.test_fill_with_free_text_and_multiple_choices_in_instructions.0.wording')
  })

  it('renders gabby.adaptation.MultipleAdaptationEffectsTestCase.test_many_adaptations_in_same_exercise pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "Choose"}, {"type": "whitespace"}, {"type": "plainText", "text": "wisely"}, {"type": "whitespace"}, {"type": "boxedText", "text": "alpha"}, {"type": "whitespace"}, {"type": "plainText", "text": "ou"}, {"type": "whitespace"}, {"type": "boxedText", "text": "bravo"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleAdaptationEffectsTestCase.test_many_adaptations_in_same_exercise.0.instructions')
  })

  it('renders gabby.adaptation.MultipleAdaptationEffectsTestCase.test_many_adaptations_in_same_exercise pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "selectableText", "text": "Hello", "colors": ["red", "yellow"], "boxed": true}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["charlie", "delta"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "freeTextInput"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleAdaptationEffectsTestCase.test_many_adaptations_in_same_exercise.0.wording')
  })

  it('renders gabby.adaptation.MultipleAdaptationEffectsTestCase.test_multiple_choices_in_instructions_and_wording pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "Choose"}, {"type": "whitespace"}, {"type": "plainText", "text": "wisely"}, {"type": "whitespace"}, {"type": "boxedText", "text": "alpha"}, {"type": "whitespace"}, {"type": "plainText", "text": "ou"}, {"type": "whitespace"}, {"type": "boxedText", "text": "bravo"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleAdaptationEffectsTestCase.test_multiple_choices_in_instructions_and_wording.0.instructions')
  })

  it('renders gabby.adaptation.MultipleAdaptationEffectsTestCase.test_multiple_choices_in_instructions_and_wording pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "A"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["a", "b", "c"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "plainText", "text": "B"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["d", "e"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "plainText", "text": "C"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo"], "show_choices_by_default": false}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleAdaptationEffectsTestCase.test_multiple_choices_in_instructions_and_wording.0.wording')
  })
})
