<script setup lang="ts">
import { computed } from 'vue'

import type { Project, Exercise, InCache, Exists } from '$frontend/stores/api'
import type { Model as Deltas } from '$frontend/components/Quill.vue'


const props = defineProps<{
  project: Project & InCache & Exists
}>()

const exercisesByTextbookAndPage = computed(() => {
  const textbooks: {[id: string]: {pages: {[page: number]: (Exercise & InCache & Exists)[]}}} = {}
  for (const exercise of props.project.relationships.exercises) {
    if (exercise.inCache && exercise.exists) {
      const textbook = exercise.relationships.textbook
      if (textbook) {
        textbooks[textbook.id] = textbooks[textbook.id] ?? { textbook, pages: [] }
        const page = exercise.attributes.textbookPage
        console.assert(page !== null)
        textbooks[textbook.id].pages[page] = textbooks[textbook.id].pages[page] ?? []
        textbooks[textbook.id].pages[page].push(exercise)
      }
    }
  }
  return textbooks
})

const independentExercises = computed(() => {
  const exercises: (Exercise & InCache & Exists)[] = []
  for (const exercise of props.project.relationships.exercises) {
    if (exercise.inCache && exercise.exists) {
      if (!exercise.relationships.textbook) {
        exercises.push(exercise)
      }
    }
  }
  return exercises
})

function ellipsis(deltas: Deltas) {
  const s = deltas.map(delta => typeof delta.insert === 'string' ? delta.insert : '').join('')
  return s.length > 25 ? s.slice(0, 25) + '…' : s
}
</script>

<template>
  <template v-if="project.relationships.textbooks.length || project.relationships.exercises.length">
    <template v-if="independentExercises.length">
      <h3>{{ $t('independentExercises') }}</h3>
      <ul>
        <li v-for="exercise in independentExercises">
          <strong>{{ exercise.attributes.number }}</strong> {{ ellipsis(exercise.attributes.instructions) }}
        </li>
      </ul>
    </template>
    <template v-for="textbook in project.relationships.textbooks">
      <template v-if="textbook.inCache && textbook.exists">
        <h3><RouterLink :to="{name: 'project-textbook-page', params: {projectId: project.id, textbookId: textbook.id, page: 1}}">{{ textbook.attributes.title }}</RouterLink><template v-if="textbook.attributes.publisher">, {{ textbook.attributes.publisher }}</template><template v-if="textbook.attributes.year"> ({{ textbook.attributes.year }})</template></h3>
        <template v-if="exercisesByTextbookAndPage[textbook.id]">
          <ul v-for="[page, exercises] of Object.entries(exercisesByTextbookAndPage[textbook.id]?.pages)">
            <li>
              <RouterLink :to="{name: 'project-textbook-page', params: {projectId: project.id, textbookId: textbook.id, page}}">Page {{ page }}</RouterLink>
              <ul>
                <li v-for="exercise in exercises">
                  <RouterLink :to="{name: 'project-textbook-page-exercise', params: {projectId: project.id, textbookId: textbook.id, page, exerciseId: exercise.id}}">
                    <strong>{{ exercise.attributes.number }}</strong>
                  </RouterLink>
                  {{ ellipsis(exercise.attributes.instructions) }}
                  <em>{{ exercise.attributes.adaptation.kind !== 'generic' ? $t(exercise.attributes.adaptation.kind) : '' }}</em>
                </li>
              </ul>
            </li>
          </ul>
        </template>
      </template>
    </template>
  </template>
  <p v-else>{{ $t('noExercisesForNow') }}</p>
</template>
