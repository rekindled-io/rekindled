<template>
  <div class="text-center bg-yellow-300 font-semibold py-1 rounded-md text-gray-800">
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
