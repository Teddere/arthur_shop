<script setup>
import Header from '@/components/Header.vue'
import Footer from "@/components/Footer.vue";
import Toast from "@/components/Toast.vue";
import Loading from "@/components/loading.vue";
import { RouterView } from 'vue-router'
</script>

<template>
  <Loading></Loading>
  <Header></Header>
  <!-- ============ MAIN ================== -->
  <main class="main-section">
    <RouterView />
  </main>
  <Footer></Footer>
  <Toast></Toast>
</template>
