<template>
  <ValidationProvider v-slot="{ errors, classes }" tag="div" slim :rules="rules" :vid="vid">
    <div class="relative">
      <Icon v-if="icon" class="absolute inset-y-0 w-6 h-6 pointer-events-none" :name="icon" />
      <label
        class="text-sm font-semibold pointer-events-none"
        :for="name"
        :class="{
          'text-gray-400': !errors[0],
          'text-red-600': errors[0],
          'pl-6': icon
        }"
      >
        {{ label }}
      </label>
      <input
        v-model="innerValue"
        :name="name"
        :type="type"
        :label="label"
        :required="required"
        class="w-full text-gray-800 bg-transparent border-b-2 px-1 py-0.5 font-bold text-sm outline-none"
        :class="{
          'border-red-600 placeholder-red-600': errors[0],
          'has-value': hasValue,
          'focus:border-yellow-400': hover,
          // Probably should convert below to calculated offset value
          'pl-7': icon
        }"
      />
      <span v-if="errors[0]" class="absolute block text-xs text-red-600" :class="classes">{{ errors[0] }}</span>
    </div>
  </ValidationProvider>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  props: {
    required: {
      type: Boolean,
      default: false
    },
    rules: {
      type: [Object, String]
    },
    label: {
      type: String,
      default: ''
    },
    placeholder: {
      type: String,
      default: ''
    },
    name: {
      type: String,
      default: ''
    },
    type: {
      type: String,
      default: 'text',
      validator(value) {
        return ['url', 'text', 'password', 'tel', 'search', 'number', 'email'].includes(value);
      }
    },
    vid: {
      type: String,
      default: undefined
    },
    value: {
      type: String,
      default: ''
    },
    hover: {
      type: Boolean,
      default: false
    },
    borderColor: {
      type: String,
      default: 'border-gray-800'
    },
    icon: {
      type: String,
      default: ''
    }
  },

  data: () => ({
    innerValue: ''
  }),

  computed: {
    hasValue() {
      return !!this.innerValue;
    },
    borderCSS() {
      return {
        'border-black': this.borderColor
      };
    }
  },

  watch: {
    innerValue(value) {
      this.$emit('input', value);
    }
  }
});
</script>
