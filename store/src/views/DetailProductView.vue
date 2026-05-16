<script setup>
  import axios from "axios";
  import { ref,onMounted,computed } from 'vue';
  import { useRoute } from 'vue-router';
  import { useCartStore } from "@/stores/cart.js";
  import { useToastStore } from "@/stores/toast.js";
  import Breadcrumb from "@/components/Breadcrumb.vue";
  import ProductItem from "@/components/ProductItem.vue";

  const toast = useToastStore();
  const cart = useCartStore();
  const route = useRoute();
  // navigations links
  const links = ref([
    {'name':'Accueil', 'nameUrl':'home'},
    {'name':'Catalogue', 'nameUrl':'catalog'}
  ]);
  // product item element current
  const product = ref({});
  // size list product item element current
  const sizeList = ref([]);
  // navigations menu
  const activeTab = ref('info');
  // product reviews
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
    }
  ]);
  const noteReview = ref(0);
  const hoverReview = ref(0);
  // select product item image current
  const selectImage = ref(null);
  // select product item color current
  const selectColor = ref(null);
  // select product item size current
  const selectSize = ref(null);
  // product number in to cart
  const productCount = ref(1);
  // product informations
  const productInfo = [
    { title: 'Composition', content: 'Polyster 85%, Visco 10%, Elasthanne' },
    { title: 'Matière', content: 'Coton, Laine, Cuir, Polyester, Lin, etc.' },
    { title: 'Collection', content: 'Collection Hiver 2024, Collection Capsule' },
    { title: 'Stock', content: 'Géré par taille/couleur si applicable' },
    { title: 'Taille', content: 'XS, S, M, L, XL' },
    { title: 'Couleurs', content: 'Noir,Blanc,Vert' }
  ]
  // url image
  const getImageUrl = (url)=>{
    if (!url) return ''
    else if (url.includes('media')) return url
    else {
      return new URL(`../assets/images/${url}`,import.meta.url).href
    }
  }
  // method select color for size
  const sizeColorItem = (size)=>{
      let elementProduct = {}
      product.value.size_list.filter((sizeItem)=>{
         if (size === selectSize.value) return true
          if (size === sizeItem.size) {
            sizeList.value = sizeItem.items;
            selectSize.value = sizeItem.size;
            selectColor.value = sizeItem.items[0].color.name;
            // update product element
            elementProduct.id = sizeItem.items[0].product_item_id;
            elementProduct.sku = sizeItem.items[0].sku;
            elementProduct.size = sizeItem.size;
            elementProduct.color = {'name': sizeItem.items[0].color.name,'value': sizeItem.items[0].color.value}
            elementProduct.stock = sizeItem.items[0].stock;
            elementProduct.stock_status = sizeItem.items[0].stock_status;
            elementProduct.is_available = sizeItem.items[0].is_available;
            elementProduct.percent = sizeItem.items[0].percent;
            elementProduct.base_price = sizeItem.items[0].base_price;
            elementProduct.newPrice = sizeItem.items[0].newPrice
          }
      })
      product.value.element = elementProduct;
  }

  // method product color select
  const colorProductItem = (color)=>{
    let elementProduct = {}
    if (color.name === selectColor.value ) return true
    product.value.size_list.map((element)=>{
      element.items.filter((colorItem)=> {
        if (color.name === colorItem.color.name && element.size === product.value.element.size) {
          selectColor.value = color.name;
          // update product element
          elementProduct.id = colorItem.product_item_id;
          elementProduct.sku = colorItem.sku;
          elementProduct.size = element.size;
          elementProduct.color = {'name': colorItem.color.name, 'value': colorItem.color.value };
          elementProduct.stock = colorItem.stock;
          elementProduct.stock_status = colorItem.stock_status;
          elementProduct.is_available = colorItem.is_available;
          elementProduct.percent = colorItem.percent;
          elementProduct.base_price = colorItem.base_price;
          elementProduct.newPrice = colorItem.newPrice
        }
      })
    });
    product.value.element = elementProduct;
  }

  // onMounted
  onMounted(()=>{
    getProduct()
  })
  // product element
  const getProduct = ()=>{
    const category_slug = route.params.category_slug;
    const product_slug = route.params.product_slug;
    axios
      .get(`/api/v1/products/${category_slug}/${product_slug}`)
      .then(response=>{
        console.log(response.data)
        // Breadcrumb navigation
        links.value.push({
          'name':response.data.category.name,
          'nameUrl':'catalog_name',
          'params': {'category_slug': category_slug.toLocaleLowerCase()}
        });
        links.value.push({
          'name': response.data.title,
          'nameUrl': null
        })
        // product value element
        product.value = response.data;
        selectImage.value = product.value.image_default;
        selectSize.value = product.value.element.size;
        selectColor.value = product.value.element.color.name;
        // size selection
        product.value.size_list.map((productItem)=>{
          if (selectSize.value === productItem.size) {
            sizeList.value = productItem.items;
            console.log(sizeList.value);
          }
        });
        // title page
        document.title = `${product.value.title} | Arthur`;
      })
      .catch(err=>{
        console.log(err);
      });
  }

  // add product to cart
  const addProductCart = ()=>{
    const quantity = parseInt(productCount.value);
    if (isNaN(quantity) || quantity < 1) {
      toast.warning('Veuillez la quantité souhaiter !');
    }
    else if (quantity > product.value.element.stock) {
      toast.error('Pas assez de produit pour le moment !')
    }
    else {
      // cart.addToCart()
    }
  }
</script>
<template>
  <Breadcrumb :links="links" />
  <!-- =========== DETAILS ============= -->
  <section class="details section--lg">
    <div class="details__container container grid">
      <div class="details__group">
        <img :src="getImageUrl(selectImage)" alt="product image" class="details__img">
        <div class="detail__small-images grid">
          <img :src="product.image_default"
               @click="selectImage = product.image_default"
               :class="{'active': selectImage === product.image_default }"
               alt="description product image"
               class="details__small-img">
          <img :src="product.image_hover"
               @click="selectImage = product.image_hover"
               :class="{'active': selectImage === product.image_hover }"
               alt="description product image"
               class="details__small-img">
        </div>
      </div>
      <div class="details___group">
        <h2 class="details__title">{{product.title}}</h2>
        <p class="details__brand">Marque : <span>{{product.brand}}</span></p>
        <div class="details__price flex" v-if="product.element?.newPrice">
          <span class="new__price">{{product.element.newPrice}} €</span>
          <span class="old__price">{{product.element.base_price}} €</span>
          <span class="save__price">{{product.element.percent}}% de réduction</span>
        </div>
        <div class="details__price flex" v-else>
          <span class="new__price">{{product.element?.base_price}} €</span>
        </div>
        <p class="short__description">{{product.description}}</p>
        <ul class="product__list">
          <li class="list__item flex">
            <i class="fa-solid fa-crown"></i>
            <template v-if="product.warranty === 1">1 an de garantie de fabrication</template>
            <template v-else-if="product.waranty > 1">{{product.warranty}} ans de garantie de fabrication</template>
            <template v-else>Article non garanti</template>
          </li>
          <li class="list__item flex">
            <i class="fa-solid fa-credit-card"></i>
            Paiement en plusieurs fois disponible
          </li>
        </ul>
        <div class="details__color flex">
          <span class="details__color-title">Couleur</span>
          <ul class="color__list" v-if="sizeList">
            <li v-for="(colorItem,index) in sizeList" :key="index">
              <button type="button"
                      :style="{backgroundColor: colorItem.color.value}"
                      :class="{'active': selectColor === colorItem.color.name}"
                      @click="colorProductItem(colorItem.color)"
                      class="color__link"
              ></button>
            </li>
          </ul>
          <span v-else class="option">Pas d'option de couleur</span>
        </div>
        <div class="details__size flex">
          <span class="details__size-title">Taille</span>
          <ul class="size__list" v-if="product.size_list">
            <li v-for="(sizeProduct,index) in product.size_list" :key="index">
              <button type="button"
                      @click="sizeColorItem(sizeProduct.size)"
                      :class="{'size-active': selectSize === sizeProduct.size}"
                      class="size__link"
              >
                {{ sizeProduct.size }}
              </button>
            </li>
          </ul>
          <span v-else>Taille unique</span>
        </div>
        <form @submit.prevent="addProductCart">
          <div class="details__action">
            <input type="number" v-model="productCount"  id="article_number" min="1" :max="product.element?.stock" class="quantity">
            <button type="submit" class="btn btn-sm">Mettre au panier</button>
            <button type="button" class="details__action-btn">
              <i class="fa-solid fa-right-left"></i>
            </button>
          </div>
        </form>
        <ul class="details__meta">
          <li class="meta__list flex">Ref : {{product.element?.sku}}</li>
          <li class="meta__list flex">
            Etiquette :&nbsp;
            <template v-for="(tag,index) in product.tag" :key="index">
              <span v-if="index < product.tag.length - 1">{{tag.name}},</span>
              <span v-else>{{tag.name}}</span>
            </template>
          </li>
          <li class="meta__list flex">
              Disponibilité:<span>{{product.element.stock}} article(s) en stock</span>
          </li>
        </ul>
      </div>
    </div>
  </section>
</template>
<style></style>
