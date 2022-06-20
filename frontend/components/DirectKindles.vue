<template>
  <div>
    <div class="flex mx-4 mt-4 space-x-4">
      <label class="relative">
        <Icon class="absolute w-4 h-4 pointer-events-none left-2 top-2" name="search" />
        <input v-model="search.name" @keyup.enter="$fetch" class="search" type="text" placeholder="Search..." />
      </label>
    </div>

    <Loading v-if="$fetchState.pending" />

    <div class="flex justify-center p-4 my-4" v-else-if="!this.kindles.count">
      <span class="text-xl font-semibold">No kindles found!</span>
    </div>

    <div class="mt-4" v-else>
      <Datatable :data="kindles.results" :keys="kindles.results[0].dataTableKeys()" :total="kindles.count" />
    </div>
  </div>
</template>

<script>
import Vue from 'vue';

export default Vue.extend({
  data() {
    return {
      kindles: [],
      search: {
        name: ''
      }
    };
  },

  async fetch() {
    this.kindles = await this.$services.directKindle.list();
  }
});
</script>
