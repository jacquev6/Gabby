import type { components } from '../openapi'


export interface Settings {
  tricolorWording: boolean,
}


type schemas = components['schemas']

export type Section = schemas['Section']

export type Exercise = schemas['AdaptedExercise']

export interface Data {
  exercises: {
    [index: string]: {
      id: string,
      adapted: Exercise,
    }
  },
}
