import { createRouter, createWebHistory } from 'vue-router'

import PdfView from '../views/PdfView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'pdf',
      component: PdfView
    },
    {
      path: '/help',
      name: 'help',
      component: () => import('../views/HelpView.vue')
    },
  ],
})

export default router
