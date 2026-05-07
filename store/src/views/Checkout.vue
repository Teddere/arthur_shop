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
  const stripe = ref({})
  const card = ref({})
  const firstName = ref(null);
  const lastName = ref(null);
  const email = ref(null);
  const phone = ref(null);
  const address = ref(null);
  const comment = ref(null)
  const errors = ref([]);

  const style = {
    base: {
      color:'#475C53',
      fontFamily: "'lato', sans-serif",
      fontSize: '0.875rem',
      letterSpacing: '0.02em',
      '::placeholder': {
        color: '#9ca3af',
        letterSpacing: '0.05em',
      },
      ':focus': {
        color: '#4E31CE',
      },
    },
    invalid: {
      color: '#E24B4A',
      iconColor: '#E24B4A',
   },
    complete: {
      color: '#0F6E56',
      iconColor: '#0F6E56',
    },
  }
  onMounted(()=>{
    document.title ='Checkout | Arthur'
    if(cart.isInCart) {
      //
      stripe.value = Stripe(stripe_secret);
      const elements = stripe.value.elements();
      card.value = elements.create('card',{hidePostalCode:true,style,})

      card.value.mount('#card-element')
    }
    card.value.on('change', (event) => {
    const errorEl = document.getElementById('card-errors');
    if (event.error) {
      errorEl.textContent = event.error.message;
    } else {
      errorEl.textContent = '';
    }
  });
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
        <p id="card-errors" style="color: #E24B4A; font-size: 12px; margin-top: 5px;"></p>
        <div id="card-element" class="payment__methods"></div>
        <button @click="submitForm" type="button" class="btn btn-md">Confirmer</button>
      </div>
    </div>
  </section>
</template>
<style>
#card-element {
  background:  #f8f8f8;
  border: 0.5px solid #d1d5db;
  border-radius: 8px;
  padding: 11px 14px;
  height: 44px;
  transition: border-color 0.15s, box-shadow 0.15s;
}
#card-element.StripeElement--focus {
  border-color: #7F77DD;
  box-shadow: 0 0 0 3px rgba(127, 119, 221, 0.12);
  background: #ffffff;
  outline: none;
}
#card-element.StripeElement--invalid {
  border-color: #E24B4A;
  box-shadow: 0 0 0 3px rgba(226, 75, 74, 0.10);
}
#card-element.StripeElement--complete {
  border-color: #1D9E75;
}
</style>
