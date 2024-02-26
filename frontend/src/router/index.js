import { createRouter, createWebHistory } from 'vue-router'

import IndexView from '../views/IndexView.vue'
import PdfView from '../views/PdfView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'index',
      component: IndexView,
    },
    {
      path: '/pdf',
      name: 'pdf',
      component: PdfView
    },
    // This route shall be removed when we actually need the Vue Router.
    // Until then, it's used in end-to-end tests checking the Vue Router is working in all environments.
    {
      path: '/other',
      name: 'other',
      component: () => import('../views/OtherView.vue')
    },
  ],
})

export default router
