<script>
  export default {
    props:{
      product:{
        type:Object,
        required:true
      }
    },
    methods:{
      getImageUrl(imageName){
        return new URL(`../assets/images/${imageName}`,import.meta.url).href
      },
    }
  }
</script>

<template>
  <article class="showcase__item">
    <a href="#" class="showcase__img-box">
      <img :src="getImageUrl(product.image)" alt="showcase image" class="showcase__img">
    </a>
    <div class="showcase__content">
      <a href="#">
        <h4 class="showcase__title">{{product.title}}</h4>
      </a>
      <div class="showcase__price flex">
        <span class="new__price">{{product.newPrice}} €</span>
        <span class="old__price">{{product.oldPrice}} €</span>
      </div>
    </div>
  </article>
</template>


