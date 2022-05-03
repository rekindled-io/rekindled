<template>
  <component :is="src" />
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  props: {
    name: {
      type: String,
      required: true
    }
  },
  computed: {
    src() {
      try {
        return require(`~/assets/icons/${this.name}.svg?inline`);
      } catch {
        console.log('File not found.');
      }
    }
  }
});
</script>
