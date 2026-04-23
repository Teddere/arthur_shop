<script>
  import {RouterLink} from 'vue-router'
  export default {
    props: {
      links:{
        type:Array,
        required: true,
        default: ()=>[]
      }
    },
    components: {
      RouterLink,
    },
    methods: {
      getRoute(link) {
        if(link.nameUrl){
          return {
            name : link.nameUrl,
            params: link.params || {}
          }
        }
        return null;
      }
    }
  }
</script>

<template>
  <section class="breadcrumb">
    <ul class="breadcrumb__list container flex">
      <li v-for="(link,index) in links" :key="link.name">
        <RouterLink v-if="index !== links.length - 1" :to="getRoute(link)" class="breadcrumb__link">
          {{link.name}}
        </RouterLink>
        <span v-else class="breadcrumb__link">
          {{link.name}}
        </span>
      </li>
    </ul>
  </section>
</template>
