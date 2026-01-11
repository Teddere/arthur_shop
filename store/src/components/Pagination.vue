<script setup>
  import { computed } from 'vue';

  const props = defineProps({
    currentPage : {
      type: Number,
      required:true
    },
    totalPages: {
      type: Number,
      required:true
    }
  });
  const emit = defineEmits(['update:currentPage']);

  // Afficher le nombre de pages avec ellipse
  const pageNumbers = computed(()=>{
    const pages = [];
    const total = props.totalPages;
    const current = props.currentPage;

    // Si on a peu pages, afficher tous les numéros
    if (total <= 8) {
      for(let i=1;i<=total;i++) {
        pages.push(i)
      }
      return pages;
    }
    // Toujours afficher le 1er numéro page
    pages.push(1);

    //Logique pour les pages du milieu

    if (current <=3 ){
      // Structure : 1, 2, 3, 4, ..., last
      for(let i=2; i<=4; i++) {
        pages.push(i)
      }
      pages.push('...');
      pages.push(total);
    }
    else if (current >= total -2){
      // Structure: 1, ..., last-3, last-2, last-1, last
      pages.push('...');
      for (let i = total - 3; i <= total; i++) {
        pages.push(i);
      }

    }
    else {
      // Milieu: 1, ..., current-1, current, current+1, ..., last
      pages.push('...');
      pages.push(current - 1);
      pages.push(current);
      pages.push(current + 1);
      pages.push('...');
      pages.push(total);
    }

    return pages
  });

  const changePage = (page)=>{
    // Vérifier que page est un nombre et dans les limites
    if (typeof page === 'number' && page >=1 && page <= props.totalPages && page !== props.currentPage ) {
      emit('update:currentPage',page)
    }
  }

  const prevPage = ()=>{
    if (props.currentPage > 1) {
      changePage(props.currentPage - 1)
    }
  }

  const nextPage = ()=>{
    if (props.currentPage < props.totalPages) {
      changePage(props.currentPage + 1)
    }
  }

</script>
<template>
  <ul class="pagination" v-if="totalPages > 1">
    <li class="pagination__item" v-if="currentPage > 1" @click="prevPage">
      <span class="pagination__link pagination__arrow">
        <i class="fa-solid fa-chevron-left"></i>
      </span>
    </li>
    <li
      v-for="(page,i) in pageNumbers"
      :key="i"
      class="pagination__item"
      :class="{'active': page === currentPage,'ellipsis': page==='...'}"
      >
      <span v-if="page === '...'" class="pagination__link pagination__ellipsis">
        {{ page }}
      </span>
      <span v-else
        class="pagination__link"
        @click="changePage(page)"
      >
        {{ page }}
      </span>
    </li>
    <li class="pagination__item" v-if=" currentPage < totalPages" @click="nextPage">
      <span class="pagination__link pagination__arrow">
        <i class="fa-solid fa-chevron-right"></i>
      </span>
    </li>
  </ul>
</template>
