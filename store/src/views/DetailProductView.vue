<script setup>
  import axios from "axios";
  import {ref,onMounted,watch} from 'vue';
  import {useRoute} from "vue-router";
  import ProductItem from "@/components/ProductItem.vue";
  import Breadcrumb from '@/components/Breadcrumb.vue';
  import {useCartStore} from'@/stores/cart.js';
  import {useToastStore} from '@/stores/toast.js'


  const toast = useToastStore();
  const cart = useCartStore();
  const route = useRoute()
  // navigation d'entête
  const links = ref([]);
  // liste d'articles associés
  const productList = ref([]);
  // article courante
  const productObject = ref({});
  // navigation de menu
  const activeTab = ref('info');
  // liste d'avis
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
  // list d'images courantes
  const selectImage = ref(null);
  // liste de couleurs courantes
  const selectColor = ref(null);
  // liste de tailles courantes
  const selectSize = ref(null);
  // informations articles
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
        // navigation Breadcrumb
        links.value.push({'name':response.data.category.name,'nameUrl':'catalog_name','params':{'category_slug':response.data.category.name.toLocaleLowerCase()}});
        links.value.push({'name':response.data.title,'nameUrl':null})
        // product value
        productObject.value = response.data;
        // page title
        document.title = `${productObject.value.title} | Arthur`;
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
  // Fonction pour scroller page
  const scrollToProduct = ()=>{
    const prodSection = document.getElementById('detailProduction');
    if (prodSection) {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  }
  onMounted(()=>{
    getProduct()
    getProductAll()
    document.title = 'Accueil | Arthur ';
  })
  watch(
    ()=> route.params.product_slug,
    ()=>{
      productObject.value={};
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
      scrollToProduct();
    }
  );
  // add product to cart
  const productNumber = ref(1);

  const addProductCart = ()=>{
    const quantity = parseInt(productNumber.value);
    if(isNaN(quantity) || quantity < 1) {
      toast.warning('Veuillez la quantité souhaiter !')
    }
    else {
      cart.addToCart(productObject.value,quantity);
    }
  }
</script>
<template>
  <Breadcrumb :links="links" />
  <!-- =========== DETAILS ============= -->
  <section id="detailProduction" class="details section--lg">
    <div class="details__container container grid">
      <div class="details___group">
        <img :src="getImageUrl(selectImage)" alt="product image" class="details__img" >
        <div class="detail__small-images grid">
          <img :src="productObject.get_image_default"
            @click="selectImage = productObject.get_image_default"
            :class="{'active': selectImage === productObject.get_image_default}"
            alt="description product image"
            class="details__small-img"
          >
          <img :src="productObject.get_image_hover"
            @click="selectImage = productObject.get_image_hover"
            :class="{'active': selectImage === productObject.get_image_hover}"
            alt="description product image"
            class="details__small-img"
          >
        </div>
      </div>
      <div class="details___group">
        <h3 class="details__title">{{productObject.title}}</h3>
        <p class="details__brand">Marque: <span>{{productObject.brand}}</span></p>
        <div class="details__price flex" v-if="productObject.newPrice">
          <span class="new__price">{{productObject.newPrice}} €</span>
          <span class="old__price">{{productObject.oldPrice}} €</span>
          <span class="save__price">{{productObject.percent}}% de réduction</span>
        </div>
        <div class="details__price flex" v-else>
          <span class="new__price">{{productObject.oldPrice}} €</span>
        </div>
        <p class="short__description">{{productObject.description}}</p>
        <ul class="product__list">
          <li class="list__item flex">
            <i class="fa-solid fa-crown"></i>
            <template v-if="productObject.warranty === 1"> 1 an de garantie de fabrication</template>
            <template v-else-if="productObject.warranty > 1">{{productObject.warranty}} ans de garantie de fabrication</template>
            <template v-else>Article non garanti</template>
          </li>
          <li class="list__item flex">
            <i class="fa-solid fa-credit-card"></i>
            Paiement en plusieurs fois disponible
          </li>
        </ul>
        <div class="details__color flex">
          <span class="details__color-title">Couleur</span>
          <ul class="color__list" v-if="productObject.color">
            <li v-for="(color,index) in productObject.color" :key="index" >
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
          <ul class="size__list" v-if="productObject.size">
            <li v-for="(size,index) in productObject.size" :key="index">
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
        <form @submit.prevent="addProductCart">
          <div class="details__action">
            <input type="number" v-model="productNumber" min="1" name="article_number" id="article_number" class="quantity">
            <button type="submit" class="btn btn-sm">Mettre au panier</button>
            <button type="button" class="details__action-btn">
              <i class="fa-solid fa-right-left"></i>
            </button>
          </div>
        </form>
        <ul class="details__meta">
          <li class="meta__list flex">Ref:<span> {{productObject.ref}}</span></li>
          <li class="meta__list flex">
            Etiquette:
            <template v-for="(tag,index) in productObject.tag" :key="index">
              <span v-if="index < productObject.tag.length - 1">{{tag.name}},</span>
              <span v-else>{{tag.name}}</span>
            </template>
          </li>
          <li class="meta__list flex">
            Disponibilité:<span>{{productObject.stock}} article(s) en stock</span>
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
