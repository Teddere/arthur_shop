<template>
  <transition name="fade">
    <div v-if="loading.isLoading" class="loading-overlay">
      <div class="loading-container">
        <div class="logo-wrapper">
          <img src="@/assets/images/logo_3.png" alt="website logo" class="logo_loading">
          <div class="circle circle-1"></div>
          <div class="circle circle-2"></div>
        </div>
      </div>
    </div>
  </transition>
</template>
<script setup>
import {useLoadingStore} from '@/stores/store.js';

const loading = useLoadingStore()
</script>
<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity .3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 999;
  background: var(--body-color);
}
.loading-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 15px;
  animation: slideUp .6s ease-out;
}
@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
.logo-wrapper {
  position: relative;
  width: 100px;
  height: 100px;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 50%;
  box-shadow: rgba(100, 100, 111, 0.2) 0 7px 29px 0;
}
.logo_loading {
  width: 60px;
  height: 60px;
  object-fit: contain;
  z-index: 10;
  animation: rotateLogo 3s linear infinite;
}
@keyframes rotateLogo {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
.circle {
  position: absolute;
  border: 3px solid rgba(var(--primary-rgb), 0.3);
  border-radius: 50%;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.circle-1 {
  width: 140px;
  height: 140px;
  border-top: 3px solid rgba(var(--primary-rgb), .8);
  animation: spinCircle 2s linear infinite;
}
@keyframes spinCircle {
  from {
    transform: translate(-50%,-50%) rotate(0deg);
  }
  to {
    transform: translate(-50%,-50%) rotate(360deg);
  }
}
@media screen and (min-width: 480px) {
  .loading-container {
    gap: 30px;
  }
  .logo-wrapper {
    width: 140px;
    height: 140px;
  }
  .logo_loading {
    width: 100px;
    height: 100px;
  }
}
</style>
