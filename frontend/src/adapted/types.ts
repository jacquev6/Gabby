export interface NullAdaptation {
  type: '-',
}

export interface FillWithFreeTextAdaptation {
  type: 'fillWithFreeText',
  placeholder: string,
}

export interface SelectWordsAdaptation {
  type: 'selectWords',
  colors: number,
}

export interface Exercise<Adaptation> {
  number: string,
  textbookPage: number,
  instructions: string,
  wording: string,
  adaptation: Adaptation,
}

export interface Data {
  exercises: {
    [index: string]:
      Exercise<NullAdaptation>
      | Exercise<FillWithFreeTextAdaptation>
      | Exercise<SelectWordsAdaptation>
  },
}
