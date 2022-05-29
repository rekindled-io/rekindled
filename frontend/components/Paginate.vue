<template>
  <div class="flex items-center justify-between space-x-4">
    <FormButton
      class="w-10 font-bold bg-yellow-300 rounded-lg h-11"
      :disabled="previous == null"
      text="←"
      v-bind:class="[previous ? 'cursor-pointer' : 'disabled:cursor-not-allowed bg-yellow-100 text-gray-400']"
      @click="switchPage(previous)"
    />
    <span class="text-xs font-semibold" v-if="current_page < last_page">{{ current_page }} of {{ last_page }}</span>
    <FormButton
      class="w-10 font-bold bg-yellow-300 rounded-lg h-11"
      :disabled="next == null"
      text="→"
      v-bind:class="[next ? 'cursor-pointer' : 'disabled:cursor-not-allowed bg-yellow-100 text-gray-400']"
      @click="switchPage(next)"
    />
  </div>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  props: {
    next: {
      type: Number
    },
    previous: {
      type: Number
    },
    current_page: { type: Number },
    last_page: { type: Number }
  },
  methods: {
    switchPage(page: null | string) {
      if (page == null) {
        return;
      }
      this.$router.push({ query: { ...this.$route.query, page: page } });
    }
  }
});
</script>
