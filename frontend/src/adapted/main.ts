import { createApp } from 'vue'
import { createRouter, createWebHashHistory } from 'vue-router'

import RootLayout from './RootLayout.vue'
import IndexView from './views/IndexView.vue'
import ExerciseView from './views/ExerciseView.vue'


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

createApp(RootLayout)
  .use(router)
  .mount('#app')
