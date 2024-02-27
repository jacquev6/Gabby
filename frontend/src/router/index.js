import { createRouter, createWebHistory } from 'vue-router'

import IndexView from '../views/IndexView.vue'
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
      path: '/textbook/:textbookId/page/:page',
      name: 'textbook-page',
      component: TextbookPageView,
      props: (route) => {
        return {...route.params, page: Number.parseInt(route.params.page, 10)}
      },
    },
    {
      path: '/pdf',
      name: 'pdf',
      component: () => import('../views/PdfView.vue')
    },
  ],
})

export default router
