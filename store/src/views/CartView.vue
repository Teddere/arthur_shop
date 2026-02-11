<script setup>
  import {ref,computed} from 'vue';
  import Breadcrumb from "@/components/Breadcrumb.vue";
  import {useCartStore} from "@/stores/store.js";

  const linkNavigatePage =ref([]);
  const updateTimers = ref({})
  linkNavigatePage.value = [
    { 'name': 'Accueil', 'nameUrl': 'home' },
    { 'name': 'Catalogue', 'nameUrl': 'catalog'},
    { 'name': 'Panier', 'nameUrl': 'catalog' }
  ]


  const couponDiscount = ref(0)
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

  const applyCoupon = ()=>{
    console.log(couponDiscount.value)
  }
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
        <tr>
          <th></th>
          <th>Article</th>
          <th>Prix</th>
          <th>Quantité</th>
          <th>Total</th>
          <th>Action</th>
        </tr>
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
      </table>
    </div>
    <div class="cart__action">
      <button type="button" class="btn btn-md flex">
        <i class="fa-solid fa-bag-shopping"></i>
        Validé
      </button>
    </div>
    <div class="divider">
      <i class="fa-solid fa-fingerprint"></i>
    </div>
    <div class="cart__group grid">
      <div>
        <div class="cart__shipping">
            <h3 class="section__title">Frais de livraison</h3>
            <form action="" class="form grid">
            <input type="text"  placeholder="Entrez le pays" class="form__input">
            <div class="form__group grid">
              <input type="text"  placeholder="Entrez la ville" class="form__input">
              <input type="text"  placeholder="Entrez le code postal" class="form__input">
            </div>
            <div class="form__btn">
              <button type="submit" class="btn flex btn-sm">
                <i class="fa-solid fa-arrows-rotate"></i>
                Actualise
              </button>
            </div>
          </form>
            <div class="cart__coupon">
              <h3 class="section__title">Coupon</h3>
              <form class="coupon__form" @submit.prevent="applyCoupon()">
                  <input ref="" type="text" placeholder="Entrez le code promo" class="form__input">
                  <div class="from__btn">
                    <button type="button" class="btn">Validé</button>
                  </div>
              </form>
            </div>
        </div>
      </div>
      <div class="cart__total">
          <h3 class="section__title">Total du panier</h3>
          <table class="cart__total-table">
            <tr>
              <td><span class="cart__total-title">Total achat</span></td>
              <td><span class="cart__total-price">{{subTotal.toFixed(2)}} €</span></td>
            </tr>
            <tr>
              <td><span class="cart__total-title">Livraison</span></td>
              <td><span class="cart__total-price">5.00 €</span></td>
            </tr>
            <tr>
              <td><span class="cart__total-title">Total</span></td>
              <td><span class="cart__total-price">565.00 €</span></td>
            </tr>
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
