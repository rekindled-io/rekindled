<template>
  <div>
    <Heading content="Dashboard" />
    <div class="w-3/5 mx-auto my-12 bg-white border-2 border-black rounded">
      <nav class="flex flex-col sm:flex-row">
        <Tab class="rounded-tl" name="Overview" link="/dashboard/" />
        <Tab name="Handles" link="/dashboard/handles/" />
        <Tab name="Kindles" link="/dashboard/kindles/" />
        <Tab class="rounded-tr" name="Notifications" link="/dashboard/notifications/" />
      </nav>
      <NuxtChild keep-alive />
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  middleware: 'auth',
  head() {
    return {
      title: `Dashboard | ${this.$config.title}`
    };
  }
});
</script>

<style scoped>
.nuxt-link-exact-active {
  @apply bg-gray-100 border-yellow-400 border-b-2 font-bold subpixel-antialiased;
}
</style>
