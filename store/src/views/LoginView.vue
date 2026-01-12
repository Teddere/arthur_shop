<script setup>
  import {ref} from 'vue';
  import { RouterLink } from 'vue-router';
  import Breadcrumb from '@/components/Breadcrumb.vue';
  const links = ref([]);

  links.value = [
    { 'name': 'Accueil', 'nameUrl': 'home' },
    {'name':'Connexion', 'nameUrl':'login'}
  ];

</script>
<template>
  <Breadcrumb :links="links"></Breadcrumb>
  <!-- ============== LOGIN ================ -->
  <section class="login-register section--lg">
    <div class="login-register__container container grid">
      <div class="login">
        <h3 class="section__title">Compte utilisateur</h3>
        <form class="form grid">
          <input type="email" placeholder="Entrez votre email" class="form__input">
          <input type="password" placeholder="Entrez votre mot de passe" class="form__input">
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
