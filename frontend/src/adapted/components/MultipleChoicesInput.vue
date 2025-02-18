<script setup lang="ts">
import { ref, computed, inject, watch } from 'vue'
import { useFloating, shift, autoUpdate } from '@floating-ui/vue'
import type { Paragraph } from '$adapted/types'
import Renderable from './Renderable.vue'


defineOptions({
  inheritAttrs: false
})

type Choices = (Paragraph['contents'][number] & {kind: 'multipleChoicesInput'})['choices']
type Choice = Choices[number]

const props = defineProps<{
  showArrowBefore: boolean
  choices: Choices
  placeholder: string
  showChoicesByDefault: boolean
}>()

const model = defineModel<number | undefined>({
  required: true,
})

const showChoices = ref(false)

const showBackdrop = computed(() => !props.showChoicesByDefault)

watch(
  [() => props.showChoicesByDefault, model],
  ([showChoicesByDefault, model]) => {
    if (model === undefined) {
      showChoices.value = showChoicesByDefault
    } else {
      showChoices.value = false
    }
  },
  {immediate: true}
)

function set(choice: number) {
  model.value = choice
  showChoices.value = false
}

const reference = ref<HTMLElement | null>(null)
const floating = ref<HTMLElement | null>(null)
const { floatingStyles } = useFloating(
  reference,
  floating,
  {
    placement: 'bottom',
    middleware: [shift({crossAxis: true})],
    whileElementsMounted: autoUpdate,
  },
);

const choicesLines = computed(() => {
  const lines: {index: number, colorIndex: number, content: Choice}[][] = [[], []]
  for (let i = 0; i < props.choices.length; ++i) {
    lines[i % 2].push({index: i, content: props.choices[i], colorIndex: i % 3})
  }
  return lines
})

const unusedModels = ref<Record<string, any>>({})  // @todo Remove

const backdropCovers = inject<string>('adaptedExerciseBackdropCovers', 'body')
</script>

<template>
  <span v-bind="$attrs" style="display: inline flow-root; vertical-align: top">
    <template v-if="showArrowBefore">⮕</template>
    <span ref="reference" class="main" :class="{open: showChoices}" @click="showChoices = !showChoices">
      <template v-if="model !== undefined">
        <Renderable v-for="node in choices[model]" :node :inStack="true" v-model="unusedModels" :modelKey="[0]" />
      </template>
      <template v-else>
        {{ placeholder }}
      </template>
    </span>
    <!-- Insert hidden nodes in the DOM to ensure the floating choices does not cover any text. -->
    <span class="choices" style="display: block; margin-top: -24px; max-width: 0; overflow: hidden; visibility: hidden;">
      <span class="choicesColumn" style="display: block;">
        <span class="choicesLine" style="display: block;"><span class="choice">1</span></span>
        <span class="choicesLine" style="display: block;"><span class="choice">2</span></span>
      </span>
    </span>
    <template v-if="showChoices">
      <template v-if="showBackdrop">
        <Teleport :to="backdropCovers">
          <div class="backdrop" @click="showChoices = false"></div>
        </Teleport>
      </template>
      <div ref="floating" class="choices" :style="floatingStyles">
        <div class="choicesColumn">
          <p v-for="choicesLine in choicesLines" class="choicesLine">
            <template v-for="(choice, i) in choicesLine">
              <span v-if="i !== 0">&nbsp;&nbsp;</span><span class="choice" :class="`choice${choice.colorIndex}`"@click="set(choice.index)">
                <Renderable v-for="node in choice.content" :node :inStack="true" v-model="unusedModels" :modelKey="[0]" />
              </span>
            </template>
          </p>
        </div>
      </div>
    </template>
  </span>
</template>

<style scoped>
span {
  user-select: none;
  margin: 0;
  padding: 0;
  background: none;
}

span.main {
  cursor: pointer;
  font-family: Arial, sans-serif;
  font-size: 32px;
  border: 2px outset #888;
}

span.main.open {
  background-color: #FFFDD4;
}

div.backdrop {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.choices {
  border: 1px dashed green;
  background: white;
  z-index: 10;  /* Arbitrary z-order is fragile but used only in preview */
}

.choicesColumn {
  margin: 15px 5px;
}

.choicesLine {
  font-family: Arial, sans-serif;
  font-size: 32px;
  line-height: 3;
  margin-top: -24px;
  margin-bottom: -24px;
}

span.choice {
  cursor: pointer;
  border: 1px solid black;
  padding: 1px 4px;
}

/* Colors provided by client */
span.choice0 {
  color: #00F;
}

span.choice1 {
  color: #F00;
}

span.choice2 {
  color: #0C0;
}
</style>
