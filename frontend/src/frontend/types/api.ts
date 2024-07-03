import type { Item } from '../stores/api/interface'
import type { components  } from '$/openapi'


type schemas = components["schemas"]

export type SelectThingsAdaptationOptions = schemas["SelectThingsAdaptationOptions"]
export type FillWithFreeTextAdaptationOptions = schemas["FillWithFreeTextAdaptationOptions"]
export type MultipleChoicesInInstructionsAdaptationOptions = schemas["MultipleChoicesInInstructionsAdaptationOptions"]
export type MultipleChoicesInWordingAdaptationOptions = schemas["MultipleChoicesInWordingAdaptationOptions"]

export type User = Item<schemas["userOutputItemAttributes"], {}>

export type Ping = Item<schemas["pingOutputItemAttributes"], {
  // @todo Preserve typing of relationships: make sure that 'type' is specified in the OpenAPI schema instead of being a plain string
  prev: Ping
  next: Array<Ping>
  createdBy: User | null
  updatedBy: User | null
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
  textbook: Textbook
}>

export type SelectThingsAdaptation = Item<schemas["selectThingsAdaptationOutputItemAttributes"], {
  exercise: Exercise
}>

export type FillWithFreeTextAdaptation = Item<schemas["fillWithFreeTextAdaptationOutputItemAttributes"], {
  exercise: Exercise
}>

export type MultipleChoicesInWordingAdaptation = Item<schemas["multipleChoicesInWordingAdaptationOutputItemAttributes"], {
  exercise: Exercise
}>

export type MultipleChoicesInInstructionsAdaptation = Item<schemas["multipleChoicesInInstructionsAdaptationOutputItemAttributes"], {
  exercise: Exercise
}>

export type Exercise = Item<schemas["exerciseOutputItemAttributes"], {
  project: Project
  textbook: Textbook | null
  adaptation: SelectThingsAdaptation | FillWithFreeTextAdaptation | MultipleChoicesInWordingAdaptation | MultipleChoicesInInstructionsAdaptation | null
}>

export type AdaptedExercise = Item<schemas["adaptedExerciseOutputItemAttributes"], {
}>
