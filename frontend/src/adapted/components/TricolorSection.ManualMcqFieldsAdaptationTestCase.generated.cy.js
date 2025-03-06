import MonocolorSection from './MonocolorSection.vue'
import TricolorSection from './TricolorSection.vue'

describe('TricolorSection for ManualMcqFieldsAdaptationTestCase', () => {
  beforeEach(() => {
    cy.viewport(1000, 100)
  })

  it('renders gabby.adaptation.manual_mcq_fields_adaptation_tests.ManualMcqFieldsAdaptationTestCase.test_simplest pagelet 0 section 0', () => {
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
    cy.screenshot('gabby.adaptation.manual_mcq_fields_adaptation_tests.ManualMcqFieldsAdaptationTestCase.test_simplest.0.1')
  })
})
