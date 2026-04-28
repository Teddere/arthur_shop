<script setup>
  defineProps({
    activeTab : {
      type: Number,
      default: 0,
    }
  })
  defineEmits(['tab_change'])
</script>


<template>
  <ul class="account__tabs">
    <li @click="$emit('tab_change',0)" class="account__tab" :class="{'active-tab': activeTab===0}">
      <i class="fa-solid fa-layer-group"></i>
      Dashboard
    </li>
    <li @click="$emit('tab_change',1)" class="account__tab" :class="{'active-tab': activeTab===1}">
      <i class="fa-solid fa-shopping-bag"></i>
      Commande
    </li>
    <li @click="$emit('tab_change',2)" class="account__tab" :class="{'active-tab': activeTab===2}">
      <i class="fa-solid fa-user"></i>
      Profile
    </li>
    <li @click="$emit('tab_change',3)" class="account__tab" :class="{'active-tab': activeTab===3}">
      <i class="fa-solid fa-location-arrow"></i>
      Adresse
    </li>
    <li class="account__tab" @click="$emit('tab_change',4)">
      <i class="fa-solid fa-arrow-right-from-bracket"></i>
      Déconnexion
    </li>
  </ul>
</template>

