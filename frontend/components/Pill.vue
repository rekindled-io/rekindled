<template>
  <span class="px-2 py-1 text-xs font-semibold tracking-wide bg-gray-100 rounded whitespace-nowrap" :class="klass">
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
        'platform--pc': this.name == 'PC',
        'platform--xbox': this.name == 'Xbox Network',
        'platform--steam': this.name == 'Steam',
        'platform--playstation': this.name == 'Playstation Network',
        'platform--nintendo': this.name == 'Nintendo Network'
      };
    }
  }
};
</script>

<style scoped>
span[class*='platform--'] {
  @apply text-gray-100;
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
