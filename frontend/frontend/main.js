import { createApp } from 'vue'
import { createRouter, createWebHistory, RouterView } from 'vue-router'
import { createPinia } from 'pinia'
import { createHead } from '@unhead/vue'
import { PiniaSharedState } from 'pinia-shared-state'
import * as pdfjs from 'pdfjs-dist/build/pdf'

import { i18n } from './locales'
import RootView from './views/root-view.vue'
import IndexView from './views/index/index-view.vue'
import ProjectView from './views/project/project-view.vue'
import ProjectTextbookPageRootView from './views/project-textbook-page/project-textbook-page-root-view.vue'
import ProjectTextbookPageListExercisesView from './views/project-textbook-page/project-textbook-page-list-exercises-view.vue'
import ProjectTextbookPageCreateExerciseView from './views/project-textbook-page/project-textbook-page-create-exercise-view.vue'
import ProjectTextbookPageEditExerciseView from './views/project-textbook-page/project-textbook-page-edit-exercise-view.vue'


pdfjs.GlobalWorkerOptions.workerSrc = '/pdf.worker.min.js'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/ping',
      name: 'ping',
      component: () => import('./views/ping-view.vue'),
    },
    {
      path: '/pdfs',
      name: 'pdfs',
      component: () => import('./views/pdfs-view.vue'),
    },
    {
      path: '/',
      component: RootView,
      children: [
        {
          path: '',
          name: 'index',
          component: IndexView,
        },
        {
          path: 'project/:projectId',
          name: 'project',
          component: ProjectView,
          props: (route) => (
            {
              projectId: route.params.projectId,
            }
          ),
        },
        {
          path: 'project/:projectId/textbook/:textbookId/page/:page',
          component: ProjectTextbookPageRootView,
          props: (route) => (
            {
              projectId: route.params.projectId,
              textbookId: route.params.textbookId,
              page: Number.parseInt(route.params.page, 10),
            }
          ),
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
})


createApp(RouterView)
  .use(i18n)
  .use(createHead())
  .use(createPinia().use(PiniaSharedState({enable: false})))
  .use(router)
  .mount('#app')
