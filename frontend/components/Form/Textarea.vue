<template>
  <div>
    <label v-if="label" class="block text-sm font-bold text-gray-500" :for="label">{{ label }}</label>
    <textarea
      class="w-full px-3 py-2 text-sm font-semibold text-gray-900 placeholder-gray-500 transition duration-200 ease-in-out bg-gray-100 border-2 border-gray-100 rounded-md focus:outline-none focus:ring-yellow-400 focus:border-yellow-400 focus:bg-white"
      v-model="innerValue"
      :placeholder="placeholder"
      :maxlength="maxlength"
    ></textarea>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  props: {
    value: {
      type: String
    },
    label: {
      type: String,
      required: false
    },
    placeholder: {
      type: String,
      required: false
    },
    maxlength: {
      type: Number,
      required: true
    }
  },

  data() {
    return {
      innerValue: ''
    };
  },

  watch: {
    innerValue(value: string) {
      this.$emit('input', value);
    }
  },

  created() {
    if (this.value) {
      this.innerValue = this.value;
    }
  }
});
</script>
