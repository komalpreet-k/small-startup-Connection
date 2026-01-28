import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import BusinessDetailView from '../views/BusinessDetailView.vue'
import LoginView from "../views/LoginView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/business/:id',
      name: 'business-detail',
      component: BusinessDetailView,
    },
    {
      path: "/login",
      name: "Login",
      component: LoginView,
    }
  ],
})

export default router
