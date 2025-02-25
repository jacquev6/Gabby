import MonocolorSection from './MonocolorSection.vue'
import TricolorSection from './TricolorSection.vue'

describe('TricolorSection for LenientParagraphTestCase', () => {
  beforeEach(() => {
    cy.viewport(1000, 100)
  })

  it('renders gabby.adaptation.lenient_paragraph_tests.LenientParagraphTestCase.test_bold_and_italic pagelet 0 section 0', () => {
    cy.mount(MonocolorSection, {
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
                "kind": "text",
                "bold": true,
                "text": "strict"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "instructions"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "italic": true,
                "text": "paragraph"
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
                "text": "And"
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
                "kind": "text",
                "bold": true,
                "text": "lenient"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "instructions"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "italic": true,
                "text": "paragraph"
              }
            ]
          }
        ],
        first: false,
        centered: true,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.lenient_paragraph_tests.LenientParagraphTestCase.test_bold_and_italic.0.0')
  })

  it('renders gabby.adaptation.lenient_paragraph_tests.LenientParagraphTestCase.test_bold_and_italic pagelet 0 section 1', () => {
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
                "kind": "text",
                "bold": true,
                "text": "strict"
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
                "italic": true,
                "text": "paragraph"
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
                "text": "And"
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
                "kind": "text",
                "bold": true,
                "text": "lenient"
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
                "italic": true,
                "text": "paragraph"
              }
            ]
          }
        ],
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.lenient_paragraph_tests.LenientParagraphTestCase.test_bold_and_italic.0.1')
  })

  it('renders gabby.adaptation.lenient_paragraph_tests.LenientParagraphTestCase.test_fill_with_free_text pagelet 0 section 0', () => {
    cy.mount(MonocolorSection, {
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
        first: false,
        centered: true,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.lenient_paragraph_tests.LenientParagraphTestCase.test_fill_with_free_text.0.0')
  })

  it('renders gabby.adaptation.lenient_paragraph_tests.LenientParagraphTestCase.test_fill_with_free_text pagelet 0 section 1', () => {
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
                "text": "strict"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "paragraph"
              },
              {
                "kind": "text",
                "text": "."
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "With"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "some"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "punctuation"
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
                "text": "And"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "this"
              },
              {
                "kind": "text",
                "text": ","
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
                "text": "lenient"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "paragraph"
              }
            ]
          }
        ],
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.lenient_paragraph_tests.LenientParagraphTestCase.test_fill_with_free_text.0.1')
  })

  it('renders gabby.adaptation.lenient_paragraph_tests.LenientParagraphTestCase.test_multiple_choices pagelet 0 section 0', () => {
    cy.mount(MonocolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "Choose"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "passiveSequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "alpha"
                  }
                ],
                "boxed": true
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "ou"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "passiveSequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "bravo"
                  }
                ],
                "boxed": true
              },
              {
                "kind": "text",
                "text": "."
              }
            ]
          }
        ],
        first: false,
        centered: true,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.lenient_paragraph_tests.LenientParagraphTestCase.test_multiple_choices.0.0')
  })

  it('renders gabby.adaptation.lenient_paragraph_tests.LenientParagraphTestCase.test_multiple_choices pagelet 0 section 1', () => {
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
                "kind": "multipleChoicesInput",
                "choices": [
                  [
                    {
                      "kind": "text",
                      "text": "alpha"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "bravo"
                    }
                  ]
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "strict"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "paragraph"
              },
              {
                "kind": "text",
                "text": "."
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "With"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "some"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "punctuation"
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
                "text": "And"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "this"
              },
              {
                "kind": "text",
                "text": ","
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
                "kind": "multipleChoicesInput",
                "choices": [
                  [
                    {
                      "kind": "text",
                      "text": "alpha"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "bravo"
                    }
                  ]
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "lenient"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "paragraph"
              }
            ]
          }
        ],
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.lenient_paragraph_tests.LenientParagraphTestCase.test_multiple_choices.0.1')
  })

  it('renders gabby.adaptation.lenient_paragraph_tests.LenientParagraphTestCase.test_select_words_with_punctuation pagelet 0 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "This"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "is"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "a"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "strict"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "paragraph"
                  }
                ]
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": ","
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "with"
                  }
                ]
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "..."
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "some"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "punctuation"
                  }
                ]
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "."
                  }
                ]
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "And"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "this"
                  }
                ]
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": ","
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "is"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "a"
                  }
                ]
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "..."
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "lenient"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "paragraph"
                  }
                ]
              }
            ]
          }
        ],
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.lenient_paragraph_tests.LenientParagraphTestCase.test_select_words_with_punctuation.0.1')
  })

  it('renders gabby.adaptation.lenient_paragraph_tests.LenientParagraphTestCase.test_select_words_without_punctuation pagelet 0 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "This"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "is"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "a"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "strict"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "paragraph"
                  }
                ]
              },
              {
                "kind": "text",
                "text": ","
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "with"
                  }
                ]
              },
              {
                "kind": "text",
                "text": "..."
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "some"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "punctuation"
                  }
                ]
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
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "And"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "this"
                  }
                ]
              },
              {
                "kind": "text",
                "text": ","
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "is"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "a"
                  }
                ]
              },
              {
                "kind": "text",
                "text": "..."
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "lenient"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "paragraph"
                  }
                ]
              }
            ]
          }
        ],
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.lenient_paragraph_tests.LenientParagraphTestCase.test_select_words_without_punctuation.0.1')
  })
})
