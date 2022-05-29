<template>
  <button
    type="submit"
    class="flex items-center justify-center w-full leading-6 primary-button min-h-max"
    :disabled="disableButton"
    :class="[!disableButton ? 'cursor-pointer' : 'button-disabled']"
  >
    <Icon v-if="loading" name="spinner" class="w-6 h-6 text-yellow-400 animate-spin" />
    <span v-else>{{ text }}</span>
  </button>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  props: {
    text: {
      type: String,
      required: false,
      default: 'Submit'
    },
    loading: {
      required: false,
      default: false
    },
    disabled: {
      required: false,
      default: true
    },
    icon: {
      default: ''
    }
  },

  computed: {
    disableButton() {
      return this.disabled || this.loading;
    }
  }
});
</script>
