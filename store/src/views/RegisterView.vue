<script setup>
  import {ref} from 'vue'
  import { RouterLink } from 'vue-router';
  import Breadcrumb from '@/components/Breadcrumb.vue';
  const links = ref([]);
  links.value = [
    { 'name': 'Accueil', 'nameUrl': 'home' },
    {'name':'Nouveau compte', 'nameUrl':'register'}
  ];
</script>
<template>
  <Breadcrumb :links="links" />
  <!-- ============== LOGIN ================ -->
   <section class="login-register section--lg">
    <div class="login-register__container container grid">
      <div class="register">
        <h3 class="section__title">Création de compte</h3>
        <form  class="form grid">
          <input type="text" placeholder="Entrez votre utilisateur" class="form__input">
          <input type="email" placeholder="Entrez votre email" class="form__input">
          <input type="password" placeholder="Entrez votre le mot de passe" class="form__input">
          <input type="password" placeholder="Confirmez votre le mot de passe" class="form__input">
          <div class="form__btn">
            <button type="submit" class="btn">Créer</button>
          </div>
        </form>
      </div>
      <p>Vous possèdez de compte, <RouterLink :to="{name:'login'}">se connecter</RouterLink></p>
    </div>
   </section>
</template>
