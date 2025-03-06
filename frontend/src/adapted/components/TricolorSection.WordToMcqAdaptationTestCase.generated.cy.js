import MonocolorSection from './MonocolorSection.vue'
import TricolorSection from './TricolorSection.vue'

describe('TricolorSection for WordToMcqAdaptationTestCase', () => {
  beforeEach(() => {
    cy.viewport(1000, 100)
  })

  it('renders gabby.adaptation.word_to_mcq_adaptation_tests.WordToMcqAdaptationTestCase.test_words_in_sentences pagelet 0 section 0', () => {
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
    cy.screenshot('gabby.adaptation.word_to_mcq_adaptation_tests.WordToMcqAdaptationTestCase.test_words_in_sentences.0.0')
  })

  it('renders gabby.adaptation.word_to_mcq_adaptation_tests.WordToMcqAdaptationTestCase.test_words_in_sentences pagelet 0 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "a"
              },
              {
                "kind": "text",
                "text": "."
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "sequence",
                "contents": [
                  {
                    "kind": "sequence",
                    "contents": [
                      {
                        "kind": "text",
                        "text": "Firsta"
                      },
                      {
                        "kind": "whitespace"
                      },
                      {
                        "kind": "text",
                        "highlighted": "#ffff00",
                        "text": "firstb"
                      },
                      {
                        "kind": "whitespace"
                      },
                      {
                        "kind": "text",
                        "text": "firstc"
                      }
                    ]
                  },
                  {
                    "kind": "sequence",
                    "contents": [
                      {
                        "kind": "text",
                        "text": "\u2192"
                      },
                      {
                        "kind": "whitespace"
                      },
                      {
                        "kind": "text",
                        "text": "Firsta"
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
                          ],
                          [
                            {
                              "kind": "text",
                              "text": "charlie"
                            }
                          ]
                        ]
                      },
                      {
                        "kind": "whitespace"
                      },
                      {
                        "kind": "text",
                        "text": "firstc"
                      }
                    ]
                  }
                ],
                "vertical": true
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "b"
              },
              {
                "kind": "text",
                "text": "."
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "sequence",
                "contents": [
                  {
                    "kind": "sequence",
                    "contents": [
                      {
                        "kind": "text",
                        "highlighted": "#ffff00",
                        "text": "Seconda"
                      },
                      {
                        "kind": "whitespace"
                      },
                      {
                        "kind": "text",
                        "text": "secondb"
                      },
                      {
                        "kind": "whitespace"
                      },
                      {
                        "kind": "text",
                        "text": "secondc"
                      }
                    ]
                  },
                  {
                    "kind": "sequence",
                    "contents": [
                      {
                        "kind": "text",
                        "text": "\u2192"
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
                          ],
                          [
                            {
                              "kind": "text",
                              "text": "charlie"
                            }
                          ]
                        ]
                      },
                      {
                        "kind": "whitespace"
                      },
                      {
                        "kind": "text",
                        "text": "secondb"
                      },
                      {
                        "kind": "whitespace"
                      },
                      {
                        "kind": "text",
                        "text": "secondc"
                      }
                    ]
                  }
                ],
                "vertical": true
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "c"
              },
              {
                "kind": "text",
                "text": "."
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "sequence",
                "contents": [
                  {
                    "kind": "sequence",
                    "contents": [
                      {
                        "kind": "text",
                        "text": "Thirda"
                      },
                      {
                        "kind": "whitespace"
                      },
                      {
                        "kind": "text",
                        "text": "thirdb"
                      },
                      {
                        "kind": "whitespace"
                      },
                      {
                        "kind": "text",
                        "highlighted": "#ffff00",
                        "text": "thirdc"
                      }
                    ]
                  },
                  {
                    "kind": "sequence",
                    "contents": [
                      {
                        "kind": "text",
                        "text": "\u2192"
                      },
                      {
                        "kind": "whitespace"
                      },
                      {
                        "kind": "text",
                        "text": "Thirda"
                      },
                      {
                        "kind": "whitespace"
                      },
                      {
                        "kind": "text",
                        "text": "thirdb"
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
    cy.screenshot('gabby.adaptation.word_to_mcq_adaptation_tests.WordToMcqAdaptationTestCase.test_words_in_sentences.0.1')
  })
})
