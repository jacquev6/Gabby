import { createRouter, createWebHistory } from 'vue-router'

import IndexView from '../views/IndexView.vue'


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
      component: () => import('../views/PingView.vue'),
    },
  ]
})

export default router
