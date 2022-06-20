<template>
  <div class="w-full px-4 py-1 text-sm font-semibold text-center bg-yellow-300 rounded-md">
    {{ text }}
  </div>
</template>

<script>
export default {
  props: {
    text: {
      required: true,
      type: String
    }
  }
};
</script>
