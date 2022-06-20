<template>
  <div class="relative">
    <div @mouseover="mouseover" @mouseleave="mouseleave">
      <slot name="head" />
    </div>
    <transition
      enter-active-class="duration-100 ease-out"
      enter-class="transform translate-y-2 opacity-0"
      enter-to-class="transform scale-100 -translate-y-0"
      leave-active-class="duration-100 ease-in"
      leave-to-class="transform translate-y-2 opacity-0"
    >
      <div
        v-show="showMenu"
        class="absolute z-10 overflow-hidden bg-gray-100 border-2 border-black rounded right-1/4 w-96"
        @mouseover="mouseover"
        @mouseleave="mouseleave"
      >
        <slot name="body"></slot>
      </div>
    </transition>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  data() {
    return {
      showMenu: false,
      timer: 0
    };
  },

  methods: {
    toggleMenu() {
      this.showMenu = !this.showMenu;
    },

    mouseover() {
      if (this.timer) {
        clearTimeout(this.timer);
      }
      this.showMenu = true;
    },

    mouseleave() {
      this.timer = window.setTimeout(() => {
        this.showMenu = false;
      }, 100);
    }
  }
});
</script>
