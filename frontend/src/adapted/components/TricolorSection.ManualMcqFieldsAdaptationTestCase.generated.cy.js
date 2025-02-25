import TricolorSection from './TricolorSection.vue'

describe('TricolorSection for ManualMcqFieldsAdaptationTestCase', () => {
  beforeEach(() => {
    cy.viewport(1000, 100)
  })

  it('renders gabby.adaptation.manual_mcq_fields_adaptation_tests.ManualMcqFieldsAdaptationTestCase.test_simplest pagelet 0 section 0', () => {
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
        centered: false,
        tricolored: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.manual_mcq_fields_adaptation_tests.ManualMcqFieldsAdaptationTestCase.test_simplest.0.0')
  })

  it('renders gabby.adaptation.manual_mcq_fields_adaptation_tests.ManualMcqFieldsAdaptationTestCase.test_simplest pagelet 0 section 1', () => {
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
        tricolored: false,
        modelValue: {},
      },
    })
    cy.screenshot('gabby.adaptation.manual_mcq_fields_adaptation_tests.ManualMcqFieldsAdaptationTestCase.test_simplest.0.1')
  })
})
