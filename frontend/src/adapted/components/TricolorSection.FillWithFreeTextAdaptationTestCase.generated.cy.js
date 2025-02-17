import TricolorSection from './TricolorSection.vue'

describe('TricolorSection for FillWithFreeTextAdaptationTestCase', () => {
  beforeEach(() => {
    cy.viewport(1000, 100)
  })

  it('renders gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_example_and_clue pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "instructions"
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "This"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "@"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "is"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "the"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "example"
              },
              {
                "kind": "text",
                "text": "."
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "This"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "@"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "is"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "the"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "clue"
              },
              {
                "kind": "text",
                "text": "."
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_example_and_clue.0.instructions')
  })

  it('renders gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_example_and_clue pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "This"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "freeTextInput"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "is"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "the"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "wording"
              },
              {
                "kind": "text",
                "text": "."
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_example_and_clue.0.wording')
  })

  it('renders gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_multiple_lines_in_instructions pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "instructions"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "are"
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "on"
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "multiple"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "lines"
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_multiple_lines_in_instructions.0.instructions')
  })

  it('renders gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_multiple_lines_in_instructions pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "wording"
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_multiple_lines_in_instructions.0.wording')
  })

  it('renders gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_multiple_lines_in_wording pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "instructions"
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_multiple_lines_in_wording.0.instructions')
  })

  it('renders gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_multiple_lines_in_wording pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "foo"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "toto"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": ":"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "freeTextInput"
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "bar"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": ":"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "freeTextInput"
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "baz"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": ":"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "freeTextInput"
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_multiple_lines_in_wording.0.wording')
  })

  it('renders gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_single_sentence pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "The"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "wording"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "of"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "this"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "freeTextInput"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "is"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "a"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "freeTextInput"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "sentence"
              },
              {
                "kind": "text",
                "text": "."
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_single_sentence.0.wording')
  })

  it('renders gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_start_and_end_with_placeholder pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "freeTextInput"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "a"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "freeTextInput"
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_start_and_end_with_placeholder.0.wording')
  })

  it('renders gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_strip_whitespace pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "abc"
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_strip_whitespace.0.instructions')
  })

  it('renders gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_strip_whitespace pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "def"
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_strip_whitespace.0.wording')
  })

  it('renders gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_unknown_tags pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "{"
              },
              {
                "kind": "text",
                "text": "tag"
              },
              {
                "kind": "text",
                "text": "|"
              },
              {
                "kind": "text",
                "text": "abc"
              },
              {
                "kind": "text",
                "text": "}"
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_unknown_tags.0.instructions')
  })

  it('renders gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_unknown_tags pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "{"
              },
              {
                "kind": "text",
                "text": "tag"
              },
              {
                "kind": "text",
                "text": "|"
              },
              {
                "kind": "text",
                "text": "def"
              },
              {
                "kind": "text",
                "text": "}"
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.fill_with_free_text_adaptation_tests.FillWithFreeTextAdaptationTestCase.test_unknown_tags.0.wording')
  })
})
