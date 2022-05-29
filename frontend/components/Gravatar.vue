<template>
  <img :src="gravatar_url" />
</template>

<script lang="ts">
import Vue from 'vue';
export default Vue.extend({
  props: {
    email: {
      type: String,
      required: true
    },
    size: {
      type: Number,
      required: false,
      default: 80
    }
  },

  computed: {
    gravatar_url() {
      const hash = this.email.trim().toLowerCase();
      return `https://www.gravatar.com/avatar/${hash}?s=${this.size}&d=retro`;
    }
  }
});
</script>
