<script setup>
  import {ref,onMounted,onUnmounted} from 'vue'
  import {RouterLink} from 'vue-router'
  import {useCartStore} from '@/stores/store.js';


  const showMenu = ref(false)
  const openMenu = ()=>{
    showMenu.value = true;
  }
  const closeMenu = ()=>{
    showMenu.value = false;
  }

  const cart = useCartStore()
  const isScrolled = ref(false);
  const handleScroll = ()=>{
    isScrolled.value = window.scrollY >= 100;
  }
  onMounted(()=>{
    window.addEventListener('scroll',handleScroll);
  })
  onUnmounted(()=>{
    window.removeEventListener('scroll',handleScroll);
  })
</script>

<template>
  <section class="header-section" :class="{'headerFixed': isScrolled}">
    <div class="header__top">
      <div class="header__container container">
        <div class="header__contact">
          <span>(+33) 03-21-30-10-40</span>
          <!--<span>15 rue du louvre, 75001 Paris</span>-->
        </div>
        <p class="header__alert-news">30% de remise pour 150 € d'achats</p>
        <div class="header__top-nav">
          <RouterLink :to="{name:'register'}" class="header__top-action">Créer</RouterLink>
          <RouterLink :to="{name:'login'}" class="header__top-action">Connexion</RouterLink>
        </div>
      </div>
    </div>
    <nav class="nav container">
      <RouterLink :to="{name:'home'}"  class="nav__logo">
        <img src="@/assets/images/logo_1.png" alt="website logo" class="nav__logo-img" />
      </RouterLink>
      <div class="nav__menu" id="nav-menu" :class="showMenu ? 'show-menu':''">
        <div class="nav__menu-top">
          <a href="#" class="nav__logo">
            <img src="@/assets/images/logo_3.png" alt="logo website" class="nav__logo-img">
          </a>
          <div class="nav__close" @click="closeMenu">
            <i class="fa-solid fa-xmark"></i>
          </div>
        </div>
        <ul class="nav__list">
          <li class="nav__item"><a href="#" class="nav__link">Tendances</a></li>
          <li class="nav__item">
            <RouterLink :to="{name:'catalog'}" class="nav__link">Catalogues</RouterLink>
          </li>
          <li class="nav__item">
            <RouterLink :to="{name:'catalog_name',params:{'category_slug':'manteaux'}}" class="nav__link">Vêtements</RouterLink>
          </li>
          <li class="nav__item"><a href="#" class="nav__link">Chaussures</a></li>
          <li class="nav__item"><a href="#" class="nav__link">Accessoires</a></li>
        </ul>
        <div class="header__search">
          <form method="get" action="/search">
            <input
            type="text"
            class="form__input"
            id="search"
            name="query"
            placeholder="Recherche..."
          />
              <button type="submit" class="search__btn">
            <i class="fa-solid fa-search"></i>
          </button>
          </form>

        </div>
      </div>
      <div class="header__user-actions">
        <RouterLink :to="{name:'cart'}" class="header__action-btn">
          <i class="fa-solid fa-cart-shopping"></i>
          <span class="count">{{cart.itemCount}}</span>
        </RouterLink>
        <RouterLink :to="{name:'login'}" class="header__action-btn user-link">
          <i class="fa-solid fa-user"></i>
        </RouterLink>
        <button @click="openMenu" type="button" class="header__action-btn btn-toggle">
          <i class="fa-solid fa-bars"></i>
        </button>
      </div>
    </nav>
  </section>
</template>
