import type { Item } from '$frontend/stores/api'
import type { components  } from '$/openapi'


type schemas = components["schemas"]


export type SelectThingsAdaptationOptions = schemas["SelectThingsAdaptationOptions"]
export type FillWithFreeTextAdaptationOptions = schemas["FillWithFreeTextAdaptationOptions"]
export type MultipleChoicesInInstructionsAdaptationOptions = schemas["MultipleChoicesInInstructionsAdaptationOptions"]
export type MultipleChoicesInWordingAdaptationOptions = schemas["MultipleChoicesInWordingAdaptationOptions"]


export type Ping = Item<schemas["pingOutputItemAttributes"], {
  // @todo Preserve typing of relationships: make sure that 'type' is specified in the OpenAPI schema instead of being a plain string
  prev: Ping
  next: Array<Ping>
}>

export type Project = Item<schemas["projectOutputItemAttributes"], {
  exercises: Exercise[]
  textbooks: Textbook[]
}>

export type Textbook = Item<schemas["textbookOutputItemAttributes"], {
  project: Project
  sections: Section[]
}>

export type Naming = Item<schemas["pdfFileNamingOutputItemAttributes"], {
}>

export type PdfFile = Item<schemas["pdfFileOutputItemAttributes"], {
  namings: Naming[]
}>

export type Section = Item<schemas["sectionOutputItemAttributes"], {
  pdfFile: PdfFile
}>

export type Adaptation = Item<{
}, {
}>

export type Exercise = Item<schemas["exerciseOutputItemAttributes"], {
  project: Project
  textbook: Textbook | null
  adaptation: Adaptation | null
}>

export type AdaptedExercise = Item<schemas["adaptedExerciseOutputItemAttributes"], {
}>
