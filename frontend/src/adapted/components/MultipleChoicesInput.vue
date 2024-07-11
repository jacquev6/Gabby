<script setup lang="ts">
import { ref, computed } from 'vue'
import { inject } from 'vue'
import { useFloating, shift } from '@floating-ui/vue'


const props = withDefaults(defineProps<{
  choices: string[],
  placeholder?: string,
  // @todo alwaysShowChoices?: boolean = false
  // @todo allowReset?: boolean = true
}>(), {
  placeholder: '........',
})

const model = defineModel<string | undefined>({
  required: true,
})

const teleportTo: string = inject('adaptedExerciseTeleportPoint') ?? 'body'

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
    transform: false,
    middleware: [shift({crossAxis: true})],
  },
);

</script>

<template>
  <span ref="reference" class="main" :class="{open: showChoices}" @click="showChoices = !showChoices">{{ value }}</span>
  <Teleport v-if="showChoices" :to="teleportTo">
    <div class="backdrop" @click="showChoices = false"></div>
    <div ref="floating" class="choices" :style="floatingStyles">
      <template v-for="choice, choiceIndex in choices" :key="choice">
        <wbr v-if="choiceIndex !== 0" />
        <span class="choice" :class="`choice${choiceIndex % 3}`" @click="set(choice)">
          {{ choice }}
        </span>
      </template>
      <span class="choice" @click="set(undefined)">{{ props.placeholder }}</span>
    </div>
  </Teleport>
</template>

<style scoped>
/* Based on Etude_de_la_langue_CE1_Belin/P8Ex1_hboj.html */

span {
  cursor: pointer;
  user-select: none;
  margin: 0;
  padding: 0 0.4em;
  background: none;
}

span.main {
  border: 2px solid grey;
}

span.main.open {
  background-color: lightyellow;
}

div.backdrop {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

div.choices {
  border: 1px dashed darkgreen;
  background: white;
  padding: 0.5em;
  max-width: 12em;
}

span.choice {
  border: 1px solid black;
}

span.choice0 {
  color: red;
}

span.choice1 {
  color: blue;
}

span.choice2 {
  color: green;
}
</style>
