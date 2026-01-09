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
    }
  }
</script>

<template>
  <section class="breadcrumb">
    <ul class="breadcrumb__list container flex">
      <li v-for="(link,index) in links" :key="link.name">
        <RouterLink v-if="index !== links.length - 1" :to="{name:link.nameUrl}" class="breadcrumb__link">
          {{link.name}}
        </RouterLink>
        <span v-else class="breadcrumb__link">
          {{link.name}}
        </span>
      </li>
    </ul>
  </section>
</template>

<style scoped>

</style>
