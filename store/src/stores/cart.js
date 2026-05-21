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
  const addToCart = (product)=>{
    const existingItem = items.value.find(item => item.id === product.element.id );
    if(existingItem) {
      existingItem.quantity += 1;
    }
    else {
      items.value.push({
        id: product.element.id,
        product_id: product.id,
        title: product.title,
        price: product.element.newPrice || product.element.base_price,
        size: product.element.size,
        color: product.element.color.name,
        image_default: product.image_default,
        description: description(product.description,10),
        quantity: 1,
        ref: product.ref,
        sku: product.element.sku,
        url: product.url,
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

  const updateProduct = (product,quantity)=>{
    const existingItem = items.value.find((item)=> item.product_id === product.id);
    if(existingItem) {
     existingItem.id = product.element.id
      existingItem.quantity = quantity;
      existingItem.size = product.element.size;
      existingItem.color = product.element.color.name;
      existingItem.price = product.element.newPrice || product.element.base_price;
      existingItem.sku = product.element.sku;
    }
    else {
      items.value.push({
        id: product.element.id,
        product_id: product.id,
        title: product.title,
        price: product.element.newPrice || product.element.base_price,
        size: product.element.size,
        color: product.element.color.name,
        image_default: product.image_default,
        description: description(product.description,10),
        quantity: quantity,
        ref: product.ref,
        sku: product.element.sku,
        url: product.url,
      });

    }
    /*updateStorageCart();
    return `${product.title} a été ajouter au panier`;*/
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
    updateProduct,
    clearCart
  }
})
