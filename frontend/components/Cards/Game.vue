<template>
  <div
    class="relative my-4 transform hover:-translate-y-1 transition duration-300 ease-in-out"
  >
    <Nuxt-Link :to="`/search?game=${data.name}`">
      <div
        class="absolute mx-1 my-1 bg-yellow-300 text-black py-1 px-2 font-semibold"
      >
        #{{ index + 1 }}
      </div>
      <div class="absolute bottom-0 right-0 bottom-7">
        <span
          class="bg-yellow-300 text-black rounded-l-lg inline-block px-1.5 py-1.5 text-xs font-semibold"
          >{{ data.handle_count }} Handles</span
        >
      </div>
      <ImageLoader
        :image-source="`${$config.baseURL}${data.image}`"
        image-class="object-cover h-48"
      />
      <div class="items-center text-center">
        <h2
          class="font-bold tracking-tight text-gray-800 mx-auto overflow-hidden"
        >
          {{ data.name }}
        </h2>
      </div>
    </Nuxt-Link>
  </div>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  props: {
    data: {
      type: Object,
      required: true,
    },
    index: {
      type: Number,
      required: false,
    },
  },
});
</script>
