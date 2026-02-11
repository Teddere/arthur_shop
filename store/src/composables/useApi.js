import {useLoadingStore} from '@/stores/store.js';
import {useErrorHandler} from "@/composables/useErrorHandler.js";
import axios from "axios";

/**
 * Composable pour les appels API avec loading automatique
 * Gère le timeout, les erreurs et la redirection 404
 */

export const useApi = ()=>{
  const loading = useLoadingStore();
  const {handlerError } = useErrorHandler();

  /**
   * Crée une instance Axios personnalisée
   * @param {number} timeout - Délai d'attente en ms
   */
  const createAxiosInstance = (timeout=5000)=>{
    return axios.create({
      timeout:timeout,
      headers: {
        "content-type":'application/json'
      }
    })
  }

  const request = async (method,url,data=null,timeout=5000,delay=300)=>{
    return loading.loadingPage(async ()=>{
      try {
        const instance = createAxiosInstance(timeout);
        const response = await instance({method,url,data});
        return response.data;
      }catch (err) {
        throw await handlerError(err);
      }
    },delay)
  }

  const get = (url,timeout,delay)=> request('get',url,null,timeout,delay);
  const post = (url,data,timeout,delay)=> request('post',url,data,timeout,delay);
  const put = (url,data,timeout,delay)=> request('put',url,data,timeout,delay);
  const del = (url,timeout,delay)=> request('delete',url,null,timeout,delay);

  return {
    get,
    post,
    put,
    del,
  }
}
