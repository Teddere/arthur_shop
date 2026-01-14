<script>
  import {RouterLink} from "vue-router";

  export  default {
    name:'ProductItem',
    props:{
      product:{
        type:Object,
        required:true
      }
    },
    components: {
      RouterLink
    }
  }
</script>
<template>
  <article class="product__item">
    <div class="product__banner">
      <a href="#" class="product__images">
        <img :src="product.get_image_default" alt="product image" class="product__img default">
        <img :src="product.get_image_hover" alt="product image" class="product__img hover">
      </a>
      <div class="product__actions">
        <a href="#" class="action__btn" aria-label="Aperçu">
          <i class='fa-solid fa-expand'></i>
        </a>
        <a href="#" class="action__btn" aria-label="Aimez-vous ?">
          <i class='fa-solid fa-heart'></i>
        </a>
        <a href="#" class="action__btn" aria-label="Comparer">
          <i class='fa-solid fa-shuffle'></i>
        </a>
      </div>
      <div v-if="product.badge" class="product__badge" :class="product.badge.className">{{product.badge.name}}</div>
    </div>
    <div class="product_content">
      <span class="product__category">{{product.category.name}}</span>
      <RouterLink :to="product.get_absolute_url">
        <h3 class="product__title">{{product.title}}</h3>
      </RouterLink>
      <div class="product__rating">
        <i class="fa-regular fa-star"></i>
        <i class="fa-regular fa-star"></i>
        <i class="fa-regular fa-star"></i>
        <i class="fa-regular fa-star"></i>
        <i class="fa-regular fa-star"></i>
      </div>
      <div class="product__price flex">
        <span class="new__price">{{product.newPrice}} €</span>
        <span class="old__price">{{product.oldPrice}} €</span>
      </div>
      <a href="#"  class="action__btn cart__btn" aria-label="Ajouter au panier">
          <i class="fa-solid fa-plus"></i>
      </a>
    </div>
  </article>
</template>



