<script setup>
defineProps({
  name_category: {
    type: String,
    required: true,
  },
  image: {
    type: String,
    required: true,
  },
  category: {
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
  <a href="#" class="category_item">
    <img :src="getImageUrl(image)" :alt="category + ' image'" class="category__img" />
    <h3 class="category__title">{{ name_category }}</h3>
  </a>
</template>

