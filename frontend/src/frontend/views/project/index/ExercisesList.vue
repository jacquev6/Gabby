<script setup lang="ts">
import { computed } from 'vue'

import type { Project, Exercise } from '$frontend/stores/api'


const props = defineProps<{
  project: Project,
}>()

const exercisesByTextbookAndPage = computed(() => {
  console.assert(props.project.relationships !== undefined)

  const textbooks: {[id: string]: {pages: {[page: number]: Exercise[]}}} = {}
  for (const exercise of props.project.relationships.exercises) {
    console.assert(exercise.attributes !== undefined)
    console.assert(exercise.relationships !== undefined)

    const textbook = exercise.relationships.textbook
    if (textbook) {
      textbooks[textbook.id] = textbooks[textbook.id] ?? { textbook, pages: [] }
      const page = exercise.attributes.textbookPage
      console.assert(page !== null)
      textbooks[textbook.id].pages[page] = textbooks[textbook.id].pages[page] ?? []
      textbooks[textbook.id].pages[page].push(exercise)
    }
  }
  return textbooks
})

const independentExercises = computed(() => {
  console.assert(props.project.relationships !== undefined)

  const exercises = []
  for (const exercise of props.project.relationships.exercises) {
    console.assert(exercise.relationships !== undefined)
    if (!exercise.relationships.textbook) {
      exercises.push(exercise)
    }
  }
  return exercises
})

function ellipsis(s: string) {
  return s.length > 25 ? s.slice(0, 25) + '…' : s
}
</script>

<template>
  <template v-if="project.relationships!.textbooks.length || project.relationships!.exercises.length">
    <template v-if="independentExercises.length">
      <h3>{{ $t('independentExercises') }}</h3>
      <ul>
        <li v-for="exercise in independentExercises">
          <strong>{{ exercise.attributes!.number }}</strong> {{ ellipsis(exercise.attributes!.instructions) }}
        </li>
      </ul>
    </template>
    <template v-for="textbook in project.relationships!.textbooks">
      <h3><RouterLink :to="{name: 'project-textbook-page-list-exercises', params: {projectId: project.id, textbookId: textbook.id, page: 1}}">{{ textbook.attributes!.title }}</RouterLink><template v-if="textbook.attributes!.publisher">, {{ textbook.attributes!.publisher }}</template><template v-if="textbook.attributes!.year"> ({{ textbook.attributes!.year }})</template></h3>
      <template v-if="exercisesByTextbookAndPage[textbook.id]">
        <ul v-for="[page, exercises] of Object.entries(exercisesByTextbookAndPage[textbook.id]?.pages)">
          <li>
            <RouterLink :to="{name: 'project-textbook-page-list-exercises', params: {projectId: project.id, textbookId: textbook.id, page}}">Page {{ page }}</RouterLink>
            <ul>
              <li v-for="exercise in exercises">
                <RouterLink :to="{name: 'project-textbook-page-edit-exercise', params: {projectId: project.id, textbookId: textbook.id, page, exerciseId: exercise.id}}">
                  <strong>{{ exercise.attributes!.number }}</strong>
                </RouterLink>
                {{ ellipsis(exercise.attributes!.instructions) }}
                <em>{{ exercise.relationships!.adaptation? $t(exercise.relationships!.adaptation.type) : '' }}</em>
              </li>
            </ul>
          </li>
        </ul>
      </template>
    </template>
  </template>
  <p v-else>{{ $t('noExercisesForNow') }}</p>
</template>
