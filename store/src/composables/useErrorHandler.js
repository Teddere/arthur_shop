import {handleRouterError} from "@/router/index.js";

export const useErrorHandler = ()=>{
  const handlerError = async (error)=>{
    return handleRouterError(error);
  }
  return {handlerError}
}

