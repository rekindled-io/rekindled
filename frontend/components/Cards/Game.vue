<template>
  <div class="relative my-4 transition duration-300 ease-in-out transform hover:-translate-y-1">
    <Nuxt-Link :to="`/search?game=${data.name}`">
      <div class="absolute px-2 py-1 mx-1 my-1 font-semibold text-black bg-yellow-300">#{{ index + 1 }}</div>
      <div class="absolute right-0 bottom-7">
        <span class="bg-yellow-300 text-black rounded-l-lg inline-block px-1.5 py-1.5 text-xs font-semibold">
          {{ data.handle_count }} Handles
        </span>
      </div>
      <ImageLoader :image-source="`${$config.baseURL}${data.image}`" image-class="object-cover h-48" />
      <div class="items-center text-center">
        <h2 class="mx-auto overflow-hidden font-bold tracking-tight text-gray-800">
          {{ data.name }}
        </h2>
      </div>
    </Nuxt-Link>
  </div>
</template>

<script lang="ts">
import Vue, { PropType } from 'vue';

import { Game } from '~/modules/game/Game';

export default Vue.extend({
  props: {
    data: {
      type: Object as PropType<Game>,
      required: true
    },
    index: {
      type: Number,
      required: false
    }
  }
});
</script>
