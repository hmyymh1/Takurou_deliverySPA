import { createRouter, createWebHistory } from 'vue-router'
import home from './home'
import menuPage from './menuPage'
import mine from './mine'
import login from './login'
import mailPass from './mailPass'
import register from './register'

const routes = [
  home,
  mine,
  menuPage,
  login,
  mailPass,
  register,
  {
    path: '/',
    redirect: '/home'
  },
  {
    path: '/:notFind',
    redirect: '/home'
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
