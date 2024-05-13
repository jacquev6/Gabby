import { createApp } from 'vue'
import { createRouter, createWebHashHistory } from 'vue-router'

import { i18n } from '$/locales'
import ExerciseView from './views/ExerciseView.vue'
import IndexView from './views/IndexView.vue'
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
  ],
})

createApp(RootLayout)
  .use(i18n)
  .use(router)
  .mount('#app')
