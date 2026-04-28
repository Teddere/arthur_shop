<script setup>
  import {ref,onMounted} from 'vue';
  import { RouterLink,useRouter } from 'vue-router';
  import { useAuthenticate } from '@/stores/store';
  import Breadcrumb from '@/components/Breadcrumb.vue';

  import axios from 'axios';


  const links = ref([]);

  links.value = [
    { 'name': 'Accueil', 'nameUrl': 'home' },
    {'name':'Connexion', 'nameUrl':'login'}
  ];
  const auth = useAuthenticate();
  const router = useRouter();
  const errors = ref([]);
  const email = ref('');
  const password = ref('');

  onMounted(()=>{
    document.title = 'Connexion | Arthur'
  })
  const submitForm  = async ()=>{
    errors.value = [];
    const dataForm = {
      email : email.value,
      password : password.value
    }
    if (email.value.length == 0 || !email.value.includes('@') || !email.value.includes('.')) {
      errors.value.push('Veuillez entrer un email valide')
    }

    if(password.value.length == 0) {
      errors.value.push('Veuillez entrer un mot de passe valide')
    }

    if(!errors.value.length) {
      axios.defaults.headers.common['Authorization'] = null;
      localStorage.removeItem('token')
      auth.removeToken();

      await axios
      .post('/api/V1/login',dataForm)
      .then(response=> {
        const token = response.data.authToken;
        auth.setToken(token);
        axios.defaults.headers.common['Authorization'] = `Token ${auth.token}`;
        localStorage.setItem('token',token);

        const toPath = router.query.to || '/account';
        router.push(toPath);

      })
      .catch(error=>{
        if (error.response) {
          for(const property in error.response.data) {
            errors.value.push(`${property} : ${error.response.data[property]}`)
          }
        } else {
          errors.value.push('Erreur s\'est productée, veuillez réessayer !')
          console.log(JSON.stringify(error))
        }
      })
    }

  }
</script>
<template>
  <Breadcrumb :links="links"></Breadcrumb>
  <!-- ============== LOGIN ================ -->
  <section class="login-register section--lg">
    <div class="login-register__container container grid">
      <div class="login">
        <h3 class="section__title">Compte utilisateur</h3>
        <form class="form grid" @submit.prevent="submitForm">
          <input type="email" v-model="email" placeholder="Entrez votre email" class="form__input">
          <input type="password" v-model="password" placeholder="Entrez votre mot de passe" class="form__input">
          <div class="form__btn">
            <button type="submit" class="btn">
              Connexion
            </button>
          </div>
        </form>
      </div>
      <p>Vous ne possèdez pas de compte, créer un <RouterLink :to="{name:'register'}">nouveau</RouterLink> compte</p>
    </div>
  </section>
</template>
