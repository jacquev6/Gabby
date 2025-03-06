import MonocolorSection from './MonocolorSection.vue'
import TricolorSection from './TricolorSection.vue'

describe('TricolorSection for WordingPaginationTestCase', () => {
  beforeEach(() => {
    cy.viewport(1000, 100)
  })

  it('renders gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_full_pagelet pagelet 0 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "wording"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "1"
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "wording"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "2"
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "wording"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "3"
              }
            ]
          }
        ],
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_full_pagelet.0.1')
  })

  it('renders gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_manual_and_automated_pagination pagelet 0 section 0', () => {
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
                "text": "example"
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "clue"
              }
            ]
          }
        ],
        first: false,
        centered: true,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_manual_and_automated_pagination.0.0')
  })

  it('renders gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_manual_and_automated_pagination pagelet 0 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "wording"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "1"
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "wording"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "2"
              }
            ]
          }
        ],
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_manual_and_automated_pagination.0.1')
  })

  it('renders gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_manual_and_automated_pagination pagelet 1 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "wording"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "3"
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "wording"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "4"
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "wording"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "5"
              }
            ]
          }
        ],
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_manual_and_automated_pagination.1.1')
  })

  it('renders gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_manual_and_automated_pagination pagelet 2 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "wording"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "6"
              }
            ]
          }
        ],
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_manual_and_automated_pagination.2.1')
  })

  it('renders gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_no_pagination pagelet 0 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "wording"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "1"
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "wording"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "2"
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "wording"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "3"
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "wording"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "4"
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "wording"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "5"
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "wording"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "6"
              }
            ]
          }
        ],
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_no_pagination.0.1')
  })

  it('renders gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_one_letter_per_paragraph pagelet 0 section 0', () => {
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
    cy.screenshot('gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_one_letter_per_paragraph.0.0')
  })

  it('renders gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_one_letter_per_paragraph pagelet 0 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "a"
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "b"
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "c"
              }
            ]
          }
        ],
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_one_letter_per_paragraph.0.1')
  })

  it('renders gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_one_letter_per_paragraph pagelet 1 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "d"
              }
            ]
          }
        ],
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_one_letter_per_paragraph.1.1')
  })

  it('renders gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_one_manual_item_per_paragraph pagelet 0 section 0', () => {
    cy.mount(MonocolorSection, {
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
        first: false,
        centered: true,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_one_manual_item_per_paragraph.0.0')
  })

  it('renders gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_one_manual_item_per_paragraph pagelet 0 section 1', () => {
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
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "the"
              }
            ]
          },
          {
            "contents": [
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
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_one_manual_item_per_paragraph.0.1')
  })

  it('renders gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_one_punctuation_per_paragraph__plain pagelet 0 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "word"
              },
              {
                "kind": "text",
                "text": ","
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "word"
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "word"
              },
              {
                "kind": "text",
                "text": "!"
              }
            ]
          }
        ],
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_one_punctuation_per_paragraph__plain.0.1')
  })

  it('renders gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_one_punctuation_per_paragraph__plain pagelet 1 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "word"
              }
            ]
          }
        ],
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_one_punctuation_per_paragraph__plain.1.1')
  })

  it('renders gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_one_punctuation_per_paragraph__with_list pagelet 0 section 1', () => {
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
                "text": "word"
              },
              {
                "kind": "text",
                "text": ","
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "word"
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
                "text": "word"
              },
              {
                "kind": "text",
                "text": "!"
              }
            ]
          }
        ],
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_one_punctuation_per_paragraph__with_list.0.1')
  })

  it('renders gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_one_sentence_per_paragraph pagelet 0 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
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
                "text": "fait"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "beau"
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
                "text": "fait"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "chaud"
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
    cy.screenshot('gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_one_sentence_per_paragraph.0.1')
  })

  it('renders gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_one_sentence_per_paragraph pagelet 1 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
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
                "text": "ne"
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
                "text": "pas"
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
    cy.screenshot('gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_one_sentence_per_paragraph.1.1')
  })

  it('renders gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_one_word_per_paragraph__plain pagelet 0 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "worda"
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "wordb"
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "wordc"
              }
            ]
          }
        ],
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_one_word_per_paragraph__plain.0.1')
  })

  it('renders gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_one_word_per_paragraph__plain pagelet 1 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "wordd"
              }
            ]
          }
        ],
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_one_word_per_paragraph__plain.1.1')
  })

  it('renders gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_one_word_per_paragraph__with_list pagelet 0 section 1', () => {
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
                "text": "worda"
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "wordb"
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
                "text": "wordc"
              }
            ]
          }
        ],
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_one_word_per_paragraph__with_list.0.1')
  })

  it('renders gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_only_manual_pagination pagelet 1 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "wording"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "3"
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "wording"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "4"
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "wording"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "5"
              }
            ]
          },
          {
            "contents": [
              {
                "kind": "text",
                "text": "wording"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "6"
              }
            ]
          }
        ],
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_only_manual_pagination.1.1')
  })

  it('renders gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_single_paragraph pagelet 0 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "wording"
              }
            ]
          }
        ],
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_single_paragraph.0.1')
  })

  it('renders gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_single_paragraph_on_second_page pagelet 1 section 1', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [
          {
            "contents": [
              {
                "kind": "text",
                "text": "wording"
              },
              {
                "kind": "whitespace"
              },
              {
                "kind": "text",
                "text": "3"
              }
            ]
          }
        ],
        first: false,
        centered: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.wording_pagination_tests.WordingPaginationTestCase.test_single_paragraph_on_second_page.1.1')
  })
})
