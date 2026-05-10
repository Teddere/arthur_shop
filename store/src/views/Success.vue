<script setup>
  import { RouterLink } from 'vue-router';
  import { onMounted } from 'vue';
  import Breadcrumb from '@/components/Breadcrumb.vue';

  const linkNavigatePage = [
    { 'name': 'Accueil', 'nameUrl': 'home' },
    { 'name': 'Catalogue', 'nameUrl': 'catalog'},
    { 'name': 'Panier', 'nameUrl': 'catalog' }
  ]
  onMounted(()=>{
    document.title = 'Success | Arthur'
  })
</script>
<template>
  <Breadcrumb :links="linkNavigatePage" />
  <section class="success-section">
    <div class="success-container section--lg">
      <div class="success__content container">
         <h1 class="success__title"><i class="fa-solid fa-check"></i>&ensp;Merci !</h1>
         <p class="success_decription">Votre commande a été validée avec succès.<br>Vous trouverez votre facture dans votre espace</p>
         <RouterLink :to="{name:'home'}" class="btn btn-md">Retour à acceil</RouterLink>
      </div>
    </div>
  </section>
</template>
