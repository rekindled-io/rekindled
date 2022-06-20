<template>
  <Transition name="fade" appear>
    <div class="fixed inset-0 z-[200] flex items-center justify-center bg-opacity-60">
      <div class="fixed inset-0 transition bg-black opacity-40" @click="$emit('cancel')"></div>
      <div class="z-50 flex flex-col w-1/3 mx-auto" @click.stop>
        <div class="flex justify-between items-center p-3 mb-0.5 bg-yellow-400 rounded">
          <span class="px-3 py-2 font-semibold text-white bg-gray-800 rounded">
            {{ title }}
          </span>
          <button type="button" @click="$emit('cancel')">
            <Icon name="close" class="w-8 h-8 p-2 text-white bg-gray-800 rounded" />
          </button>
        </div>
        <div class="flex flex-col px-6 py-4 rounded bg-gray-50">
          <div class="w-full mb-5">
            <slot name="body" />
          </div>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  props: {
    title: {
      type: String,
      required: true
    }
  },

  methods: {
    close() {
      this.$emit('close');
    }
  }
});
</script>
