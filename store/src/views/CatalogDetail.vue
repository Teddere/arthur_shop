<script setup>
  import axios from "axios";
  import Breadcrumb from "@/components/Breadcrumb.vue";
  import ProductItem from "@/components/ProductItem.vue";
  import Pagination from "@/components/Pagination.vue";
  import { useRoute, useRouter } from "vue-router";
  import { ref, computed, onMounted, watch } from 'vue'

  const route = useRoute();
  const router = useRouter();
  const products = ref([]);
  const currentPage = ref(1);
  const itemPerPage = ref(12);
  const linkNavigatePage = ref([
    { 'name': 'Accueil', 'nameUrl': 'home' },
    { 'name': 'Catalogue', 'nameUrl': 'catalog' }
  ]);

  // Nombre total de produits
  const totalProducts = computed(()=>products.value.length);
  // Produits de la page courante
  const paginationProducts = computed(()=>{
    const startIndex = (currentPage.value - 1) * itemPerPage.value;
    const endIndex = startIndex + itemPerPage.value;
    return products.value.slice(startIndex,endIndex)
  });

  // Nombre total de pages
  const totalPages = computed(()=>{
    return Math.ceil(totalProducts.value/itemPerPage.value);
  })
  // Gestion de changement de page
  const handlePageChange = (newPage)=>{
    // Vérifier que la nouvelle page est valide
    if (newPage < 1 || newPage > totalPages.value) return;
    currentPage.value = newPage;
    // Mettre à jour l'URL
    router.push({
      query:{...route.query,page:newPage}
    })
    // Scroll vers la section produits
    scrollToProducts();
  }
  const scrollToProducts = ()=>{
    const prodSection = document.getElementById('products');
    if (prodSection) {
      prodSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }
  // récuperation
  const getProductSelected = ()=>{
    const category_slug = route.params.category_slug;
    linkNavigatePage.value.push({ 'name': category_slug, 'nameUrl': 'catalog' })
    axios
      .get(`api/v1/catalog/${category_slug}`)
      .then(response=>{
        console.log(response.data)
        products.value = response.data;
        document.title = `${category_slug.toLocaleLowerCase()} | Arthur`
      })
      .catch(err=>{
        console.log(err)
      });
  }
  // Montage du composant
  onMounted(()=>{
    getProductSelected()
    // Initialiser la page depuis l'URL
    const pageFromUrl = parseInt(route.query.page);
    if (pageFromUrl && !isNaN(pageFromUrl) && pageFromUrl >= 1 && pageFromUrl <= totalPages.value) {
      currentPage.value = pageFromUrl;
    } else if (pageFromUrl && (pageFromUrl < 1 || pageFromUrl > totalPages.value)) {
      // Si la page dans l'URL est invalide, rediriger vers la page 1
      router.replace({ query: { ...route.query, page: 1 } });
      currentPage.value = 1;
    } else {
      // Pas de page dans l'URL, définir par défaut à 1
      currentPage.value = 1
    }

  });
  // Surveiller les changements de route (navigation par boutons navigateur)
  watch(()=>route.query.page,(newPage)=>{
    const pageNumber = parseInt(newPage);
    if (newPage && !isNaN(pageNumber) && pageNumber >= 1 && pageNumber <= totalPages.value) {
      currentPage.value = pageNumber;
      scrollToProducts();
    } else if(!newPage) {
      currentPage.value = 1
    }
  });
</script>

<template>
  <Breadcrumb :links="linkNavigatePage" />
  <section class="products section--lg container" id="products">
    <div class="products__container grid">
      <ProductItem
        v-for="(product,index) in paginationProducts"
        :key="index"
        :product="product"
        />
    </div>
    <!-- Composant pagination -->
    <Pagination
      :current-page="currentPage"
      :total-pages="totalPages"
      @update:current-page="handlePageChange"
      />
  </section>
</template>

<style scoped>
.products {
  padding: 2rem 0;
}

.products__header {
  margin-bottom: 2rem;
  font-size: 1.125rem;
  color: #374151;
}

.products__count {
  font-weight: 700;
  color: #333;
}

.products__container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 2rem;
  margin-bottom: 2rem;
}

@media (max-width: 768px) {
  .products__container {
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 1rem;
  }
}

@media (max-width: 480px) {
  .products__container {
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
    gap: 0.75rem;
  }
}
</style>
