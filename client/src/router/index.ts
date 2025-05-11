import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '@/views/Dashboard.vue'
import Auth from '@/views/Auth.vue'
import AuthCallback from '@/views/AuthCallback.vue'

const routes = [
    { path: '/', name: 'Dashboard', component: Dashboard },
    { path: '/auth', name: 'Auth', component: Auth },
    { path: '/auth/auth-callback', component: AuthCallback }
]
const router = createRouter({ history: createWebHistory(), routes })

export default router
