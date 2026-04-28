<script setup>
  import {useToastStore} from "@/stores/toast.js";

  const toastStore = useToastStore();
  const getIcon = (type)=> {
    const icons = {
      success: 'fa-circle-check',
      error: 'fa-circle-xmark',
      warning: 'fa-triangle-exclamation',
      info: 'fa-circle-info',
    }
    return icons[type] || icons.info;
  }
  const removeToast = (id)=>{
    toastStore.removeToast(id)
  }
</script>

<template>
  <div class="toast-container">
    <transition-group name="toast-slide" tag="div">
      <div v-for="toast in toastStore.toasts"
           :key="toast.id"
           class="toast" :class="`toast-${toast.type}`">
        <!-- Icône -->
        <i class="fa-solid" :class="getIcon(toast.type)"></i>
        <!-- Message -->
        <span class="toast-message">{{toast.message}}</span>
        <!-- close btn -->
        <button @click="removeToast(toast.id)" type="button" class="toast-close">
          <i class="fa-solid fa-xmark"></i>
        </button>
        <!-- Progressing -->
        <div class="toast-progress"></div>
      </div>
    </transition-group>
  </div>
</template>

<style scoped>
.toast-container {
  position: fixed;
  bottom: 20px;
  right: 0;
  z-index: 999;
  pointer-events: none;
}
.toast {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px 18px;
  border-radius: 8px;
  background: var(--body-color);
  box-shadow: 0 4px 16px rgba(0,0,0,.15);
  pointer-events: auto;
  min-width: 300px;
  position: relative;
  overflow: hidden;
}
.toast i {
  font-size: 20px;
}
.toast-success {
  border-left: 4px solid var(--green-color);
  background: #f0f8f5;
}
.toast-success i {
  color: var(--green-color);
}
.toast-error {
  border-left: 4px solid var(--red-color);
  background: #faddd1;
}
.toast-error i {
  color: var(--red-color);
}
.toast-warning {
  border-left: 4px solid var(--warning-color);
  background: #fef5e7;
}
.toast--warning i {
   color: var(--warning-color);
}
.toast-info {
  border-left: 4px solid var(--info-color);
  background: #ebf5fb;
}
.toast-info i {
  color: var(--info-color);
}
.toast-message {
  flex: 1;
  color: var(--text-color-light);
  font-weight: var(--weight-500);
  font-size: 14px;
}
.toast-close {
  background: none;
  border: none;
  color: #999;
  font-size: 18px;
  padding: 0;
  transition: color .2s;
}
.toast-close:hover {
  color: var(--text-color-light);
}
.toast-progress {
  position: absolute;
  bottom: 0;
  left: 0;
  height: 3px;
  background: currentColor;
  animation: progress 3s linear forwards;
}
.toast-success .toast-progress {
  background: var(--green-color);
}
.toast-error .toast-progress {
  background: var(--red-color);
}
.toast-warning .toast-progress {
  background: var(--warning-color);
}
.toast-info .toast-progress {
  background: var(--info-color);
}
@keyframes progress {
  from {
    width: 100%;
  }
  to {
    width: 0;
  }
}
.toast-slide-enter-active,
.toast-slide-leave-active {
  transition: all .3s ease;
}
.toast-slide-enter-from {
  transform: translateX(400px);
  opacity: 0;
}
.toast-slide-leave-to {
  transform: translateX(400px);
  opacity: 0;
}
.toast-slide-move {
  transition: transform 0.3s ease;
}
@media (max-width: 480px) {
  .toast-container {
    left: 10px;
    right: 10px;
    top: 10px;
  }
  .toast {
    min-width: auto;
  }
}
</style>
