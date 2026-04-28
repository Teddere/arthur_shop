<script setup>
  import {ref,computed,onMounted} from 'vue';
  import Breadcrumb from "@/components/Breadcrumb.vue";
  import {useCartStore} from "@/stores/cart.js";

  const linkNavigatePage =ref([]);
  const updateTimers = ref({})
  linkNavigatePage.value = [
    { 'name': 'Accueil', 'nameUrl': 'home' },
    { 'name': 'Catalogue', 'nameUrl': 'catalog'},
    { 'name': 'Panier', 'nameUrl': 'catalog' }
  ]



  const cart = useCartStore();
  const subTotal = computed(()=>{
    return cart.totalPrice
  });

  const productTop = (id)=>{
    cart.updateTopProduct(id)
  }
  const productDown = (id)=>{
    cart.updateDownProduct(id)
  }
  const updateProduct = (id,quantity)=>{
    if(updateTimers.value[id]) {
      clearTimeout(updateTimers.value[id]);
    }
    const count = parseInt(quantity);
    if(isNaN(count) || count < 0)  return;

    updateTimers.value[id] = setTimeout(()=>{
      if (count === 0){
        cart.removeCart(id);
      }
      else {
        cart.editProduct(id,count);
      }
    },500)
  }
  const removeItem = (productId)=>{
    cart.removeCart(productId)
  }


  onMounted(()=>{
    document.title = 'Panier | Arthur'
  })
</script>

<template>
  <Breadcrumb :links="linkNavigatePage" />
  <!-- =============== CART ============================= -->
  <section v-if="cart.items.length === 0" class="empty-cart">
    <p>Votre panier est vide</p>
  </section>
  <section v-else class="cart container section--lg">
    <div class="table__container">
      <table class="table">
        <thead>
          <tr>
            <th></th>
            <th>Article</th>
            <th>Prix</th>
            <th>Quantité</th>
            <th>Total</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item,index) in cart.items" :key="index">
            <td><img :src="item.image_default" alt="article image" class="table__img"></td>
            <td>
            <h3 class="table__title">{{item.title}}</h3>
            <p class="table__description">{{item.description}}</p>
            </td>
            <td>
              <span  class="table__price">{{item.price}} €</span>
            </td>
            <td>
              <div class="btn__carts">
                <button @click="productTop(item.id)" type="button" class="btn-cart btn-up">
                  <i class="fa-solid fa-arrow-up"></i>
                </button>
                <input @input="updateProduct(item.id,$event.target.value)" type="number" :value="item.quantity" name="quantity" id="quantity" class="quantity">
                <button @click="productDown(item.id)" type="button" class="btn-cart btn-down">
                  <i class="fa-solid fa-arrow-down"></i>
                </button>
              </div>
            </td>
            <td>
              <span class="table__subtotal">{{(item.price * item.quantity).toFixed(2)}} €</span>
            </td>
            <td><i @click="removeItem(item.id)" class="table__trash fa-solid fa-trash-alt"></i></td>
          </tr>
        </tbody>

      </table>
    </div>

    <div class="divider">
      <i class="fa-solid fa-fingerprint"></i>
    </div>
    <div class="cart__group grid">

      <div class="cart__total">
          <h3 class="section__title">Total du panier</h3>
          <table class="cart__total-table">
            <tbody>
              <tr>
                <td><span class="cart__total-title">Total achat</span></td>
                <td><span class="cart__total-price">{{subTotal.toFixed(2)}} €</span></td>
              </tr>
              <tr>
                <td><span class="cart__total-title">Total</span></td>
                <td><span class="cart__total-price">565.00 €</span></td>
              </tr>
            </tbody>
          </table>
          <button type="button" class="btn btn-md flex">
            <i class="fa-solid fa-box"></i>
            Validé
          </button>
        </div>
    </div>
  </section>
</template>

<style scoped>
.empty-cart {
  text-align: center;
  padding: 40px;
}
</style>
