<script setup>
import Header from '@/components/Header.vue'
import Footer from "@/components/Footer.vue";
import Toast from "@/components/Toast.vue";
import Loading from "@/components/loading.vue";

import { RouterView } from 'vue-router'
import { onBeforeMount } from 'vue';

import { useAuthenticate } from './stores/store';
import axios from 'axios';

const auth = useAuthenticate();
onBeforeMount(()=>{
  if(auth.token) {
    axios.defaults.headers.common['Authorization'] = `token ${auth.token}`;
  } else {
    axios.defaults.headers.common['Authorization'] = null;
  }
})
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
