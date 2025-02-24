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

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_automated_items__letters pagelet 0 wording', () => {
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
                    "text": "B"
                  }
                ],
                "boxed": true
              },
              {
                "kind": "passiveSequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "l"
                  }
                ],
                "boxed": true
              },
              {
                "kind": "passiveSequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "a"
                  }
                ],
                "boxed": true
              },
              {
                "kind": "passiveSequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "h"
                  }
                ],
                "boxed": true
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
                  }
                ],
                "boxed": true
              },
              {
                "kind": "passiveSequence",
                "contents": [
                  {
                    "kind": "text",
                    "bold": true,
                    "text": "l"
                  }
                ],
                "boxed": true
              },
              {
                "kind": "passiveSequence",
                "contents": [
                  {
                    "kind": "text",
                    "bold": true,
                    "text": "a"
                  }
                ],
                "boxed": true
              },
              {
                "kind": "passiveSequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "h"
                  }
                ],
                "boxed": true
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
                  }
                ],
                "boxed": true
              },
              {
                "kind": "passiveSequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "l"
                  }
                ],
                "boxed": true
              },
              {
                "kind": "passiveSequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "a"
                  }
                ],
                "boxed": true
              },
              {
                "kind": "passiveSequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "h"
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
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_automated_items__letters.0.wording')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_automated_items__punctuation pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "Blah"
              },
              {
                "kind": "passiveSequence",
                "contents": [
                  {
                    "kind": "text",
                    "bold": true,
                    "text": ","
                  }
                ],
                "boxed": true
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "blah"
              },
              {
                "kind": "passiveSequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "."
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
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_automated_items__punctuation.0.wording')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_automated_items__sentences pagelet 0 wording', () => {
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
                    "text": "Blah"
                  },
                  {
                    "kind": "whitespace"
                  },
                  {
                    "kind": "text",
                    "text": "b"
                  },
                  {
                    "kind": "text",
                    "bold": true,
                    "text": "la"
                  },
                  {
                    "kind": "text",
                    "text": "h"
                  },
                  {
                    "kind": "text",
                    "text": "."
                  }
                ],
                "boxed": true
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "passiveSequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "Blah"
                  },
                  {
                    "kind": "text",
                    "text": "."
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
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_automated_items__sentences.0.wording')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_automated_items__separated pagelet 0 wording', () => {
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
                    "text": "Blah"
                  },
                  {
                    "kind": "whitespace"
                  },
                  {
                    "kind": "text",
                    "text": "b"
                  },
                  {
                    "kind": "text",
                    "bold": true,
                    "text": "la"
                  },
                  {
                    "kind": "text",
                    "text": "h"
                  }
                ],
                "boxed": true
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "passiveSequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "blah"
                  },
                  {
                    "kind": "text",
                    "text": "."
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
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_automated_items__separated.0.wording')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_automated_items__words pagelet 0 wording', () => {
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
                    "text": "Blah"
                  }
                ],
                "boxed": true
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
                    "text": "la"
                  },
                  {
                    "kind": "text",
                    "text": "h"
                  }
                ],
                "boxed": true
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "passiveSequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "blah"
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
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_automated_items__words.0.wording')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_manual_items pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "Blah"
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
                    "text": "la"
                  },
                  {
                    "kind": "text",
                    "text": "h"
                  }
                ],
                "boxed": true
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "blah"
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
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_manual_items.0.wording')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_mcq_placeholder pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "Instructions"
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
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_mcq_placeholder.0.instructions')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_mcq_placeholder pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "sequence",
                "contents": [
                  {
                    "kind": "sequence",
                    "contents": [
                      {
                        "kind": "text",
                        "text": "Blah"
                      },
                      {
                        "kind": "whitespace"
                      },
                      {
                        "kind": "text",
                        "highlighted": "#ffff00",
                        "text": "b"
                      },
                      {
                        "kind": "text",
                        "bold": true,
                        "highlighted": "#ffff00",
                        "text": "la"
                      },
                      {
                        "kind": "text",
                        "highlighted": "#ffff00",
                        "text": "h"
                      },
                      {
                        "kind": "text",
                        "text": "."
                      }
                    ]
                  },
                  {
                    "kind": "sequence",
                    "contents": [
                      {
                        "kind": "text",
                        "text": "Blah"
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
                        "kind": "text",
                        "text": "."
                      }
                    ]
                  }
                ],
                "vertical": true
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_mcq_placeholder.0.wording')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_one_choice_in_choices2_in_instructions_with_mcq_beside_words pagelet 0 instructions', () => {
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
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_one_choice_in_choices2_in_instructions_with_mcq_beside_words.0.instructions')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_one_choice_in_choices2_in_instructions_with_mcq_beside_words pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "blah"
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
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_one_choice_in_choices2_in_instructions_with_mcq_beside_words.0.wording')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_one_choice_in_choices2_in_instructions_with_placeholder pagelet 0 wording', () => {
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
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_one_choice_in_choices2_in_instructions_with_placeholder.0.wording')
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
