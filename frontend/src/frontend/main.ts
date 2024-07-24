import { createApp } from 'vue'
import { createRouter, createWebHistory, RouterView } from 'vue-router'
import { createPinia } from 'pinia'
import { createHead } from '@unhead/vue'
import { PiniaSharedState } from 'pinia-shared-state'
// @ts-ignore/* Temporary untyped */
import * as untypedPdfjs from 'pdfjs-dist/build/pdf'
import type PdfjsType from 'pdfjs-dist/types/src/pdf'

import { i18n } from '$/locales'
import ResetPasswordView from './views/ResetPasswordView.vue'
import RootView from './views/RootView.vue'
import ProjectView from './views/project/ProjectView.vue'
import ProjectTextbookPageView from './views/project/textbook/page/ProjectTextbookPageView.vue'
import ProjectTextbookPageNewExerciseView from './views/project/textbook/page/ProjectTextbookPageNewExerciseView.vue'
import ProjectTextbookPageExerciseView from './views/project/textbook/page/ProjectTextbookPageExerciseView.vue'
import '$/promise-with-resolvers-polyfill.js'


const pdfjs = untypedPdfjs as typeof PdfjsType
pdfjs.GlobalWorkerOptions.workerSrc = '/pdf.worker.min.js'


const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/ping',
      name: 'ping',
      component: () => import('./views/PingView.vue'),
    },
    {
      path: '/pdfs',
      name: 'pdfs',
      component: () => import('./views/PdfsView.vue'),
    },
    {
      path: '/reset-password/:emailAddress/:token',
      name: 'reset-password',
      component: ResetPasswordView,
      props: true,
    },
    {
      path: '/',
      children: [
        {
          path: '',
          name: 'index',
          component: RootView,
        },
        {
          path: 'errors',
          name: 'errors',
          component: () => import('./views/ErrorsView.vue'),
        },
        {
          path: 'project-:projectId',
          children: [
            {
              path: '',
              name: 'project',
              component: ProjectView,
              props: true,
            },
            {
              path: 'textbook-:textbookId/page-:page',
              children: [
                {
                  path: '',
                  name: 'project-textbook-page',
                  component: ProjectTextbookPageView,
                  props: (route) => {
                    console.assert(typeof(route.params.projectId) === 'string')
                    console.assert(typeof(route.params.textbookId) === 'string')
                    console.assert(typeof(route.params.page) === 'string')
                    return {
                      projectId: route.params.projectId,
                      textbookId: route.params.textbookId,
                      page: Number.parseInt(route.params.page),
                    }
                  },
                },
                {
                  path: 'new-exercise',
                  name: 'project-textbook-page-new-exercise',
                  component: ProjectTextbookPageNewExerciseView,
                  props: (route) => {
                    console.assert(typeof(route.params.projectId) === 'string')
                    console.assert(typeof(route.params.textbookId) === 'string')
                    console.assert(typeof(route.params.page) === 'string')
                    return {
                      projectId: route.params.projectId,
                      textbookId: route.params.textbookId,
                      page: Number.parseInt(route.params.page),
                    }
                  },
                },
                {
                  path: 'exercise-:exerciseId',
                  name: 'project-textbook-page-exercise',
                  component: ProjectTextbookPageExerciseView,
                  props: (route) => {
                    console.assert(typeof(route.params.projectId) === 'string')
                    console.assert(typeof(route.params.textbookId) === 'string')
                    console.assert(typeof(route.params.page) === 'string')
                    console.assert(typeof(route.params.exerciseId) === 'string')
                    console.assert(route.query.displayPage === undefined || typeof(route.query.displayPage) === 'string')
                    return {
                      projectId: route.params.projectId,
                      textbookId: route.params.textbookId,
                      page: Number.parseInt(route.params.page),
                      exerciseId: route.params.exerciseId,
                      displayPage: route.query.displayPage === undefined ? undefined : Number.parseInt(route.query.displayPage),
                    }
                  },
                }
              ],
            },
          ],
        },
      ],
    },
  ],
})


export const app = createApp(RouterView)

app.use(i18n)
app.use(createHead())
app.use(createPinia().use(PiniaSharedState({enable: false})))
app.use(router)
app.mount('#app')
