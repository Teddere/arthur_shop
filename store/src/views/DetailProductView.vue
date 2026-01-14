<script setup>
  import {ref,onMounted} from 'vue';
  import axios  from "axios";
  import {useRoute} from "vue-router";
  import ProductItem from "@/components/ProductItem.vue";
  import Breadcrumb from '@/components/Breadcrumb.vue';

  const links = ref([]);
  const productList = ref([]);
  const product = ref({});
  const activeTab = ref('info');
  const reviews = ref([
    {
      author:'Marie Antoinette',
      rating: 5,
      text:'Merci pour la livraison très rapide depuis la Pologne, en seulement 3 jours.',
      date:'18 Novembre 2024 à 15h30',
      image:'coat_pub.png'
    },
    {
      author:'Marie Antoinette',
      rating: 5,
      text:'Merci pour la livraison très rapide depuis la Pologne, en seulement 3 jours.',
      date:'18 Novembre 2024 à 15h30',
      image:'banner-pub-2.png'
    },
    {
      author:'Marie Antoinette',
      rating: 5,
      text:'Merci pour la livraison très rapide depuis la Pologne, en seulement 3 jours.',
      date:'18 Novembre 2024 à 15h30',
      image:'manteau-2.jpg'
    },
  ]);
  const productInfo = [
    { title: 'Composition', content: 'Polyster 85%, Visco 10%, Elasthanne' },
    { title: 'Matière', content: 'Coton, Laine, Cuir, Polyester, Lin, etc.' },
    { title: 'Collection', content: 'Collection Hiver 2024, Collection Capsule' },
    { title: 'Stock', content: 'Géré par taille/couleur si applicable' },
    { title: 'Taille', content: 'XS, S, M, L, XL' },
    { title: 'Couleurs', content: 'Noir,Blanc,Vert' }
  ]

  product.value = {
    'ref':'FWM15VKT',
    'name':'Pull Rousseur brun',
    'defaultImg':'sweater.png',
    'imgItem': ['sweater-1.png','sweater.png','pul.png'],
    'brand': 'Adidas',
    'newPrice': 75.00,
    'oldPrice': 90.00,
    'percent': 22,
    'warranty': 1,
    'return': 15,
    'colors':['hsl(37,100%,65%)','hsl(353,100%,67%)','hsl(49,100%,60%)','hsl(304,100%,78%)','hsl(126,61%,52%)'],
    'sizes':['S','M','L','XL','XXL'],
    'stock': 10,
    'tags':['Linne','Mixte','Pull'],
    'description':"Lorem ipsum dolor sit amet, consectetur adipisicing elit.Tenetur ad nihil iste provident sapiente corporis distinctio dolores natus voluptate nulla! Cumque quas saepe provident, laborum ducimuslaudantium accusamus beatae quis."
  }

  const selectImage = ref(product.value.imgItem.find((item)=> item === product.value.defaultImg))
  const selectColor = ref(product.value.colors[0]);
  const selectSize = ref(product.value.sizes[0]);
  productList.value = [
    {
      id: 3,
      imgDefault: 'shoe-5.png',
      imgHover: 'shoe-7.png',
      badge: '-22%',
      badgeClass: 'light-pink',
      category: 'Chaussure',
      title: 'Weston Mark Time',
      newPrice: 450.00,
      oldPrice: 599.90
    },
    {
      id: 6,
      imgDefault: 'sandals.png',
      imgHover: 'sandals-1.png',
      badge: 'Nouveauté',
      badgeClass: '',
      category: 'Sandale',
      title: 'Lacost drum',
      newPrice: 50.90,
      oldPrice: 99.90
    },
    {
      id: 9,
      imgDefault: 'scarf.png',
      imgHover: 'scarf-1.png',
      badge: '-30%',
      badgeClass: 'light-pink',
      category: 'Foulards',
      title: 'Tiffany Chou',
      newPrice: 9.90,
      oldPrice: 19.90
    },
    {
      id: 12,
      imgDefault: 'pull-4.png',
      imgHover: 'pull-3.png',
      badge: '',
      badgeClass: '',
      category: 'Pull',
      title: 'Cromatic',
      newPrice: 60.00,
      oldPrice: 90.00
    },
  ]

  const getImageUrl = (url)=>{
    return new URL(`../assets/images/${url}`,import.meta.url).href
  }
  // Review
  const noteReview = ref(0);
  const hoverReview = ref(0);
  links.value = [
    { 'name': 'Accueil', 'nameUrl': 'home' },
    { 'name': 'Catalogue', 'nameUrl': 'catalog' },
    { 'name': product.value.name, 'nameUrl': 'catalog' },
  ]

  // product
  const getProduct = ()=>{


  }
  onMounted(()=>{
    getProduct()
  })
</script>
<template>
  <Breadcrumb :links="links" />
  <!-- =========== DETAILS ============= -->
  <section class="details section--lg">
    <div class="details__container container grid">
      <div class="details___group">
        <img :src="getImageUrl(selectImage)" alt="product image" class="details__img" >
        <div class="detail__small-images grid">
          <img
            v-for="(image,index) in product.imgItem"
            :key="index"
            :src="getImageUrl(image)"
            @click="selectImage = image"
            :class="{'active': selectImage === image}"
            alt="description product image"
            class="details__small-img"
          >
        </div>
      </div>
      <div class="details___group">
        <h3 class="details__title">{{product.name}}</h3>
        <p class="details__brand">Marque: <span>{{product.brand}}</span></p>
        <div class="details__price flex">
          <span class="new__price">{{product.newPrice}} €</span>
          <span class="old__price">{{product.oldPrice}} €</span>
          <span class="save__price">{{product.percent}}% de réduction</span>
        </div>
        <p class="short__description">{{product.description}}</p>
        <ul class="product__list">
          <li class="list__item flex">
            <i class="fa-solid fa-crown"></i>
            <template v-if="product.warranty === 1"> 1 an de garantie de fabrication</template>
            <template v-else>{{product.warranty}} ans de garantie de fabrication</template>
          </li>
          <li class="list__item flex">
            <i class="fa-solid fa-refresh"></i>
            <template v-if="product.return < 15 ">Pas de retour possible</template>
            <template v-else>{{product.return}} jours pour un retour.</template>
          </li>
          <li class="list__item flex">
            <i class="fa-solid fa-credit-card"></i>
            Paiement en plusieurs fois disponible
          </li>
        </ul>
        <div class="details__color flex">
          <span class="details__color-title">Couleur</span>
          <ul class="color__list" v-if="product.colors">
            <li v-for="(color,index) in product.colors" :key="index" >
              <button type="button"
                :style="{backgroundColor:color}"
                :class="{'active': selectColor === color}"
                @click="selectColor = color"
                class="color__link"
              ></button>
            </li>
          </ul>
          <span v-else class="option">Pas d'option de couleur</span>

        </div>
        <div class="details__size flex">
          <span class="details__size-title">Taille</span>
          <ul class="size__list">
            <li v-for="(size,index) in product.sizes" :key="index">
              <button type="button"
                      @click="selectSize = size"
                      :class="{'size-active': selectSize === size}"
                      class="size__link"
              >
                {{size}}
              </button>
              </li>
          </ul>
        </div>
        <form >
          <div class="details__action">
            <input type="number" value="3" name="article_number" id="article_number" class="quantity">
            <button type="submit" class="btn btn-sm">Mettre au panier</button>
            <button type="button" class="details__action-btn">
              <i class="fa-solid fa-heart"></i>
            </button>
          </div>
        </form>
        <ul class="details__meta">
          <li class="meta__list flex">Ref:<span> {{product.ref}}</span></li>
          <li class="meta__list flex">
            Etiquette:
            <template v-for="(tag,index) in product.tags" :key="index">
              <span v-if="index < product.tags.length - 1">{{tag}},</span>
              <span v-else>{{tag}}</span>
            </template>
          </li>
          <li class="meta__list flex">
            Disponibilité:<span>{{product.stock}} article(s) en stock</span>
          </li>
        </ul>
      </div>
    </div>
  </section>
  <!-- ========= DETAILS TAB =========================-->
  <section class="details_tab container">
    <div class="details__tabs">
      <span
        @click="activeTab='info'"
        :class="{'active-tab':activeTab === 'info'}"
        class="detail__tab"
      >
        Description détaillée
      </span>
      <span
        @click="activeTab = 'reviews'"
        :class="{ 'active-tab': activeTab === 'reviews' }"
        class="detail__tab"
      >
       Avis({{reviews.length}})
      </span>
    </div>
    <div class="details__tabs-content">
      <transition name="fade" mode="out-in">
        <div v-if="activeTab === 'info'" class="details__tab-content">
        <table class="info__table">
          <tr v-for="(item,index) in productInfo" :key="index">
            <th>{{item.title}}</th>
            <td>{{item.content}}</td>
          </tr>
        </table>
      </div>
      </transition>
      <transition name="fade" mode="out-in">
        <div v-if="activeTab === 'reviews'" class="details__tab-content">
          <div class="reviews__container grid">
            <transition-group name="review" tag="div">
              <article v-for="(review, index) in reviews" :key="`review-${index}`" class="review__single">
                <div>
                  <img :src="getImageUrl(review.image)" :alt="review.author" class="review__img">
                  <h4 class="review__title">{{ review.author }}</h4>
                </div>
                <div class="review__data">
                  <div class="review__rating">
                    <i v-for="n in review.rating" :key="n" class="fa-regular fa-star"></i>
                  </div>
                  <p class="review__description">{{review.text}}</p>
                  <span class="review__data">{{review.date}}</span>
                </div>
              </article>
            </transition-group>
          </div>
          <div class="review__form">
            <h4 class="review__form-title">Donner un avis</h4>
            <div class="rate__product">
              <button type="button"
                      v-for="n in 5"
                      :key="n"
                      @click="noteReview = n"
                      @mouseenter="hoverReview = n"
                      @mouseleave="hoverReview = 0"
                      :class="{'active':(hoverReview || noteReview) >= n}"
                      class="star_review"
              >
                <i class="fa-solid fa-star"></i>
              </button>
            </div>
            <form  class="form grid">
              <textarea  class="form__input textarea" placeholder="Entrez votre commentaire"></textarea>
              <div class="form__group grid">
                <input type="text" placeholder="Entrez votre nom" class="form__input">
                <input type="email" placeholder="Entrez votre email" class="form__input">
              </div>
              <div class="form__btn">
                <button type="submit" class="btn">Soumettre</button>
              </div>
            </form>
          </div>
        </div>
      </transition>
    </div>
  </section>
  <!-- ========= PRODUCTS ==================-->
   <section class="products container section--lg">
    <h3 class="section__title">Articles <span>Similiaires</span></h3>
    <div class="products__container grid">
      <productItem
        v-for="prod in productList"
        :key="prod.id"
        :product="prod"
      ></productItem>
    </div>
   </section>
</template>
<style scoped>
  .fade-enter-active, .fade-leave-active {
    transition: opacity 0.3s ease;
  }
  .fade-enter-from, .fade-leave-to {
    opacity: 0;
  }
  .review-enter-active, .review-leave-active {
    transition: all 0.3s ease;
  }
  .review-enter-from {
    opacity: 0;
    transform: translateY(-10px);
  }
  .review-leave-to {
    opacity: 0;
    transform: translateY(10px);
  }
</style>
