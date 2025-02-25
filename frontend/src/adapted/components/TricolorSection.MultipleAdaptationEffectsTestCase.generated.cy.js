import TricolorSection from './TricolorSection.vue'

describe('TricolorSection for MultipleAdaptationEffectsTestCase', () => {
  beforeEach(() => {
    cy.viewport(1000, 100)
  })

  it('renders gabby.adaptation.multiple_adaptation_effects_tests.MultipleAdaptationEffectsTestCase.test_fill_with_free_text_and_multiple_choices_in_instructions pagelet 0 section 0', () => {
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
                "kind": "passiveSequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "short"
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
                    "text": "long"
                  }
                ],
                "boxed": true
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
    cy.screenshot('gabby.adaptation.multiple_adaptation_effects_tests.MultipleAdaptationEffectsTestCase.test_fill_with_free_text_and_multiple_choices_in_instructions.0.0')
  })

  it('renders gabby.adaptation.multiple_adaptation_effects_tests.MultipleAdaptationEffectsTestCase.test_fill_with_free_text_and_multiple_choices_in_instructions pagelet 0 section 1', () => {
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
                "kind": "multipleChoicesInput",
                "choices": [
                  [
                    {
                      "kind": "text",
                      "text": "short"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "long"
                    }
                  ]
                ]
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
        first: false,
        centered: false,
        tricolored: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.multiple_adaptation_effects_tests.MultipleAdaptationEffectsTestCase.test_fill_with_free_text_and_multiple_choices_in_instructions.0.1')
  })

  it('renders gabby.adaptation.multiple_adaptation_effects_tests.MultipleAdaptationEffectsTestCase.test_many_adaptations_in_same_exercise pagelet 0 section 0', () => {
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
        centered: false,
        tricolored: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.multiple_adaptation_effects_tests.MultipleAdaptationEffectsTestCase.test_many_adaptations_in_same_exercise.0.0')
  })

  it('renders gabby.adaptation.multiple_adaptation_effects_tests.MultipleAdaptationEffectsTestCase.test_many_adaptations_in_same_exercise pagelet 0 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "selectableInput",
                "colors": [
                  "red",
                  "yellow"
                ],
                "boxed": true,
                "contents": [
                  {
                    "kind": "text",
                    "text": "Hello"
                  }
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
                "kind": "multipleChoicesInput",
                "choices": [
                  [
                    {
                      "kind": "text",
                      "text": "charlie"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "delta"
                    }
                  ]
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "freeTextInput"
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
    cy.screenshot('gabby.adaptation.multiple_adaptation_effects_tests.MultipleAdaptationEffectsTestCase.test_many_adaptations_in_same_exercise.0.1')
  })

  it('renders gabby.adaptation.multiple_adaptation_effects_tests.MultipleAdaptationEffectsTestCase.test_multiple_choices_in_instructions_and_wording pagelet 0 section 0', () => {
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
        centered: false,
        tricolored: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.multiple_adaptation_effects_tests.MultipleAdaptationEffectsTestCase.test_multiple_choices_in_instructions_and_wording.0.0')
  })

  it('renders gabby.adaptation.multiple_adaptation_effects_tests.MultipleAdaptationEffectsTestCase.test_multiple_choices_in_instructions_and_wording pagelet 0 section 1', () => {
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
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "C"
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
        first: false,
        centered: false,
        tricolored: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.multiple_adaptation_effects_tests.MultipleAdaptationEffectsTestCase.test_multiple_choices_in_instructions_and_wording.0.1')
  })
})
