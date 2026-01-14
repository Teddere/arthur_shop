<script>
import axios from 'axios'
// Import Swiper Vue.js components
import { Swiper, SwiperSlide } from 'swiper/vue'
// Import Swiper styles
import 'swiper/css'
import 'swiper/css/navigation'
// import required modules
import { Navigation } from 'swiper/modules'
import CategoryItem from '@/components/CategoryItem.vue'
import ProductItem from '@/components/ProductItem.vue'
import ShowaseItem from '@/components/ShowaseItem.vue'

export default {
  data: () => {
    return {
      categoryItem: [
        { id: 1, name: 'Pull', category: 'sweater', image: 'pull-2.png' },
        { id: 2, name: 'Sac', category: 'bag', image: 'bag.png' },
        { id: 3, name: 'Sneakers', category: 'snearkers', image: 'snearkes.png' },
        { id: 4, name: 'Foulards', category: 'scarf', image: 'scarf-1.png' },
        { id: 5, name: 'Sandales', category: 'sandale', image: 'sandals.png' },
        { id: 6, name: 'Oreillers', category: 'cushion', image: 'cushion-1.png' },
        { id: 7, name: 'Manteaux', category: 'coat', image: 'coat.png' },
        { id: 8, name: 'chapeaux', category: 'hat', image: 'chapeau.png' },
      ],
      activeTab : 'new',
      tabs: [
        {
          id:'new',
          label:'Nouveauté',
          products:[]
        },
        {
          id:'sale',
          label:'Promotion',
          products:[]
        },
        {
          id:'moment',
          label:'Article du moment',
          products: [
            /*
            {
              id:1,
              imgDefault:'snearkes-1.png',
              imgHover:'snearkes.png',
              badge:'Nouveauté',
              badgeClass:'light-blue',
              category:'Sac',
              title:'Converse all time',
              newPrice:'39.00',
              oldPrice:'59.90'
            },
            {
              id:2,
              imgDefault:'product-1-1.jpg',
              imgHover:'product-1-2.jpg',
              badge:'promo',
              badgeClass:'',
              category:'Foulards',
              title:'Hawaii Thuph',
              newPrice:'25.00',
              oldPrice:'35.00'
            },
            {
              id:3,
              imgDefault:'sandals.png',
              imgHover:'sandals-1.png',
              badge:'Nouveauté',
              badgeClass:'',
              category:'Sandale',
              title:'Lacost drum',
              newPrice:'50.90',
              oldPrice:'99.90'
            },
            {
              id:4,
              imgDefault:'shoe-5.png',
              imgHover:'shoe-7.png',
              badge:'-22%',
              badgeClass:'light-pink',
              category:'Chaussure',
              title:'Weston Mark Time',
              newPrice:'450.00',
              oldPrice:'599.90'
            },
            {
              id:5,
              imgDefault:'bag.png',
              imgHover:'bag-3.png',
              badge:'collection',
              badgeClass:'light-orange',
              category:'Sac',
              title:'Hermes Lagardène',
              newPrice:'5000.00',
              oldPrice:'8699.99'
            },
            {
              id:6,
              imgDefault:'pull-1.png',
              imgHover:'pull-2.png',
              badge:'collection',
              badgeClass:'light-blue',
              category:'Pull',
              title:'Pull Pouma white',
              newPrice:'89.90',
              oldPrice:'99.99'
            },
            {
              id:7,
              imgDefault:'polo.png',
              imgHover:'polo-2.png',
              badge:'',
              badgeClass:'',
              category:'Pull',
              title:'Tiffany Grey',
              newPrice:'40.00',
              oldPrice:'69.90'
            },
            {
              id:8,
              imgDefault:'scarf.png',
              imgHover:'scarf-1.png',
              badge:'-30%',
              badgeClass:'light-pink',
              category:'Foulards',
              title:'Tiffany Chou',
              newPrice:'9.90',
              oldPrice:'19.90'
            },*/
          ]
        }
      ],
      arrivals : [
        {
          id:1,
          imgDefault:'sweater-1.png',
          imgHover:'sweater.png',
          badge:'',
          badgeClass:'',
          category:'Pull',
          title:'Pull Rousseur',
          newPrice:'75.00',
          oldPrice:'90.00'
        },
        {
          id:2,
          imgDefault:'sneakers-3.png',
          imgHover:'sneakers-4.png',
          badge:'Collection',
          badgeClass:'light-orange',
          category:'Sneakers',
          title:'All Star',
          newPrice:'70.00',
          oldPrice:'90.00'
        },
        {
          id:3,
          imgDefault:'t-shirt.png',
          imgHover:'t-shirt--1.png',
          badge:'Promo',
          badgeClass:'light-blue',
          category:'T-shirt',
          title:'Nike Workers',
          newPrice:'70.00',
          oldPrice:'90.00'
        },
        {
          id:4,
          imgDefault:'shirt-3.png',
          imgHover:'shirt-2.png',
          badge:'',
          badgeClass:'',
          category:'Chemise',
          title:'Carrinton',
          newPrice:'80.00',
          oldPrice:'120.00'
        },
        {
          id:5,
          imgDefault:'t-shirt-6.png',
          imgHover:'t-shirt-6-1.png',
          badge:'50%',
          badgeClass:'',
          category:'T-shirt',
          title:'Lutin',
          newPrice:'40.00',
          oldPrice:'80.00'
        },
        {
          id:6,
          imgDefault:'pul.png',
          imgHover:'sweater-3.png',
          badge:'Collection',
          badgeClass:'light-green',
          category:'Pull',
          title:'Flamer',
          newPrice:'70.00',
          oldPrice:'90.00'
        }
      ],
      showcases : [
        {
          id:1,
          label:'Nouveautés',
          products:[
          {image:'shoe-1.png',title:'Timberland Rageur',newPrice:'145.00',oldPrice:'160.00'},
          {image:'bag-4.png',title:'Hermes Morgane',newPrice:'1300.00',oldPrice:'1450.00'},
          {image:'polo_black.png',title:'Master bown',newPrice:'1300.00',oldPrice:'1450.00'},
        ]
        },
        {
          id:2,
          label:'Offres & Sorties',
          products:[
          {id:1,image:'bag-4.png',title:'Sac Tiffany',newPrice:'100.00',oldPrice:'120.00'},
          {id:2,image:'shoe-8.png',title:'Weston Creval',newPrice:'350.00',oldPrice:'450.00'},
          {id:3,image:'snearkes-3.png',title:'NIKE Ramport',newPrice:'90.00',oldPrice:'120.00'},
        ]
      },
        {
          id:3,
          label:'Meilleurs Ventes',
          products:[
            {id:1,image:'polo-1.png',title:'Lacost Lavoine',newPrice:'70.00',oldPrice:'90.00'},
            {id:2,image:'sandale-2.png',title:'Clara',newPrice:'20.00',oldPrice:'25.00'},
            {id:3,image:'product-2-1.jpg',title:'Hawaii bleu',newPrice:'45.00',oldPrice:'70.00'},
          ]
      },
        {
          id:4,
          label:'Dernières Tendances',
          products:[
            {id:1,image:'t-shirt-4.png',title:'Pink Roger',newPrice:'60.00',oldPrice:'100.00'},
            {id:2,image:'pull-3.png',title:'Rouleur pull',newPrice:'47.00',oldPrice:'60.00'},
            {id:3,image:'scarf-2.png',title:'Lontin',newPrice:'50.00',oldPrice:'100.00'},
          ]
      },
      ],
      date: Date.now(),
      deals:[
        {
          id:1,
          brand:"L'offre du jour",
          category:"Quantité limitée",
          title:"Collection d'hiver, nouveau arrivage",
          newPrice:99.90,
          oldPrice:160.00,
          countdownText:"Dépêchez-vous, l'offre se termine bientôt :",
          endDate:"2026-01-12T23:59:59Z"
        },
        {
          id:2,
          brand:"Vêtements pour femme",
          category:"Chemise & Sac",
          title:"Nouvelle collection",
          newPrice:99.90,
          oldPrice:160.00,
          countdownText:"Dépêchez-vous, l'offre se termine bientôt :",
          endDate:"2026-01-10T23:59:59Z"
        },
      ],
      timer:null
    }
  },
  computed: {
    getCurrentTabProducts(){
      const currentTab = this.tabs.find(tab => tab.id === this.activeTab);
      return currentTab ? currentTab.products:[];
    },
    dealWithCountdown(){
      return this.deals.map(deal =>({
        ...deal,
        countdown:this.getTimeRemaining(deal.endDate)
      }))
    }
  },
  mounted() {

    this.getProductAll()

    this.date = Date.now()
    this.timer = setInterval(()=>{
      this.date = Date.now()
    },1000);
  },
  beforeMount() {
    if(this.timer){
      clearInterval(this.timer)
    }
  },
  methods:{

    getProductAll(){
      axios
        .get('/api/v1/last-products/')
        .then(response => {
          console.log(response.data)
            this.tabs.forEach((item)=>{
              item.products = response.data;
            });
        })
        .catch(err => {
          console.log(err)
        });
    },
    getTimeRemaining(endDate){
      const total = new Date(endDate).getTime() - this.date;
      if (total <=0 ){
        return {days:0,hours:0,minutes:0,seconds:0};
      }
      const seconds = Math.floor((total/1000)%60);
      const minutes = Math.floor((total/1000/60)%60);
      const hours = Math.floor((total/(1000*60*60))%24);
      const days = Math.floor((total/(1000*60*60*24)));
      return {days,hours,minutes,seconds}
    }
  },
  components: {
    Swiper,
    SwiperSlide,
    CategoryItem,
    ProductItem,
    ShowaseItem
  },
  setup() {
    return {
      modules: [Navigation],
    }
  },
}
</script>

<template>
    <!-- ============ HOME section--lg================== -->
    <section class="home">
      <div class="home__container container grid">
        <div class="home__content">
          <span class="home__subtitle">Hot promotions</span>
          <h1 class="home_title">Fashion trending <span>Great Collections</span></h1>
          <p class="home__description">Save more with coupons & up to 20%</p>
          <a href="#" class="btn">Shop now</a>
        </div>
        <img src="@/assets/images/banner.png" alt="banner image" class="home__img" />
      </div>
    </section>
    <!-- ============ CATEGORIES ======================= -->
    <section class="categories container section">
      <h3 class="section__title">Catégories<span>&nbsp;Tendances</span></h3>
      <div class="swiper-wrapper-custom">
        <div class="button-prev">
          <i class="fa-solid fa-chevron-left"></i>
        </div>
        <div class="button-next">
          <i class="fa-solid fa-chevron-right"></i>
        </div>
      </div>
      <Swiper
        :slidesPerView="1"
        :loop="true"
        :spaceBetween="30"
        :modules="modules"
        class="mySwiper"
        :navigation="{
          nextEl: '.button-next',
          prevEl: '.button-prev',
        }"
        :breakpoints="{
          350: {
            slidesPerView: 2,
            spaceBetween: 24,
          },
          768: {
            slidesPerView: 3,
            spaceBetween: 24,
          },
          992: {
            slidesPerView: 4,
            spaceBetween: 24,
          },
          1200: {
            slidesPerView: 5,
            spaceBetween: 24,
          },
          1400: {
            slidesPerView: 6,
            spaceBetween: 24,
          },
        }"
      >
        <SwiperSlide v-for="category in categoryItem" :key="category.id">
          <CategoryItem
            :name_category="category.name"
            :image="category.image"
            :category="category.category"
          ></CategoryItem>
        </SwiperSlide>
      </Swiper>
    </section>
    <!-- =========== PRODUCTS ========================= -->
    <section class="products section container">
      <div class="tab__btns">
        <span @click="activeTab=tab.id" v-for="tab in tabs" :key="tab.id" class="tab__btn" :class="tab.id === activeTab ? 'active-tab':''">
          {{tab.label}}
        </span>
      </div>
      <div class="tab__items">
        <transition name="fade" mode="out-in">
          <div :key="activeTab" class="tab__item active-tab">
            <transition-group name="scale" tag="div" class="products__container grid">
              <ProductItem
                v-for="(product,index) in getCurrentTabProducts"
                :key="index"
                :style="{'--index':index}"
                :product="product"
              ></ProductItem>
            </transition-group>
          </div>
        </transition>
      </div>
    </section>
    <!-- ========== DEALS ============================ -->
    <section class="deals section">
      <div class="deals__container container grid">
        <div class="deals__item" v-for="deal in dealWithCountdown" :key="deal.id">
          <div class="deals__group">
            <h3 class="deals__brand">{{deal.brand}}</h3>
            <span class="deals__category">{{deal.category}}</span>
          </div>
          <h4 class="deals__title">{{deal.title}}</h4>
          <div class="deals__price flex">
            <span class="new__price">{{deal.newPrice}} €</span>
            <span class="old__price">{{deal.oldPrice}} €</span>
          </div>
          <div class="deals__group">
            <p class="deals__countdown-text">{{deal.countdownText}}</p>
            <div class="countdown">
              <div class="countdown__amount">
                <p class="countdown__period">{{deal.countdown.days.toString().padStart(2, '0')}}</p>
                <span class="unit">Jours</span>
              </div>
              <div class="countdown__amount">
                <p class="countdown__period">{{deal.countdown.hours.toString().padStart(2, '0')}}</p>
                <span class="unit">Heures</span>
              </div>
              <div class="countdown__amount">
                <p class="countdown__period">{{deal.countdown.minutes.toString().padStart(2, '0')}}</p>
                <span class="unit">Minutes</span>
              </div>
              <div class="countdown__amount">
                <p class="countdown__period">{{deal.countdown.seconds.toString().padStart(2, '0')}}</p>
                <span class="unit">Sec</span>
              </div>
            </div>
          </div>
          <div class="deals__btn">
            <a href="#" class="btn btn-md">Achetez maintenant</a>
          </div>
        </div>
      </div>
    </section>
    <!-- ========== New ARRIVALS ==================== -->
    <section class="new__arrivals container section">
      <h3 class="section__title">Nouvel<span>&nbsp;Arrivage</span></h3>
      <div class="swiper-wrapper-custom">
        <div class="button-prev-view">
          <i class="fa-solid fa-chevron-left"></i>
        </div>
        <div class="button-next-view">
          <i class="fa-solid fa-chevron-right"></i>
        </div>
      </div>
      <Swiper
        :slidesPerView="1"
        :loop="true"
        :spaceBetween="30"
        :modules="modules"
        :navigation="{
          nextEl: '.button-next-view',
          prevEl: '.button-prev-view',
        }"
        :breakpoints="{
          350: {
            slidesPerView: 1,
            spaceBetween: 24
          },
          576: {
            slidesPerView: 2,
            spaceBetween: 20,
          },
          768: {
            slidesPerView: 3,
            spaceBetween: 20,
          },
          992: {
            slidesPerView: 3,
            spaceBetween: 20
          },
          1400: {
            slidesPerView: 5,
            spaceBetween:24
          }

        }"
      >
      <SwiperSlide v-for="product in arrivals" v-bind:key="product.id">
        <ProductItem :product="product"></ProductItem>
      </SwiperSlide>
      </Swiper>
    </section>
    <!-- ========== SHOWCASE ====================== -->
    <section class="showcase section">
      <div class="showcase__container container grid">
        <div class="showcase__wrapper" v-for="showcase in showcases" :key="showcase.id">
          <h3 class="section__title">{{showcase.label}}</h3>
          <ShowaseItem v-for="prod in showcase.products" :key="prod.id" :product="prod"></ShowaseItem>
        </div>
      </div>
    </section>
</template>
<style>
/* Styles pour la section des produits */
.products.section.container {
  position: relative;
}
.fade-enter-active,
.fade-leave-active {
  position: absolute;
  width: 100%;
  transition: all 0.5s var(--transition);
}
.fade-enter-from {
  opacity: 0;
  transform: translateX(50px);
}
.fade-leave-to {
  opacity: 0;
  transform: translateX(-50px);
}
.fade-enter-to,
.fade-leave-from {
  opacity: 1;
  transform: translateX(0);
}

</style>

