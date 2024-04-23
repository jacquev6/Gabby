import { createApp } from 'vue'
import { createRouter, createWebHistory, RouterView } from 'vue-router'
import { createPinia } from 'pinia'
import { createHead } from '@unhead/vue'
import { PiniaSharedState } from 'pinia-shared-state'
// @ts-ignore/* Temporary untyped */
import * as untypedPdfjs from 'pdfjs-dist/build/pdf'
import type PdfjsType from 'pdfjs-dist/types/src/pdf'

import { i18n } from './locales'
import RootLayout from './views/RootLayout.vue'
import ProjectLayout from './views/project/ProjectLayout.vue'
import ProjectTextbookLayout from './views/project/textbook/ProjectTextbookLayout.vue'
import ProjectTextbookPageLayout from './views/project/textbook/page/ProjectTextbookPageLayout.vue'
import RootIndexView from './views/index/RootIndexView.vue'
import ProjectIndexView from './views/project/index/ProjectIndexView.vue'
import ProjectTextbookPageListExercisesView from './views/project/textbook/page/list-exercises/ListExercisesView.vue'
import ProjectTextbookPageCreateExerciseView from './views/project/textbook/page/create-exercise/CreateExerciseView.vue'
import ProjectTextbookPageEditExerciseView from './views/project/textbook/page/edit-exercise/EditExerciseView.vue'


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
      path: '/',
      component: RootLayout,
      children: [
        {
          path: '',
          name: 'index',
          component: RootIndexView,
        },
        {
          path: 'project/:projectId',
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
              path: 'textbook/:textbookId',
              component: ProjectTextbookLayout,
              props: (route) => (
                {
                  textbookId: route.params.textbookId,
                }
              ),
              children: [
                {
                  path: 'page/:page',
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
                      path: 'exercise/:exerciseId',
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


createApp(RouterView)
  .use(i18n)
  .use(createHead())
  .use(createPinia().use(PiniaSharedState({enable: false})))
  .use(router)
  .mount('#app')
