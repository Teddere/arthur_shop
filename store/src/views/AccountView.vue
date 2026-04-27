<script setup>
  import {ref} from 'vue';
  import SideBar from "@/components/SideBar.vue";
  import Breadcrumb from "@/components/Breadcrumb.vue";

  const linkNavigatePage = ref([]);
  linkNavigatePage.value = [
    { 'name': 'Accueil', 'nameUrl': 'home' },
    { 'name': 'Catalogue', 'nameUrl': 'catalog'},
    { 'name': 'Compte', 'nameUrl': 'catalog' }
  ]

</script>

<template>
  <Breadcrumb :links="linkNavigatePage" />
  <!-- =================== ACCOUNT =================== -->
  <section class="accounts section--lg">
    <div class="accounts__container container grid">
      <SideBar></SideBar>
      <div class="tabs__content">
        <div class="tab__content active-tab">
          <h3 class="tab__header">Bonjour Antoine !</h3>
          <div class="tab__body">
            <p class="tab__description">
              Depuis votre tableau de bord, vous pouvez facilement consulter vos commandes récentes,
              gérer vos adresses de livraison et de facturation, et modifier votre mot de passe et
              les informations de votre compte.
            </p>
          </div>
        </div>
        <div class="tab__content">
          <h3 class="tab__header">Vos Commandes</h3>
          <div class="tab__body">
            <table class="placed__order-table">
              <thead>
                <tr>
                  <th>Commande</th>
                  <th>Date</th>
                  <th>Statut</th>
                  <th>Total</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>#1357</td>
                  <td>22 mars 2026</td>
                  <td>En attente</td>
                  <td>300.00 €</td>
                  <td><a href="#" class="view__order">Aperçu</a></td>
                </tr>
                <tr>
                  <td>#13258</td>
                  <td>21 février 2026</td>
                  <td>Validé</td>
                  <td>300.00 €</td>
                  <td><a href="#" class="view__order">Aperçu</a></td>
                </tr>
                <tr>
                  <td>#13258</td>
                  <td>21 février 2026</td>
                  <td>Completé</td>
                  <td>150.00 €</td>
                  <td><a href="#" class="view__order">Aperçu</a></td>
                </tr>
                </tbody>
            </table>
          </div>
        </div>
        <div class="tab__content">
          <h3 class="tab__header">Profile</h3>
          <div class="tab__body">
            <form action="" class="form grid">
              <input type="text" class="form__input" placeholder="Utilisateur"/>
              <input type="password" class="form__input" placeholder="Mot de passe actuel"/>
              <input type="password" class="form__input"  placeholder="Nouveau mot de passe"/>
              <input type="password" class="form__input"  placeholder="Confirmez mot de passe">
              <div class="form__btn">
                <button type="submit" class="btn btn-md">Enregistre</button>
              </div>
            </form>
          </div>
        </div>
        <div class="tab__content">
          <h3 class="tab__header">Adresse de livraison</h3>
          <div class="tab__body">
            <address class="adress">
              33 Villa de porte, <br>Jouy-le-moutier 95280,<br>France
            </address>
            <p class="city">Jouy-le-moutier</p>
            <a href="#" class="edit">Modifier</a>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>

</style>
