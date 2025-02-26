import MonocolorSection from './MonocolorSection.vue'
import TricolorSection from './TricolorSection.vue'

describe('TricolorSection for FormattingCompatibilityTestCase', () => {
  beforeEach(() => {
    cy.viewport(1000, 100)
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_and_italic pagelet 0 section 0', () => {
    cy.mount(MonocolorSection, {
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
        first: false,
        centered: true,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_and_italic.0.0')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_and_italic pagelet 0 section 1', () => {
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
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_and_italic.0.1')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_and_italic pagelet 1 section 0', () => {
    cy.mount(MonocolorSection, {
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
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_and_italic.1.0')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_automated_items__letters pagelet 0 section 1', () => {
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
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_automated_items__letters.0.1')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_automated_items__punctuation pagelet 0 section 1', () => {
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
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_automated_items__punctuation.0.1')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_automated_items__sentences pagelet 0 section 1', () => {
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
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_automated_items__sentences.0.1')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_automated_items__separated pagelet 0 section 1', () => {
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
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_automated_items__separated.0.1')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_automated_items__words pagelet 0 section 1', () => {
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
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_automated_items__words.0.1')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_manual_items pagelet 0 section 1', () => {
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
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_manual_items.0.1')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_mcq_placeholder pagelet 0 section 0', () => {
    cy.mount(MonocolorSection, {
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
        first: false,
        centered: true,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_mcq_placeholder.0.0')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_mcq_placeholder pagelet 0 section 1', () => {
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
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_mcq_placeholder.0.1')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_one_choice_in_choices2_in_instructions_with_mcq_beside_words pagelet 0 section 0', () => {
    cy.mount(MonocolorSection, {
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
        first: false,
        centered: true,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_one_choice_in_choices2_in_instructions_with_mcq_beside_words.0.0')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_one_choice_in_choices2_in_instructions_with_mcq_beside_words pagelet 0 section 1', () => {
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
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_one_choice_in_choices2_in_instructions_with_mcq_beside_words.0.1')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_one_choice_in_choices2_in_instructions_with_placeholder pagelet 0 section 1', () => {
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
                      "text": "Alpha"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "B"
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
                      "text": "Charlie"
                    }
                  ]
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
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_one_choice_in_choices2_in_instructions_with_placeholder.0.1')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_one_choice_in_choices2_in_wording_without_placeholder pagelet 0 section 1', () => {
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
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_bold_in_one_choice_in_choices2_in_wording_without_placeholder.0.1')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_choices2_with_one_line_end_in_instructions pagelet 0 section 0', () => {
    cy.mount(MonocolorSection, {
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
        first: false,
        centered: true,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_choices2_with_one_line_end_in_instructions.0.0')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_choices2_with_one_line_end_in_instructions pagelet 0 section 1', () => {
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
                      "text": "Alpha"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Bravo"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Charlie"
                    }
                  ]
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
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_choices2_with_one_line_end_in_instructions.0.1')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_choices2_with_one_line_end_in_wording pagelet 0 section 1', () => {
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
                      "text": "bravo"
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
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_choices2_with_one_line_end_in_wording.0.1')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_manual_item_with_one_line_end pagelet 0 section 1', () => {
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
                    "text": "bl"
                  },
                  {
                    "kind": "whitespace"
                  },
                  {
                    "kind": "text",
                    "text": "ah"
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
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_manual_item_with_one_line_end.0.1')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_mcq_placeholder_with_one_line_end pagelet 0 section 1', () => {
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
                        "text": "bl"
                      },
                      {
                        "kind": "whitespace",
                        "highlighted": "#ffff00"
                      },
                      {
                        "kind": "text",
                        "highlighted": "#ffff00",
                        "text": "ah"
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
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_mcq_placeholder_with_one_line_end.0.1')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_sel_and_bold pagelet 0 section 0', () => {
    cy.mount(MonocolorSection, {
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
        first: false,
        centered: true,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_sel_and_bold.0.0')
  })

  it('renders gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_sel_and_italic pagelet 0 section 0', () => {
    cy.mount(MonocolorSection, {
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
        first: false,
        centered: true,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.formatting_compatibility_tests.FormattingCompatibilityTestCase.test_sel_and_italic.0.0')
  })
})
