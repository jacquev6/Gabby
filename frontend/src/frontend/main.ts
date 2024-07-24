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
import RootLayout from './views/RootLayout.vue'
import ProjectLayout from './views/project/ProjectLayout.vue'
import ProjectTextbookLayout from './views/project/textbook/ProjectTextbookLayout.vue'
import ProjectTextbookPageLayout from './views/project/textbook/page/ProjectTextbookPageLayout.vue'
import RootIndexView from './views/index/RootIndexView.vue'
import ProjectIndexView from './views/project/index/ProjectIndexView.vue'
import ProjectTextbookPageListExercisesView from './views/project/textbook/page/list-exercises/ListExercisesView.vue'
import ProjectTextbookPageCreateExerciseView from './views/project/textbook/page/create-exercise/CreateExerciseView.vue'
import ProjectTextbookPageEditExerciseView from './views/project/textbook/page/edit-exercise/EditExerciseView.vue'
import RootView from './new-views/RootView.vue'
import ProjectView from './new-views/project/ProjectView.vue'
import ProjectTextbookPageView from './new-views/project/textbook/page/ProjectTextbookPageView.vue'
import ProjectTextbookPageNewExerciseView from './new-views/project/textbook/page/ProjectTextbookPageNewExerciseView.vue'
import ProjectTextbookPageExerciseView from './new-views/project/textbook/page/ProjectTextbookPageExerciseView.vue'
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
          name: 'new--index',
          component: RootView,
        },
        {
          path: 'errors',
          name: 'new--errors',
          component: () => import('./new-views/ErrorsView.vue'),
        },
        {
          path: 'project-:projectId',
          children: [
            {
              path: '',
              name: 'new--project',
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
    {
      path: '/old',
      component: RootLayout,
      children: [
        {
          path: '',
          name: 'index',
          component: RootIndexView,
        },
        {
          path: 'errors',
          name: 'errors',
          component: () => import('./views/ErrorsView.vue'),
        },
        {
          path: 'project-:projectId',
          component: ProjectLayout,
          props: (route) => (
            {
              projectId: route.params.projectId,
            }
          ),
          children: [
            {
              path: '',
              name: 'project',
              component: ProjectIndexView,
            },
            {
              path: 'textbook-:textbookId',
              component: ProjectTextbookLayout,
              props: (route) => (
                {
                  textbookId: route.params.textbookId,
                }
              ),
              children: [
                {
                  path: 'page-:page',
                  component: ProjectTextbookPageLayout,
                  props: (route) => {
                    console.assert(typeof(route.params.page) === 'string')
                    return {
                      page: Number.parseInt(route.params.page, 10),
                    }
                  },
                  children: [
                    {
                      path: '',
                      name: 'project-textbook-page-list-exercises',
                      component: ProjectTextbookPageListExercisesView,
                    },
                    {
                      path: 'new-exercise',
                      name: 'project-textbook-page-create-exercise',
                      component: ProjectTextbookPageCreateExerciseView,
                    },
                    {
                      path: 'exercise-:exerciseId',
                      name: 'project-textbook-page-edit-exercise',
                      component: ProjectTextbookPageEditExerciseView,
                      props: (route) => (
                        {
                          exerciseId: route.params.exerciseId,
                        }
                      ),
                    },
                  ],
                },
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
