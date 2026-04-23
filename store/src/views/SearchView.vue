<script setup>
  import axios from "axios";
  import {onMounted,ref} from "vue";
  import ProductItem from "@/components/ProductItem.vue";


  const query = ref('');
  const listProducts = ref([]);

  onMounted(()=>{
    document.title = 'Recherche | artur';
    let url = window.location.search.substring(1);
    let params = new URLSearchParams(url);

    if (params.get('query')){
      query.value = params.get('query');
      formSearch();
    }
  });

  const formSearch = ()=>{
    // chargement

    axios
      .post('/api/v1/products/search/',{'query':query.value})
      .then(response => {
        listProducts.value = response.data
      })
      .catch(err=>{
        console.log(err)
      })
  }


</script>

<template>
    <section class="search-section">
      <section class="products section--lg container" id="products">
        <div class="products__header">
           Nous avons trouvé <span class="products__count">
          {{ listProducts.length }}</span>
          article{{ listProducts.length > 1 ? 's' : '' }}
        </div>
          <div class="products__container grid">
            <ProductItem
              v-for="(product,index) in listProducts"
              :key="index"
              :product="product"
            >
            </ProductItem>
          </div>
      </section>
    </section>
</template>

<style scoped>

</style>
