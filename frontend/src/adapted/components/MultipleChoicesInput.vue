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
  placeholder: '....',
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
  <span ref="reference" class="main" @click="showChoices = !showChoices">{{ value }}</span>
  <Teleport v-if="showChoices" :to="teleportTo">
    <div class="backdrop" @click="showChoices = false"></div>
    <div ref="floating" class="choices" :style="floatingStyles">
      <template v-for="choice, choiceIndex in choices" :key="choice">
        <wbr v-if="choiceIndex !== 0" />
        <span class="choice" @click="set(choice)">
          {{ choice }}
        </span>
      </template>
      <span class="choice" @click="set(undefined)">{{ props.placeholder }}</span>
    </div>
  </Teleport>
</template>

<style scoped>
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

div.backdrop {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.1);
}

div.choices {
  border: 2px solid grey;
  background: white;
  padding: 0.5em;
  max-width: 10em;
}

span.choice {
  border: 2px solid black;
}
</style>
