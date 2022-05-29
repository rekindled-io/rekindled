<template>
  <Nuxt-Link
    :to="link"
    tag="div"
    class="w-full text-center text-gray-600 bg-gray-100 py-3 block text-sm hover:border-gray-400 focus:outline-none border-b-2 border-gray-300 cursor-pointer"
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
