import TricolorSection from './OldTricolorSection.vue'

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
        paragraphs: [{"tokens": [{"type": "plainText", "text": "wording"}, {"type": "whitespace"}, {"type": "plainText", "text": "1"}]}, {"tokens": [{"type": "plainText", "text": "wording"}, {"type": "whitespace"}, {"type": "plainText", "text": "2"}]}, {"tokens": [{"type": "plainText", "text": "wording"}, {"type": "whitespace"}, {"type": "plainText", "text": "3"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.WordingPaginationTestCase.test_full_pagelet.0.wording')
  })

  it('renders gabby.adaptation.WordingPaginationTestCase.test_manual_and_automated_pagination pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "instructions"}]}, {"tokens": [{"type": "plainText", "text": "example"}]}, {"tokens": [{"type": "plainText", "text": "clue"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.WordingPaginationTestCase.test_manual_and_automated_pagination.0.instructions')
  })

  it('renders gabby.adaptation.WordingPaginationTestCase.test_manual_and_automated_pagination pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "wording"}, {"type": "whitespace"}, {"type": "plainText", "text": "1"}]}, {"tokens": [{"type": "plainText", "text": "wording"}, {"type": "whitespace"}, {"type": "plainText", "text": "2"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.WordingPaginationTestCase.test_manual_and_automated_pagination.0.wording')
  })

  it('renders gabby.adaptation.WordingPaginationTestCase.test_manual_and_automated_pagination pagelet 1 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "wording"}, {"type": "whitespace"}, {"type": "plainText", "text": "3"}]}, {"tokens": [{"type": "plainText", "text": "wording"}, {"type": "whitespace"}, {"type": "plainText", "text": "4"}]}, {"tokens": [{"type": "plainText", "text": "wording"}, {"type": "whitespace"}, {"type": "plainText", "text": "5"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.WordingPaginationTestCase.test_manual_and_automated_pagination.1.wording')
  })

  it('renders gabby.adaptation.WordingPaginationTestCase.test_manual_and_automated_pagination pagelet 2 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "wording"}, {"type": "whitespace"}, {"type": "plainText", "text": "6"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.WordingPaginationTestCase.test_manual_and_automated_pagination.2.wording')
  })

  it('renders gabby.adaptation.WordingPaginationTestCase.test_no_pagination pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "wording"}, {"type": "whitespace"}, {"type": "plainText", "text": "1"}]}, {"tokens": [{"type": "plainText", "text": "wording"}, {"type": "whitespace"}, {"type": "plainText", "text": "2"}]}, {"tokens": [{"type": "plainText", "text": "wording"}, {"type": "whitespace"}, {"type": "plainText", "text": "3"}]}, {"tokens": [{"type": "plainText", "text": "wording"}, {"type": "whitespace"}, {"type": "plainText", "text": "4"}]}, {"tokens": [{"type": "plainText", "text": "wording"}, {"type": "whitespace"}, {"type": "plainText", "text": "5"}]}, {"tokens": [{"type": "plainText", "text": "wording"}, {"type": "whitespace"}, {"type": "plainText", "text": "6"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.WordingPaginationTestCase.test_no_pagination.0.wording')
  })

  it('renders gabby.adaptation.WordingPaginationTestCase.test_only_manual_pagination pagelet 1 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "wording"}, {"type": "whitespace"}, {"type": "plainText", "text": "3"}]}, {"tokens": [{"type": "plainText", "text": "wording"}, {"type": "whitespace"}, {"type": "plainText", "text": "4"}]}, {"tokens": [{"type": "plainText", "text": "wording"}, {"type": "whitespace"}, {"type": "plainText", "text": "5"}]}, {"tokens": [{"type": "plainText", "text": "wording"}, {"type": "whitespace"}, {"type": "plainText", "text": "6"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.WordingPaginationTestCase.test_only_manual_pagination.1.wording')
  })

  it('renders gabby.adaptation.WordingPaginationTestCase.test_single_paragraph pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "wording"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.WordingPaginationTestCase.test_single_paragraph.0.wording')
  })

  it('renders gabby.adaptation.WordingPaginationTestCase.test_single_paragraph_on_second_page pagelet 1 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "wording"}, {"type": "whitespace"}, {"type": "plainText", "text": "3"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.WordingPaginationTestCase.test_single_paragraph_on_second_page.1.wording')
  })
})
