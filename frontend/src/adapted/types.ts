import type { paths } from '$/openapi'


export interface Settings {
  centeredInstructions: boolean
  tricolorWording: boolean
}

export type Exercise = Exclude<paths['/api/parsedExercises/{id}']['get']['responses']['200']['content']['application/vnd.api+json']['data']['attributes']['adapted'], null>

export type Section = Exercise['pagelets'][number]['instructions']

export type Paragraph = Section['paragraphs'][number]


export interface Data {
  projectId: string,
  exercises: {
    [id: string]: Exercise,
  },
}
