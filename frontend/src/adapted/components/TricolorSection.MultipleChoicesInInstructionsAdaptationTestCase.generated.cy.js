import TricolorSection from './TricolorSection.vue'

describe('TricolorSection for MultipleChoicesInInstructionsAdaptationTestCase', () => {
  beforeEach(() => {
    cy.viewport(1000, 100)
  })

  it('renders gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2 pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "Choose"}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "a"}], "boxed": true}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "ou"}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "b"}], "boxed": true}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2.0.instructions')
  })

  it('renders gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2 pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "A"}, {"kind": "whitespace"}, {"kind": "multipleChoicesInput", "show_arrow_before": false, "choices": [[{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "a"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "b"}]], "show_choices_by_default": false}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "B"}, {"kind": "whitespace"}, {"kind": "multipleChoicesInput", "show_arrow_before": false, "choices": [[{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "a"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "b"}]], "show_choices_by_default": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2.0.wording')
  })

  it('renders gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_empty_separator pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "Choose"}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "a b"}], "boxed": true}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_empty_separator.0.instructions')
  })

  it('renders gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_empty_separator pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "A"}, {"kind": "whitespace"}, {"kind": "multipleChoicesInput", "show_arrow_before": false, "choices": [[{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "a b"}]], "show_choices_by_default": false}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "B"}, {"kind": "whitespace"}, {"kind": "multipleChoicesInput", "show_arrow_before": false, "choices": [[{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "a b"}]], "show_choices_by_default": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_empty_separator.0.wording')
  })

  it('renders gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_oxford_comma pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "Choose"}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "a"}], "boxed": true}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": ","}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "b"}], "boxed": true}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": ","}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "c"}], "boxed": true}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "ou"}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "d"}], "boxed": true}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_oxford_comma.0.instructions')
  })

  it('renders gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_oxford_comma pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "A"}, {"kind": "whitespace"}, {"kind": "multipleChoicesInput", "show_arrow_before": false, "choices": [[{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "a"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "b"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "c"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "d"}]], "show_choices_by_default": false}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "B"}, {"kind": "whitespace"}, {"kind": "multipleChoicesInput", "show_arrow_before": false, "choices": [[{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "a"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "b"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "c"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "d"}]], "show_choices_by_default": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_oxford_comma.0.wording')
  })

  it('renders gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_successive_separators pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "Choose"}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "a"}], "boxed": true}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": ","}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "b"}], "boxed": true}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "ou"}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "c"}], "boxed": true}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_successive_separators.0.instructions')
  })

  it('renders gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_successive_separators pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "A"}, {"kind": "whitespace"}, {"kind": "multipleChoicesInput", "show_arrow_before": false, "choices": [[{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "a"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "b"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "c"}]], "show_choices_by_default": false}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "B"}, {"kind": "whitespace"}, {"kind": "multipleChoicesInput", "show_arrow_before": false, "choices": [[{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "a"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "b"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "c"}]], "show_choices_by_default": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_successive_separators.0.wording')
  })

  it('renders gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_chose_a_single_letter_to_complete_a_word pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "Compl\u00e8te"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "les"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "mots"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "avec"}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "m"}], "boxed": true}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "ou"}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "n"}], "boxed": true}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_chose_a_single_letter_to_complete_a_word.0.instructions')
  })

  it('renders gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_chose_a_single_letter_to_complete_a_word pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "i"}, {"kind": "multipleChoicesInput", "show_arrow_before": false, "choices": [[{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "m"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "n"}]], "show_choices_by_default": false}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "mense"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "i"}, {"kind": "multipleChoicesInput", "show_arrow_before": false, "choices": [[{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "m"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "n"}]], "show_choices_by_default": false}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "juste"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_chose_a_single_letter_to_complete_a_word.0.wording')
  })

  it('renders gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_example_and_clue pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "Choose"}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "a"}], "boxed": true}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "ou"}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "b"}], "boxed": true}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "This"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "{"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "choices2"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "|"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "|"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "/"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "|"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "|"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "|"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "|"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "is"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "}"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "the"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "@"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "example"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "This"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "is"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "{"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "choices2"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "|"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "|"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "/"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "|"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "|"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "|"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "|"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "the"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "}"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "@"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "clue"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_example_and_clue.0.instructions')
  })

  it('renders gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_two_choices2 pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "Choose"}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "a"}], "boxed": true}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "ou"}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "b"}], "boxed": true}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "and"}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "c"}], "boxed": true}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "ou"}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "d"}], "boxed": true}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_two_choices2.0.instructions')
  })

  it('renders gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_two_choices2 pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "A"}, {"kind": "whitespace"}, {"kind": "multipleChoicesInput", "show_arrow_before": false, "choices": [[{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "a"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "b"}]], "show_choices_by_default": false}, {"kind": "whitespace"}, {"kind": "multipleChoicesInput", "show_arrow_before": false, "choices": [[{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "c"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "d"}]], "show_choices_by_default": false}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "B"}, {"kind": "whitespace"}, {"kind": "multipleChoicesInput", "show_arrow_before": false, "choices": [[{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "a"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "b"}]], "show_choices_by_default": false}, {"kind": "whitespace"}, {"kind": "multipleChoicesInput", "show_arrow_before": false, "choices": [[{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "c"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "d"}]], "show_choices_by_default": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInInstructionsAdaptationTestCase.test_two_choices2.0.wording')
  })
})
