import TricolorSection from './NewTricolorSection.vue'

describe('TricolorSection for MultipleChoicesInWordingAdaptationTestCase', () => {
  beforeEach(() => {
    cy.viewport(1000, 100)
  })

  it('renders gabby.adaptation.MultipleChoicesInWordingAdaptationTestCase.test_choices2_with_empty_separator pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "Choose"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wisely"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInWordingAdaptationTestCase.test_choices2_with_empty_separator.0.instructions')
  })

  it('renders gabby.adaptation.MultipleChoicesInWordingAdaptationTestCase.test_choices2_with_empty_separator pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "A"}, {"kind": "whitespace"}, {"kind": "multipleChoicesInput", "show_arrow_before": false, "choices": [[{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "blah / blih"}]], "show_choices_by_default": false}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInWordingAdaptationTestCase.test_choices2_with_empty_separator.0.wording')
  })

  it('renders gabby.adaptation.MultipleChoicesInWordingAdaptationTestCase.test_choices2_with_empty_start_and_stop pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "A"}, {"kind": "whitespace"}, {"kind": "multipleChoicesInput", "show_arrow_before": false, "choices": [[{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "blah"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "blih"}]], "show_choices_by_default": false}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInWordingAdaptationTestCase.test_choices2_with_empty_start_and_stop.0.wording')
  })

  it('renders gabby.adaptation.MultipleChoicesInWordingAdaptationTestCase.test_choices2_with_placeholder_after pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "The"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "sky"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "is"}, {"kind": "whitespace"}, {"kind": "multipleChoicesInput", "show_arrow_before": false, "choices": [[{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "blue"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "red"}]], "show_choices_by_default": false}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInWordingAdaptationTestCase.test_choices2_with_placeholder_after.0.wording')
  })

  it('renders gabby.adaptation.MultipleChoicesInWordingAdaptationTestCase.test_choices2_with_two_placeholders pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "The"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "sky"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "is"}, {"kind": "whitespace"}, {"kind": "multipleChoicesInput", "show_arrow_before": false, "choices": [[{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "blue"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "yellow"}]], "show_choices_by_default": false}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": ","}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "the"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "sun"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "is"}, {"kind": "whitespace"}, {"kind": "multipleChoicesInput", "show_arrow_before": false, "choices": [[{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "blue"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "yellow"}]], "show_choices_by_default": false}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInWordingAdaptationTestCase.test_choices2_with_two_placeholders.0.wording')
  })

  it('renders gabby.adaptation.MultipleChoicesInWordingAdaptationTestCase.test_simple pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "A"}, {"kind": "whitespace"}, {"kind": "multipleChoicesInput", "show_arrow_before": false, "choices": [[{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "a"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "b"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "c"}]], "show_choices_by_default": false}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "B"}, {"kind": "whitespace"}, {"kind": "multipleChoicesInput", "show_arrow_before": false, "choices": [[{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "d"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "e"}]], "show_choices_by_default": false}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInWordingAdaptationTestCase.test_simple.0.wording')
  })

  it('renders gabby.adaptation.MultipleChoicesInWordingAdaptationTestCase.test_two_choices2_with_identical_placeholders pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "The"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "sky"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "is"}, {"kind": "whitespace"}, {"kind": "multipleChoicesInput", "show_arrow_before": false, "choices": [[{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "blue"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "red"}]], "show_choices_by_default": false}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "The"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "sun"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "is"}, {"kind": "whitespace"}, {"kind": "multipleChoicesInput", "show_arrow_before": false, "choices": [[{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "green"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "yellow"}]], "show_choices_by_default": false}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInWordingAdaptationTestCase.test_two_choices2_with_identical_placeholders.0.wording')
  })

  it('renders gabby.adaptation.MultipleChoicesInWordingAdaptationTestCase.test_two_choices2_with_matching_placeholders pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "The"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "sky"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "is"}, {"kind": "whitespace"}, {"kind": "multipleChoicesInput", "show_arrow_before": false, "choices": [[{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "blue"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "red"}]], "show_choices_by_default": false}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": ","}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "the"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "sun"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "is"}, {"kind": "whitespace"}, {"kind": "multipleChoicesInput", "show_arrow_before": false, "choices": [[{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "green"}], [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "yellow"}]], "show_choices_by_default": false}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.MultipleChoicesInWordingAdaptationTestCase.test_two_choices2_with_matching_placeholders.0.wording')
  })
})
