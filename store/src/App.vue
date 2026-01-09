<script setup>
import Header from '@/components/Header.vue'
import Footer from "@/components/Footer.vue";
import { RouterView } from 'vue-router'
</script>

<template>
  <Header></Header>
  <!-- ============ MAIN ================== -->
  <main class="main-section">
    <RouterView />
  </main>
  <Footer></Footer>
</template>
