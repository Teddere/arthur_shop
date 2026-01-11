<script setup>
  import {ref} from 'vue'
  import ProductItem from "@/components/ProductItem.vue";
  const productItem = ref([]);
  const product = ref({});
  productItem.value = [
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
    }
  ];

  product.value = {
    'ref':'FWM15VKT',
    'name':'Pull Rousseur brun',
    'defaultImg':'sweater.png',
    'imgItem': ['sweater-1.png','sweater.png','pul.png'],
    'brand': 'Adidas',
    'newPrice': 75.00,
    'oldPrice': 90.00,
    'pourcent': 22,
    'warranty': 1,
    'return': 15,
    'colors':['hsl(37,100%,65%)','hsl(353,100%,67%)','hsl(49,100%,60%)','hsl(304,100%,78%)','hsl(126,61%,52%)'],
    'sizes':['S','M','L','XL','XXL'],
    'stock': 10,
    'etiquette':['Linne','Mixte','Pull'],
    'composition':{
      'Polyster': 85,
      'Visco': 10,
      'Elasthanne': 10
    },
    'matiere': {}

  }
</script>
<template>
  <!-- =========== DETAILS ============= -->
  <section class="details section--lg">
    <div class="details__container container grid">
      <div class="details___group">
        <img src="@/assets/images/sweater.png" alt="product image" class="details__img">
        <div class="detail__small-images grid">
          <img src="@/assets/images/sweater-1.png" alt="product image" class="details__small-img">
          <img src="@/assets/images/sweater.png" alt="product image" class="details__small-img">
          <img src="@/assets/images/pul.png" alt="product image" class="details__small-img">
        </div>
      </div>
      <div class="details___group">
        <h3 class="details__title">Pull Rousseur brun</h3>
        <p class="details__brand">Marque: <span>Adidas</span></p>
        <div class="details__price flex">
          <span class="new__price">75.00 €</span>
          <span class="old__price">90.00 €</span>
          <span class="save__price">22% de réduction</span>
        </div>
        <p class="short__description">
          Lorem ipsum dolor sit amet, consectetur adipisicing elit.
          Tenetur ad nihil iste provident sapiente corporis distinctio dolores
          natus voluptate nulla! Cumque quas saepe provident, laborum ducimus
          laudantium accusamus beatae quis.
        </p>
        <ul class="product__list">
          <li class="list__item flex">
            <i class="fa-solid fa-crown"></i> 1 ans de garantie de fabrication.
          </li>
          <li class="list__item flex">
            <i class="fa-solid fa-refresh"></i> 15 jour pour un retour.
          </li>
          <li class="list__item flex">
            <i class="fa-solid fa-credit-card"></i> Paiment en plusieurs fois disponible
          </li>
        </ul>
        <div class="details__color flex">
          <span class="details__color-title">Couleur</span>
          <ul class="color__list">
            <li><a href="#" class="color__link" style="background: hsl(37,100%,65%);" ></a></li>
            <li><a href="#" class="color__link" style="background: hsl(353,100%,67%);" ></a></li>
            <li><a href="#" class="color__link" style="background: hsl(49,100%,60%);"></a></li>
            <li><a href="#" class="color__link" style="background: hsl(304,100%,78%);"></a></li>
            <li><a href="#" class="color__link" style="background: hsl(126,61%,52%);"></a></li>
          </ul>
        </div>
        <div class="details__size flex">
          <span class="details__size-title">Taille</span>
          <ul class="size__list">
            <li><a href="#" class="size__link size-active" >S</a></li>
            <li><a href="#" class="size__link"  >M</a></li>
            <li><a href="#" class="size__link" >L</a></li>
            <li><a href="#" class="size__link" >XL</a></li>
            <li><a href="#" class="size__link" >XXL</a></li>
          </ul>
        </div>
        <div class="details__action">
          <input type="number" value="3" name="article_number" id="article_number" class="quantity">
          <a href="#" class="btn btn-sm">Mettre au panier</a>
          <a href="#" class="details__action-btn">
            <i class="fa-solid fa-heart"></i>
          </a>
        </div>
        <ul class="details__meta">
          <li class="meta__list flex">Ref:<span> FWM15VKT</span></li>
          <li class="meta__list flex">Etiquette:<span>Linne,Mixte,Pull</span></li>
          <li class="meta__list flex">Disponibilité:<span>8 articles en stock</span></li>
        </ul>
      </div>
    </div>
  </section>
  <!-- ========= DETAILS TAB =========================-->
  <section class="details_tab container">
    <div class="details__tabs">
      <span class="detail__tab">
        Description detaillée
      </span>
      <span class="detail__tab active-tab">Avis(3)</span>
    </div>
    <div class="details__tabs-content">
      <div class="details__tab-content">
        <table class="info__table">
          <tr>
            <th>Composition</th>
            <td>Polyster 85%, Visco 10%, Elasthanne</td>
          </tr>
          <tr>
            <th>Matière</th>
            <td>Coton, Laine, Cuir, Polyester, Lin, etc.</td>
          </tr>
          <tr>
            <th>Collection</th>
            <td>Collection Hiver 2024, Collection Capsule</td>
          </tr>
          <tr>
            <th>Stock</th>
            <td>Géré par taille/couleur si applicable</td>
          </tr>
          <tr>
            <th>Taille</th>
            <td>XS, S, M, L, XL</td>
          </tr>
          <tr>
            <th>Couleurs</th>
            <td>Noir,Blanc,Vert</td>
          </tr>
        </table>
      </div>
      <div class="details__tab-content active-tab">
        <div class="reviews__container grid">
          <div class="review__single">
            <div class="">
              <img src="@/assets/images/coat_pub.png" alt="personal review image" class="review__img">
              <h4 class="review__title">Marie Antoinette</h4>
            </div>
            <div class="review__data">
              <div class="review__rating">
                <i class="fa-regular fa-star"></i>
                <i class="fa-regular fa-star"></i>
                <i class="fa-regular fa-star"></i>
                <i class="fa-regular fa-star"></i>
                <i class="fa-regular fa-star"></i>
              </div>
              <p class="review__description">
                Merci pour la livraison très rapide depuis la Pologne, en seulement 3 jours.
              </p>
              <span class="review__data">18 Novembre 2024 à 15h30</span>
            </div>
          </div>
          <div class="review__single">
            <div class="">
              <img src="@/assets/images/coat_pub.png" alt="personal review image" class="review__img">
              <h4 class="review__title">Marie Antoinette</h4>
            </div>
            <div class="review__data">
              <div class="review__rating">
                <i class="fa-regular fa-star"></i>
                <i class="fa-regular fa-star"></i>
                <i class="fa-regular fa-star"></i>
                <i class="fa-regular fa-star"></i>
                <i class="fa-regular fa-star"></i>
              </div>
              <p class="review__description">
                Merci pour la livraison très rapide depuis la Pologne, en seulement 3 jours.
              </p>
              <span class="review__data">18 Novembre 2024 à 15h30</span>
            </div>
          </div>
          <div class="review__form">
            <h4 class="review__form-title">Donner un avis</h4>
            <div class="rate__product">
              <i class="fa-regular fa-star"></i>
              <i class="fa-regular fa-star"></i>
              <i class="fa-regular fa-star"></i>
              <i class="fa-regular fa-star"></i>
              <i class="fa-regular fa-star"></i>
            </div>
            <form action="" class="form grid">
              <textarea name="review" id="review" class="form__input textarea" placeholder="Entrez votre commentaire"></textarea>
              <div class="form__group grid">
                <input type="text" name="name" id="name" class="form__input" placeholder="Entrez votre nom">
                <input type="email" name="email" id="email" class="form__input" placeholder="Entrez votre email">
              </div>
              <div class="form__btn">
                <button type="submit" class="btn">Sumettre le commentaire</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- ========== PRODUCTS ========================== -->
  <section class="products container section--lg">
    <h3 class="section__title">Articles <span>Similaires</span></h3>
    <div class="products__container grid">
      <ProductItem v-for="prod in productItem" :key="prod.id" :product="prod" />
    </div>
  </section>
</template>

