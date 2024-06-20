import type { components } from '$/openapi'


export interface Settings {
  tricolorWording: boolean,
  wordingParagraphsPerPagelet: number | null,
}


type schemas = components['schemas']

export type Section = schemas['Section']

export type Paragraph = schemas['Paragraph']

export type Exercise = schemas['AdaptedExercise']

export interface Data {
  projectId: string,
  exercises: {
    [id: string]: Exercise,
  },
}
