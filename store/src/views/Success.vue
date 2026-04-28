<script setup>
  import { RouterLink } from 'vue-router';
  import { onMounted } from 'vue';

  onMounted(()=>{
    document.title = 'Success | Arthur'
  })
</script>
<template>
  <section class="success-section">
    <div class="success-container section--lg">
      <div class="success__content container">
         <h1 class="success__title">Merci</h1>
         <p class="success_decription">Votre commande a été validée avec succès.<br>Vous trouverez votre facture dans votre espace</p>
         <RouterLink :to="{name:'home'}" class="btn btn-md">Retour à acceil</RouterLink>
      </div>
    </div>
  </section>
</template>
