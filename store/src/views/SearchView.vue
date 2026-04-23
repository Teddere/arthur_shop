<script setup>
  import {onMounted,ref} from "vue";
  import ProductItem from "@/components/ProductItem.vue";


  const query = ref(0);
  const listProducts = ref([]);

  onMounted(()=>{
    document.title = 'Recherche | artur'
  })


</script>

<template>
    <section class="search-section">
      <section class="products section--lg container" id="products">
        <div class="products__header">
           Nous avons trouvé <span class="products__count">
          {{ listProducts.length }}</span>
          article{{ listProducts.length > 1 ? 's' : '' }}
        </div>
      </section>
    </section>
</template>

<style scoped>

</style>
