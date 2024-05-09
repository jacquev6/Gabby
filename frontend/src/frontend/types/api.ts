import type { Item } from '$frontend/stores/api'
import type { components  } from '$/openapi'


type schemas = components["schemas"]


export type SelectThingsOptions = schemas["SelectThingsOptionsModel"]
export type FillWithFreeTextOptions = schemas["FillWithFreeTextOptionsModel"]


export type Ping = Item<schemas["ping-OutputItem-Attributes"], {
  // @todo Preserve typing of relationships: make sure that 'type' is specified in the OpenAPI schema instead of being a plain string
  prev: Ping
  next: Array<Ping>
}>

export type Project = Item<schemas["project-OutputItem-Attributes"], {
  exercises: Exercise[]
  textbooks: Textbook[]
}>

export type Textbook = Item<schemas["textbook-OutputItem-Attributes"], {
  project: Project
  sections: Section[]
}>

export type Naming = Item<schemas["pdfFileNaming-OutputItem-Attributes"], {
}>

export type PdfFile = Item<schemas["pdfFile-OutputItem-Attributes"], {
  namings: Naming[]
}>

export type Section = Item<schemas["section-OutputItem-Attributes"], {
  pdfFile: PdfFile
}>

export type Adapted = Item<{
}, {
}>

export type Exercise = Item<schemas["exercise-OutputItem-Attributes"], {
  project: Project
  textbook: Textbook | null
  adapted: Adapted | null
}>

export type AdaptedExercise = Item<schemas["adaptedExercise-OutputItem-Attributes"], {
}>
