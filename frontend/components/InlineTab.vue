<template>
  <div v-show="active" class="flex flex-col flex-1"><slot /></div>
</template>
<script>
export default {
  name: 'InlineTab',
  props: {
    title: {
      required: true
    },
    selected: {
      type: Boolean,
      default: false
    }
  },

  data() {
    return {
      active: false
    };
  },

  mounted() {
    this.active = this.selected;
  }
};
</script>
