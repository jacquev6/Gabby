import TricolorSection from './TricolorSection.vue'

describe('TricolorSection for MultipleAdaptationEffectsTestCase', () => {
  beforeEach(() => {
    cy.viewport(1000, 100)
  })

  it('renders gabby.adaptation.multiple_adaptation_effects_tests.MultipleAdaptationEffectsTestCase.test_fill_with_free_text_and_multiple_choices_in_instructions pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "instructions"}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "short"}], "boxed": true}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "ou"}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "long"}], "boxed": true}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.multiple_adaptation_effects_tests.MultipleAdaptationEffectsTestCase.test_fill_with_free_text_and_multiple_choices_in_instructions.0.instructions')
  })

  it('renders gabby.adaptation.multiple_adaptation_effects_tests.MultipleAdaptationEffectsTestCase.test_fill_with_free_text_and_multiple_choices_in_instructions pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "The"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wording"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "of"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "this"}, {"kind": "whitespace"}, {"kind": "freeTextInput"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "is"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "a"}, {"kind": "whitespace"}, {"kind": "multipleChoicesInput", "show_arrow_before": false, "choices": [[{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "short"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "long"}]], "show_choices_by_default": false}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "sentence"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.multiple_adaptation_effects_tests.MultipleAdaptationEffectsTestCase.test_fill_with_free_text_and_multiple_choices_in_instructions.0.wording')
  })

  it('renders gabby.adaptation.multiple_adaptation_effects_tests.MultipleAdaptationEffectsTestCase.test_many_adaptations_in_same_exercise pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "Choose"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wisely"}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "alpha"}], "boxed": true}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "ou"}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "bravo"}], "boxed": true}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.multiple_adaptation_effects_tests.MultipleAdaptationEffectsTestCase.test_many_adaptations_in_same_exercise.0.instructions')
  })

  it('renders gabby.adaptation.multiple_adaptation_effects_tests.MultipleAdaptationEffectsTestCase.test_many_adaptations_in_same_exercise pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "selectableInput", "colors": ["red", "yellow"], "boxed": true, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "Hello"}]}, {"kind": "whitespace"}, {"kind": "multipleChoicesInput", "show_arrow_before": false, "choices": [[{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "alpha"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "bravo"}]], "show_choices_by_default": false}, {"kind": "whitespace"}, {"kind": "multipleChoicesInput", "show_arrow_before": false, "choices": [[{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "charlie"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "delta"}]], "show_choices_by_default": false}, {"kind": "whitespace"}, {"kind": "freeTextInput"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.multiple_adaptation_effects_tests.MultipleAdaptationEffectsTestCase.test_many_adaptations_in_same_exercise.0.wording')
  })

  it('renders gabby.adaptation.multiple_adaptation_effects_tests.MultipleAdaptationEffectsTestCase.test_multiple_choices_in_instructions_and_wording pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "Choose"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wisely"}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "alpha"}], "boxed": true}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "ou"}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "bravo"}], "boxed": true}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.multiple_adaptation_effects_tests.MultipleAdaptationEffectsTestCase.test_multiple_choices_in_instructions_and_wording.0.instructions')
  })

  it('renders gabby.adaptation.multiple_adaptation_effects_tests.MultipleAdaptationEffectsTestCase.test_multiple_choices_in_instructions_and_wording pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "A"}, {"kind": "whitespace"}, {"kind": "multipleChoicesInput", "show_arrow_before": false, "choices": [[{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "a"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "b"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "c"}]], "show_choices_by_default": false}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "B"}, {"kind": "whitespace"}, {"kind": "multipleChoicesInput", "show_arrow_before": false, "choices": [[{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "d"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "e"}]], "show_choices_by_default": false}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "C"}, {"kind": "whitespace"}, {"kind": "multipleChoicesInput", "show_arrow_before": false, "choices": [[{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "alpha"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "bravo"}]], "show_choices_by_default": false}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.multiple_adaptation_effects_tests.MultipleAdaptationEffectsTestCase.test_multiple_choices_in_instructions_and_wording.0.wording')
  })
})
