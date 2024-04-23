import type { Item } from '../stores/api'


// @todo Generate this file from the API schema

export type Ping = Item<{
  createdAt: string
  message: string | null
}, {
  prev: Ping
  next: Array<Ping>
}>

export type Project = Item<{
  title: string,
  description: string
}, {
  exercises: Exercise[]
  textbooks: Textbook[]
}>

export type Textbook = Item<{
  title: string
  publisher: string
  year: number
}, {
  project: Project
  sections: Section[]
}>

export type Naming = Item<{
  name: string
}, {
}>

export type PdfFile = Item<{
}, {
  namings: Naming[]
}>

export type Section = Item<{
  pdfFileStartPage: number
  pagesCount: number
  textbookStartPage: number
}, {
  pdfFile: PdfFile
}>

export type Adapted = Item<{
}, {
}>

export type Exercise = Item<{
  boundingRectangle: any/*@todo Type*/
  textbookPage: number | null
  number: string
  instructions: string
  wording: string
  example: string
  clue: string
}, {
  project: Project
  textbook: Textbook | null
  adapted: Adapted | null
}>
