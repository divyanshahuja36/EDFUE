import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../pages/HomePage.vue'
import CounsellingSession from '../pages/CounsellingSession.vue'
import RegisterPage from '../pages/RegisterPage.vue'

const routes = [
  { path: '/', component: HomePage },
  { path: '/counselling-session', component: CounsellingSession },
  { path: '/register', component: RegisterPage }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
