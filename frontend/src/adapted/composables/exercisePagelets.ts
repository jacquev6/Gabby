import { computed, type Ref } from 'vue'


export function useExercisePagelets(
  paragraphsCountPerPagelet: Ref<number | null>,
  totalParagraphsCount: Ref<number>,
  pageletIndex: Ref<number>,
) {
  return {
    firstWordingParagraph: computed(() => {
      if (paragraphsCountPerPagelet.value === null) {
        return null
      } else {
        return pageletIndex.value * paragraphsCountPerPagelet.value
      }    
    }),
    lastWordingParagraph: computed(() => {
      if (paragraphsCountPerPagelet.value === null) {
        return null
      } else {
        return (pageletIndex.value + 1) * paragraphsCountPerPagelet.value
      }    
    }),
    pageletsCount: computed(() => {
      if (paragraphsCountPerPagelet.value === null) {
        return 1
      } else {
        console.assert(paragraphsCountPerPagelet.value > 0)
        return Math.ceil(totalParagraphsCount.value / paragraphsCountPerPagelet.value)
      }
    })
  }
}
