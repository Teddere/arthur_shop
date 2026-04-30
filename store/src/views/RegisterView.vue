<script setup>
  import axios from 'axios'
  import {ref,onMounted} from 'vue'
  import { RouterLink,useRouter } from 'vue-router';
  import Breadcrumb from '@/components/Breadcrumb.vue';
  import { useToastStore } from '@/stores/toast.js';

  const toast = useToastStore();
  const router = useRouter();
  const links = ref([]);
  const errors = ref([]);
  links.value = [
    { 'name': 'Accueil', 'nameUrl': 'home' },
    {'name':'Nouveau compte', 'nameUrl':'register'}
  ];
  const username = ref('');
  const email = ref('');
  const password = ref('');
  const password2 = ref('');
  onMounted(()=>{
    document.title = 'Création | Arthur';
  })

  const submitForm =()=>{
    errors.value =[]

    if (username.value.length===0){
      errors.value.push('Veuillez entrer un nom utilisateur !')
    }

    if (!email.value.includes('@') || !email.value.includes('.') || email.value.length == 0)
    {
      errors.value.push('Veuillez entrer un email valide')
    }
    if(password.value.length == 0 || password.value !== password2.value)
    {
      errors.value.push('Veuillez un mot de passe valide')
    }

    if (errors.value.length) {
      toast.warning('Message de test !',3000)
    }
    else {
      const dataForm = {
        username: username.value,
        email: email.value,
        password: password.value,
        re_password: password2.value,
      }
      axios
      .post('/api/v1/users/',dataForm)
      .then(response=> {
        toast.success(`Le compte utilisateur ${response.data.username} crée avec succès !`,3000);
        setTimeout(
          router.push('/login'),3000)
        })
      .catch(err=>{
        if (err.response) {
          for (const property in err.response.data) {
            errors.value.push(`${err.response.data[property]}`)
          }
        } else if (err.message) {
            errors.value.push('Une erreur s\'est produite. Veuillez réessayer');
            console.log(JSON.stringify(err))
        }
      })
    }

  }
</script>
<template>
  <Breadcrumb :links="links" />
  <!-- ============== LOGIN ================ -->
   <section class="login-register section--lg">
    <div class="login-register__container container grid">
      <div class="register">
        <h3 class="section__title">Création de compte</h3>
        <form  class="form grid" @submit.prevent="submitForm">
          <input type="text" v-model="username" placeholder="Entrez votre utilisateur" class="form__input">
          <input type="email" v-model="email" placeholder="Entrez votre email" class="form__input">
          <input type="password" v-model="password" placeholder="Entrez votre le mot de passe" class="form__input">
          <input type="password" v-model="password2" placeholder="Confirmez votre le mot de passe" class="form__input">
          <div class="form__btn">
            <button type="submit" class="btn">Créer</button>
          </div>
          <div class="form__notification" v-if="errors.length">
            <ul v-for="err in errors" :key="err">
              <li>{{ err }}</li>
            </ul>
          </div>
        </form>
      </div>
      <p>Vous possèdez de compte, <RouterLink :to="{name:'login'}">se connecter</RouterLink></p>
    </div>
   </section>
</template>
