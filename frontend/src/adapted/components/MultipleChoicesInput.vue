<script setup lang="ts">
import { ref, computed, inject } from 'vue'
import { useFloating, shift } from '@floating-ui/vue'


defineOptions({
  inheritAttrs: false
})

const props = withDefaults(defineProps<{
  choices: string[],
  placeholder?: string,
  // @todo alwaysShowChoices?: boolean = false
}>(), {
  placeholder: '....',
})

const model = defineModel<string | undefined>({
  required: true,
})

const showChoices = ref(false)

const value = computed(() => model.value || props.placeholder)

function set(choice: string | undefined) {
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
    transform: false,
    middleware: [shift({crossAxis: true})],
  },
);

const choiceColumns = computed(() => {
  const columns = []
  for (let i = 0; i < props.choices.length; i += 2) {
    columns.push([
      {text: props.choices[i], colorIndex: i % 3},
    ])
    if (i + 1 < props.choices.length) {
      columns[columns.length - 1].push(
        {text: props.choices[i + 1], colorIndex: (i + 1) % 3},
      )
    }
  }
  return columns
})

const backdropCovers = inject<string>('adaptedExerciseBackdropCovers', 'body')
</script>

<template>
  <span v-bind="$attrs" style="display: inline flow-root; vertical-align: top">
    <span ref="reference" class="main" :class="{open: showChoices}" @click="showChoices = true">{{ value }}</span>
    <!-- Insert hidden nodes in the DOM to ensure the floating choices does not cover any text. -->
    <span class="choices" style="display: block; margin-top: -24px; max-width: 0; overflow: hidden; visibility: hidden;">
      <span class="choiceColumn" style="display: block; min-width: 1000vw;">
        <span class="choice" style="display: block;"><span>Option 1</span></span>
        <span class="choice" style="display: block;"><span>Option 2</span></span>
      </span>
    </span>
  </span>
  <template v-if="showChoices">
    <Teleport :to="backdropCovers">
      <div class="backdrop" @click="showChoices = false"></div>
    </Teleport>
    <div ref="floating" class="choices" :style="floatingStyles">
      <div v-for="choiceColumn in choiceColumns" class="choiceColumn">
        <p v-for="choice in choiceColumn" class="choice" @click="set(choice.text)"><span :class="`choice${choice.colorIndex}`">{{ choice.text }}</span></p>
      </div>
    </div>
  </template>
</template>

<style scoped>
/* Based on Etude_de_la_langue_CE1_Belin/P8Ex1_hboj.html */

span {
  cursor: pointer;
  user-select: none;
  margin: 0;
  padding: 0;
  background: none;
}

span.main {
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

.choiceColumn {
  float: left;
  margin: 15px 5px;
}

.choice {
  font-family: Arial, sans-serif;
  font-size: 32px;
  line-height: 3;
  margin-top: -24px;
  margin-bottom: -24px;
}

.choice >span {
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
