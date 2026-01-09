<script setup>
import Breadcrumb from "@/components/Breadcrumb.vue";
import ProductItem from "@/components/ProductItem.vue";
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from "vue-router";

const route = useRoute()
const router = useRouter()
const links = ref([]);
const products = ref([]);
const currentPage = ref(1);
const itemPerPage = ref(8);
const totalProducts = ref(10)

links.value = [
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
    title: 'Hawaii Thuph',
    newPrice: '25.00',
    oldPrice: '35.00'
  },
  {
    id: 2,
    imgDefault: 'scarf.png',
    imgHover: 'scarf-1.png',
    badge: '-30%',
    badgeClass: 'light-pink',
    category: 'Foulards',
    title: 'Tiffany Chou',
    newPrice: '9.90',
    oldPrice: '19.90'
  },
  {
    id: 3,
    imgDefault: 'shoe-5.png',
    imgHover: 'shoe-7.png',
    badge: '-22%',
    badgeClass: 'light-pink',
    category: 'Chaussure',
    title: 'Weston Mark Time',
    newPrice: '450.00',
    oldPrice: '599.90'
  },
  {
    id: 4,
    imgDefault: 'polo.png',
    imgHover: 'polo-2.png',
    badge: '',
    badgeClass: '',
    category: 'Pull',
    title: 'Tiffany Grey',
    newPrice: '40.00',
    oldPrice: '69.90'
  },
  {
    id: 5,
    imgDefault: 'pull-1.png',
    imgHover: 'pull-2.png',
    badge: 'collection',
    badgeClass: 'light-blue',
    category: 'Pull',
    title: 'Pull Pouma white',
    newPrice: '89.90',
    oldPrice: '99.99'
  },
  {
    id: 6,
    imgDefault: 'sandals.png',
    imgHover: 'sandals-1.png',
    badge: 'Nouveauté',
    badgeClass: '',
    category: 'Sandale',
    title: 'Lacost drum',
    newPrice: '50.90',
    oldPrice: '99.90'
  },
  {
    id: 7,
    imgDefault: 'bag.png',
    imgHover: 'bag-3.png',
    badge: 'collection',
    badgeClass: 'light-orange',
    category: 'Sac',
    title: 'Hermes Lagardène',
    newPrice: '5000.00',
    oldPrice: '8699.99'
  },
  {
    id: 8,
    imgDefault: 'shirt.png',
    imgHover: 'shirt-1.png',
    badge: 'collection',
    badgeClass: 'light-orange',
    category: 'Chemise',
    title: 'Roi Luc',
    newPrice: '39.00',
    oldPrice: '69.99'
  },
  {
    id: 9,
    imgDefault: 'scarf.png',
    imgHover: 'scarf-1.png',
    badge: '-30%',
    badgeClass: 'light-pink',
    category: 'Foulards',
    title: 'Tiffany Chou',
    newPrice: '9.90',
    oldPrice: '19.90'
  },
  {
    id: 10,
    imgDefault: 'polo.png',
    imgHover: 'polo-2.png',
    badge: '',
    badgeClass: '',
    category: 'Pull',
    title: 'Tiffany Grey',
    newPrice: '40.00',
    oldPrice: '69.90'
  }
]

onMounted(() => {
  if (route.query.page) {
    currentPage.value = parseInt(route.query.page)
  }
});

const paginateProducts = computed(() => {
  const startIndex = (currentPage.value - 1) * itemPerPage.value
  const endIndex = startIndex + itemPerPage.value
  return products.value.slice(startIndex, endIndex);
});

const totalPages = computed(() => {
  return Math.ceil(totalProducts.value / itemPerPage.value)
});

const showingRange = computed(() => {
  const start = (currentPage.value - 1) * itemPerPage.value + 1
  const end = Math.min(currentPage.value * itemPerPage.value, totalProducts.value)
  return { start, end }
});

const pageNumbers = computed(() => {
  const pages = []
  const maxVisiblePages = 5

  if (totalPages.value <= maxVisiblePages) {
    for (let i = 1; i <= totalPages.value; i++) {
      pages.push(i)
    }
  } else {
    if (currentPage.value <= 3) {
      for (let i = 1; i <= 4; i++) {
        pages.push(i)
      }
      pages.push('...')
      pages.push(totalPages.value)
    } else if (currentPage.value >= totalPages.value - 2) {
      pages.push(1)
      pages.push('...')
      for (let i = totalPages.value - 3; i <= totalPages.value; i++) {
        pages.push(i)
      }
    } else {
      pages.push(1)
      pages.push('...')
      pages.push(currentPage.value - 1)
      pages.push(currentPage.value)
      pages.push(currentPage.value + 1)
      pages.push('...')
      pages.push(totalPages.value)
    }
  }
  return pages
})

const goToPage = (page) => {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page
    router.push({ query: { ...route.query, page: page } })

    const productSection = document.getElementById('products');
    if (productSection) {
      productSection.scrollIntoView({ behavior: 'smooth' })
    }
  }
}

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    goToPage(currentPage.value + 1)
  }
}

const prevPage = () => {
  if (currentPage.value > 1) {
    goToPage(currentPage.value - 1)
  }
}
</script>

<template>
  <Breadcrumb :links="links" />
  <section class="products section--lg container" id="products">
    <p class="total__products">
      Nous avons trouvé <span>{{ totalProducts }}</span> articles
      <span class="showing-range" v-if="totalProducts > itemPerPage">
        (Affichage {{ showingRange.start }} à {{ showingRange.end }})
      </span>
    </p>
    <div class="products__container grid">
      <ProductItem v-for="product in paginateProducts" :key="product.id" :product="product" />
    </div>

    <ul class="pagination" v-if="totalPages > 1">
      <li @click="prevPage" :class="{ disabled: currentPage === 1 }">
        <span class="pagination__link fa-solid fa-chevron-left"></span>
      </li>
      <li v-for="(page, index) in pageNumbers" :key="index"
        @click="page !== '...' ? goToPage(page) : null"
        :class="{ active: page === currentPage, ellipsis: page === '...' }">
        <span class="pagination__link" v-if="page !== '...'">{{ String(page).padStart(2, '0') }}</span>
        <span class="pagination__link" v-else>{{ page }}</span>
      </li>
      <li @click="nextPage" :class="{ disabled: currentPage === totalPages }">
        <span class="pagination__link fa-solid fa-chevron-right"></span>
      </li>
    </ul>
  </section>
</template>

<style scoped>
.pagination {
  display: flex;
  justify-content: center;
  gap: 0.5rem;
  margin-top: 2rem;
  list-style: none;
}

.pagination li {
  cursor: pointer;
  padding: 0.5rem;
}

.pagination li.disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.pagination__link {
  display: inline-block;
  padding: 0.5rem 0.75rem;
  border-radius: 4px;
  transition: all 0.3s ease;
}

.pagination li.active .pagination__link {
  background-color: #333;
  color: white;
}

.pagination li.ellipsis .pagination__link {
  cursor: default;
}
</style>
