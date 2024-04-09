import { createApp } from 'vue'
import { createRouter, createWebHistory, RouterView } from 'vue-router'
import { createPinia } from 'pinia'
import { createHead } from '@unhead/vue'
import { PiniaSharedState } from 'pinia-shared-state'
import * as pdfjs from 'pdfjs-dist/build/pdf'

import { i18n } from './locales'
import RootView from './views/root-view.vue'
import IndexNavbar from './views/index/index-navbar.vue'
import IndexView from './views/index/index-view.vue'
import ProjectNavbar from './views/project/project-navbar.vue'
import ProjectView from './views/project/project-view.vue'
import ProjectTextbookPageNavbar from './views/project-textbook-page/project-textbook-page-navbar.vue'
import ProjectTextbookPageView from './views/project-textbook-page/project-textbook-page-view.vue'


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
      props: {
        title: 'MALIN',
        breadcrumbs: [],
      },
      children: [
        {
          path: '',
          name: 'index',
          components: {
            nav: IndexNavbar,
            main: IndexView,
          },
          props: {
            NavBar: {
              title: 'MALIN',
              breadcrumbs: [],
            },
          }
        },
        {
          path: 'project/:projectId',
          name: 'project',
          components: {
            nav: ProjectNavbar,
            main: ProjectView,
          },
          props: true,
        },
        {
          path: 'project/:projectId/textbook/:textbookId/page/:page',
          name: 'project-textbook-page',
          components: {
            nav: ProjectTextbookPageNavbar,
            main: ProjectTextbookPageView,
          },
          props: (route) => (
            {...route.params, page: Number.parseInt(route.params.page, 10)}
          ),
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
