import { computed, type Ref } from 'vue'


export function useExercisePagelets(
  paragraphsCountPerPagelet: Ref<number | null>,
  totalParagraphsCount: Ref<number>,
  pageletIndex: Ref<number>,
) {
  const degenerate = computed(() => paragraphsCountPerPagelet.value === null || totalParagraphsCount.value === 0)

  return {
    firstWordingParagraph: computed(() => {
      if (degenerate.value) {
        return null
      } else {
        return pageletIndex.value * paragraphsCountPerPagelet.value!
      }    
    }),
    lastWordingParagraph: computed(() => {
      if (degenerate.value) {
        return null
      } else {
        return (pageletIndex.value + 1) * paragraphsCountPerPagelet.value!
      }    
    }),
    pageletsCount: computed(() => {
      if (degenerate.value) {
        return 1
      } else {
        console.assert(paragraphsCountPerPagelet.value! > 0)
        return Math.ceil(totalParagraphsCount.value / paragraphsCountPerPagelet.value!)
      }
    })
  }
}
