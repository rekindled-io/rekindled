<template>
  <div class="bg-yellow-400">
    <div class="max-w-5xl mx-auto py-8 px-4">
      <span class="bg-black text-white text-2xl font-semibold px-2 py-3 rounded">{{ title }}</span>
    </div>
  </div>
</template>

<script lang="ts">
export default {
  props: {
    title: {
      type: String,
      required: true
    }
  }
};
</script>
