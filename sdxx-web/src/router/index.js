import {createRouter,createWebHashHistory} from 'vue-router'

import image_loader from '../components/Imageloder.vue' 
import home from '../components/home.vue'
import outcome from '../components/outcome.vue'
import author from '../components/author.vue'
import resource from '../components/resource.vue'
import more from '../components/more.vue'

const routes=[
  {
    path:'/',
    name:'Home',
    component:home,
    children:[
      {
        path:'/',
        name:'classify',
        component:image_loader,
      },
      {
        path:'/Outcome',
        name:'outcome',
        component:outcome,
      },
    ]
  },
  {
    path:'/author',
    name:'author',
    component:author,
  },
  {
    path:'/resource',
    name:'resource',
    component:resource,
  },
  {
    path:'/more',
    name:'more',
    component:more,
  }
]

const router=createRouter({
  history:createWebHashHistory(),
  routes
})

export default router