import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '@/views/Dashboard.vue'
import Auth from '@/views/Auth.vue'


const routes = [
  { path: '/', name: 'Dashboard', component: Dashboard },
  { path: '/auth', name: 'Auth', component: Auth }
]
const router = createRouter({ history: createWebHistory(), routes })

export default router
