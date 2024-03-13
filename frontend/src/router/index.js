import { createRouter, createWebHistory } from 'vue-router'

import IndexView from '../views/index/index-view.vue'
import ProjectView from '../views/project-view.vue'
import ProjectTextbookPageView from '../views/project-textbook-page-view.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'index',
      component: IndexView,
    },
    {
      path: '/ping',
      name: 'ping',
      component: () => import('../views/ping-view.vue'),
    },
    {
      path: '/project/:projectId',
      name: 'project',
      component: ProjectView,
      props: true,
    },
    {
      path: '/project/:projectId/textbook/:textbookId/page/:page',
      name: 'project-textbook-page',
      component: ProjectTextbookPageView,
      props: (route) => {
        return {...route.params, page: Number.parseInt(route.params.page, 10)}
      },
    },
  ],
})

export default router
