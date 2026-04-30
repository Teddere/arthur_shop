<script setup>
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  import { useCartStore } from '@/stores/cart';
  import Breadcrumb from '@/components/Breadcrumb.vue';
  import axios from 'axios';

  const stripe_secret = import.meta.env.VITE_STRIPE_SECRET_KEY_PUBLIC;
  const linkNavigatePage = [
  { 'name': 'Accueil', 'nameUrl': 'home' },
  { 'name': 'Catalogue', 'nameUrl': 'catalog' },
  { 'name': 'Panier', 'nameUrl':'cart'}
  ];
  const router = useRouter();
  const cart = useCartStore();
  const payment = ref(null);
  const stripe = ref({})
  const card = ref({})
  const firstName = ref(null);
  const lastName = ref(null);
  const email = ref(null);
  const phone = ref(null);
  const address = ref(null);
  const comment = ref(null)
  const errors = ref([]);

  onMounted(()=>{
    document.title ='Checkout | Arthur'
    if(cart.isInCart) {

      stripe.value = Stripe(stripe_secret);
      const elements = stripe.value.elements();
      card.value = elements.create('card',{hidePostalCode:true})

      card.value.mount('#card-element')
    }
  })

  const submitForm = ()=>{
    errors.value = [];
    if (firstName.value.length === 0) {
      errors.value.push('Entrez un nom prénom')
    }
    if (lastName.value.length === 0) {
      errors.value.push('Entrez un nom de famille')
    }
    if (email.value.length === 0) {
      errors.value.push('Entrez un email')
    }
    if (phone.value.length === 0) {
      errors.value.push('Entrez un numéro de téléphone')
    }


    if (!errors.value.length) {

        // chargement
        stripe.value.createToken(card.value).then(result => {
          if(result.error) {
            // arreter le chargment
            errors.value.push('Paiment n\'a pas abouti avec stripe, veuillez réessayer')
            console.log(result.error.message)
          } else {
            stripeTokenHandler(result.token)
          }
        })
        /*axios.post('/api/v1/order',dataForm)
        .then(response=> {
          console.log(response.data)
          // router.push('/cart/success')
          // chargement
          stripe.value.createToken(cart)
          .then(resus)
        })
        .catch(error=> {
          if (error.response) {
            for(const property in error.response.data) {
              errors.value.push(`${property} : ${error.response.data[property]}`)
            }
          } else {
            errors.value.push('Erreur s\'est productée, veuillez réessayer !')
            console.log(JSON.stringify(error))
          }
        })*/
    }
  }

  const stripeTokenHandler = async (token)=>{
    const items = []
    for (let i=0; i < cart.items.length; i++) {
      const item = cart.items[i]
      const obj = {
        product : item.id,
        quantity: parseInt(item.quantity),
        price: parseFloat(item.price)
      }

      items.push(obj)

    }

    const dataForm = {
          'first_name': firstName.value,
          'last_name': lastName.value,
          'email': email.value,
          'phone': phone.value,
          //'payment': payment.value,
          // optional
          'address': address.value,
          'comment': comment.value,
          'items': items,
          'stripe_token': token.id
        }
      await axios
      .post('/api/v1/checkout/',dataForm)
      .then(response=>{
        cart.clearCart();
        router.push('/cart/success');
        console.log(response.data)
      })
      .catch(error=>{

        errors.value.push('Une erreur s\'est produite, veuillez réessayer')
        console.log(error.response.data)
      })
  }
</script>
<template>
  <Breadcrumb :links="linkNavigatePage" />
  <section class="checkout section--lg">
    <div class="checkout__container container grid">
      <div class="checkout__group">
        <h3 class="section__title">Utilisateur</h3>
        <form @submit.prevent="submitForm" class="form grid">
          <input type="text" v-model="firstName"  class="form__input" placeholder="Entrez votre prénom " >
          <input type="text" v-model="lastName"  class="form__input" placeholder="Entrez votre nom" >
          <input type="text" v-model="email"  class="form__input" placeholder="Entrez email" >
          <input type="text" v-model="phone" class="form__input" placeholder="Entrez le numéro de téléphone" >
          <input type="text" v-model="address" class="form__input" placeholder="Entrez l'adresse " >
          <h3 class="checkout__title">Commentaire</h3>
          <textarea v-model="comment" class="form__input textarea" placeholder="Entrez un commentaire"></textarea>
        </form>
        <div class="form__notification" v-if="errors.length">
          <ul v-for="err in errors" :key="err">
            <li>{{ err }}</li>
          </ul>
        </div>
      </div>
      <div class="checkout__group">
        <h3 class="section__title">Validation de panier</h3>
        <table class="order__table">
          <thead>
            <tr>
              <th colspan="2">Article(s)</th>
              <th>Total</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item,index) in cart.items" :key="index">
              <td><img :src="item.image_default" alt="article image" class="order__img"></td>
              <td>
                <h3 class="table__title">{{ item.title }}</h3>
                <p class="table__quantity">X{{ item.quantity }}</p>
              </td>
              <td><span class="table__price">{{ (item.price * item.quantity).toFixed(2) }} €</span></td>
            </tr>
            <tr>
              <td><span class="order__subtitle">Panier</span></td>
              <td colspan="2"><span class="table__price">{{ cart.totalPrice }} €</span></td>
            </tr>
            <tr>
              <td><span class="order__subtitle">Livraison</span></td>
              <td colspan="2"><span class="table__price">5 €</span></td>
            </tr>
            <tr>
              <td><span class="order__subtitle">Total</span></td>
              <td colspan="2"><span class="table__grand-total"> {{ cart.totalPrice + 5 }}€</span></td>
            </tr>
          </tbody>
        </table>
        <div class="payment__methods">
          <h3 class="checkout__title">Mode de paiment</h3>
          <div class="payment__option flex">
            <input type="radio" v-model="payment" value="creditCard" id="payement_1" checked class="payment_input">
            <label for="payement_1" class="payment_label">Par Carte</label>
          </div>
          <div class="payment__option flex">
            <input type="radio" v-model="payment" value="strip"  id="payement_2"  class="payment_input">
            <label for="payement_2" class="payment_label">Par Stripe</label>
          </div>
          <div class="payment__option flex">
            <input type="radio" v-model="payment" value="paypal" id="payement_3"  class="payment_input">
            <label for="payement_3" class="payment_label">Par Paypal</label>
          </div>

        </div>
        <button @click="submitForm" type="button" class="btn btn-md">Confirmer</button>
      </div>
      <div id="card-element"></div>
    </div>
  </section>
</template>
