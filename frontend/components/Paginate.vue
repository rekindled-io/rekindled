<template>
  <div class="flex justify-between items-center">
    <button
      class="h-11 w-10 rounded-lg font-bold bg-yellow-300"
      :disabled="previous == null"
      v-bind:class="[previous ? 'cursor-pointer' : 'disabled:cursor-not-allowed bg-yellow-100 text-gray-400']"
      @click="switchPage(previous)"
    >
      ←
    </button>
    <span class="text-sm" v-if="current_page < last_page">Pg. {{ current_page }} of {{ last_page }}</span>
    <button
      class="h-11 w-10 rounded-lg font-bold bg-yellow-300"
      :disabled="next == null"
      v-bind:class="[next ? 'cursor-pointer' : 'disabled:cursor-not-allowed bg-yellow-100 text-gray-400']"
      @click="switchPage(next)"
    >
      →
    </button>
  </div>
</template>

<script>
export default {
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
    switchPage(page) {
      if (page == null) {
        return;
      }
      this.$router.push({ query: { ...this.$route.query, page: page } });
    }
  }
};
</script>
