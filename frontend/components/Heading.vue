<template>
  <div class="bg-yellow-300 shadow-xl">
    <div class="max-w-5xl px-4 mx-auto py-7">
      <span class="bg-black text-white text-2xl font-semibold px-2 py-1.5 rounded">{{ content }}</span>
    </div>
  </div>
</template>

<script lang="ts">
export default {
  props: {
    content: {
      type: String,
      required: true
    }
  }
};
</script>
