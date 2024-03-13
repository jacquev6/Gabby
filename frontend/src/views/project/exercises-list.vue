<script setup>
import { computed } from 'vue'


const props = defineProps({
  project: {type: Object, required: true},
})

const exercisesByTextbookAndPage = computed(() => {
  const textbooks = {}
  for (const exercise of props.project?.relationships.exercises) {
    const textbook = exercise.relationships.textbook
    if (textbook) {
      textbooks[textbook.id] = textbooks[textbook.id] ?? { textbook, pages: [] }
      const page = exercise.attributes.textbookPage
      textbooks[textbook.id].pages[page] = textbooks[textbook.id].pages[page] ?? []
      textbooks[textbook.id].pages[page].push(exercise)
    }
  }
  return textbooks
})

const independentExercises = computed(() => {
  const exercises = []
  for (const exercise of props.project?.relationships.exercises) {
    if (!exercise.relationships.textbook) {
      exercises.push(exercise)
    }
  }
  return exercises
})

function ellipsis(s) {
  return s.length > 25 ? s.slice(0, 25) + '…' : s
}
</script>

<template>
  <template v-if="project.relationships.textbooks.length || project.relationships.exercises.length">
    <template v-if="independentExercises.length">
      <h3>{{ $t('independentExercises') }}</h3>
      <ul>
        <li v-for="exercise in independentExercises">
          <strong>{{ exercise.attributes.number }}</strong> : {{ ellipsis(exercise.attributes.instructions) }}
        </li>
      </ul>
    </template>
    <template v-for="textbook in project.relationships.textbooks">
      <h3><router-link :to="{name: 'project-textbook-page', params: {projectId: project.ud, textbookId: textbook.id, page: 1}}">{{ textbook.attributes.title }}</router-link><template v-if="textbook.attributes.publisher">, {{ textbook.attributes.publisher }}</template><template v-if="textbook.attributes.year"> ({{ textbook.attributes.year }})</template></h3>
      <template v-if="exercisesByTextbookAndPage[textbook.id]">
        <ul v-for="[page, exercises] of Object.entries(exercisesByTextbookAndPage[textbook.id]?.pages)">
          <li>
            <router-link :to="{name: 'project-textbook-page', params: {projectId: project.ud, textbookId: textbook.id, page}}">Page {{ page }}</router-link>
            <ul>
              <li v-for="exercise in exercises">
              <strong>{{ exercise.attributes.number }}</strong> : {{ ellipsis(exercise.attributes.instructions) }}
            </li>
            </ul>
          </li>
        </ul>
      </template>
    </template>
  </template>
  <p v-else>{{ $t('noExercisesForNow') }}</p>
</template>
