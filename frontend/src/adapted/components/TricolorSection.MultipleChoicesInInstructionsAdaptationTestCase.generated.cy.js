import TricolorSection from './TricolorSection.vue'

describe('TricolorSection for MultipleChoicesInInstructionsAdaptationTestCase', () => {
  beforeEach(() => {
    cy.viewport(1000, 100)
  })

  it('renders gabby.adaptation.multiple_choices_in_instructions_adaptation_tests.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2 pagelet 0 section 0', () => {
    cy.mount(TricolorSection, {
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
                    "text": "a"
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
                    "text": "b"
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
        tricolored: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.multiple_choices_in_instructions_adaptation_tests.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2.0.0')
  })

  it('renders gabby.adaptation.multiple_choices_in_instructions_adaptation_tests.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2 pagelet 0 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "A"
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
                      "text": "a"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "b"
                    }
                  ]
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "B"
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
                      "text": "a"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "b"
                    }
                  ]
                ]
              }
            ]
          }
        ],
        first: false,
        centered: false,
        tricolored: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.multiple_choices_in_instructions_adaptation_tests.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2.0.1')
  })

  it('renders gabby.adaptation.multiple_choices_in_instructions_adaptation_tests.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_empty_separator pagelet 0 section 0', () => {
    cy.mount(TricolorSection, {
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
                    "text": "a"
                  },
                  {
                    "kind": "whitespace"
                  },
                  {
                    "kind": "text",
                    "text": "b"
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
        tricolored: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.multiple_choices_in_instructions_adaptation_tests.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_empty_separator.0.0')
  })

  it('renders gabby.adaptation.multiple_choices_in_instructions_adaptation_tests.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_empty_separator pagelet 0 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "A"
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
                      "text": "a"
                    },
                    {
                      "kind": "whitespace"
                    },
                    {
                      "kind": "text",
                      "text": "b"
                    }
                  ]
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "B"
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
                      "text": "a"
                    },
                    {
                      "kind": "whitespace"
                    },
                    {
                      "kind": "text",
                      "text": "b"
                    }
                  ]
                ]
              }
            ]
          }
        ],
        first: false,
        centered: false,
        tricolored: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.multiple_choices_in_instructions_adaptation_tests.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_empty_separator.0.1')
  })

  it('renders gabby.adaptation.multiple_choices_in_instructions_adaptation_tests.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_oxford_comma pagelet 0 section 0', () => {
    cy.mount(TricolorSection, {
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
                    "text": "a"
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
                "kind": "whitespace"
              },
              {
                "kind": "passiveSequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "c"
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
                    "text": "d"
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
        tricolored: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.multiple_choices_in_instructions_adaptation_tests.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_oxford_comma.0.0')
  })

  it('renders gabby.adaptation.multiple_choices_in_instructions_adaptation_tests.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_oxford_comma pagelet 0 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "A"
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
                      "text": "a"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "b"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "c"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "d"
                    }
                  ]
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "B"
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
                      "text": "a"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "b"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "c"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "d"
                    }
                  ]
                ]
              }
            ]
          }
        ],
        first: false,
        centered: false,
        tricolored: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.multiple_choices_in_instructions_adaptation_tests.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_oxford_comma.0.1')
  })

  it('renders gabby.adaptation.multiple_choices_in_instructions_adaptation_tests.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_successive_separators pagelet 0 section 0', () => {
    cy.mount(TricolorSection, {
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
                    "text": "a"
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
                    "text": "c"
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
        tricolored: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.multiple_choices_in_instructions_adaptation_tests.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_successive_separators.0.0')
  })

  it('renders gabby.adaptation.multiple_choices_in_instructions_adaptation_tests.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_successive_separators pagelet 0 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "A"
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
                      "text": "a"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "b"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "c"
                    }
                  ]
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "B"
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
                      "text": "a"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "b"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "c"
                    }
                  ]
                ]
              }
            ]
          }
        ],
        first: false,
        centered: false,
        tricolored: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.multiple_choices_in_instructions_adaptation_tests.MultipleChoicesInInstructionsAdaptationTestCase.test_choices2_with_successive_separators.0.1')
  })

  it('renders gabby.adaptation.multiple_choices_in_instructions_adaptation_tests.MultipleChoicesInInstructionsAdaptationTestCase.test_chose_a_single_letter_to_complete_a_word pagelet 0 section 0', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "Compl\u00e8te"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "les"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "mots"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "avec"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "passiveSequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "m"
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
                    "text": "n"
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
        tricolored: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.multiple_choices_in_instructions_adaptation_tests.MultipleChoicesInInstructionsAdaptationTestCase.test_chose_a_single_letter_to_complete_a_word.0.0')
  })

  it('renders gabby.adaptation.multiple_choices_in_instructions_adaptation_tests.MultipleChoicesInInstructionsAdaptationTestCase.test_chose_a_single_letter_to_complete_a_word pagelet 0 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "i"
              },
              {
                "kind": "multipleChoicesInput",
                "choices": [
                  [
                    {
                      "kind": "text",
                      "text": "m"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "n"
                    }
                  ]
                ]
              },
              {
                "kind": "text",
                "text": "mense"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "i"
              },
              {
                "kind": "multipleChoicesInput",
                "choices": [
                  [
                    {
                      "kind": "text",
                      "text": "m"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "n"
                    }
                  ]
                ]
              },
              {
                "kind": "text",
                "text": "juste"
              }
            ]
          }
        ],
        first: false,
        centered: false,
        tricolored: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.multiple_choices_in_instructions_adaptation_tests.MultipleChoicesInInstructionsAdaptationTestCase.test_chose_a_single_letter_to_complete_a_word.0.1')
  })

  it('renders gabby.adaptation.multiple_choices_in_instructions_adaptation_tests.MultipleChoicesInInstructionsAdaptationTestCase.test_example_and_clue pagelet 0 section 0', () => {
    cy.mount(TricolorSection, {
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
                    "text": "a"
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
                    "text": "b"
                  }
                ],
                "boxed": true
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
                "text": "{"
              },
              {
                "kind": "text",
                "text": "choices2"
              },
              {
                "kind": "text",
                "text": "|"
              },
              {
                "kind": "text",
                "text": "|"
              },
              {
                "kind": "text",
                "text": "/"
              },
              {
                "kind": "text",
                "text": "|"
              },
              {
                "kind": "text",
                "text": "|"
              },
              {
                "kind": "text",
                "text": "|"
              },
              {
                "kind": "text",
                "text": "|"
              },
              {
                "kind": "text",
                "text": "is"
              },
              {
                "kind": "text",
                "text": "}"
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
                "text": "@"
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
                "text": "is"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "{"
              },
              {
                "kind": "text",
                "text": "choices2"
              },
              {
                "kind": "text",
                "text": "|"
              },
              {
                "kind": "text",
                "text": "|"
              },
              {
                "kind": "text",
                "text": "/"
              },
              {
                "kind": "text",
                "text": "|"
              },
              {
                "kind": "text",
                "text": "|"
              },
              {
                "kind": "text",
                "text": "|"
              },
              {
                "kind": "text",
                "text": "|"
              },
              {
                "kind": "text",
                "text": "the"
              },
              {
                "kind": "text",
                "text": "}"
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
                "text": "clue"
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
        tricolored: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.multiple_choices_in_instructions_adaptation_tests.MultipleChoicesInInstructionsAdaptationTestCase.test_example_and_clue.0.0')
  })

  it('renders gabby.adaptation.multiple_choices_in_instructions_adaptation_tests.MultipleChoicesInInstructionsAdaptationTestCase.test_two_choices2 pagelet 0 section 0', () => {
    cy.mount(TricolorSection, {
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
                    "text": "a"
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
                    "text": "b"
                  }
                ],
                "boxed": true
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "and"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "passiveSequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "c"
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
                    "text": "d"
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
        tricolored: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.multiple_choices_in_instructions_adaptation_tests.MultipleChoicesInInstructionsAdaptationTestCase.test_two_choices2.0.0')
  })

  it('renders gabby.adaptation.multiple_choices_in_instructions_adaptation_tests.MultipleChoicesInInstructionsAdaptationTestCase.test_two_choices2 pagelet 0 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "A"
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
                      "text": "a"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "b"
                    }
                  ]
                ]
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
                      "text": "c"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "d"
                    }
                  ]
                ]
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "B"
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
                      "text": "a"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "b"
                    }
                  ]
                ]
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
                      "text": "c"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "d"
                    }
                  ]
                ]
              }
            ]
          }
        ],
        first: false,
        centered: false,
        tricolored: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.multiple_choices_in_instructions_adaptation_tests.MultipleChoicesInInstructionsAdaptationTestCase.test_two_choices2.0.1')
  })
})
