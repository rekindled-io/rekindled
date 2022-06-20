<template>
  <Nuxt-Link
    :to="link"
    tag="div"
    class="flex items-center justify-center w-full py-3 text-sm text-center text-gray-600 bg-gray-100 border-b-2 border-gray-300 cursor-pointer hover:border-gray-400 focus:outline-none"
  >
    {{ name }}
  </Nuxt-Link>
</template>

<script>
export default {
  props: {
    link: {
      type: String,
      required: true
    },
    name: {
      type: String,
      required: true
    }
  }
};
</script>
