import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from './views/HomeView.vue'
import About from './views/AboutView.vue'
import Services from './views/ServicesView.vue'
import Donate from './views/DonateView.vue'
import Support from './views/SupportView.vue'
import Events from './views/EventsView.vue'
import Contact from './views/ContactView.vue'
import Register from './views/RegisterView.vue'
import Login from './views/LoginView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/services',
    name: 'Services',
    component: Services
  },
  {
    path: '/donate',
    name: 'Donate',
    component: Donate
  },
  {
    path: '/support',
    name: 'Support',
    component: Support
  },
  {
    path: '/events',
    name: 'Events',
    component: Events
  },
  {
    path: '/contact',
    name: 'Contact',
    component: Contact
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
