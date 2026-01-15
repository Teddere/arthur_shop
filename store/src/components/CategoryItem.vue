<script setup>
import { RouterLink } from 'vue-router';
defineProps({
  name_category: {
    type: String,
    required: true,
  },
  image: {
    type: String,
    required: true,
  },
  category_url: {
    type: String,
    required: true,
  },
})
const getImageUrl = (imageName) => {
  return imageName;
  //return new URL(`../assets/images/${imageName}`, import.meta.url).href
}
</script>
<template>
  <RouterLink :to="category_url" class="category_item">
    <img :src="getImageUrl(image)" :alt="name_category + ' image'" class="category__img" />
    <h3 class="category__title">{{ name_category }}</h3>
  </RouterLink>
</template>

