<script setup>
import Breadcrumb from "@/components/Breadcrumb.vue";
import ProductItem from "@/components/ProductItem.vue";
import Pagination from "@/components/Pagination.vue";
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute, useRouter } from "vue-router";

const route = useRoute();
const router = useRouter();
const products = ref([]);
const currentPage = ref(1);
const itemPerPage = ref(8);

const linkNavigatePage = [
  { 'name': 'Accueil', 'nameUrl': 'home' },
  { 'name': 'Catalogue', 'nameUrl': 'catalog' }
];

products.value = [
  {
    id: 1,
    imgDefault: 'product-1-1.jpg',
    imgHover: 'product-1-2.jpg',
    badge: 'promo',
    badgeClass: '',
    category: 'Foulards',
    title: 'Hawaï Thuph',
    newPrice: 25.00,
    oldPrice: 35.00
  },
  {
    id: 2,
    imgDefault: 'scarf.png',
    imgHover: 'scarf-1.png',
    badge: '-30%',
    badgeClass: 'light-pink',
    category: 'Foulards',
    title: 'Hawaï Thuph',
    newPrice: 25.00,
    oldPrice: 35.00
  },
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
    id: 4,
    imgDefault: 'polo.png',
    imgHover: 'polo-2.png',
    badge: '',
    badgeClass: '',
    category: 'Pull',
    title: 'Tiffany Grey',
    newPrice: 40.00,
    oldPrice: 69.90,
  },
  {
    id: 5,
    imgDefault: 'pull-1.png',
    imgHover: 'pull-2.png',
    badge: 'collection',
    badgeClass: 'light-blue',
    category: 'Pull',
    title: 'Pull Pouma white',
    newPrice: 89.90,
    oldPrice: 99.99
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
    id: 7,
    imgDefault: 'bag.png',
    imgHover: 'bag-3.png',
    badge: 'collection',
    badgeClass: 'light-orange',
    category: 'Sac',
    title: 'Hermes Lagardène',
    newPrice: 5000.00,
    oldPrice: 8699.99
  },
  {
    id: 8,
    imgDefault: 'shirt.png',
    imgHover: 'shirt-1.png',
    badge: 'collection',
    badgeClass: 'light-orange',
    category: 'Chemise',
    title: 'Roi Luc',
    newPrice: 39.00,
    oldPrice: 69.99
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
    id: 10,
    imgDefault: 'polo.png',
    imgHover: 'polo-2.png',
    badge: '',
    badgeClass: '',
    category: 'Pull',
    title: 'Tiffany Grey',
    newPrice: 40.00,
    oldPrice: 69.90
  },
  {
    id: 11,
    imgDefault: 'ceinture.png',
    imgHover: 'ceinture-1.png',
    badge: 'Collection',
    badgeClass: 'light-blue',
    category: 'Ceinture',
    title: 'Armeni',
    newPrice: 40.00,
    oldPrice: 69.90
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

// Nombre total de produits
const totalProducts = computed(() => products.value.length);

// Produits de la page courante
const paginationProducts = computed(() => {
  const startIndex = (currentPage.value - 1) * itemPerPage.value;
  const endIndex = startIndex + itemPerPage.value;
  return products.value.slice(startIndex, endIndex);
});

// Nombre total de pages
const totalPages = computed(() => {
  return Math.ceil(totalProducts.value / itemPerPage.value);
});

// Gestion de changement de page
const handlePageChange = (newPage) => {
  // Vérifier que la nouvelle page est valide
  if (newPage < 1 || newPage > totalPages.value) {
    return;
  }

  currentPage.value = newPage;

  // Mettre à jour l'URL
  router.push({
    query: { ...route.query, page: newPage }
  });

  // Scroll vers la section produits
  scrollToProducts();
}

// Fonction pour scroller vers les produits
const scrollToProducts = () => {
  const prodSection = document.getElementById('products');
  if (prodSection) {
    prodSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
}

// Montage du composant
onMounted(() => {
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
    currentPage.value = 1;
  }
});

// Surveiller les changements de route (navigation par boutons navigateur)
watch(() => route.query.page, (newPage) => {
  const pageNumber = parseInt(newPage);

  if (newPage && !isNaN(pageNumber) && pageNumber >= 1 && pageNumber <= totalPages.value) {
    currentPage.value = pageNumber;
    scrollToProducts();
  } else if (!newPage) {
    currentPage.value = 1;
  }
});
</script>

<template>
  <Breadcrumb :links="linkNavigatePage" />
  <section class="products section--lg container" id="products">
    <div class="products__header">
      Nous avons trouvé <span class="products__count">{{ totalProducts }}</span> article{{ totalProducts > 1 ? 's' : '' }}
    </div>

    <div class="products__container grid">
      <ProductItem
        v-for="product in paginationProducts"
        :key="product.id"
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
