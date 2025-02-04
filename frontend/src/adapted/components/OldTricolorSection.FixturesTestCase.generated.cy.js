import TricolorSection from './OldTricolorSection.vue'

describe('TricolorSection for FixturesTestCase', () => {
  beforeEach(() => {
    cy.viewport(1000, 100)
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_01 pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "Compl\u00e8te"}, {"type": "whitespace"}, {"type": "plainText", "text": "avec"}, {"type": "whitespace"}, {"type": "plainText", "text": ":"}, {"type": "whitespace"}, {"type": "boxedText", "text": "le"}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "boxedText", "text": "une"}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "boxedText", "text": "un"}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "boxedText", "text": "des"}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "boxedText", "text": "tu"}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "boxedText", "text": "elles"}, {"type": "whitespace"}, {"type": "plainText", "text": "ou"}, {"type": "whitespace"}, {"type": "boxedText", "text": "ils"}, {"type": "plainText", "text": "."}]}, {"tokens": [{"type": "plainText", "text": "Puis"}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "plainText", "text": "souligne"}, {"type": "whitespace"}, {"type": "plainText", "text": "les"}, {"type": "whitespace"}, {"type": "plainText", "text": "verbes"}, {"type": "plainText", "text": "."}]}, {"tokens": [{"type": "plainText", "text": "Il"}, {"type": "whitespace"}, {"type": "plainText", "text": "peut"}, {"type": "whitespace"}, {"type": "plainText", "text": "y"}, {"type": "whitespace"}, {"type": "plainText", "text": "avoir"}, {"type": "whitespace"}, {"type": "plainText", "text": "plusieurs"}, {"type": "whitespace"}, {"type": "plainText", "text": "solutions"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_01.0.instructions')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_01 pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["le", "une", "un", "des", "tu", "elles", "ils"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "plainText", "text": "vide"}]}, {"tokens": [{"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["le", "une", "un", "des", "tu", "elles", "ils"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "plainText", "text": "vident"}]}, {"tokens": [{"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["le", "une", "un", "des", "tu", "elles", "ils"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "plainText", "text": "d\u00e9penses"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_01.0.wording')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_01 pagelet 1 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["le", "une", "un", "des", "tu", "elles", "ils"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "plainText", "text": "d\u00e9pensent"}]}, {"tokens": [{"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["le", "une", "un", "des", "tu", "elles", "ils"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "plainText", "text": "savon"}]}, {"tokens": [{"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["le", "une", "un", "des", "tu", "elles", "ils"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "plainText", "text": "savons"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_01.1.wording')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_01 pagelet 2 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["le", "une", "un", "des", "tu", "elles", "ils"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "plainText", "text": "commande"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_01.2.wording')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_02 pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "\u00c9cris"}, {"type": "whitespace"}, {"type": "plainText", "text": "une"}, {"type": "whitespace"}, {"type": "plainText", "text": "phrase"}, {"type": "whitespace"}, {"type": "plainText", "text": "en"}, {"type": "whitespace"}, {"type": "plainText", "text": "respectant"}, {"type": "whitespace"}, {"type": "plainText", "text": "l"}, {"type": "plainText", "text": "'"}, {"type": "plainText", "text": "ordre"}, {"type": "whitespace"}, {"type": "plainText", "text": "des"}, {"type": "whitespace"}, {"type": "plainText", "text": "classes"}, {"type": "whitespace"}, {"type": "plainText", "text": "grammaticales"}, {"type": "whitespace"}, {"type": "plainText", "text": "indiqu\u00e9es"}, {"type": "plainText", "text": "."}]}, {"tokens": [{"type": "plainText", "text": "pronom"}, {"type": "whitespace"}, {"type": "plainText", "text": "personnel"}, {"type": "whitespace"}, {"type": "plainText", "text": "/"}, {"type": "whitespace"}, {"type": "plainText", "text": "verbe"}, {"type": "whitespace"}, {"type": "plainText", "text": "/"}, {"type": "whitespace"}, {"type": "plainText", "text": "d\u00e9terminant"}, {"type": "whitespace"}, {"type": "plainText", "text": "/"}, {"type": "whitespace"}, {"type": "plainText", "text": "nom"}, {"type": "whitespace"}, {"type": "plainText", "text": "commun"}, {"type": "whitespace"}, {"type": "plainText", "text": ":"}, {"type": "whitespace"}, {"type": "plainText", "text": "Je"}, {"type": "whitespace"}, {"type": "plainText", "text": "mange"}, {"type": "whitespace"}, {"type": "plainText", "text": "une"}, {"type": "whitespace"}, {"type": "plainText", "text": "pomme"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_02.0.instructions')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_02 pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "nom"}, {"type": "whitespace"}, {"type": "plainText", "text": "propre"}, {"type": "whitespace"}, {"type": "plainText", "text": "/"}, {"type": "whitespace"}, {"type": "plainText", "text": "verbe"}, {"type": "whitespace"}, {"type": "plainText", "text": "/"}, {"type": "whitespace"}, {"type": "plainText", "text": "d\u00e9terminant"}, {"type": "whitespace"}, {"type": "plainText", "text": "/"}, {"type": "whitespace"}, {"type": "plainText", "text": "adjectif"}, {"type": "whitespace"}, {"type": "plainText", "text": "/"}, {"type": "whitespace"}, {"type": "plainText", "text": "nom"}, {"type": "whitespace"}, {"type": "plainText", "text": "commun"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_02.0.wording')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_03 pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "Recopie"}, {"type": "whitespace"}, {"type": "plainText", "text": "l"}, {"type": "plainText", "text": "\u2019"}, {"type": "plainText", "text": "intrus"}, {"type": "whitespace"}, {"type": "plainText", "text": "qui"}, {"type": "whitespace"}, {"type": "plainText", "text": "se"}, {"type": "whitespace"}, {"type": "plainText", "text": "cache"}, {"type": "whitespace"}, {"type": "plainText", "text": "dans"}, {"type": "whitespace"}, {"type": "plainText", "text": "chaque"}, {"type": "whitespace"}, {"type": "plainText", "text": "liste"}, {"type": "whitespace"}, {"type": "plainText", "text": "et"}, {"type": "whitespace"}, {"type": "plainText", "text": "\u00e9cris"}, {"type": "whitespace"}, {"type": "plainText", "text": "sa"}, {"type": "whitespace"}, {"type": "plainText", "text": "classe"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_03.0.instructions')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_03 pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "a"}, {"type": "plainText", "text": "."}, {"type": "whitespace"}, {"type": "plainText", "text": "partons"}, {"type": "whitespace"}, {"type": "plainText", "text": "\u25c6"}, {"type": "whitespace"}, {"type": "plainText", "text": "bidons"}, {"type": "whitespace"}, {"type": "plainText", "text": "\u25c6"}, {"type": "whitespace"}, {"type": "plainText", "text": "allons"}, {"type": "whitespace"}, {"type": "plainText", "text": "\u25c6"}, {"type": "whitespace"}, {"type": "plainText", "text": "vendons"}]}, {"tokens": [{"type": "plainText", "text": "b"}, {"type": "plainText", "text": "."}, {"type": "whitespace"}, {"type": "plainText", "text": "vidons"}, {"type": "whitespace"}, {"type": "plainText", "text": "\u25c6"}, {"type": "whitespace"}, {"type": "plainText", "text": "mentons"}, {"type": "whitespace"}, {"type": "plainText", "text": "\u25c6"}, {"type": "whitespace"}, {"type": "plainText", "text": "ballons"}, {"type": "whitespace"}, {"type": "plainText", "text": "\u25c6"}, {"type": "whitespace"}, {"type": "plainText", "text": "salons"}]}, {"tokens": [{"type": "plainText", "text": "c"}, {"type": "plainText", "text": "."}, {"type": "whitespace"}, {"type": "plainText", "text": "voir"}, {"type": "whitespace"}, {"type": "plainText", "text": "\u25c6"}, {"type": "whitespace"}, {"type": "plainText", "text": "armoire"}, {"type": "whitespace"}, {"type": "plainText", "text": "\u25c6"}, {"type": "whitespace"}, {"type": "plainText", "text": "couloir"}, {"type": "whitespace"}, {"type": "plainText", "text": "\u25c6"}, {"type": "whitespace"}, {"type": "plainText", "text": "dortoir"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_03.0.wording')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_04 pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "Faire"}, {"type": "whitespace"}, {"type": "plainText", "text": "des"}, {"type": "whitespace"}, {"type": "plainText", "text": "choses"}, {"type": "whitespace"}, {"type": "plainText", "text": "intelligentes"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_04.0.instructions')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_04 pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_04.0.wording')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_05 pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "Faire"}, {"type": "whitespace"}, {"type": "plainText", "text": "d"}, {"type": "plainText", "text": "'"}, {"type": "plainText", "text": "autres"}, {"type": "whitespace"}, {"type": "plainText", "text": "choses"}, {"type": "whitespace"}, {"type": "plainText", "text": "intelligentes"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_05.0.instructions')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_06 pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "Prendre"}, {"type": "whitespace"}, {"type": "plainText", "text": "le"}, {"type": "whitespace"}, {"type": "plainText", "text": "temps"}, {"type": "whitespace"}, {"type": "plainText", "text": "de"}, {"type": "whitespace"}, {"type": "plainText", "text": "faire"}, {"type": "whitespace"}, {"type": "plainText", "text": "aussi"}, {"type": "whitespace"}, {"type": "plainText", "text": "des"}, {"type": "whitespace"}, {"type": "plainText", "text": "choses"}, {"type": "whitespace"}, {"type": "plainText", "text": "banales"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_06.0.instructions')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_07 pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "Rel\u00e8ve"}, {"type": "whitespace"}, {"type": "plainText", "text": "dans"}, {"type": "whitespace"}, {"type": "plainText", "text": "le"}, {"type": "whitespace"}, {"type": "plainText", "text": "texte"}, {"type": "whitespace"}, {"type": "plainText", "text": "trois"}, {"type": "whitespace"}, {"type": "selectedText", "text": "d\u00e9terminants", "color": "#ffff00"}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "plainText", "text": "un"}, {"type": "whitespace"}, {"type": "selectedText", "text": "nom propre", "color": "#ffc0cb"}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "plainText", "text": "quatre"}, {"type": "whitespace"}, {"type": "selectedText", "text": "noms communs", "color": "#bbbbff"}, {"type": "whitespace"}, {"type": "plainText", "text": "et"}, {"type": "whitespace"}, {"type": "plainText", "text": "trois"}, {"type": "whitespace"}, {"type": "selectedText", "text": "verbes", "color": "#bbffbb"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_07.0.instructions')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_07 pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "selectableText", "text": "Les", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "Touaregs", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "sont", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "des", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "Berb\u00e8res", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "selectableText", "text": ",", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "un", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "peuple", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "qui", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "habite", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "en", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "Afrique", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "du", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "Nord", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "depuis", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "la", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "pr\u00e9histoire", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "selectableText", "text": ".", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}]}, {"tokens": [{"type": "selectableText", "text": "Ils", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "vivent", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "dans", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "le", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "d\u00e9sert", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "du", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "Sahara", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "(", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "selectableText", "text": "Alg\u00e9rie", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "selectableText", "text": ",", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "Libye", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "selectableText", "text": ",", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "Mali", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "selectableText", "text": ",", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "Niger", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "selectableText", "text": ",", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "Burkina", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "Faso", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "selectableText", "text": "\u2026", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "selectableText", "text": ")", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "selectableText", "text": ".", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}]}, {"tokens": [{"type": "selectableText", "text": "En", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "\u00e9t\u00e9", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "selectableText", "text": ",", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "les", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "temp\u00e9ratures", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "y", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "montent", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "\u00e0", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "plus", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "de", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "50", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "\u00b0", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "selectableText", "text": "C", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "et", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "elles", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "descendent", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "en", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "dessous", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "de", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "z\u00e9ro", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "durant", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "les", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "nuits", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "d\u2019", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "selectableText", "text": "hiver", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "selectableText", "text": ".", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_07.0.wording')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_07 pagelet 1 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "Mon"}, {"type": "whitespace"}, {"type": "plainText", "text": "quotidien"}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "plainText", "text": "pour"}, {"type": "whitespace"}, {"type": "plainText", "text": "les"}, {"type": "whitespace"}, {"type": "plainText", "text": "10"}, {"type": "plainText", "text": "-"}, {"type": "plainText", "text": "14"}, {"type": "whitespace"}, {"type": "plainText", "text": "ans"}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "plainText", "text": "www"}, {"type": "plainText", "text": "."}]}, {"tokens": [{"type": "plainText", "text": "monquotidien"}, {"type": "plainText", "text": "."}]}, {"tokens": [{"type": "plainText", "text": "fr"}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "plainText", "text": "13"}, {"type": "whitespace"}, {"type": "plainText", "text": "septembre"}, {"type": "whitespace"}, {"type": "plainText", "text": "2014"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_07.1.instructions')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_08 pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "Ajoute"}, {"type": "whitespace"}, {"type": "plainText", "text": "le"}, {"type": "whitespace"}, {"type": "plainText", "text": "suffixe"}, {"type": "whitespace"}, {"type": "plainText", "text": "\u2013"}, {"type": "plainText", "text": "eur"}, {"type": "whitespace"}, {"type": "plainText", "text": "aux"}, {"type": "whitespace"}, {"type": "plainText", "text": "verbes"}, {"type": "plainText", "text": "."}]}, {"tokens": [{"type": "plainText", "text": "Indique"}, {"type": "whitespace"}, {"type": "plainText", "text": "la"}, {"type": "whitespace"}, {"type": "plainText", "text": "classe"}, {"type": "whitespace"}, {"type": "plainText", "text": "des"}, {"type": "whitespace"}, {"type": "plainText", "text": "mots"}, {"type": "whitespace"}, {"type": "plainText", "text": "fabriqu\u00e9s"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_08.0.instructions')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_08 pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "nager"}, {"type": "whitespace"}, {"type": "plainText", "text": "\u279e"}, {"type": "whitespace"}, {"type": "freeTextInput"}, {"type": "whitespace"}, {"type": "plainText", "text": "\u25c6"}, {"type": "whitespace"}, {"type": "plainText", "text": "tracter"}, {"type": "whitespace"}, {"type": "plainText", "text": "\u279e"}, {"type": "whitespace"}, {"type": "freeTextInput"}, {"type": "whitespace"}, {"type": "plainText", "text": "\u25c6"}, {"type": "whitespace"}, {"type": "plainText", "text": "manger"}, {"type": "whitespace"}, {"type": "plainText", "text": "\u279e"}, {"type": "whitespace"}, {"type": "freeTextInput"}, {"type": "whitespace"}, {"type": "plainText", "text": "\u25c6"}]}, {"tokens": [{"type": "plainText", "text": "inventer"}, {"type": "whitespace"}, {"type": "plainText", "text": "\u279e"}, {"type": "whitespace"}, {"type": "freeTextInput"}, {"type": "whitespace"}, {"type": "plainText", "text": "\u25c6"}, {"type": "whitespace"}, {"type": "plainText", "text": "livrer"}, {"type": "whitespace"}, {"type": "plainText", "text": "\u279e"}, {"type": "whitespace"}, {"type": "freeTextInput"}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_08.0.wording')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_09 pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "R\u00e9ponds"}, {"type": "whitespace"}, {"type": "plainText", "text": "par"}, {"type": "whitespace"}, {"type": "boxedText", "text": "vrai"}, {"type": "whitespace"}, {"type": "plainText", "text": "ou"}, {"type": "whitespace"}, {"type": "boxedText", "text": "faux"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_09.0.instructions')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_09 pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "a"}, {"type": "plainText", "text": "."}, {"type": "whitespace"}, {"type": "plainText", "text": "coccinelle"}, {"type": "whitespace"}, {"type": "plainText", "text": "est"}, {"type": "whitespace"}, {"type": "plainText", "text": "un"}, {"type": "whitespace"}, {"type": "plainText", "text": "adjectif"}, {"type": "plainText", "text": "."}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["vrai", "faux"], "show_choices_by_default": false}]}, {"tokens": [{"type": "plainText", "text": "b"}, {"type": "plainText", "text": "."}, {"type": "whitespace"}, {"type": "plainText", "text": "b\u00fbche"}, {"type": "whitespace"}, {"type": "plainText", "text": "est"}, {"type": "whitespace"}, {"type": "plainText", "text": "un"}, {"type": "whitespace"}, {"type": "plainText", "text": "verbe"}, {"type": "plainText", "text": "."}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["vrai", "faux"], "show_choices_by_default": false}]}, {"tokens": [{"type": "plainText", "text": "c"}, {"type": "plainText", "text": "."}, {"type": "whitespace"}, {"type": "plainText", "text": "cette"}, {"type": "whitespace"}, {"type": "plainText", "text": "est"}, {"type": "whitespace"}, {"type": "plainText", "text": "un"}, {"type": "whitespace"}, {"type": "plainText", "text": "d\u00e9terminant"}, {"type": "plainText", "text": "."}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["vrai", "faux"], "show_choices_by_default": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_09.0.wording')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_09 pagelet 1 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "d"}, {"type": "plainText", "text": "."}, {"type": "whitespace"}, {"type": "plainText", "text": "dentier"}, {"type": "whitespace"}, {"type": "plainText", "text": "est"}, {"type": "whitespace"}, {"type": "plainText", "text": "un"}, {"type": "whitespace"}, {"type": "plainText", "text": "verbe"}, {"type": "plainText", "text": "."}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["vrai", "faux"], "show_choices_by_default": false}]}, {"tokens": [{"type": "plainText", "text": "e"}, {"type": "plainText", "text": "."}, {"type": "whitespace"}, {"type": "plainText", "text": "respirer"}, {"type": "whitespace"}, {"type": "plainText", "text": "est"}, {"type": "whitespace"}, {"type": "plainText", "text": "un"}, {"type": "whitespace"}, {"type": "plainText", "text": "verbe"}, {"type": "plainText", "text": "."}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["vrai", "faux"], "show_choices_by_default": false}]}, {"tokens": [{"type": "plainText", "text": "f"}, {"type": "plainText", "text": "."}, {"type": "whitespace"}, {"type": "plainText", "text": "aspiration"}, {"type": "whitespace"}, {"type": "plainText", "text": "est"}, {"type": "whitespace"}, {"type": "plainText", "text": "un"}, {"type": "whitespace"}, {"type": "plainText", "text": "nom"}, {"type": "plainText", "text": "."}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["vrai", "faux"], "show_choices_by_default": false}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_09.1.wording')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_10 pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "selectableText", "text": "Les", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "Touaregs", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "sont", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "des", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "Berb\u00e8res", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "selectableText", "text": "un", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "peuple", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "qui", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "habite", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "en", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "Afrique", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "du", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "Nord", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "depuis", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "la", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "pr\u00e9histoire", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_10.0.wording')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_10 pagelet 1 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "selectableText", "text": "Ils", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "vivent", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "dans", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "le", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "d\u00e9sert", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "du", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "Sahara", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "plainText", "text": "("}, {"type": "selectableText", "text": "Alg\u00e9rie", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "selectableText", "text": "Libye", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "selectableText", "text": "Mali", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "selectableText", "text": "Niger", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "selectableText", "text": "Burkina", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "Faso", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "plainText", "text": "\u2026"}, {"type": "plainText", "text": ")"}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_10.1.wording')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_10 pagelet 2 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "selectableText", "text": "En", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "\u00e9t\u00e9", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "plainText", "text": ","}, {"type": "whitespace"}, {"type": "selectableText", "text": "les", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "temp\u00e9ratures", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "y", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "montent", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "\u00e0", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "plus", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "de", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "50", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "plainText", "text": "\u00b0"}, {"type": "selectableText", "text": "C", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "et", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "elles", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "descendent", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "en", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "dessous", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "de", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "z\u00e9ro", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "durant", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "les", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "nuits", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "whitespace"}, {"type": "selectableText", "text": "d\u2019", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "selectableText", "text": "hiver", "colors": ["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb"], "boxed": false}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_10.2.wording')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_11 pagelet 0 instructions', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "..."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_11.0.instructions')
  })

  it('renders gabby.fixtures.FixturesTestCase.test_adapt_exercise_11 pagelet 0 wording', () => {
    cy.mount(TricolorSection, {
      props: {
        paragraphs: [{"tokens": [{"type": "plainText", "text": "a"}, {"type": "plainText", "text": "."}, {"type": "whitespace"}, {"type": "passiveFormattedText", "text": "Aujourd'hui", "bold": true, "italic": false}, {"type": "whitespace"}, {"type": "plainText", "text": "il"}, {"type": "whitespace"}, {"type": "plainText", "text": "fait"}, {"type": "whitespace"}, {"type": "passiveFormattedText", "text": "gris", "bold": false, "italic": true}, {"type": "whitespace"}, {"type": "plainText", "text": "et"}, {"type": "whitespace"}, {"type": "plainText", "text": "("}, {"type": "plainText", "text": "il"}, {"type": "whitespace"}, {"type": "plainText", "text": "pleuvra"}, {"type": "whitespace"}, {"type": "plainText", "text": "/"}, {"type": "whitespace"}, {"type": "plainText", "text": "il"}, {"type": "whitespace"}, {"type": "plainText", "text": "pleut"}, {"type": "whitespace"}, {"type": "plainText", "text": "/"}, {"type": "whitespace"}, {"type": "plainText", "text": "il"}, {"type": "whitespace"}, {"type": "plainText", "text": "pleuvait"}, {"type": "plainText", "text": ")"}, {"type": "plainText", "text": "."}]}, {"tokens": [{"type": "plainText", "text": "b"}, {"type": "plainText", "text": "."}, {"type": "whitespace"}, {"type": "passiveFormattedText", "text": "Aujourd'hui", "bold": true, "italic": false}, {"type": "whitespace"}, {"type": "plainText", "text": "il"}, {"type": "whitespace"}, {"type": "plainText", "text": "fait"}, {"type": "whitespace"}, {"type": "passiveFormattedText", "text": "gris", "bold": false, "italic": true}, {"type": "whitespace"}, {"type": "plainText", "text": "et"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["il pleuvra", "il pleut", "il pleuvait"], "show_choices_by_default": false}, {"type": "plainText", "text": "."}]}, {"tokens": [{"type": "plainText", "text": "c"}, {"type": "plainText", "text": "."}, {"type": "whitespace"}, {"type": "plainText", "text": "Aujourd"}, {"type": "plainText", "text": "'"}, {"type": "plainText", "text": "hui"}, {"type": "whitespace"}, {"type": "plainText", "text": "il"}, {"type": "whitespace"}, {"type": "plainText", "text": "fait"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["gris", "beau"], "show_choices_by_default": false}, {"type": "whitespace"}, {"type": "plainText", "text": "et"}, {"type": "whitespace"}, {"type": "plainText", "text": "il"}, {"type": "whitespace"}, {"type": "multipleChoicesInput", "show_arrow_before": false, "choices": ["pleut", "pleuvra"], "show_choices_by_default": false}, {"type": "plainText", "text": "."}]}],
        modelValue: {},
      },
    })
    cy.screenshot('gabby.fixtures.FixturesTestCase.test_adapt_exercise_11.0.wording')
  })
})
