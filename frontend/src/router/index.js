import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import NotFound from '../views/NotFound.vue'
import Home from '../views/Index.vue'
import Dashboard from '../views/Dashboard.vue'
import List from "../views/List.vue"
import Detail from "../views/Detail.vue"
import TemplateView from "../views/business/template.vue"

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    children: [
      {
        path: "dashboard",
        name: "Dashboard",
        component: Dashboard
      },
      {
        path: "list/:table",
        name: "List",
        component: List
      },
      {
        path: "detail/template/:type/:id",
        name: "Template",
        component: TemplateView
      }
      // {
      //   path: "detail/:table/:type/:id",
      //   name: "Detail",
      //   component: Detail
      // }
    ]
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  { path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFound },
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
