import type { paths } from '$/openapi'


export interface Settings {
  centeredInstructions: boolean
  tricolorWording: boolean
}


export type Exercise = paths['/api/parsedExercises/{id}']['get']['responses']['200']['content']['application/vnd.api+json']['data']['attributes']['oldAdapted']

export type Section = Exercise['pagelets'][number]['instructions']

export type Paragraph = Section['paragraphs'][number]

export type NewExercise = Exclude<paths['/api/parsedExercises/{id}']['get']['responses']['200']['content']['application/vnd.api+json']['data']['attributes']['newAdapted'], null>

export type NewSection = NewExercise['pagelets'][number]['instructions']

export type NewParagraph = NewSection['paragraphs'][number]


export interface Data {
  projectId: string,
  exercises: {
    [id: string]: NewExercise,
  },
}
