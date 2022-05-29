<template>
  <div class="flex flex-col min-h-screen">
    <LazyToast v-if="toast.message" :type="toast.type">{{ toast.message }}</LazyToast>

    <LayoutHeader />
    <div class="flex-grow bg-gray-100">
      <nuxt />
    </div>
    <LayoutFooter />
  </div>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  computed: {
    toast() {
      return this.$store.state.toast;
    }
  },

  watch: {
    $route(to, from) {
      if (to.name != 'search') {
        this.$store.dispatch('filters/clearAll', '');
      }

      this.$store.dispatch('toast/clear');
    }
  }
});
</script>
