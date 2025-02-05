import TricolorSection from './TricolorSection.vue'

describe('TricolorSection for WordingPaginationTestCase', () => {
  beforeEach(() => {
    cy.viewport(1000, 100)
  })

  it('renders gabby.adaptation.WordingPaginationTestCase.test_empty pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.WordingPaginationTestCase.test_empty.0.instructions')
  })

  it('renders gabby.adaptation.WordingPaginationTestCase.test_full_pagelet pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wording"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "1"}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wording"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "2"}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wording"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "3"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.WordingPaginationTestCase.test_full_pagelet.0.wording')
  })

  it('renders gabby.adaptation.WordingPaginationTestCase.test_manual_and_automated_pagination pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "instructions"}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "example"}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "clue"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.WordingPaginationTestCase.test_manual_and_automated_pagination.0.instructions')
  })

  it('renders gabby.adaptation.WordingPaginationTestCase.test_manual_and_automated_pagination pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wording"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "1"}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wording"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "2"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.WordingPaginationTestCase.test_manual_and_automated_pagination.0.wording')
  })

  it('renders gabby.adaptation.WordingPaginationTestCase.test_manual_and_automated_pagination pagelet 1 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wording"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "3"}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wording"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "4"}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wording"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "5"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.WordingPaginationTestCase.test_manual_and_automated_pagination.1.wording')
  })

  it('renders gabby.adaptation.WordingPaginationTestCase.test_manual_and_automated_pagination pagelet 2 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wording"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "6"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.WordingPaginationTestCase.test_manual_and_automated_pagination.2.wording')
  })

  it('renders gabby.adaptation.WordingPaginationTestCase.test_no_pagination pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wording"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "1"}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wording"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "2"}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wording"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "3"}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wording"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "4"}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wording"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "5"}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wording"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "6"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.WordingPaginationTestCase.test_no_pagination.0.wording')
  })

  it('renders gabby.adaptation.WordingPaginationTestCase.test_one_letter_per_paragraph pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "instructions"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.WordingPaginationTestCase.test_one_letter_per_paragraph.0.instructions')
  })

  it('renders gabby.adaptation.WordingPaginationTestCase.test_one_letter_per_paragraph pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "a"}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "b"}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "c"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.WordingPaginationTestCase.test_one_letter_per_paragraph.0.wording')
  })

  it('renders gabby.adaptation.WordingPaginationTestCase.test_one_letter_per_paragraph pagelet 1 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "d"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.WordingPaginationTestCase.test_one_letter_per_paragraph.1.wording')
  })

  it('renders gabby.adaptation.WordingPaginationTestCase.test_one_manual_item_per_paragraph pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "Instructions"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.WordingPaginationTestCase.test_one_manual_item_per_paragraph.0.instructions')
  })

  it('renders gabby.adaptation.WordingPaginationTestCase.test_one_manual_item_per_paragraph pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "This"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "is"}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "the"}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wording"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.WordingPaginationTestCase.test_one_manual_item_per_paragraph.0.wording')
  })

  it('renders gabby.adaptation.WordingPaginationTestCase.test_one_punctuation_per_paragraph pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "a"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "word"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": ","}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "word"}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "b"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "word"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "!"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.WordingPaginationTestCase.test_one_punctuation_per_paragraph.0.wording')
  })

  it('renders gabby.adaptation.WordingPaginationTestCase.test_one_punctuation_per_paragraph pagelet 1 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "word"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.WordingPaginationTestCase.test_one_punctuation_per_paragraph.1.wording')
  })

  it('renders gabby.adaptation.WordingPaginationTestCase.test_one_sentence_per_paragraph pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "Il"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "fait"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "beau"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "Il"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "fait"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "chaud"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.WordingPaginationTestCase.test_one_sentence_per_paragraph.0.wording')
  })

  it('renders gabby.adaptation.WordingPaginationTestCase.test_one_sentence_per_paragraph pagelet 1 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "Il"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "ne"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "pleut"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "pas"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.WordingPaginationTestCase.test_one_sentence_per_paragraph.1.wording')
  })

  it('renders gabby.adaptation.WordingPaginationTestCase.test_one_word_per_paragraph pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "a"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "worda"}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wordb"}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "b"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "."}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wordc"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.WordingPaginationTestCase.test_one_word_per_paragraph.0.wording')
  })

  it('renders gabby.adaptation.WordingPaginationTestCase.test_one_word_per_paragraph pagelet 1 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wordd"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.WordingPaginationTestCase.test_one_word_per_paragraph.1.wording')
  })

  it('renders gabby.adaptation.WordingPaginationTestCase.test_only_manual_pagination pagelet 1 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wording"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "3"}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wording"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "4"}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wording"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "5"}]}, {"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wording"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "6"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.WordingPaginationTestCase.test_only_manual_pagination.1.wording')
  })

  it('renders gabby.adaptation.WordingPaginationTestCase.test_single_paragraph pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wording"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.WordingPaginationTestCase.test_single_paragraph.0.wording')
  })

  it('renders gabby.adaptation.WordingPaginationTestCase.test_single_paragraph_on_second_page pagelet 1 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"contents": [{"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "wording"}, {"kind": "whitespace"}, {"kind": "text", "bold": false, "italic": false, "highlighted": null, "text": "3"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.WordingPaginationTestCase.test_single_paragraph_on_second_page.1.wording')
  })
})
