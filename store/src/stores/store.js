import {defineStore} from "pinia";
import {ref,computed} from 'vue';

export const useAuth = defineStore('auth',()=>{
  const user = ref(null);
  const authentificate = ()=>{
    user.value = {
      username:'',
    }
  }
  return {
    user,
    authentificate,
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
  /*
   *@param {function} asyncFn - fonction à exécuter
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

export const useCartStore=defineStore('cart',()=>{
  const items = ref([]);
  const description = (description,limit)=>{

    const words = description.split(/\s+/);
    let descripLimit = words.slice(0,limit).join(' ');
    if(words.length > limit) {
      descripLimit += '...';
    }
    return descripLimit
  }
  // Nombre total d'articles
  const itemCount = computed(()=>{
    return items.value.reduce((total,item)=>{
      return total + item.quantity
    },0)
  })
  // Vérifier si un produit est dans le panier
  const isInCart = (productId)=>{
    return items.value.some(item=>item.id === productId)
  }
  // Prix total du panier
  const totalPrice = computed(()=>{
    return items.value.reduce((total,item)=> total + (item.price * item.quantity),0)
  })
  // ACTIONS - Méthodes pour modifier l'état
  const addToCart = (product)=>{
    const existingItem = items.value.find(item => item.id === product.id)

    if(existingItem) {
      // Si le produit existe, augmenter la quantité
      existingItem.quantity +=1
    }else {
      // Sinon, l'ajouter avec une quantité de 1
      items.value.push({
        id: product.id,
        title: product.title,
        price: product.newPrice || product.oldPrice,
        image_default: product.get_image_default,
        description: description(product.description,12),
        quantity: 1,
        ref: product.ref
      })
    }
    return `${product.title} a été ajouter au panier`;
  }
  // Augmenter la quantité d'un produit
  const updateTopProduct=(productId)=>{
    const item = items.value.find(item => item.id === productId)
    if(item) {
      item.quantity += 1;
    }
  }
  const updateDownProduct = (productId)=>{
    const item = items.value.find(item => item.id === productId)
    if(item && item.quantity > 1){
      item.quantity -= 1;
    }
  }

  const editProduct = (productId,productValue)=>{
    const item = items.value.find(item => item.id === productId)
    if (item) {
      item.quantity = productValue;
    }
  }

  const removeCart = (productId)=>{
    items.value = items.value.filter(item => item.id !== productId)
  }

  const clearCart = ()=>{
    items.value = []
  }
  return {
    // state
    items,
    // Getters
    itemCount,
    totalPrice,
    isInCart,
    // Action
    addToCart,
    updateTopProduct,
    updateDownProduct,
    editProduct,
    removeCart,
    clearCart,

  }
});

export const useToastStore = defineStore('toast',()=>{
  const toasts = ref([]);
  let toastId = 0;
  const addToast = (message,type='success',duration=3000)=>{
    const id = toastId++;
    const toast = {
      id,
      message,
      type,
      duration
    }
    toasts.value.push(toast);

    if (duration > 0){
      setTimeout(()=>{
        removeToast(id)
      },duration)
    }
    return id;
  }

  const removeToast = (id)=>{
    const index = toasts.value.findIndex(t => t.id === id);
    if (index !== -1 ) toasts.value.splice(index,1);
  }
  const success = (message,duration) => addToast(message,'success',duration);
  const error = (message,duration) => addToast(message,'error',duration);
  const warning = (message,duration) => addToast(message,'warning',duration);
  const info = (message,duration) => addToast(message,'info',duration);
  return {
    toasts,
    addToast,
    removeToast,
    success,
    error,
    warning,
    info
  }
})
