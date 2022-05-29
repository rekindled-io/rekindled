<template>
  <div
    class="px-2 py-1 text-xs font-semibold tracking-wide bg-transparent border rounded overflow-hidden whitespace-nowrap"
    :class="klass"
  >
    {{ name }}
  </div>
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
div[class*='platform--'] {
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
