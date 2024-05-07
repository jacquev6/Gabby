import { createApp } from 'vue'
import { createRouter, createWebHashHistory } from 'vue-router'

import ExerciseView from './views/ExerciseView.vue'
import IndexView from './views/IndexView.vue'
import NotAdaptedView from './views/NotAdaptedView.vue'
import ErrorView from './views/ErrorView.vue'
import RootLayout from './RootLayout.vue'


const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    {
      path: '/',
      name: 'index',
      component: IndexView,
    },
    {
      path: '/exercise/:exerciseId',
      name: 'exercise',
      component: ExerciseView,
      props: true,
    },
    {
      path: '/not-adapted',
      name: 'not-adapted',
      component: NotAdaptedView,
    },
    {
      path: '/error',
      name: 'error',
      component: ErrorView,
    },
  ],
})

createApp(RootLayout)
  .use(router)
  .mount('#app')
