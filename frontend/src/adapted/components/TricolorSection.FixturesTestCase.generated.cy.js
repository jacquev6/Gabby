import MonocolorSection from './MonocolorSection.vue'
import TricolorSection from './TricolorSection.vue'

describe('TricolorSection for FixturesTestCase', () => {
  beforeEach(() => {
    cy.viewport(1000, 100)
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_01 pagelet 0 section 0', () => {
    cy.mount(MonocolorSection, {
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
                "text": "avec"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": ":"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "passiveSequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "le"
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
                    "text": "une"
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
                    "text": "un"
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
                    "text": "des"
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
                    "text": "tu"
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
                    "text": "elles"
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
                    "text": "ils"
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
                "text": "Puis"
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
                "text": "souligne"
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
                "text": "verbes"
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
                "text": "Il"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "peut"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "y"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "avoir"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "plusieurs"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "solutions"
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
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_01.0.0')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_01 pagelet 0 section 1', () => {
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
                      "text": "Le"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Une"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Un"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Des"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Tu"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Elles"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Ils"
                    }
                  ]
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "vide"
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "multipleChoicesInput",
                "choices": [
                  [
                    {
                      "kind": "text",
                      "text": "Le"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Une"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Un"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Des"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Tu"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Elles"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Ils"
                    }
                  ]
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "vident"
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "multipleChoicesInput",
                "choices": [
                  [
                    {
                      "kind": "text",
                      "text": "Le"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Une"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Un"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Des"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Tu"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Elles"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Ils"
                    }
                  ]
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "d\u00e9penses"
              }
            ]
          }
        ],
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_01.0.1')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_01 pagelet 1 section 1', () => {
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
                      "text": "Le"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Une"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Un"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Des"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Tu"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Elles"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Ils"
                    }
                  ]
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "d\u00e9pensent"
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "multipleChoicesInput",
                "choices": [
                  [
                    {
                      "kind": "text",
                      "text": "Le"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Une"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Un"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Des"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Tu"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Elles"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Ils"
                    }
                  ]
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "savon"
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "multipleChoicesInput",
                "choices": [
                  [
                    {
                      "kind": "text",
                      "text": "Le"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Une"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Un"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Des"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Tu"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Elles"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Ils"
                    }
                  ]
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "savons"
              }
            ]
          }
        ],
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_01.1.1')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_01 pagelet 2 section 1', () => {
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
                      "text": "Le"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Une"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Un"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Des"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Tu"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Elles"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Ils"
                    }
                  ]
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "commande"
              }
            ]
          }
        ],
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_01.2.1')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_02 pagelet 0 section 0', () => {
    cy.mount(MonocolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "\u00c9cris"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "une"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "phrase"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "en"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "respectant"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "l"
              },
              {
                "kind": "text",
                "text": "'"
              },
              {
                "kind": "text",
                "text": "ordre"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "des"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "classes"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "grammaticales"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "indiqu\u00e9es"
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
                "text": "pronom"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "personnel"
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
                "text": "verbe"
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
                "text": "d\u00e9terminant"
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
                "text": "nom"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "commun"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": ":"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "Je"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "mange"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "une"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "pomme"
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
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_02.0.0')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_02 pagelet 0 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "nom"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "propre"
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
                "text": "verbe"
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
                "text": "d\u00e9terminant"
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
                "text": "adjectif"
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
                "text": "nom"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "commun"
              }
            ]
          }
        ],
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_02.0.1')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_03 pagelet 0 section 0', () => {
    cy.mount(MonocolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "Recopie"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "l"
              },
              {
                "kind": "text",
                "text": "\u2019"
              },
              {
                "kind": "text",
                "text": "intrus"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "qui"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "se"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "cache"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "dans"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "chaque"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "liste"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "et"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "\u00e9cris"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "sa"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "classe"
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
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_03.0.0')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_03 pagelet 0 section 1', () => {
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
                "kind": "text",
                "text": "partons"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "\u25c6"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "bidons"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "\u25c6"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "allons"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "\u25c6"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "vendons"
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
                "kind": "text",
                "text": "vidons"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "\u25c6"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "mentons"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "\u25c6"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "ballons"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "\u25c6"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "salons"
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
                "kind": "text",
                "text": "voir"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "\u25c6"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "armoire"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "\u25c6"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "couloir"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "\u25c6"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "dortoir"
              }
            ]
          }
        ],
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_03.0.1')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_04 pagelet 0 section 0', () => {
    cy.mount(MonocolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "Faire"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "des"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "choses"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "intelligentes"
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
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_04.0.0')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_05 pagelet 0 section 0', () => {
    cy.mount(MonocolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "Faire"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "d"
              },
              {
                "kind": "text",
                "text": "'"
              },
              {
                "kind": "text",
                "text": "autres"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "choses"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "intelligentes"
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
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_05.0.0')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_06 pagelet 0 section 0', () => {
    cy.mount(MonocolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "Prendre"
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
                "text": "temps"
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
                "text": "faire"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "aussi"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "des"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "choses"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "banales"
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
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_06.0.0')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_07 pagelet 0 section 0', () => {
    cy.mount(MonocolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "Rel\u00e8ve"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "dans"
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
                "text": "texte"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "trois"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "highlighted": "#ffff00",
                "text": "d\u00e9terminants"
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
                "text": "un"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "highlighted": "#ffc0cb",
                "text": "nom"
              },
              {
                "kind": "whitespace",
                "highlighted": "#ffc0cb"
              },
              {
                "kind": "text",
                "highlighted": "#ffc0cb",
                "text": "propre"
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
                "text": "quatre"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "highlighted": "#bbbbff",
                "text": "noms"
              },
              {
                "kind": "whitespace",
                "highlighted": "#bbbbff"
              },
              {
                "kind": "text",
                "highlighted": "#bbbbff",
                "text": "communs"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "et"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "trois"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "highlighted": "#bbffbb",
                "text": "verbes"
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
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_07.0.0')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_07 pagelet 0 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "Les"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "Touaregs"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "sont"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "des"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "Berb\u00e8res"
                  }
                ]
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
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
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "un"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "peuple"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "qui"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "habite"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "en"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "Afrique"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "du"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "Nord"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "depuis"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "la"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "pr\u00e9histoire"
                  }
                ]
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
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
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "Ils"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "vivent"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "dans"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "le"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "d\u00e9sert"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "du"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "Sahara"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "("
                  }
                ]
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "Alg\u00e9rie"
                  }
                ]
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
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
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "Libye"
                  }
                ]
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
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
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "Mali"
                  }
                ]
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
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
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "Niger"
                  }
                ]
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
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
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "Burkina"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "Faso"
                  }
                ]
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "\u2026"
                  }
                ]
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": ")"
                  }
                ]
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
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
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "En"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "\u00e9t\u00e9"
                  }
                ]
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
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
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "les"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "temp\u00e9ratures"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "y"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "montent"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "\u00e0"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "plus"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "de"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "50"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "\u00b0"
                  }
                ]
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "C"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "et"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "elles"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "descendent"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "en"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "dessous"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "de"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "z\u00e9ro"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "durant"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "les"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "nuits"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "d"
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
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "hiver"
                  }
                ]
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
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
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_07.0.1')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_07 pagelet 1 section 0', () => {
    cy.mount(MonocolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "Mon"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "quotidien"
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
                "text": "pour"
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
                "text": "10"
              },
              {
                "kind": "text",
                "text": "-"
              },
              {
                "kind": "text",
                "text": "14"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "ans"
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
                "text": "www"
              },
              {
                "kind": "text",
                "text": "."
              },
              {
                "kind": "text",
                "text": "monquotidien"
              },
              {
                "kind": "text",
                "text": "."
              },
              {
                "kind": "text",
                "text": "fr"
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
                "text": "13"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "septembre"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "2014"
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
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_07.1.0')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_08 pagelet 0 section 0', () => {
    cy.mount(MonocolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "Ajoute"
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
                "text": "suffixe"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "\u2013"
              },
              {
                "kind": "text",
                "text": "eur"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "aux"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "verbes"
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
                "text": "Indique"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "la"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "classe"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "des"
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
                "text": "fabriqu\u00e9s"
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
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_08.0.0')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_08 pagelet 0 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "nager"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "\u279e"
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
                "text": "\u25c6"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "tracter"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "\u279e"
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
                "text": "\u25c6"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "manger"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "\u279e"
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
                "text": "\u25c6"
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "inventer"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "\u279e"
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
                "text": "\u25c6"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "livrer"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "\u279e"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "freeTextInput"
              }
            ]
          }
        ],
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_08.0.1')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_09 pagelet 0 section 0', () => {
    cy.mount(MonocolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "R\u00e9ponds"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "par"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "passiveSequence",
                "contents": [
                  {
                    "kind": "text",
                    "text": "vrai"
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
                    "text": "faux"
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
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_09.0.0')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_09 pagelet 0 section 1', () => {
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
                "kind": "text",
                "text": "coccinelle"
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
                "text": "un"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "adjectif"
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
                      "text": "Vrai"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Faux"
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
                "kind": "text",
                "text": "b\u00fbche"
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
                "text": "un"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "verbe"
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
                      "text": "Vrai"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Faux"
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
                "kind": "text",
                "text": "cette"
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
                "text": "un"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "d\u00e9terminant"
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
                      "text": "Vrai"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Faux"
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
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_09.0.1')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_09 pagelet 1 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "d"
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
                "text": "dentier"
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
                "text": "un"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "verbe"
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
                      "text": "Vrai"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Faux"
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
                "text": "e"
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
                "text": "respirer"
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
                "text": "un"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "verbe"
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
                      "text": "Vrai"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Faux"
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
                "text": "f"
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
                "text": "aspiration"
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
                "text": "un"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "nom"
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
                      "text": "Vrai"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "Faux"
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
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_09.1.1')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_10 pagelet 0 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "Les"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "Touaregs"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "sont"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "des"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "Berb\u00e8res"
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
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "un"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "peuple"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "qui"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "habite"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "en"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "Afrique"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "du"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "Nord"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "depuis"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "la"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "pr\u00e9histoire"
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
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_10.0.1')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_10 pagelet 1 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "Ils"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "vivent"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "dans"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "le"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "d\u00e9sert"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "du"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "Sahara"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "("
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "Alg\u00e9rie"
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
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "Libye"
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
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "Mali"
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
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "Niger"
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
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "Burkina"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "Faso"
                  }
                ]
              },
              {
                "kind": "text",
                "text": "\u2026"
              },
              {
                "kind": "text",
                "text": ")"
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
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_10.1.1')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_10 pagelet 2 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "En"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "\u00e9t\u00e9"
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
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "les"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "temp\u00e9ratures"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "y"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "montent"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "\u00e0"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "plus"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "de"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "50"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "\u00b0"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "C"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "et"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "elles"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "descendent"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "en"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "dessous"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "de"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "z\u00e9ro"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "durant"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "les"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "nuits"
                  }
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "selectableInput",
                "colors": [
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "d"
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
                  "#ffff00",
                  "#ffc0cb",
                  "#bbbbff",
                  "#bbffbb"
                ],
                "contents": [
                  {
                    "kind": "text",
                    "text": "hiver"
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
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_10.2.1')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_11 pagelet 0 section 0', () => {
    cy.mount(MonocolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "..."
              }
            ]
          }
        ],
        first: false,
        centered: true,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_11.0.0')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_11 pagelet 0 section 1', () => {
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
                "kind": "text",
                "bold": true,
                "text": "Aujourd"
              },
              {
                "kind": "text",
                "bold": true,
                "text": "'"
              },
              {
                "kind": "text",
                "bold": true,
                "text": "hui"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "il"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "fait"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "italic": true,
                "text": "gris"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "et"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "("
              },
              {
                "kind": "text",
                "text": "il"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "pleuvra"
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
                "text": "il"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "pleut"
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
                "text": "il"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "pleuvait"
              },
              {
                "kind": "text",
                "text": ")"
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
                "kind": "text",
                "bold": true,
                "text": "Aujourd"
              },
              {
                "kind": "text",
                "bold": true,
                "text": "'"
              },
              {
                "kind": "text",
                "bold": true,
                "text": "hui"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "il"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "fait"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "italic": true,
                "text": "gris"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "et"
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
                      "text": "il"
                    },
                    {
                      "kind": "whitespace"
                    },
                    {
                      "kind": "text",
                      "text": "pleuvra"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "il"
                    },
                    {
                      "kind": "whitespace"
                    },
                    {
                      "kind": "text",
                      "text": "pleut"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "il"
                    },
                    {
                      "kind": "whitespace"
                    },
                    {
                      "kind": "text",
                      "text": "pleuvait"
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
                "kind": "text",
                "text": "Aujourd"
              },
              {
                "kind": "text",
                "text": "'"
              },
              {
                "kind": "text",
                "text": "hui"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "il"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "fait"
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
                      "text": "gris"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "beau"
                    }
                  ]
                ]
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "et"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "il"
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
                      "text": "pleut"
                    }
                  ],
                  [
                    {
                      "kind": "text",
                      "text": "pleuvra"
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
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_11.0.1')
  })
})
