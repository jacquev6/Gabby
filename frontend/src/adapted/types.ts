import type { paths } from '$/openapi'


export interface Settings {
  centeredInstructions: boolean
  tricolorWording: boolean
}

export type Exercise = Exclude<paths['/api/parsedExercises/{id}']['get']['responses']['200']['content']['application/vnd.api+json']['data']['attributes']['adapted'], null>

export type Paragraph = Exercise['pagelets'][number]['sections'][number]['paragraphs'][number]


export interface Data {
  projectId: string,
  exercises: {
    [id: string]: Exercise,
  },
}
