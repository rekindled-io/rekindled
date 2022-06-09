<template>
  <span
    class="px-1.5 py-0.5 overflow-hidden text-xs font-semibold tracking-wide bg-transparent border rounded whitespace-nowrap inline-flex"
    :class="klass"
  >
    {{ name }}
  </span>
</template>
<script>
export default {
  props: {
    name: {
      required: true
    }
  },

  computed: {
    klass() {
      return {
        'platform--pc': ['PC'].includes(this.name),
        'platform--xbox': ['Xbox Network', 'XBL'].includes(this.name),
        'platform--steam': ['Steam', 'ST'].includes(this.name),
        'platform--playstation': ['Playstation Network', 'PSN'].includes(this.name),
        'platform--nintendo': ['Nintendo Network', 'NN'].includes(this.name)
      };
    }
  }
};
</script>

<style scoped>
span[class*='platform--'] {
  @apply text-gray-100 border-none;
}
.platform--pc {
  @apply bg-black;
}
.platform--xbox {
  @apply bg-green-500;
}
.platform--steam {
  @apply bg-gray-500;
}
.platform--playstation {
  @apply bg-blue-500;
}
.platform--nintendo {
  @apply bg-red-500;
}
</style>
