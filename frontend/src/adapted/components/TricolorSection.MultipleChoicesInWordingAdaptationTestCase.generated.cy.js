import TricolorSection from './TricolorSection.vue'

describe('TricolorSection for MultipleChoicesInWordingAdaptationTestCase', () => {
  beforeEach(() => {
    cy.viewport(1000, 100)
  })

  it('renders gabby.adaptation.multiple_choices_in_wording_adaptation_tests.MultipleChoicesInWordingAdaptationTestCase.test_choices2_with_empty_separator pagelet 0 section 0', () => {
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
                "kind": "text",
                "text": "wisely"
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
    cy.screenshot('gabby.adaptation.multiple_choices_in_wording_adaptation_tests.MultipleChoicesInWordingAdaptationTestCase.test_choices2_with_empty_separator.0.0')
  })

  it('renders gabby.adaptation.multiple_choices_in_wording_adaptation_tests.MultipleChoicesInWordingAdaptationTestCase.test_choices2_with_empty_separator pagelet 0 section 1', () => {
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
                      "text": "blah"
                    },
                    {
                      "kind": "whitespace"
                    },
                    {
                      "kind": "text",
                      "text": "/"
                    },
                    {
                      "kind": "whitespace"
                    },
                    {
                      "kind": "text",
                      "text": "blih"
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
        first: false,
        centered: false,
        tricolored: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.multiple_choices_in_wording_adaptation_tests.MultipleChoicesInWordingAdaptationTestCase.test_choices2_with_empty_separator.0.1')
  })

  it('renders gabby.adaptation.multiple_choices_in_wording_adaptation_tests.MultipleChoicesInWordingAdaptationTestCase.test_choices2_with_empty_start_and_stop pagelet 0 section 1', () => {
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
                      "text": "blah"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "blih"
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
        first: false,
        centered: false,
        tricolored: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.multiple_choices_in_wording_adaptation_tests.MultipleChoicesInWordingAdaptationTestCase.test_choices2_with_empty_start_and_stop.0.1')
  })

  it('renders gabby.adaptation.multiple_choices_in_wording_adaptation_tests.MultipleChoicesInWordingAdaptationTestCase.test_choices2_with_placeholder_after pagelet 0 section 1', () => {
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
                "text": "sky"
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
                "kind": "multipleChoicesInput",
                "choices": [
                  [
                    {
                      "kind": "text",
                      "text": "blue"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "red"
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
        first: false,
        centered: false,
        tricolored: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.multiple_choices_in_wording_adaptation_tests.MultipleChoicesInWordingAdaptationTestCase.test_choices2_with_placeholder_after.0.1')
  })

  it('renders gabby.adaptation.multiple_choices_in_wording_adaptation_tests.MultipleChoicesInWordingAdaptationTestCase.test_choices2_with_two_placeholders pagelet 0 section 1', () => {
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
                "text": "sky"
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
                "kind": "multipleChoicesInput",
                "choices": [
                  [
                    {
                      "kind": "text",
                      "text": "blue"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "yellow"
                    }
                  ]
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
                "kind": "text",
                "text": "the"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "sun"
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
                "kind": "multipleChoicesInput",
                "choices": [
                  [
                    {
                      "kind": "text",
                      "text": "blue"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "yellow"
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
        first: false,
        centered: false,
        tricolored: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.multiple_choices_in_wording_adaptation_tests.MultipleChoicesInWordingAdaptationTestCase.test_choices2_with_two_placeholders.0.1')
  })

  it('renders gabby.adaptation.multiple_choices_in_wording_adaptation_tests.MultipleChoicesInWordingAdaptationTestCase.test_simple pagelet 0 section 1', () => {
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
                      "text": "d"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "e"
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
        first: false,
        centered: false,
        tricolored: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.multiple_choices_in_wording_adaptation_tests.MultipleChoicesInWordingAdaptationTestCase.test_simple.0.1')
  })

  it('renders gabby.adaptation.multiple_choices_in_wording_adaptation_tests.MultipleChoicesInWordingAdaptationTestCase.test_two_choices2_with_identical_placeholders pagelet 0 section 1', () => {
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
                "text": "sky"
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
                "kind": "multipleChoicesInput",
                "choices": [
                  [
                    {
                      "kind": "text",
                      "text": "blue"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "red"
                    }
                  ]
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
                "kind": "text",
                "text": "The"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "sun"
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
                "kind": "multipleChoicesInput",
                "choices": [
                  [
                    {
                      "kind": "text",
                      "text": "green"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "yellow"
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
        first: false,
        centered: false,
        tricolored: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.multiple_choices_in_wording_adaptation_tests.MultipleChoicesInWordingAdaptationTestCase.test_two_choices2_with_identical_placeholders.0.1')
  })

  it('renders gabby.adaptation.multiple_choices_in_wording_adaptation_tests.MultipleChoicesInWordingAdaptationTestCase.test_two_choices2_with_matching_placeholders pagelet 0 section 1', () => {
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
                "text": "sky"
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
                "kind": "multipleChoicesInput",
                "choices": [
                  [
                    {
                      "kind": "text",
                      "text": "blue"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "red"
                    }
                  ]
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
                "kind": "text",
                "text": "the"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "sun"
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
                "kind": "multipleChoicesInput",
                "choices": [
                  [
                    {
                      "kind": "text",
                      "text": "green"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "yellow"
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
        first: false,
        centered: false,
        tricolored: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.multiple_choices_in_wording_adaptation_tests.MultipleChoicesInWordingAdaptationTestCase.test_two_choices2_with_matching_placeholders.0.1')
  })
})
