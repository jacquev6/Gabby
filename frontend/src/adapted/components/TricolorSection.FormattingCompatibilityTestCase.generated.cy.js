import TricolorSection from './TricolorSection.vue'

describe('TricolorSection for FormattingCompatibilityTestCase', () => {
  beforeEach(() => {
    cy.viewport(1000, 100)
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_and_italic pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "bold": true,
                "italic": true,
                "text": "The"
              },
              {
                "kind": "whitespace",
                "bold": true,
                "italic": true
              },
              {
                "kind": "text",
                "bold": true,
                "italic": true,
                "text": "instructions"
              },
              {
                "kind": "text",
                "bold": true,
                "italic": true,
                "text": "."
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "bold": true,
                "italic": true,
                "text": "The"
              },
              {
                "kind": "whitespace",
                "bold": true,
                "italic": true
              },
              {
                "kind": "text",
                "bold": true,
                "italic": true,
                "text": "example"
              },
              {
                "kind": "text",
                "bold": true,
                "italic": true,
                "text": "."
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "bold": true,
                "italic": true,
                "text": "The"
              },
              {
                "kind": "whitespace",
                "bold": true,
                "italic": true
              },
              {
                "kind": "text",
                "bold": true,
                "italic": true,
                "text": "clue"
              },
              {
                "kind": "text",
                "bold": true,
                "italic": true,
                "text": "."
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_and_italic.0.instructions')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_and_italic pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "bold": true,
                "italic": true,
                "text": "The"
              },
              {
                "kind": "whitespace",
                "bold": true,
                "italic": true
              },
              {
                "kind": "text",
                "bold": true,
                "italic": true,
                "text": "wording"
              },
              {
                "kind": "text",
                "bold": true,
                "italic": true,
                "text": "."
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_and_italic.0.wording')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_and_italic pagelet 1 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "bold": true,
                "italic": true,
                "text": "The"
              },
              {
                "kind": "whitespace",
                "bold": true,
                "italic": true
              },
              {
                "kind": "text",
                "bold": true,
                "italic": true,
                "text": "reference"
              },
              {
                "kind": "text",
                "bold": true,
                "italic": true,
                "text": "."
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_and_italic.1.instructions')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_and_italic pagelet 1 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_and_italic.1.wording')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_one_choice_in_choices2_in_instructions pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
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
                "kind": "text",
                "text": ","
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "passiveSequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "b"
                  },
                  {
                    "kind": "text",
                    "bold": true,
                    "text": "rav"
                  },
                  {
                    "kind": "text",
                    "text": "o"
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
                    "text": "charlie"
                  }
                ],
                "boxed": true
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_one_choice_in_choices2_in_instructions.0.instructions')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_one_choice_in_choices2_in_instructions pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
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
                      "text": "b"
                    },
                    {
                      "kind": "text",
                      "bold": true,
                      "text": "rav"
                    },
                    {
                      "kind": "text",
                      "text": "o"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "charlie"
                    }
                  ]
                ]
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_one_choice_in_choices2_in_instructions.0.wording')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_sel_and_bold pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "bold": true,
                "highlighted": "lightgreen",
                "text": "The"
              },
              {
                "kind": "whitespace",
                "bold": true,
                "highlighted": "lightgreen"
              },
              {
                "kind": "text",
                "bold": true,
                "highlighted": "lightgreen",
                "text": "instructions"
              },
              {
                "kind": "text",
                "bold": true,
                "highlighted": "lightgreen",
                "text": "."
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "bold": true,
                "highlighted": "lightgreen",
                "text": "The"
              },
              {
                "kind": "whitespace",
                "bold": true,
                "highlighted": "lightgreen"
              },
              {
                "kind": "text",
                "bold": true,
                "highlighted": "lightgreen",
                "text": "example"
              },
              {
                "kind": "text",
                "bold": true,
                "highlighted": "lightgreen",
                "text": "."
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "bold": true,
                "highlighted": "lightgreen",
                "text": "The"
              },
              {
                "kind": "whitespace",
                "bold": true,
                "highlighted": "lightgreen"
              },
              {
                "kind": "text",
                "bold": true,
                "highlighted": "lightgreen",
                "text": "clue"
              },
              {
                "kind": "text",
                "bold": true,
                "highlighted": "lightgreen",
                "text": "."
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_sel_and_bold.0.instructions')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_sel_and_italic pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "italic": true,
                "highlighted": "lightgreen",
                "text": "The"
              },
              {
                "kind": "whitespace",
                "italic": true,
                "highlighted": "lightgreen"
              },
              {
                "kind": "text",
                "italic": true,
                "highlighted": "lightgreen",
                "text": "instructions"
              },
              {
                "kind": "text",
                "italic": true,
                "highlighted": "lightgreen",
                "text": "."
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "italic": true,
                "highlighted": "lightgreen",
                "text": "The"
              },
              {
                "kind": "whitespace",
                "italic": true,
                "highlighted": "lightgreen"
              },
              {
                "kind": "text",
                "italic": true,
                "highlighted": "lightgreen",
                "text": "example"
              },
              {
                "kind": "text",
                "italic": true,
                "highlighted": "lightgreen",
                "text": "."
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "italic": true,
                "highlighted": "lightgreen",
                "text": "The"
              },
              {
                "kind": "whitespace",
                "italic": true,
                "highlighted": "lightgreen"
              },
              {
                "kind": "text",
                "italic": true,
                "highlighted": "lightgreen",
                "text": "clue"
              },
              {
                "kind": "text",
                "italic": true,
                "highlighted": "lightgreen",
                "text": "."
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_sel_and_italic.0.instructions')
  })
})
