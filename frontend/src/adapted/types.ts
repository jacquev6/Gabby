import type { components } from '$/openapi'


export interface Settings {
  tricolorWording: boolean,
}


type schemas = components['schemas']

export type Section = schemas['Section']

export type Exercise = schemas['AdaptedExercise']

export interface Data {
  projectId: string,
  exercises: {
    [id: string]: Exercise,
  },
}
