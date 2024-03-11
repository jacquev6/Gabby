import { createRouter, createWebHistory } from 'vue-router'


// @todo Move this router into an 'opinion' directory, move the view into a 'opinion' directory

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/ping',
      name: 'ping',
      component: () => import('../views/ping-view.vue'),
    },
  ]
})

export default router
