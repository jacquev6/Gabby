import TricolorSection from './OldTricolorSection.vue'

describe('TricolorSection for SelectThingsAdaptationTestCase', () => {
  beforeEach(() => {
    cy.viewport(1000, 100)
  })

  it('renders gabby.adaptation.SelectThingsAdaptationTestCase.test_example_and_clue pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "instructions"}]}, {"tokens": [{"type": "plainText", "text": "This"}, {"type": "whitespace"}, {"type": "plainText", "text": "is"}, {"type": "whitespace"}, {"type": "plainText", "text": "the"}, {"type": "whitespace"}, {"type": "plainText", "text": "example"}, {"type": "plainText", "text": "."}]}, {"tokens": [{"type": "plainText", "text": "This"}, {"type": "whitespace"}, {"type": "plainText", "text": "is"}, {"type": "whitespace"}, {"type": "plainText", "text": "the"}, {"type": "whitespace"}, {"type": "plainText", "text": "clue"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.SelectThingsAdaptationTestCase.test_example_and_clue.0.instructions')
  })

  it('renders gabby.adaptation.SelectThingsAdaptationTestCase.test_example_and_clue pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "selectableText", "text": "wording", "colors": ["red"], "boxed": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.SelectThingsAdaptationTestCase.test_example_and_clue.0.wording')
  })

  it('renders gabby.adaptation.SelectThingsAdaptationTestCase.test_example_and_clue_with_sel_tags pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "instructions"}]}, {"tokens": [{"type": "selectedText", "text": "abc", "color": "red"}, {"type": "whitespace"}, {"type": "selectedText", "text": "def", "color": "green"}]}, {"tokens": [{"type": "selectedText", "text": "ghi", "color": "blue"}, {"type": "whitespace"}, {"type": "plainText", "text": "jkl"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.SelectThingsAdaptationTestCase.test_example_and_clue_with_sel_tags.0.instructions')
  })

  it('renders gabby.adaptation.SelectThingsAdaptationTestCase.test_example_and_clue_with_sel_tags pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "selectableText", "text": "wording", "colors": ["red", "green", "blue"], "boxed": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.SelectThingsAdaptationTestCase.test_example_and_clue_with_sel_tags.0.wording')
  })

  it('renders gabby.adaptation.SelectThingsAdaptationTestCase.test_french_elision_of_articles__punctuation_only pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "Selectionne"}, {"type": "whitespace"}, {"type": "plainText", "text": "les"}, {"type": "whitespace"}, {"type": "plainText", "text": "articles"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.SelectThingsAdaptationTestCase.test_french_elision_of_articles__punctuation_only.0.instructions')
  })

  it('renders gabby.adaptation.SelectThingsAdaptationTestCase.test_french_elision_of_articles__punctuation_only pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "La"}, {"type": "whitespace"}, {"type": "plainText", "text": "maison"}, {"type": "whitespace"}, {"type": "plainText", "text": "est"}, {"type": "whitespace"}, {"type": "plainText", "text": "belle"}, {"type": "selectableText", "text": ".", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "plainText", "text": "L"}, {"type": "selectableText", "text": "'", "colors": ["red"], "boxed": false}, {"type": "plainText", "text": "\u00e9cole"}, {"type": "whitespace"}, {"type": "plainText", "text": "est"}, {"type": "whitespace"}, {"type": "plainText", "text": "ferm\u00e9e"}, {"type": "selectableText", "text": ".", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "plainText", "text": "L"}, {"type": "selectableText", "text": "\u2019", "colors": ["red"], "boxed": false}, {"type": "plainText", "text": "automobile"}, {"type": "whitespace"}, {"type": "plainText", "text": "est"}, {"type": "whitespace"}, {"type": "plainText", "text": "verte"}, {"type": "selectableText", "text": ".", "colors": ["red"], "boxed": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.SelectThingsAdaptationTestCase.test_french_elision_of_articles__punctuation_only.0.wording')
  })

  it('renders gabby.adaptation.SelectThingsAdaptationTestCase.test_french_elision_of_articles__punctuation_only__boxed_only pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "La"}, {"type": "whitespace"}, {"type": "plainText", "text": "maison"}, {"type": "whitespace"}, {"type": "plainText", "text": "est"}, {"type": "whitespace"}, {"type": "plainText", "text": "belle"}, {"type": "boxedText", "text": "."}, {"type": "whitespace"}, {"type": "plainText", "text": "L"}, {"type": "boxedText", "text": "'"}, {"type": "plainText", "text": "\u00e9cole"}, {"type": "whitespace"}, {"type": "plainText", "text": "est"}, {"type": "whitespace"}, {"type": "plainText", "text": "ferm\u00e9e"}, {"type": "boxedText", "text": "."}, {"type": "whitespace"}, {"type": "plainText", "text": "L"}, {"type": "boxedText", "text": "\u2019"}, {"type": "plainText", "text": "automobile"}, {"type": "whitespace"}, {"type": "plainText", "text": "est"}, {"type": "whitespace"}, {"type": "plainText", "text": "verte"}, {"type": "boxedText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.SelectThingsAdaptationTestCase.test_french_elision_of_articles__punctuation_only__boxed_only.0.wording')
  })

  it('renders gabby.adaptation.SelectThingsAdaptationTestCase.test_french_elision_of_articles__with_punctuation pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "selectableText", "text": "La", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "maison", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "est", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "belle", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": ".", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "L'", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": "\u00e9cole", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "est", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "ferm\u00e9e", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": ".", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "L\u2019", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": "automobile", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "est", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "verte", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": ".", "colors": ["red"], "boxed": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.SelectThingsAdaptationTestCase.test_french_elision_of_articles__with_punctuation.0.wording')
  })

  it('renders gabby.adaptation.SelectThingsAdaptationTestCase.test_french_elision_of_articles__with_punctuation__boxed_only pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "boxedText", "text": "La"}, {"type": "whitespace"}, {"type": "boxedText", "text": "maison"}, {"type": "whitespace"}, {"type": "boxedText", "text": "est"}, {"type": "whitespace"}, {"type": "boxedText", "text": "belle"}, {"type": "boxedText", "text": "."}, {"type": "whitespace"}, {"type": "boxedText", "text": "L'"}, {"type": "boxedText", "text": "\u00e9cole"}, {"type": "whitespace"}, {"type": "boxedText", "text": "est"}, {"type": "whitespace"}, {"type": "boxedText", "text": "ferm\u00e9e"}, {"type": "boxedText", "text": "."}, {"type": "whitespace"}, {"type": "boxedText", "text": "L\u2019"}, {"type": "boxedText", "text": "automobile"}, {"type": "whitespace"}, {"type": "boxedText", "text": "est"}, {"type": "whitespace"}, {"type": "boxedText", "text": "verte"}, {"type": "boxedText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.SelectThingsAdaptationTestCase.test_french_elision_of_articles__with_punctuation__boxed_only.0.wording')
  })

  it('renders gabby.adaptation.SelectThingsAdaptationTestCase.test_french_elision_of_articles__without_punctuation pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "selectableText", "text": "La", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "maison", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "est", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "belle", "colors": ["red"], "boxed": false}, {"type": "plainText", "text": "."}, {"type": "whitespace"}, {"type": "selectableText", "text": "L'", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": "\u00e9cole", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "est", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "ferm\u00e9e", "colors": ["red"], "boxed": false}, {"type": "plainText", "text": "."}, {"type": "whitespace"}, {"type": "selectableText", "text": "L\u2019", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": "automobile", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "est", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "verte", "colors": ["red"], "boxed": false}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.SelectThingsAdaptationTestCase.test_french_elision_of_articles__without_punctuation.0.wording')
  })

  it('renders gabby.adaptation.SelectThingsAdaptationTestCase.test_french_elision_of_articles__without_punctuation__boxed_only pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "boxedText", "text": "La"}, {"type": "whitespace"}, {"type": "boxedText", "text": "maison"}, {"type": "whitespace"}, {"type": "boxedText", "text": "est"}, {"type": "whitespace"}, {"type": "boxedText", "text": "belle"}, {"type": "plainText", "text": "."}, {"type": "whitespace"}, {"type": "boxedText", "text": "L'"}, {"type": "boxedText", "text": "\u00e9cole"}, {"type": "whitespace"}, {"type": "boxedText", "text": "est"}, {"type": "whitespace"}, {"type": "boxedText", "text": "ferm\u00e9e"}, {"type": "plainText", "text": "."}, {"type": "whitespace"}, {"type": "boxedText", "text": "L\u2019"}, {"type": "boxedText", "text": "automobile"}, {"type": "whitespace"}, {"type": "boxedText", "text": "est"}, {"type": "whitespace"}, {"type": "boxedText", "text": "verte"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.SelectThingsAdaptationTestCase.test_french_elision_of_articles__without_punctuation__boxed_only.0.wording')
  })

  it('renders gabby.adaptation.SelectThingsAdaptationTestCase.test_multiple_lines_in_instructions pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "instructions"}, {"type": "whitespace"}, {"type": "plainText", "text": "are"}]}, {"tokens": [{"type": "plainText", "text": "on"}]}, {"tokens": [{"type": "plainText", "text": "multiple"}, {"type": "whitespace"}, {"type": "plainText", "text": "lines"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.SelectThingsAdaptationTestCase.test_multiple_lines_in_instructions.0.instructions')
  })

  it('renders gabby.adaptation.SelectThingsAdaptationTestCase.test_multiple_lines_in_wording pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "instructions"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.SelectThingsAdaptationTestCase.test_multiple_lines_in_wording.0.instructions')
  })

  it('renders gabby.adaptation.SelectThingsAdaptationTestCase.test_multiple_lines_in_wording pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "selectableText", "text": "wording", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "is", "colors": ["red"], "boxed": false}]}, {"tokens": [{"type": "selectableText", "text": "on", "colors": ["red"], "boxed": false}]}, {"tokens": [{"type": "selectableText", "text": "multiple", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "lines", "colors": ["red"], "boxed": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.SelectThingsAdaptationTestCase.test_multiple_lines_in_wording.0.wording')
  })

  it('renders gabby.adaptation.SelectThingsAdaptationTestCase.test_sel_tags pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "selectedText", "text": "abc", "color": "red"}, {"type": "whitespace"}, {"type": "selectedText", "text": "def", "color": "green"}, {"type": "whitespace"}, {"type": "selectedText", "text": "ghi", "color": "blue"}, {"type": "whitespace"}, {"type": "plainText", "text": "jkl"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.SelectThingsAdaptationTestCase.test_sel_tags.0.instructions')
  })

  it('renders gabby.adaptation.SelectThingsAdaptationTestCase.test_single_color pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "selectedText", "text": "abc", "color": "red"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.SelectThingsAdaptationTestCase.test_single_color.0.instructions')
  })

  it('renders gabby.adaptation.SelectThingsAdaptationTestCase.test_single_sentence pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "selectableText", "text": "The", "colors": ["red", "blue"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "wording", "colors": ["red", "blue"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "of", "colors": ["red", "blue"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "this", "colors": ["red", "blue"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "exercise", "colors": ["red", "blue"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "is", "colors": ["red", "blue"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "a", "colors": ["red", "blue"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "single", "colors": ["red", "blue"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "sentence", "colors": ["red", "blue"], "boxed": false}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.SelectThingsAdaptationTestCase.test_single_sentence.0.wording')
  })

  it('renders gabby.adaptation.SelectThingsAdaptationTestCase.test_strip_whitespace pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "abc"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.SelectThingsAdaptationTestCase.test_strip_whitespace.0.instructions')
  })

  it('renders gabby.adaptation.SelectThingsAdaptationTestCase.test_strip_whitespace pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "selectableText", "text": "def", "colors": ["red"], "boxed": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.SelectThingsAdaptationTestCase.test_strip_whitespace.0.wording')
  })

  it('renders gabby.adaptation.SelectThingsAdaptationTestCase.test_unknown_tags pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "{"}, {"type": "plainText", "text": "tag"}, {"type": "plainText", "text": "|"}, {"type": "plainText", "text": "abc"}, {"type": "plainText", "text": "}"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.SelectThingsAdaptationTestCase.test_unknown_tags.0.instructions')
  })

  it('renders gabby.adaptation.SelectThingsAdaptationTestCase.test_unknown_tags pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "{"}, {"type": "selectableText", "text": "tag", "colors": ["red"], "boxed": false}, {"type": "plainText", "text": "|"}, {"type": "selectableText", "text": "def", "colors": ["red"], "boxed": false}, {"type": "plainText", "text": "}"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.SelectThingsAdaptationTestCase.test_unknown_tags.0.wording')
  })
})
