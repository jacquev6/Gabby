import { createRouter, createWebHistory } from 'vue-router'

// @todo Move this router into an 'opinion' directory, move the view into a 'opinion' directory
// @todo Rename the view in kebab-case?
import IndexView from '../views/index-view.vue'


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
  ]
})

export default router
