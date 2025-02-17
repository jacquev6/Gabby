import TricolorSection from './TricolorSection.vue'

describe('TricolorSection for SelectThingsAdaptationTestCase', () => {
  beforeEach(() => {
    cy.viewport(1000, 100)
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_example_and_clue pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "instructions"}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "This"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "is"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "the"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "example"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "This"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "is"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "the"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "clue"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_example_and_clue.0.instructions')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_example_and_clue pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wording"}]}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_example_and_clue.0.wording')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_example_and_clue_with_sel_tags pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "instructions"}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": "red", "text": "abc"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": "green", "text": "def"}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": "blue", "text": "ghi"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "jkl"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_example_and_clue_with_sel_tags.0.instructions')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_example_and_clue_with_sel_tags pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "selectableInput", "colors": ["red", "green", "blue"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wording"}]}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_example_and_clue_with_sel_tags.0.wording')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_french_elision_of_articles__punctuation_only pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "Selectionne"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "les"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "articles"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_french_elision_of_articles__punctuation_only.0.instructions')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_french_elision_of_articles__punctuation_only pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "La"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "maison"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "est"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "belle"}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "L"}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "'"}]}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "\u00e9cole"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "est"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "ferm\u00e9e"}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "L"}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "\u2019"}]}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "automobile"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "est"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "verte"}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_french_elision_of_articles__punctuation_only.0.wording')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_french_elision_of_articles__punctuation_only__boxed_only pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "La"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "maison"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "est"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "belle"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}], "boxed": true}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "L"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "'"}], "boxed": true}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "\u00e9cole"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "est"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "ferm\u00e9e"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}], "boxed": true}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "L"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "\u2019"}], "boxed": true}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "automobile"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "est"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "verte"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}], "boxed": true}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_french_elision_of_articles__punctuation_only__boxed_only.0.wording')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_french_elision_of_articles__with_punctuation pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "La"}]}, {"kind": "whitespace"}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "maison"}]}, {"kind": "whitespace"}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "est"}]}, {"kind": "whitespace"}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "belle"}]}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}, {"kind": "whitespace"}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "L"}]}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "'"}]}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "\u00e9cole"}]}, {"kind": "whitespace"}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "est"}]}, {"kind": "whitespace"}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "ferm\u00e9e"}]}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}, {"kind": "whitespace"}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "L"}]}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "\u2019"}]}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "automobile"}]}, {"kind": "whitespace"}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "est"}]}, {"kind": "whitespace"}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "verte"}]}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_french_elision_of_articles__with_punctuation.0.wording')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_french_elision_of_articles__with_punctuation__boxed_only pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "La"}], "boxed": true}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "maison"}], "boxed": true}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "est"}], "boxed": true}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "belle"}], "boxed": true}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}], "boxed": true}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "L"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "'"}], "boxed": true}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "\u00e9cole"}], "boxed": true}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "est"}], "boxed": true}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "ferm\u00e9e"}], "boxed": true}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}], "boxed": true}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "L"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "\u2019"}], "boxed": true}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "automobile"}], "boxed": true}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "est"}], "boxed": true}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "verte"}], "boxed": true}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}], "boxed": true}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_french_elision_of_articles__with_punctuation__boxed_only.0.wording')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_french_elision_of_articles__without_punctuation pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "La"}]}, {"kind": "whitespace"}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "maison"}]}, {"kind": "whitespace"}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "est"}]}, {"kind": "whitespace"}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "belle"}]}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}, {"kind": "whitespace"}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "L"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "'"}]}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "\u00e9cole"}]}, {"kind": "whitespace"}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "est"}]}, {"kind": "whitespace"}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "ferm\u00e9e"}]}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}, {"kind": "whitespace"}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "L"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "\u2019"}]}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "automobile"}]}, {"kind": "whitespace"}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "est"}]}, {"kind": "whitespace"}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "verte"}]}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_french_elision_of_articles__without_punctuation.0.wording')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_french_elision_of_articles__without_punctuation__boxed_only pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "La"}], "boxed": true}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "maison"}], "boxed": true}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "est"}], "boxed": true}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "belle"}], "boxed": true}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "L"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "'"}], "boxed": true}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "\u00e9cole"}], "boxed": true}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "est"}], "boxed": true}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "ferm\u00e9e"}], "boxed": true}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "L"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "\u2019"}], "boxed": true}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "automobile"}], "boxed": true}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "est"}], "boxed": true}, {"kind": "whitespace"}, {"kind": "passiveSequence", "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "verte"}], "boxed": true}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_french_elision_of_articles__without_punctuation__boxed_only.0.wording')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_multiple_lines_in_instructions pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "instructions"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "are"}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "on"}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "multiple"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "lines"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_multiple_lines_in_instructions.0.instructions')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_multiple_lines_in_wording pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "instructions"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_multiple_lines_in_wording.0.instructions')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_multiple_lines_in_wording pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wording"}]}, {"kind": "whitespace"}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "is"}]}]}, {"contents": [{"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "on"}]}]}, {"contents": [{"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "multiple"}]}, {"kind": "whitespace"}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "lines"}]}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_multiple_lines_in_wording.0.wording')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_sel_tags pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": "red", "text": "abc"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": "green", "text": "def"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": "blue", "text": "ghi"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "jkl"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_sel_tags.0.instructions')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_single_color pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": "red", "text": "abc"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_single_color.0.instructions')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_single_sentence pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "selectableInput", "colors": ["red", "blue"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "The"}]}, {"kind": "whitespace"}, {"kind": "selectableInput", "colors": ["red", "blue"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wording"}]}, {"kind": "whitespace"}, {"kind": "selectableInput", "colors": ["red", "blue"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "of"}]}, {"kind": "whitespace"}, {"kind": "selectableInput", "colors": ["red", "blue"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "this"}]}, {"kind": "whitespace"}, {"kind": "selectableInput", "colors": ["red", "blue"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "exercise"}]}, {"kind": "whitespace"}, {"kind": "selectableInput", "colors": ["red", "blue"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "is"}]}, {"kind": "whitespace"}, {"kind": "selectableInput", "colors": ["red", "blue"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "a"}]}, {"kind": "whitespace"}, {"kind": "selectableInput", "colors": ["red", "blue"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "single"}]}, {"kind": "whitespace"}, {"kind": "selectableInput", "colors": ["red", "blue"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "sentence"}]}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_single_sentence.0.wording')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_strip_whitespace pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "abc"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_strip_whitespace.0.instructions')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_strip_whitespace pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "def"}]}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_strip_whitespace.0.wording')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_unknown_tags pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "{"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "tag"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "|"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "abc"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "}"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_unknown_tags.0.instructions')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_unknown_tags pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "{"}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "tag"}]}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "|"}, {"kind": "selectableInput", "colors": ["red"], "boxed": false, "contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "def"}]}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "}"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_unknown_tags.0.wording')
  })
})
