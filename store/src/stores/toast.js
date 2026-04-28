import {defineStore} from "pinia";
import {ref} from 'vue';


export const useToastStore = defineStore('toast',()=>{
  const toasts = ref([]);
  let toastId = 0;

  const toastMessage = (message,type='success',duration=3000) => {
    const id = toastId++;
    const toastContent = {
      id,
      message,
      type,
      duration
    }
    toasts.value.push(toastContent);

    if (duration > 0) {
      setTimeout(()=>{
        removeToast(id);
      },duration)
    }
  }

  const removeToast = (id)=>{
    const index = toasts.value.findIndex(toast => toast.id ===id);

    if(index !== -1) toasts.value.splice(index,1);
  }

  const success = (message,duration) => toastMessage(message,'success',duration);
  const error = (message,duration) => toastMessage(message,'error',duration);
  const warning = (message,duration) => toastMessage(message,'warning',duration);
  const info = (message,duration) => toastMessage(message,'info',duration);
  return {
    // Getters
      toasts,
    // Actions
      success,
      error,
      warning,
      info,
      removeToast
    }
});
