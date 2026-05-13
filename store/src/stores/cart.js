import {defineStore} from "pinia";
import { ref,computed } from "vue";

export const useCartStore=defineStore('cart',()=>{

  const items = ref([]);
  // initialization

  const initialCart = ()=>{
    if (localStorage.getItem('cart')) {
      items.value = JSON.parse(localStorage.getItem('cart'));
    }
    else {
      localStorage.setItem('cart',JSON.stringify(items.value));
    }
  }

  // update storage cart
  const updateStorageCart = ()=>{
    localStorage.setItem('cart',JSON.stringify(items.value));
  }

  initialCart();
  // short description
  const description = (description,limit)=>{

    const words = description.split(/\s+/);
    let descripLimit = words.slice(0,limit).join(' ');
    if(words.length > limit) {
      descripLimit += '...';
    }
    return descripLimit
  }

  // sum total product
  const itemCount = computed(()=>{
    return items.value.reduce((total,item)=>{
      return total + item.quantity
    },0)
  })

  // check product in cart
  const isInCart = (productId)=>{
    return items.value.some(item=>item.id === productId)
  }

  // cart prices
  const totalPrice = computed(()=>{
    return items.value.reduce((total,item)=> total + (item.price * item.quantity),0)
  });

  // add product in cart
  const addToCart = (product,quantity=1)=>{
    const existingItem = items.value.find(item => item.id === product.id );

    if(existingItem) {
      existingItem.quantity += quantity;
    }
    else {
      items.value.push({
        id: product.id,
        title: product.title,
        price: product.newPrice || product.oldPrice,
        image_default: product.get_image_default,
        description: description(product.description,12),
        quantity: quantity,
        ref: product.ref
      });
    }
    updateStorageCart();
    return `${product.title} a été ajouter au panier`;
  }

  // increment product quantity

  const updateTopProduct = (productId)=>{
    const product = items.value.find(item=> item.id === productId);

    if (product) {
      product.quantity +=1;
      updateStorageCart();
    }
  }

  // desincrement product quantity
  const updateDownProduct = (productId)=>{
    const product = items.value.find(item => item.id === productId);

    if(product && product.quantity > 1) {
      product.quantity -= 1;
      updateStorageCart();
    }
  }

  // edit product quantity
  const editProduct = (productId,productValue)=>{
    const product = items.value.find(item=>item.id === productId);

    if(product) {
      product.quantity = productValue;
      updateStorageCart();
    }
  }
  // remove product
  const removeCart = (productId)=> {
     items.value=items.value.filter(item => item.id !==productId);
     updateStorageCart();
  }

  // clearn cart
  const clearCart =()=>{
    items.value = [];
    localStorage.removeItem('cart');
  }

  return {
    // Gertters
    items,
    itemCount,
    totalPrice,
    // Actions
    isInCart,
    addToCart,
    updateTopProduct,
    updateDownProduct,
    editProduct,
    removeCart,
    clearCart
  }
})
