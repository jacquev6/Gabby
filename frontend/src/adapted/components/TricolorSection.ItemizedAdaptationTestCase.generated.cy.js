import TricolorSection from './TricolorSection.vue'

describe('TricolorSection for ItemizedAdaptationTestCase', () => {
  beforeEach(() => {
    cy.viewport(1000, 100)
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_boxed_words pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "Instructions"
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_boxed_words.0.instructions')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_boxed_words pagelet 0 wording', () => {
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
                    "text": "This"
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
                    "text": "is"
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
                    "text": "the"
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
                    "text": "wording"
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
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_boxed_words.0.wording')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_gender_and_number_mcq pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "alpha"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "multipleChoicesInput",
                "show_arrow_before": true,
                "choices": [
                  [
                    {
                      "kind": "text",
                      "text": "f\u00e9minin"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "masculin"
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
                      "text": "singulier"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "pluriel"
                    }
                  ]
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "bravo"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "multipleChoicesInput",
                "show_arrow_before": true,
                "choices": [
                  [
                    {
                      "kind": "text",
                      "text": "f\u00e9minin"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "masculin"
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
                      "text": "singulier"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "pluriel"
                    }
                  ]
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "charlie"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "multipleChoicesInput",
                "show_arrow_before": true,
                "choices": [
                  [
                    {
                      "kind": "text",
                      "text": "f\u00e9minin"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "masculin"
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
                      "text": "singulier"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "pluriel"
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
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_gender_and_number_mcq.0.wording')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_gender_and_number_mcq__single_item_per_paragraph pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "alpha"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "multipleChoicesInput",
                "show_arrow_before": true,
                "choices": [
                  [
                    {
                      "kind": "text",
                      "text": "f\u00e9minin"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "masculin"
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
                      "text": "singulier"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "pluriel"
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
                "text": "bravo"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "multipleChoicesInput",
                "show_arrow_before": true,
                "choices": [
                  [
                    {
                      "kind": "text",
                      "text": "f\u00e9minin"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "masculin"
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
                      "text": "singulier"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "pluriel"
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
                "text": "charlie"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "multipleChoicesInput",
                "show_arrow_before": true,
                "choices": [
                  [
                    {
                      "kind": "text",
                      "text": "f\u00e9minin"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "masculin"
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
                      "text": "singulier"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "pluriel"
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
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_gender_and_number_mcq__single_item_per_paragraph.0.wording')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_gender_mcq pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "alpha"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "multipleChoicesInput",
                "show_arrow_before": true,
                "choices": [
                  [
                    {
                      "kind": "text",
                      "text": "f\u00e9minin"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "masculin"
                    }
                  ]
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "bravo"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "multipleChoicesInput",
                "show_arrow_before": true,
                "choices": [
                  [
                    {
                      "kind": "text",
                      "text": "f\u00e9minin"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "masculin"
                    }
                  ]
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "charlie"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "multipleChoicesInput",
                "show_arrow_before": true,
                "choices": [
                  [
                    {
                      "kind": "text",
                      "text": "f\u00e9minin"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "masculin"
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
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_gender_mcq.0.wording')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_mcq_below_letters pagelet 0 instructions', () => {
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
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_mcq_below_letters.0.instructions')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_mcq_below_letters pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "sequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "A"
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
                ],
                "vertical": true
              },
              {
                "kind": "sequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "b"
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
                ],
                "vertical": true
              },
              {
                "kind": "sequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "c"
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
                ],
                "vertical": true
              },
              {
                "kind": "sequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "d"
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
                ],
                "vertical": true
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_mcq_below_letters.0.wording')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_mcq_below_manual_items pagelet 0 wording', () => {
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
                "kind": "sequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "is"
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
                ],
                "vertical": true
              },
              {
                "kind": "text",
                "text": ","
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "sequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "the"
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
                ],
                "vertical": true
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
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_mcq_below_manual_items.0.wording')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_mcq_below_punctuation pagelet 0 wording', () => {
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
                "kind": "sequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": ","
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
                ],
                "vertical": true
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
                "kind": "sequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "."
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
                ],
                "vertical": true
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_mcq_below_punctuation.0.wording')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_mcq_below_sentences pagelet 0 wording', () => {
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
                        "text": "Affirmative"
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
                ],
                "vertical": true
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
                        "text": "Exclamative"
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
                        "text": "!"
                      }
                    ]
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
                ],
                "vertical": true
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
                        "text": "Phrase"
                      },
                      {
                        "kind": "whitespace"
                      },
                      {
                        "kind": "text",
                        "text": "exclamative"
                      },
                      {
                        "kind": "whitespace"
                      },
                      {
                        "kind": "text",
                        "text": "!"
                      }
                    ]
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
                ],
                "vertical": true
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
                        "text": "Interrogative"
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
                        "text": "?"
                      }
                    ]
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
                ],
                "vertical": true
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
                        "text": "Phrase"
                      },
                      {
                        "kind": "whitespace"
                      },
                      {
                        "kind": "text",
                        "text": "interrogative"
                      },
                      {
                        "kind": "whitespace"
                      },
                      {
                        "kind": "text",
                        "text": "?"
                      }
                    ]
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
                ],
                "vertical": true
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
                        "text": "Suspens"
                      },
                      {
                        "kind": "text",
                        "text": "..."
                      }
                    ]
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
                ],
                "vertical": true
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_mcq_below_sentences.0.wording')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_mcq_below_separated_items pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "Indique"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "le"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "genre"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "de"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "chacun"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "de"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "ces"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "groupes"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "nominaux"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "("
              },
              {
                "kind": "passiveSequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "singulier"
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
                    "text": "pluriel"
                  }
                ],
                "boxed": true
              },
              {
                "kind": "text",
                "text": ")"
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_mcq_below_separated_items.0.instructions')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_mcq_below_separated_items pagelet 0 wording', () => {
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
                        "text": "les"
                      },
                      {
                        "kind": "whitespace"
                      },
                      {
                        "kind": "text",
                        "text": "tables"
                      }
                    ]
                  },
                  {
                    "kind": "multipleChoicesInput",
                    "choices": [
                      [
                        {
                          "kind": "text",
                          "text": "singulier"
                        }
                      ],
                      [
                        {
                          "kind": "text",
                          "text": "pluriel"
                        }
                      ]
                    ]
                  }
                ],
                "vertical": true
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
                        "text": "les"
                      },
                      {
                        "kind": "whitespace"
                      },
                      {
                        "kind": "text",
                        "text": "chaises"
                      }
                    ]
                  },
                  {
                    "kind": "multipleChoicesInput",
                    "choices": [
                      [
                        {
                          "kind": "text",
                          "text": "singulier"
                        }
                      ],
                      [
                        {
                          "kind": "text",
                          "text": "pluriel"
                        }
                      ]
                    ]
                  }
                ],
                "vertical": true
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
                        "text": "les"
                      },
                      {
                        "kind": "whitespace"
                      },
                      {
                        "kind": "text",
                        "text": "fauteuils"
                      }
                    ]
                  },
                  {
                    "kind": "multipleChoicesInput",
                    "choices": [
                      [
                        {
                          "kind": "text",
                          "text": "singulier"
                        }
                      ],
                      [
                        {
                          "kind": "text",
                          "text": "pluriel"
                        }
                      ]
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
                        "text": "les"
                      },
                      {
                        "kind": "whitespace"
                      },
                      {
                        "kind": "text",
                        "text": "enfants"
                      }
                    ]
                  },
                  {
                    "kind": "multipleChoicesInput",
                    "choices": [
                      [
                        {
                          "kind": "text",
                          "text": "singulier"
                        }
                      ],
                      [
                        {
                          "kind": "text",
                          "text": "pluriel"
                        }
                      ]
                    ]
                  }
                ],
                "vertical": true
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
                        "text": "les"
                      },
                      {
                        "kind": "whitespace"
                      },
                      {
                        "kind": "text",
                        "text": "personnes"
                      },
                      {
                        "kind": "whitespace"
                      },
                      {
                        "kind": "text",
                        "text": "\u00e2g\u00e9es"
                      }
                    ]
                  },
                  {
                    "kind": "multipleChoicesInput",
                    "choices": [
                      [
                        {
                          "kind": "text",
                          "text": "singulier"
                        }
                      ],
                      [
                        {
                          "kind": "text",
                          "text": "pluriel"
                        }
                      ]
                    ]
                  }
                ],
                "vertical": true
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
                        "text": "les"
                      },
                      {
                        "kind": "whitespace"
                      },
                      {
                        "kind": "text",
                        "text": "adultes"
                      }
                    ]
                  },
                  {
                    "kind": "multipleChoicesInput",
                    "choices": [
                      [
                        {
                          "kind": "text",
                          "text": "singulier"
                        }
                      ],
                      [
                        {
                          "kind": "text",
                          "text": "pluriel"
                        }
                      ]
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
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_mcq_below_separated_items.0.wording')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_mcq_below_words pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "sequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "This"
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
                ],
                "vertical": true
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "sequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "is"
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
                ],
                "vertical": true
              },
              {
                "kind": "text",
                "text": ","
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "sequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "the"
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
                ],
                "vertical": true
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "sequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "wording"
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
                ],
                "vertical": true
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
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_mcq_below_words.0.wording')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_mcq_below_words_and_punctuation pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "sequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "This"
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
                ],
                "vertical": true
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "sequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "is"
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
                ],
                "vertical": true
              },
              {
                "kind": "sequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": ","
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
                ],
                "vertical": true
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "sequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "the"
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
                ],
                "vertical": true
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "sequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "wording"
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
                ],
                "vertical": true
              },
              {
                "kind": "sequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "."
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
                ],
                "vertical": true
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_mcq_below_words_and_punctuation.0.wording')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_mcq_beside_letters pagelet 0 wording', () => {
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
                "kind": "text",
                "text": "b"
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
                "kind": "text",
                "text": "c"
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
                "kind": "text",
                "text": "d"
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
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_mcq_beside_letters.0.wording')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_mcq_beside_manual_items pagelet 0 wording', () => {
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
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_mcq_beside_manual_items.0.wording')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_mcq_beside_punctuation pagelet 0 wording', () => {
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
                "kind": "text",
                "text": ","
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
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_mcq_beside_punctuation.0.wording')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_mcq_beside_sentences pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "Affirmative"
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
                "text": "Exclamative"
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
                "text": "!"
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
                "text": "Phrase"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "exclamative"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "!"
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
                "text": "Interrogative"
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
                "text": "?"
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
                "text": "Phrase"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "interrogative"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "?"
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
                "text": "Suspens"
              },
              {
                "kind": "text",
                "text": "..."
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
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_mcq_beside_sentences.0.wording')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_mcq_beside_words pagelet 0 wording', () => {
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
                "text": "wording"
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
                "kind": "text",
                "text": "."
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_mcq_beside_words.0.wording')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_mcq_beside_words_and_punctuation pagelet 0 wording', () => {
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
                "kind": "text",
                "text": ","
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
                "text": "the"
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
                "text": "wording"
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
                "kind": "text",
                "text": "."
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
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_mcq_beside_words_and_punctuation.0.wording')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_number_mcq pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "alpha"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "multipleChoicesInput",
                "show_arrow_before": true,
                "choices": [
                  [
                    {
                      "kind": "text",
                      "text": "singulier"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "pluriel"
                    }
                  ]
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "bravo"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "multipleChoicesInput",
                "show_arrow_before": true,
                "choices": [
                  [
                    {
                      "kind": "text",
                      "text": "singulier"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "pluriel"
                    }
                  ]
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "charlie"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "multipleChoicesInput",
                "show_arrow_before": true,
                "choices": [
                  [
                    {
                      "kind": "text",
                      "text": "singulier"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "pluriel"
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
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_number_mcq.0.wording')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_sel_tags pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
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
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_sel_tags.0.instructions')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_sel_tags pagelet 0 wording', () => {
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
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_sel_tags.0.wording')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_selectable_letters pagelet 0 wording', () => {
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
                    "text": "T"
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
                    "text": "h"
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
                    "text": "i"
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
                    "text": "s"
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
                    "text": "i"
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
                    "text": "s"
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
                    "text": "t"
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
                    "text": "h"
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
                    "text": "e"
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
                    "text": "w"
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
                    "text": "o"
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
                    "text": "r"
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
                    "text": "d"
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
                    "text": "i"
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
                    "text": "n"
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
                    "text": "g"
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
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_selectable_letters.0.wording')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_selectable_manual_items__boxed pagelet 0 wording', () => {
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
                "kind": "selectableInput",
                "colors": [
                  "red",
                  "blue"
                ],
                "boxed": true,
                "contents": [
                  {
                    "kind": "text",
                    "text": "is"
                  },
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
                  "red",
                  "blue"
                ],
                "boxed": true,
                "contents": [
                  {
                    "kind": "text",
                    "text": "the"
                  }
                ]
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
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_selectable_manual_items__boxed.0.wording')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_selectable_manual_items__plain pagelet 0 wording', () => {
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
                "kind": "selectableInput",
                "colors": [
                  "red",
                  "blue"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "is"
                  },
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
                  "red",
                  "blue"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "the"
                  }
                ]
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
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_selectable_manual_items__plain.0.wording')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_selectable_punctuation_only pagelet 0 wording', () => {
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
                "kind": "selectableInput",
                "colors": [
                  "green",
                  "yellow",
                  "orange"
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
                "kind": "selectableInput",
                "colors": [
                  "green",
                  "yellow",
                  "orange"
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
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_selectable_punctuation_only.0.wording')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_selectable_sentences pagelet 0 wording', () => {
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
                "boxed": true,
                "contents": [
                  {
                    "kind": "text",
                    "text": "Affirmative"
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
                "boxed": true,
                "contents": [
                  {
                    "kind": "text",
                    "text": "Exclamative"
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
                    "text": "!"
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
                "boxed": true,
                "contents": [
                  {
                    "kind": "text",
                    "text": "Phrase"
                  },
                  {
                    "kind": "whitespace"
                  },
                  {
                    "kind": "text",
                    "text": "exclamative"
                  },
                  {
                    "kind": "whitespace"
                  },
                  {
                    "kind": "text",
                    "text": "!"
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
                "boxed": true,
                "contents": [
                  {
                    "kind": "text",
                    "text": "Interrogative"
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
                    "text": "?"
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
                "boxed": true,
                "contents": [
                  {
                    "kind": "text",
                    "text": "Phrase"
                  },
                  {
                    "kind": "whitespace"
                  },
                  {
                    "kind": "text",
                    "text": "interrogative"
                  },
                  {
                    "kind": "whitespace"
                  },
                  {
                    "kind": "text",
                    "text": "?"
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
                "boxed": true,
                "contents": [
                  {
                    "kind": "text",
                    "text": "Suspens"
                  },
                  {
                    "kind": "text",
                    "text": "..."
                  }
                ]
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_selectable_sentences.0.wording')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_selectable_tokens__in_bullet_list pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "\u25c6"
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
                    "text": "First"
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
                    "text": "list"
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
                    "text": "element"
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
                "kind": "text",
                "text": "\u25c6"
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
                    "text": "Second"
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
                    "text": "element"
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
                    "text": "still"
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
                    "text": "in"
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
                    "text": "list"
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
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_selectable_tokens__in_bullet_list.0.wording')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_selectable_tokens__in_bullet_list pagelet 1 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "\u25c6"
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
                    "text": "Third"
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
                    "text": "element"
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
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "last"
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
                    "text": "one"
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
                    "text": "!"
                  }
                ]
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_selectable_tokens__in_bullet_list.1.wording')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_selectable_tokens__in_lettered_list pagelet 0 wording', () => {
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
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "First"
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
                    "text": "list"
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
                    "text": "element"
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
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "Second"
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
                    "text": "element"
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
                    "text": "still"
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
                    "text": "in"
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
                    "text": "list"
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
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_selectable_tokens__in_lettered_list.0.wording')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_selectable_tokens__in_lettered_list pagelet 1 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
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
                "kind": "selectableInput",
                "colors": [
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "Third"
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
                    "text": "element"
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
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "last"
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
                    "text": "one"
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
                    "text": "!"
                  }
                ]
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_selectable_tokens__in_lettered_list.1.wording')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_selectable_tokens__in_numbered_list pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "1"
              },
              {
                "kind": "text",
                "text": ")"
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
                    "text": "First"
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
                    "text": "list"
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
                    "text": "element"
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
                "kind": "text",
                "text": "2"
              },
              {
                "kind": "text",
                "text": ")"
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
                    "text": "Second"
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
                    "text": "element"
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
                    "text": "still"
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
                    "text": "in"
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
                    "text": "list"
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
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_selectable_tokens__in_numbered_list.0.wording')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_selectable_tokens__in_numbered_list pagelet 1 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "3"
              },
              {
                "kind": "text",
                "text": ")"
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
                    "text": "Third"
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
                    "text": "element"
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
                  "red"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "last"
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
                    "text": "one"
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
                    "text": "!"
                  }
                ]
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_selectable_tokens__in_numbered_list.1.wording')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_selectable_words__boxed pagelet 0 wording', () => {
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
                "boxed": true,
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
                  "red",
                  "blue"
                ],
                "boxed": true,
                "contents": [
                  {
                    "kind": "text",
                    "text": "is"
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
                  "red",
                  "blue"
                ],
                "boxed": true,
                "contents": [
                  {
                    "kind": "text",
                    "text": "the"
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
                "boxed": true,
                "contents": [
                  {
                    "kind": "text",
                    "text": "wording"
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
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_selectable_words__boxed.0.wording')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_selectable_words__plain pagelet 0 wording', () => {
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
                "kind": "text",
                "text": ","
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
                    "text": "the"
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
                "kind": "text",
                "text": "."
              }
            ]
          }
        ],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_selectable_words__plain.0.wording')
  })

  it('renders gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_selectable_words_and_punctuation pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "selectableInput",
                "colors": [
                  "green",
                  "yellow",
                  "orange"
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
                  "green",
                  "yellow",
                  "orange"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "is"
                  }
                ]
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "green",
                  "yellow",
                  "orange"
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
                  "green",
                  "yellow",
                  "orange"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "the"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "green",
                  "yellow",
                  "orange"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "wording"
                  }
                ]
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "green",
                  "yellow",
                  "orange"
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
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.itemized_adaptation_tests.ItemizedAdaptationTestCase.test_selectable_words_and_punctuation.0.wording')
  })
})
