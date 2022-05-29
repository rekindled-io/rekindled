<template>
  <div>
    <div class="flex flex-1">
      <div class="flex justify-between flex-1 space-y-4">
        <div class="flex">
          <div
            v-for="(tab, index) in tabs"
            :key="`tab-${index}`"
            class="p-4 text-sm font-bold text-gray-500"
            :class="[{ 'border-b-4 border-yellow-400 text-black': tab.active }]"
            role="button"
            @click="selectTab(index)"
          >
            <span>{{ tab.title }}</span>
          </div>
        </div>
      </div>
    </div>
    <div class="w-full h-full contents">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'InlineTabs',
  data() {
    return {
      tabs: []
    };
  },

  mounted() {
    this.tabs = this.$children.filter((child) => child.$options.name === 'InlineTab');
  },

  methods: {
    selectTab(i) {
      this.tabs.forEach((tab, index) => {
        tab.active = index === i;
      });
    }
  }
};
</script>
