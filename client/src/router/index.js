import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Upload from '../views/Upload.vue'
import Table from '../views/Table.vue'
import Analysis from '../views/Analysis.vue'
import API from '../doc/API.vue'
import Guide from '../doc/Guide.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/upload',
    name: 'Upload',
    component: Upload
  },
 {
    path: '/table',
    name: 'Table',
    component: Table
 },
 {
    path: '/analysis',
    name: 'Analysis',
    component: Analysis
 },
{
  path: '/api',
  name: 'API',
  component: API
},
{
  path: '/guide',
  name: 'Guide',
  component: Guide
},
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// 滚动行为
router.beforeEach((to, from, next) => {
  window.scrollTo(0, 0) // 在切换路由时,将页面滚动到顶部
  next()
})

export default router