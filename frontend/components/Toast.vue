<template>
  <transition leave-class="opacity-0 -translate-x-0" leave-to-class="translate-y-full opacity-0">
    <div
      v-if="show"
      class="fixed z-[300] items-center p-4 w-full max-w-xs text-gray-500 bg-white top-40 right-10 border-gray-300 rounded transform transition-all space-y-2 shadow"
    >
      <div v-if="title" class="flex">
        <span class="text-sm font-semibold text-gray-900">{{ title }}</span>
      </div>
      <div class="flex items-center space-x-2">
        <div class="inline-flex items-center justify-center flex-shrink-0 w-6 h-6 rounded" :class="`toast--${type}`">
          <Icon :name="iconName" />
        </div>
        <div class="text-sm">
          <span class="text-gray-900"><slot></slot></span>
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
    },
    title: {
      type: String,
      required: false
    }
  },

  data() {
    return {
      show: true
    };
  },

  computed: {
    iconName() {
      return this.type == 'success' ? 'tick' : 'close';
    }
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

<style lang="scss" scoped>
.toast {
  &--success {
    @apply bg-green-200;
    @apply text-green-600;
  }
  &--error {
    @apply bg-red-100;
    @apply text-red-600;
  }
}
</style>
