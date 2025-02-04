import TricolorSection from './OldTricolorSection.vue'

describe('TricolorSection for ItemizedAdaptationTestCase', () => {
  beforeEach(() => {
    cy.viewport(1000, 100)
  })

  it('renders gabby.adaptation.ItemizedAdaptationTestCase.test_boxed_words pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "Instructions"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ItemizedAdaptationTestCase.test_boxed_words.0.instructions')
  })

  it('renders gabby.adaptation.ItemizedAdaptationTestCase.test_boxed_words pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "boxedText", "text": "This"}, {"type": "whitespace"}, {"type": "boxedText", "text": "is"}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "boxedText", "text": "the"}, {"type": "whitespace"}, {"type": "boxedText", "text": "wording"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ItemizedAdaptationTestCase.test_boxed_words.0.wording')
  })

  it('renders gabby.adaptation.ItemizedAdaptationTestCase.test_mcq_below_letters pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "Instructions"}, {"type": "whitespace"}, {"type": "boxedText", "text": "alpha"}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "boxedText", "text": "bravo"}, {"type": "whitespace"}, {"type": "plainText", "text": "ou"}, {"type": "whitespace"}, {"type": "boxedText", "text": "charlie"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ItemizedAdaptationTestCase.test_mcq_below_letters.0.instructions')
  })

  it('renders gabby.adaptation.ItemizedAdaptationTestCase.test_mcq_below_letters pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "stack", "contents": [{"type": "plainText", "text": "A"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}]}, {"type": "stack", "contents": [{"type": "plainText", "text": "b"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}]}, {"type": "stack", "contents": [{"type": "plainText", "text": "c"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}]}, {"type": "stack", "contents": [{"type": "plainText", "text": "d"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}]}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ItemizedAdaptationTestCase.test_mcq_below_letters.0.wording')
  })

  it('renders gabby.adaptation.ItemizedAdaptationTestCase.test_mcq_below_manual_items pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "This"}, {"type": "whitespace"}, {"type": "stack", "contents": [{"type": "plainText", "text": "is"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}]}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "stack", "contents": [{"type": "plainText", "text": "the"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}]}, {"type": "whitespace"}, {"type": "plainText", "text": "wording"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ItemizedAdaptationTestCase.test_mcq_below_manual_items.0.wording')
  })

  it('renders gabby.adaptation.ItemizedAdaptationTestCase.test_mcq_below_punctuation pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "This"}, {"type": "whitespace"}, {"type": "plainText", "text": "is"}, {"type": "stack", "contents": [{"type": "plainText", "text": ","}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}]}, {"type": "whitespace"}, {"type": "plainText", "text": "the"}, {"type": "whitespace"}, {"type": "plainText", "text": "wording"}, {"type": "stack", "contents": [{"type": "plainText", "text": "."}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}]}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ItemizedAdaptationTestCase.test_mcq_below_punctuation.0.wording')
  })

  it('renders gabby.adaptation.ItemizedAdaptationTestCase.test_mcq_below_sentences pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "stack", "contents": [{"type": "line", "contents": [{"type": "plainText", "text": "Affirmative"}, {"type": "whitespace"}, {"type": "plainText", "text": "sentence"}, {"type": "plainText", "text": "."}]}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}]}, {"type": "whitespace"}, {"type": "stack", "contents": [{"type": "line", "contents": [{"type": "plainText", "text": "Exclamative"}, {"type": "whitespace"}, {"type": "plainText", "text": "sentence"}, {"type": "plainText", "text": "!"}]}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}]}, {"type": "whitespace"}, {"type": "stack", "contents": [{"type": "line", "contents": [{"type": "plainText", "text": "Phrase"}, {"type": "whitespace"}, {"type": "plainText", "text": "exclamative"}, {"type": "whitespace"}, {"type": "plainText", "text": "!"}]}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}]}, {"type": "whitespace"}, {"type": "stack", "contents": [{"type": "line", "contents": [{"type": "plainText", "text": "Interrogative"}, {"type": "whitespace"}, {"type": "plainText", "text": "sentence"}, {"type": "plainText", "text": "?"}]}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}]}, {"type": "whitespace"}, {"type": "stack", "contents": [{"type": "line", "contents": [{"type": "plainText", "text": "Phrase"}, {"type": "whitespace"}, {"type": "plainText", "text": "interrogative"}, {"type": "whitespace"}, {"type": "plainText", "text": "?"}]}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}]}, {"type": "whitespace"}, {"type": "stack", "contents": [{"type": "line", "contents": [{"type": "plainText", "text": "Suspens"}, {"type": "plainText", "text": "..."}]}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}]}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ItemizedAdaptationTestCase.test_mcq_below_sentences.0.wording')
  })

  it('renders gabby.adaptation.ItemizedAdaptationTestCase.test_mcq_below_words pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "stack", "contents": [{"type": "plainText", "text": "This"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}]}, {"type": "whitespace"}, {"type": "stack", "contents": [{"type": "plainText", "text": "is"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}]}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "stack", "contents": [{"type": "plainText", "text": "the"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}]}, {"type": "whitespace"}, {"type": "stack", "contents": [{"type": "plainText", "text": "wording"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}]}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ItemizedAdaptationTestCase.test_mcq_below_words.0.wording')
  })

  it('renders gabby.adaptation.ItemizedAdaptationTestCase.test_mcq_below_words_and_punctuation pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "stack", "contents": [{"type": "plainText", "text": "This"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}]}, {"type": "whitespace"}, {"type": "stack", "contents": [{"type": "plainText", "text": "is"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}]}, {"type": "stack", "contents": [{"type": "plainText", "text": ","}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}]}, {"type": "whitespace"}, {"type": "stack", "contents": [{"type": "plainText", "text": "the"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}]}, {"type": "whitespace"}, {"type": "stack", "contents": [{"type": "plainText", "text": "wording"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}]}, {"type": "stack", "contents": [{"type": "plainText", "text": "."}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}]}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ItemizedAdaptationTestCase.test_mcq_below_words_and_punctuation.0.wording')
  })

  it('renders gabby.adaptation.ItemizedAdaptationTestCase.test_mcq_beside_letters pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "A"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}, {"type": "plainText", "text": "b"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}, {"type": "plainText", "text": "c"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}, {"type": "plainText", "text": "d"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ItemizedAdaptationTestCase.test_mcq_beside_letters.0.wording')
  })

  it('renders gabby.adaptation.ItemizedAdaptationTestCase.test_mcq_beside_manual_items pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "This"}, {"type": "whitespace"}, {"type": "plainText", "text": "is"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "plainText", "text": "the"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "plainText", "text": "wording"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ItemizedAdaptationTestCase.test_mcq_beside_manual_items.0.wording')
  })

  it('renders gabby.adaptation.ItemizedAdaptationTestCase.test_mcq_beside_punctuation pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "This"}, {"type": "whitespace"}, {"type": "plainText", "text": "is"}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "plainText", "text": "the"}, {"type": "whitespace"}, {"type": "plainText", "text": "wording"}, {"type": "plainText", "text": "."}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ItemizedAdaptationTestCase.test_mcq_beside_punctuation.0.wording')
  })

  it('renders gabby.adaptation.ItemizedAdaptationTestCase.test_mcq_beside_sentences pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "Affirmative"}, {"type": "whitespace"}, {"type": "plainText", "text": "sentence"}, {"type": "plainText", "text": "."}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "plainText", "text": "Exclamative"}, {"type": "whitespace"}, {"type": "plainText", "text": "sentence"}, {"type": "plainText", "text": "!"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "plainText", "text": "Phrase"}, {"type": "whitespace"}, {"type": "plainText", "text": "exclamative"}, {"type": "whitespace"}, {"type": "plainText", "text": "!"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "plainText", "text": "Interrogative"}, {"type": "whitespace"}, {"type": "plainText", "text": "sentence"}, {"type": "plainText", "text": "?"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "plainText", "text": "Phrase"}, {"type": "whitespace"}, {"type": "plainText", "text": "interrogative"}, {"type": "whitespace"}, {"type": "plainText", "text": "?"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "plainText", "text": "Suspens"}, {"type": "plainText", "text": "..."}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ItemizedAdaptationTestCase.test_mcq_beside_sentences.0.wording')
  })

  it('renders gabby.adaptation.ItemizedAdaptationTestCase.test_mcq_beside_words pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "This"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "plainText", "text": "is"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "plainText", "text": "the"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "plainText", "text": "wording"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ItemizedAdaptationTestCase.test_mcq_beside_words.0.wording')
  })

  it('renders gabby.adaptation.ItemizedAdaptationTestCase.test_mcq_beside_words_and_punctuation pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "This"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "plainText", "text": "is"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "plainText", "text": "the"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "plainText", "text": "wording"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}, {"type": "plainText", "text": "."}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["alpha", "bravo", "charlie"], "show_choices_by_default": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ItemizedAdaptationTestCase.test_mcq_beside_words_and_punctuation.0.wording')
  })

  it('renders gabby.adaptation.ItemizedAdaptationTestCase.test_sel_tags pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "selectedText", "text": "abc", "color": "red"}, {"type": "whitespace"}, {"type": "selectedText", "text": "def", "color": "green"}, {"type": "whitespace"}, {"type": "selectedText", "text": "ghi", "color": "blue"}, {"type": "whitespace"}, {"type": "plainText", "text": "jkl"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ItemizedAdaptationTestCase.test_sel_tags.0.instructions')
  })

  it('renders gabby.adaptation.ItemizedAdaptationTestCase.test_sel_tags pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "selectableText", "text": "wording", "colors": ["red", "green", "blue"], "boxed": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ItemizedAdaptationTestCase.test_sel_tags.0.wording')
  })

  it('renders gabby.adaptation.ItemizedAdaptationTestCase.test_selectable_letters pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "selectableText", "text": "T", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": "h", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": "i", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": "s", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "i", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": "s", "colors": ["red"], "boxed": false}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "selectableText", "text": "t", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": "h", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": "e", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "w", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": "o", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": "r", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": "d", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": "i", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": "n", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": "g", "colors": ["red"], "boxed": false}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ItemizedAdaptationTestCase.test_selectable_letters.0.wording')
  })

  it('renders gabby.adaptation.ItemizedAdaptationTestCase.test_selectable_manual_items__boxed pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "This"}, {"type": "whitespace"}, {"type": "selectableText", "text": "is", "colors": ["red", "blue"], "boxed": true}, {"type": "selectableText", "text": ",", "colors": ["red", "blue"], "boxed": true}, {"type": "whitespace"}, {"type": "selectableText", "text": "the", "colors": ["red", "blue"], "boxed": true}, {"type": "whitespace"}, {"type": "plainText", "text": "wording"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ItemizedAdaptationTestCase.test_selectable_manual_items__boxed.0.wording')
  })

  it('renders gabby.adaptation.ItemizedAdaptationTestCase.test_selectable_manual_items__plain pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "This"}, {"type": "whitespace"}, {"type": "selectableText", "text": "is", "colors": ["red", "blue"], "boxed": false}, {"type": "selectableText", "text": ",", "colors": ["red", "blue"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "the", "colors": ["red", "blue"], "boxed": false}, {"type": "whitespace"}, {"type": "plainText", "text": "wording"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ItemizedAdaptationTestCase.test_selectable_manual_items__plain.0.wording')
  })

  it('renders gabby.adaptation.ItemizedAdaptationTestCase.test_selectable_punctuation_only pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "This"}, {"type": "whitespace"}, {"type": "plainText", "text": "is"}, {"type": "selectableText", "text": ",", "colors": ["green", "yellow", "orange"], "boxed": false}, {"type": "whitespace"}, {"type": "plainText", "text": "the"}, {"type": "whitespace"}, {"type": "plainText", "text": "wording"}, {"type": "selectableText", "text": ".", "colors": ["green", "yellow", "orange"], "boxed": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ItemizedAdaptationTestCase.test_selectable_punctuation_only.0.wording')
  })

  it('renders gabby.adaptation.ItemizedAdaptationTestCase.test_selectable_sentences pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "selectable", "contents": [{"type": "plainText", "text": "Affirmative"}, {"type": "whitespace"}, {"type": "plainText", "text": "sentence"}, {"type": "plainText", "text": "."}], "colors": ["red", "blue"], "boxed": true}, {"type": "whitespace"}, {"type": "selectable", "contents": [{"type": "plainText", "text": "Exclamative"}, {"type": "whitespace"}, {"type": "plainText", "text": "sentence"}, {"type": "plainText", "text": "!"}], "colors": ["red", "blue"], "boxed": true}, {"type": "whitespace"}, {"type": "selectable", "contents": [{"type": "plainText", "text": "Phrase"}, {"type": "whitespace"}, {"type": "plainText", "text": "exclamative"}, {"type": "whitespace"}, {"type": "plainText", "text": "!"}], "colors": ["red", "blue"], "boxed": true}, {"type": "whitespace"}, {"type": "selectable", "contents": [{"type": "plainText", "text": "Interrogative"}, {"type": "whitespace"}, {"type": "plainText", "text": "sentence"}, {"type": "plainText", "text": "?"}], "colors": ["red", "blue"], "boxed": true}, {"type": "whitespace"}, {"type": "selectable", "contents": [{"type": "plainText", "text": "Phrase"}, {"type": "whitespace"}, {"type": "plainText", "text": "interrogative"}, {"type": "whitespace"}, {"type": "plainText", "text": "?"}], "colors": ["red", "blue"], "boxed": true}, {"type": "whitespace"}, {"type": "selectable", "contents": [{"type": "plainText", "text": "Suspens"}, {"type": "plainText", "text": "..."}], "colors": ["red", "blue"], "boxed": true}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ItemizedAdaptationTestCase.test_selectable_sentences.0.wording')
  })

  it('renders gabby.adaptation.ItemizedAdaptationTestCase.test_selectable_tokens__in_bullet_list pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "\u25c6"}, {"type": "whitespace"}, {"type": "selectableText", "text": "First", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "list", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "element", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": ".", "colors": ["red"], "boxed": false}]}, {"tokens": [{"type": "plainText", "text": "\u25c6"}, {"type": "whitespace"}, {"type": "selectableText", "text": "Second", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "element", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": ",", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "still", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "in", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "list", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": ".", "colors": ["red"], "boxed": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ItemizedAdaptationTestCase.test_selectable_tokens__in_bullet_list.0.wording')
  })

  it('renders gabby.adaptation.ItemizedAdaptationTestCase.test_selectable_tokens__in_bullet_list pagelet 1 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "\u25c6"}, {"type": "whitespace"}, {"type": "selectableText", "text": "Third", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "element", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": ".", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "The", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "last", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "one", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": "!", "colors": ["red"], "boxed": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ItemizedAdaptationTestCase.test_selectable_tokens__in_bullet_list.1.wording')
  })

  it('renders gabby.adaptation.ItemizedAdaptationTestCase.test_selectable_tokens__in_lettered_list pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "a"}, {"type": "plainText", "text": "."}, {"type": "whitespace"}, {"type": "selectableText", "text": "First", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "list", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "element", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": ".", "colors": ["red"], "boxed": false}]}, {"tokens": [{"type": "plainText", "text": "b"}, {"type": "plainText", "text": "."}, {"type": "whitespace"}, {"type": "selectableText", "text": "Second", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "element", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": ",", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "still", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "in", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "list", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": ".", "colors": ["red"], "boxed": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ItemizedAdaptationTestCase.test_selectable_tokens__in_lettered_list.0.wording')
  })

  it('renders gabby.adaptation.ItemizedAdaptationTestCase.test_selectable_tokens__in_lettered_list pagelet 1 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "c"}, {"type": "plainText", "text": "."}, {"type": "whitespace"}, {"type": "selectableText", "text": "Third", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "element", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": ".", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "The", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "last", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "one", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": "!", "colors": ["red"], "boxed": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ItemizedAdaptationTestCase.test_selectable_tokens__in_lettered_list.1.wording')
  })

  it('renders gabby.adaptation.ItemizedAdaptationTestCase.test_selectable_tokens__in_numbered_list pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "1"}, {"type": "plainText", "text": ")"}, {"type": "whitespace"}, {"type": "selectableText", "text": "First", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "list", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "element", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": ".", "colors": ["red"], "boxed": false}]}, {"tokens": [{"type": "plainText", "text": "2"}, {"type": "plainText", "text": ")"}, {"type": "whitespace"}, {"type": "selectableText", "text": "Second", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "element", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": ",", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "still", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "in", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "list", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": ".", "colors": ["red"], "boxed": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ItemizedAdaptationTestCase.test_selectable_tokens__in_numbered_list.0.wording')
  })

  it('renders gabby.adaptation.ItemizedAdaptationTestCase.test_selectable_tokens__in_numbered_list pagelet 1 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "3"}, {"type": "plainText", "text": ")"}, {"type": "whitespace"}, {"type": "selectableText", "text": "Third", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "element", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": ".", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "The", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "last", "colors": ["red"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "one", "colors": ["red"], "boxed": false}, {"type": "selectableText", "text": "!", "colors": ["red"], "boxed": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ItemizedAdaptationTestCase.test_selectable_tokens__in_numbered_list.1.wording')
  })

  it('renders gabby.adaptation.ItemizedAdaptationTestCase.test_selectable_words__boxed pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "selectableText", "text": "This", "colors": ["red", "blue"], "boxed": true}, {"type": "whitespace"}, {"type": "selectableText", "text": "is", "colors": ["red", "blue"], "boxed": true}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "selectableText", "text": "the", "colors": ["red", "blue"], "boxed": true}, {"type": "whitespace"}, {"type": "selectableText", "text": "wording", "colors": ["red", "blue"], "boxed": true}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ItemizedAdaptationTestCase.test_selectable_words__boxed.0.wording')
  })

  it('renders gabby.adaptation.ItemizedAdaptationTestCase.test_selectable_words__plain pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "selectableText", "text": "This", "colors": ["red", "blue"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "is", "colors": ["red", "blue"], "boxed": false}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "selectableText", "text": "the", "colors": ["red", "blue"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "wording", "colors": ["red", "blue"], "boxed": false}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ItemizedAdaptationTestCase.test_selectable_words__plain.0.wording')
  })

  it('renders gabby.adaptation.ItemizedAdaptationTestCase.test_selectable_words_and_punctuation pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "selectableText", "text": "This", "colors": ["green", "yellow", "orange"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "is", "colors": ["green", "yellow", "orange"], "boxed": false}, {"type": "selectableText", "text": ",", "colors": ["green", "yellow", "orange"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "the", "colors": ["green", "yellow", "orange"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "wording", "colors": ["green", "yellow", "orange"], "boxed": false}, {"type": "selectableText", "text": ".", "colors": ["green", "yellow", "orange"], "boxed": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.ItemizedAdaptationTestCase.test_selectable_words_and_punctuation.0.wording')
  })
})
