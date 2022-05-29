<template>
  <div>
    <Heading content="Dashboard" />
    <div class="mx-auto justify-center w-3/5 bg-white my-12 border-2 border-black rounded">
      <nav class="flex flex-col sm:flex-row">
        <Tab class="rounded-tl" name="Overview" link="/dashboard/" />
        <LazyTab name="Handles" link="/dashboard/handles/" />
        <LazyTab name="Kindles" link="/dashboard/kindles/" />
        <LazyTab class="rounded-tr" name="Notifications" link="/dashboard/notifications/" />
      </nav>
      <NuxtChild keep-alive />
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  middleware: 'auth'
});
</script>

<style scoped>
.nuxt-link-exact-active {
  @apply bg-gray-100 border-yellow-400 border-b-2 font-bold subpixel-antialiased;
}
</style>
