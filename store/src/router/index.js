import { createRouter, createWebHistory } from 'vue-router'
import {useLoadingStore} from "@/stores/store.js";

import HomeView from '@/views/HomeView.vue'
import CatalogView from '@/views/CatalogView.vue';
import CatalogDetail from "@/views/CatalogDetail.vue";
import DetailProductView from "@/views/DetailProductView.vue";
import CartView from "@/views/CartView.vue";
import LoginView from '@/views/LoginView.vue';
import RegisterView from '@/views/RegisterView.vue';
import AccountView from "@/views/AccountView.vue";
import SearchView from '@/views/SearchView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // home page
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    // catalog
    {
      path:'/catalog',
      name:'catalog',
      component: CatalogView,
    },
    // cart
    {
      path:'/cart',
      name:'cart',
      component: CartView,
    },
    {
      path:'/search',
      name:'search',
      component: SearchView
    },
    // category name catalog
    {
      path:'/catalog/:category_slug/',
      name:'catalog_name',
      component: CatalogDetail,
    },
    // Detail product
    {
      path:'/:category_slug/:product_slug/',
      name:'detail',
      component: DetailProductView,
    },
    // login page
    {
      path:'/login',
      name:'login',
      component: LoginView
    },
    // register page
    {
      path:'/register',
      name:'register',
      component: RegisterView
    },
    // account page
    {
      path:'/account',
      name:'account',
      component:AccountView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
  ],
})

router.beforeEach((to,from,next)=>{
  const loading = useLoadingStore();
  loading.isLoading = true;
  next();
})

router.afterEach(()=>{
  const loading = useLoadingStore();
  setTimeout(()=>{
    loading.isLoading = false;
  },loading.defaultDelay);
})
export function handleRouterError(error) {
  const status =  error.response?.status;

  if(status === 404) {
    router.push('/404');
    return new Error('Ressource non trouvée');
  }
  if (status === 500) {
    router.push('/404'); // router.push('/erreur-serveur');
    return new Error('Erreur serveur');
  }
  if (error.code === 'ECONNABORTED') {
    router.push('/404'); //     router.push('/timeout'); // route optionnelle
    return new Error('Délai d’attente dépassé');
  }
  console.error('Erreur non gérée :', error);
  router.push('/404');
  return error;
}
export default router
