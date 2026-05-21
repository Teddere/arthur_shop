<script setup>
  import {RouterLink} from "vue-router";
  import { useToastStore } from "@/stores/toast.js";
  import {useCartStore} from "@/stores/cart.js";

  const props = defineProps({
    product : {
      type: Object,
      required: true
    }
  })
  const toast = useToastStore();
  const cart = useCartStore();

  const getImageUrl = (url)=>{
    if(!url) return '';
    if (url.includes('http') || url.includes('media')) return url;
    return new URL(`../assets/images/${url}`,import.meta.url).href;
  }
  const handleAddToCart = ()=>{
    cart.addToCart(props.product)
    toast.success(`${props.product.title} ajouté au panier !`,3000);
  }
</script>
<template>
  <article class="product__item">
    <!-- Bannière produit -->
    <div class="product__banner">
      <RouterLink :to="product.url ? product.url : '#'" class="product__images">
        <img :src="getImageUrl(product.image_default)" loading="lazy" alt="product image" class="product__img default">
        <img :src="getImageUrl(product.image_hover)" loading="lazy" alt="product image" class="product__img hover">
      </RouterLink>
      <!-- Actions rapides -->
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
      <RouterLink :to="product.url ? product.url : '#'">
        <h3 class="product__title">{{product.title}}</h3>
      </RouterLink>
      <div class="product__rating">
        <i class="fa-regular fa-star"></i>
        <i class="fa-regular fa-star"></i>
        <i class="fa-regular fa-star"></i>
        <i class="fa-regular fa-star"></i>
        <i class="fa-regular fa-star"></i>
      </div>

      <div class="product__price flex" v-if="product.element.newPrice">
        <span class="new__price">{{product.element.newPrice}} €</span>
        <span class="old__price">{{product.element.base_price}} €</span>
      </div>
      <div class="product__price flex" v-else>
        <span class="new__price">{{product.element.base_price}} €</span>
      </div>
      <button @click="handleAddToCart" aria-label="Ajouter au panier" type="button" class="action__btn cart__btn" >
        <i class="fa-solid fa-plus"></i>
      </button>
    </div>
  </article>
</template>

