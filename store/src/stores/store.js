import {defineStore} from "pinia";
import {ref} from 'vue';

export const useAuthenticate = defineStore('auth',()=>{
  const isAuthenticated = ref(null);
  const token = ref(null)
   // initialization

   const initialization = ()=> {
      if(localStorage.getItem('token')) {
        token.value = localStorage.getItem('token');
        isAuthenticated.value = true;
      } else {
        token.value = null;
        isAuthenticated.value = false;
      }
   }
   initialization();

   const setToken = (tokenId)=>{
    token.value = tokenId;
    isAuthenticated.value = true;
   }
   const removeToken = ()=>{
    token.value = null;
    isAuthenticated.value = false;
   }
  return {
    // Getters
    token,
    // Action
    setToken,
    removeToken,
  }
})

export const useLoadingStore = defineStore('load',()=>{
  const isLoading = ref(false);
  const defaultDelay = 600;
  /**
   * @param {number} delay - par défaut 300ms
   */
  const loadingDelay = (delay = defaultDelay)=>{
    return new Promise(resolve => setTimeout(resolve,delay));
  }

   /*@param {function} asyncFn - fonction à exécuter
   *@param {number} delay - Délai de chargement en ms
   */
  const loadingPage = async (asyncFn,delay = defaultDelay)=>{
    isLoading.value = true;
    const start = Date.now();
    try {
      const result = await asyncFn();
      const elapsed = Date.now() - start;

      if (elapsed < delay) {
        await loadingDelay(delay - elapsed);
      }
      return result;
    } finally {
      isLoading.value = false;
    }
  }
  return {
    isLoading,
    defaultDelay,
    loadingPage,
    loadingDelay,
  }
})

