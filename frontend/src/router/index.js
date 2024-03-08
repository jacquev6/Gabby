import { createRouter, createWebHistory } from 'vue-router'

import IndexView from '../views/IndexView.vue'
import ProjectView from '../views/ProjectView.vue'
import TextbookPageView from '../views/TextbookPageView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'index',
      component: IndexView,
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
      component: TextbookPageView,
      props: (route) => {
        return {...route.params, page: Number.parseInt(route.params.page, 10)}
      },
    },
  ],
})

export default router
