import { createRouter, createWebHashHistory } from 'vue-router'
import Login from '../views/Login.vue'
import NotFound from '../views/NotFound.vue'
import Home from '../views/Index.vue'
import List from "../views/List.vue"
import Detail from "../views/Detail.vue"

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    children: [
      {
        path: "list",
        name: "List",
        component: List
      },
      {
        path: "detail",
        name: "Detail",
        component: Detail
      }
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
  history: createWebHashHistory(process.env.BASE_URL),
  routes
})

export default router
