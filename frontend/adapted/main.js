import { createApp } from 'vue'
import { createRouter, createWebHashHistory } from 'vue-router'

import Main from './main.vue'
import IndexView from './views/index-view.vue'
import ExerciseView from './views/exercise-view.vue'


const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    {
      path: '/',
      name: 'index',
      component: IndexView,
    },
    {
      path: '/exercise/:exerciseIndex',
      name: 'exercise',
      component: ExerciseView,
      props: true,
    },
  ],
})

createApp(Main)
  .use(router)
  .mount('#app')
