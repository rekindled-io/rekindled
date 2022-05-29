<template>
  <transition
    enter-class="translate-y-full opacity-0"
    enter-to-class="opacity-100 -translate-x-0"
    leave-class="opacity-0 -translate-x-0"
    leave-to-class="translate-y-full opacity-0"
  >
    <div
      v-if="show"
      class="fixed z-[100] items-center p-4 w-full max-w-xs text-gray-500 bg-white border-b-2 border-r-2 top-40 right-10 border-gray-200 rounded transform transition-all"
    >
      <div class="flex mb-3">
        <span class="text-sm font-semibold text-gray-900">Login failed</span>
      </div>
      <div class="flex items-center">
        <div
          class="inline-flex items-center justify-center flex-shrink-0 w-8 h-8 text-red-500 bg-red-100 rounded-lg dark:bg-red-800 dark:text-red-200"
        >
          <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <path
              fill-rule="evenodd"
              d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
              clip-rule="evenodd"
            ></path>
          </svg>
        </div>
        <div class="ml-3 text-sm font-normal">
          <h4 class="text-smtext-gray-900 dark:text-white"><slot></slot></h4>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  props: {
    message: {
      type: String,
      required: false
    },
    type: {
      type: String,
      required: true
    }
  },

  data() {
    return {
      show: true
    };
  },

  methods: {
    hide() {
      this.show = false;
      this.$store.dispatch('toast/clear');
    }
  },

  created() {
    setTimeout(this.hide, 3000);
  }
};
</script>
