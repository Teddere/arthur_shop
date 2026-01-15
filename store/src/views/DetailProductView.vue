<script setup>
  import axios from "axios";
  import {ref,onMounted,watch} from 'vue';
  import {useRoute} from "vue-router";
  import ProductItem from "@/components/ProductItem.vue";
  import Breadcrumb from '@/components/Breadcrumb.vue';

  const route = useRoute()
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
  const selectImage = ref(null);
  const selectColor = ref(null);
  const selectSize = ref(null);
  const productInfo = [
    { title: 'Composition', content: 'Polyster 85%, Visco 10%, Elasthanne' },
    { title: 'Matière', content: 'Coton, Laine, Cuir, Polyester, Lin, etc.' },
    { title: 'Collection', content: 'Collection Hiver 2024, Collection Capsule' },
    { title: 'Stock', content: 'Géré par taille/couleur si applicable' },
    { title: 'Taille', content: 'XS, S, M, L, XL' },
    { title: 'Couleurs', content: 'Noir,Blanc,Vert' }
  ];

const getImageUrl = (url)=>{
       if (!url) {
         return ''
       }else if(url.includes('media')) {
         return url
       }
       else {
         return new URL(`../assets/images/${url}`, import.meta.url).href
         }
       }
  // Review
  const noteReview = ref(0);
  const hoverReview = ref(0);
  links.value = [
    { 'name': 'Accueil', 'nameUrl': 'home' },
    { 'name': 'Catalogue', 'nameUrl': 'catalog' }
  ]

  // product
  const getProduct = ()=>{
    const category_slug = route.params.category_slug;
    const product_slug = route.params.product_slug;
    axios
      .get(`/api/v1/products/${category_slug}/${product_slug}`)
      .then(response=>{
        selectImage.value = response.data.get_image_default;
        selectColor.value = response.data.color[0].value ? response.data.color[0]:null;
        selectSize.value = response.data.size ? response.data.size[0].code:null;
        links.value.push({'name':response.data.title,'nameUrl':null})
        product.value = response.data;
      })
      .catch(err=>{
        console.log(err)
      })
  }
  // list products
  const getProductAll=()=>{
    const category_slug = route.params.category_slug;
    axios
    .get(`/api/v1/categories/detail/${category_slug}`)
    .then(response=>{
      productList.value = response.data
    })
    .catch(err=>{
      console.log(err)
    })
  }
  onMounted(()=>{
    getProduct()
    getProductAll()
  })
  watch(
    ()=> route.params.product_slug,
    ()=>{
      product.value={};
      selectImage.value = null;
      selectColor.value = null;
      selectSize.value = null;
      activeTab.value = 'info';
      links.value = [
        { name: 'Accueil', nameUrl: 'home' },
        { name: 'Catalogue', nameUrl: 'catalog' }
      ];
      getProduct();
      getProductAll();
    }
  );
</script>
<template>
  <Breadcrumb :links="links" />
  <!-- =========== DETAILS ============= -->
  <section class="details section--lg">
    <div class="details__container container grid">
      <div class="details___group">
        <img :src="getImageUrl(selectImage)" alt="product image" class="details__img" >
        <div class="detail__small-images grid">
          <img :src="product.get_image_default"
            @click="selectImage = product.get_image_default"
            :class="{'active': selectImage === product.get_image_default}"
            alt="description product image"
            class="details__small-img"
          >
          <img :src="product.get_image_hover"
            @click="selectImage = product.get_image_hover"
            :class="{'active': selectImage === product.get_image_hover}"
            alt="description product image"
            class="details__small-img"
          >
        </div>
      </div>
      <div class="details___group">
        <h3 class="details__title">{{product.title}}</h3>
        <p class="details__brand">Marque: <span>{{product.brand}}</span></p>
        <div class="details__price flex" v-if="product.newPrice">
          <span class="new__price">{{product.newPrice}} €</span>
          <span class="old__price">{{product.oldPrice}} €</span>
          <span class="save__price">{{product.percent}}% de réduction</span>
        </div>
        <div class="details__price flex" v-else>
          <span class="new__price">{{product.oldPrice}} €</span>
        </div>
        <p class="short__description">{{product.description}}</p>
        <ul class="product__list">
          <li class="list__item flex">
            <i class="fa-solid fa-crown"></i>
            <template v-if="product.warranty === 1"> 1 an de garantie de fabrication</template>
            <template v-else-if="product.warranty > 1">{{product.warranty}} ans de garantie de fabrication</template>
            <template v-else>Article non garanti</template>
          </li>
          <li class="list__item flex">
            <i class="fa-solid fa-credit-card"></i>
            Paiement en plusieurs fois disponible
          </li>
        </ul>
        <div class="details__color flex">
          <span class="details__color-title">Couleur</span>
          <ul class="color__list" v-if="product.color">
            <li v-for="(color,index) in product.color" :key="index" >
              <button type="button"
                :style="{backgroundColor:color.value}"
                :class="{'active': selectColor === color.value}"
                @click="selectColor = color.value"
                class="color__link"
              ></button>
            </li>
          </ul>
          <span v-else class="option">Pas d'option de couleur</span>

        </div>
        <div class="details__size flex">
          <span class="details__size-title">Taille</span>
          <ul class="size__list" v-if="product.size">
            <li v-for="(size,index) in product.size" :key="index">
              <button type="button"
                      @click="selectSize = size.code"
                      :class="{'size-active': selectSize === size.code}"
                      class="size__link"
              >
                {{size.code}}
              </button>
              </li>
          </ul>
          <span v-else>Taille unique</span>
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
            <template v-for="(tag,index) in product.tag" :key="index">
              <span v-if="index < product.tag.length - 1">{{tag.name}},</span>
              <span v-else>{{tag.name}}</span>
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
        v-for="(prod,index) in productList"
        :key="index"
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
