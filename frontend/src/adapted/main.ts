import { createApp } from 'vue'
import { createRouter, createWebHashHistory, RouterView } from 'vue-router'

import { i18n } from '$/locales'
import ExerciseView from './views/ExerciseView.vue'
import IndexView from './views/IndexView.vue'
import type { Data } from './types'


const data = JSON.parse('{{ data }}') as Data

const settings = {
  centeredInstructions: true,
  tricolorWording: true,
}

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    {
      path: '/',
      name: 'index',
      component: IndexView,
      props: () => ({ data, settings }),
    },
    {
      path: '/exercise-:exerciseId/:pageletIndex',
      name: 'exercise',
      component: ExerciseView,
      props: (route) => {
        console.assert(typeof(route.params.pageletIndex) === 'string')
        return {
          data,
          settings,
          exerciseId: route.params.exerciseId,
          pageletIndex: Number.parseInt(route.params.pageletIndex, 10),
        }
      },
    },
  ],
})

createApp(RouterView)
  .use(i18n)
  .use(router)
  .mount('#app')
