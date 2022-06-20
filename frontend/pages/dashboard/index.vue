<template>
  <div class="p-4">
    Recently created

    <Loading v-if="$fetchState.pending" />
    <div v-else class="w-1/3">
      <div v-for="handle in handles" :key="handle.id">
        <div>
          <span class="font-semibold">{{ handle.name }}</span> - {{ handle.timestamp }}
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import { Handle } from '~/modules/handle/Handle';
import { buildURLQuery } from '~/utils/filters';

export default Vue.extend({
  data() {
    return {
      handles: [] as Handle[],
      stats: []
    };
  },

  computed: {
    query() {
      return buildURLQuery({
        includeSelf: true
      });
    }
  },

  async fetch() {
    this.handles = await this.$services.handle.recent('user=admin&includeSelf=true');
    console.log(this.handles);
    this.stats = await this.$services.handle.stats('user=admin&includeSelf=true');
  }
});
</script>
