import MonocolorSection from './MonocolorSection.vue'
import TricolorSection from './TricolorSection.vue'

describe('TricolorSection for SelectThingsAdaptationTestCase', () => {
  beforeEach(() => {
    cy.viewport(1000, 100)
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_example_and_clue pagelet 0 section 0', () => {
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
        first: false,
        centered: true,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_example_and_clue.0.0')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_example_and_clue pagelet 0 section 1', () => {
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
                    "text": "wording"
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
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_example_and_clue.0.1')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_example_and_clue_with_sel_tags pagelet 0 section 0', () => {
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
          },
          {
            "contents": [
              {
                "kind": "text",
                "highlighted": "red",
                "text": "abc"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "highlighted": "green",
                "text": "def"
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "highlighted": "blue",
                "text": "ghi"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "jkl"
              }
            ]
          }
        ],
        first: false,
        centered: true,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_example_and_clue_with_sel_tags.0.0')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_example_and_clue_with_sel_tags pagelet 0 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "selectableInput",
                "colors": [
                  "red",
                  "green",
                  "blue"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "wording"
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
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_example_and_clue_with_sel_tags.0.1')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_french_elision_of_articles__punctuation_only pagelet 0 section 0', () => {
    cy.mount(MonocolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "Selectionne"
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
                "text": "articles"
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
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_french_elision_of_articles__punctuation_only.0.0')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_french_elision_of_articles__punctuation_only pagelet 0 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "La"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "maison"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "est"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "belle"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "padding": [
                  16.0,
                  3.2
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "."
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "L"
              },
              {
                "kind": "text",
                "text": "'"
              },
              {
                "kind": "text",
                "text": "\u00e9cole"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "est"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "ferm\u00e9e"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "padding": [
                  16.0,
                  3.2
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "."
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "L"
              },
              {
                "kind": "text",
                "text": "\u2019"
              },
              {
                "kind": "text",
                "text": "automobile"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "est"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "verte"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "padding": [
                  16.0,
                  3.2
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "."
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
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_french_elision_of_articles__punctuation_only.0.1')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_french_elision_of_articles__punctuation_only__boxed_only pagelet 0 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "La"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "maison"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "est"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "belle"
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
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "L"
              },
              {
                "kind": "text",
                "text": "'"
              },
              {
                "kind": "text",
                "text": "\u00e9cole"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "est"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "ferm\u00e9e"
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
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "L"
              },
              {
                "kind": "text",
                "text": "\u2019"
              },
              {
                "kind": "text",
                "text": "automobile"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "est"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "verte"
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
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_french_elision_of_articles__punctuation_only__boxed_only.0.1')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_french_elision_of_articles__with_punctuation pagelet 0 section 1', () => {
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
                    "text": "La"
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
                    "text": "maison"
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
                    "text": "est"
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
                    "text": "belle"
                  }
                ]
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "padding": [
                  16.0,
                  3.2
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "."
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
                    "text": "L"
                  },
                  {
                    "kind": "text",
                    "text": "'"
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
                    "text": "\u00e9cole"
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
                    "text": "est"
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
                    "text": "ferm\u00e9e"
                  }
                ]
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "padding": [
                  16.0,
                  3.2
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "."
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
                    "text": "L"
                  },
                  {
                    "kind": "text",
                    "text": "\u2019"
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
                    "text": "automobile"
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
                    "text": "est"
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
                    "text": "verte"
                  }
                ]
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "padding": [
                  16.0,
                  3.2
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "."
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
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_french_elision_of_articles__with_punctuation.0.1')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_french_elision_of_articles__with_punctuation__boxed_only pagelet 0 section 1', () => {
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
                    "text": "La"
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
                    "text": "maison"
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
                    "text": "est"
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
                    "text": "belle"
                  }
                ],
                "boxed": true
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
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "passiveSequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "L"
                  },
                  {
                    "kind": "text",
                    "text": "'"
                  }
                ],
                "boxed": true
              },
              {
                "kind": "passiveSequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "\u00e9cole"
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
                    "text": "est"
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
                    "text": "ferm\u00e9e"
                  }
                ],
                "boxed": true
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
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "passiveSequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "L"
                  },
                  {
                    "kind": "text",
                    "text": "\u2019"
                  }
                ],
                "boxed": true
              },
              {
                "kind": "passiveSequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "automobile"
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
                    "text": "est"
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
                    "text": "verte"
                  }
                ],
                "boxed": true
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
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_french_elision_of_articles__with_punctuation__boxed_only.0.1')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_french_elision_of_articles__without_punctuation pagelet 0 section 1', () => {
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
                    "text": "La"
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
                    "text": "maison"
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
                    "text": "est"
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
                    "text": "belle"
                  }
                ]
              },
              {
                "kind": "text",
                "text": "."
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
                    "text": "L"
                  },
                  {
                    "kind": "text",
                    "text": "'"
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
                    "text": "\u00e9cole"
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
                    "text": "est"
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
                    "text": "ferm\u00e9e"
                  }
                ]
              },
              {
                "kind": "text",
                "text": "."
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
                    "text": "L"
                  },
                  {
                    "kind": "text",
                    "text": "\u2019"
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
                    "text": "automobile"
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
                    "text": "est"
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
                    "text": "verte"
                  }
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
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_french_elision_of_articles__without_punctuation.0.1')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_french_elision_of_articles__without_punctuation__boxed_only pagelet 0 section 1', () => {
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
                    "text": "La"
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
                    "text": "maison"
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
                    "text": "est"
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
                    "text": "belle"
                  }
                ],
                "boxed": true
              },
              {
                "kind": "text",
                "text": "."
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "passiveSequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "L"
                  },
                  {
                    "kind": "text",
                    "text": "'"
                  }
                ],
                "boxed": true
              },
              {
                "kind": "passiveSequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "\u00e9cole"
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
                    "text": "est"
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
                    "text": "ferm\u00e9e"
                  }
                ],
                "boxed": true
              },
              {
                "kind": "text",
                "text": "."
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "passiveSequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "L"
                  },
                  {
                    "kind": "text",
                    "text": "\u2019"
                  }
                ],
                "boxed": true
              },
              {
                "kind": "passiveSequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "automobile"
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
                    "text": "est"
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
                    "text": "verte"
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
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_french_elision_of_articles__without_punctuation__boxed_only.0.1')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_multiple_lines_in_instructions pagelet 0 section 0', () => {
    cy.mount(MonocolorSection, {
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
        first: false,
        centered: true,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_multiple_lines_in_instructions.0.0')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_multiple_lines_in_wording pagelet 0 section 0', () => {
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
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_multiple_lines_in_wording.0.0')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_multiple_lines_in_wording pagelet 0 section 1', () => {
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
                    "text": "wording"
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
                    "text": "on"
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
                    "text": "multiple"
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
                    "text": "lines"
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
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_multiple_lines_in_wording.0.1')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_sel_tags pagelet 0 section 0', () => {
    cy.mount(MonocolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "highlighted": "red",
                "text": "abc"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "highlighted": "green",
                "text": "def"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "highlighted": "blue",
                "text": "ghi"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "jkl"
              }
            ]
          }
        ],
        first: false,
        centered: true,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_sel_tags.0.0')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_single_color pagelet 0 section 0', () => {
    cy.mount(MonocolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "highlighted": "red",
                "text": "abc"
              }
            ]
          }
        ],
        first: false,
        centered: true,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_single_color.0.0')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_single_sentence pagelet 0 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "selectableInput",
                "colors": [
                  "red",
                  "blue"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "The"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red",
                  "blue"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "wording"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red",
                  "blue"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "of"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red",
                  "blue"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "this"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red",
                  "blue"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "exercise"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red",
                  "blue"
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
                  "red",
                  "blue"
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
                  "red",
                  "blue"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "single"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red",
                  "blue"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "sentence"
                  }
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
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_single_sentence.0.1')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_strip_whitespace pagelet 0 section 0', () => {
    cy.mount(MonocolorSection, {
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
        first: false,
        centered: true,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_strip_whitespace.0.0')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_strip_whitespace pagelet 0 section 1', () => {
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
                    "text": "def"
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
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_strip_whitespace.0.1')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_unknown_tags pagelet 0 section 0', () => {
    cy.mount(MonocolorSection, {
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
        first: false,
        centered: true,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_unknown_tags.0.0')
  })

  it('renders gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_unknown_tags pagelet 0 section 1', () => {
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
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "tag"
                  }
                ]
              },
              {
                "kind": "text",
                "text": "|"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "def"
                  }
                ]
              },
              {
                "kind": "text",
                "text": "}"
              }
            ]
          }
        ],
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.select_things_adaptation_tests.SelectThingsAdaptationTestCase.test_unknown_tags.0.1')
  })
})
