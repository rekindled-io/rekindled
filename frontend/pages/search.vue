<template>
  <div>
    <Heading content="Search" />
    <div class="justify-center w-3/5 mx-auto mt-12">
      <div class="flex space-x-4">
        <div class="sticky bottom-0 w-1/4">
          <SearchOptions />
        </div>
        <div class="w-3/4 px-4">
          <Loading v-if="$fetchState.pending" />
          <div v-else-if="$fetchState.error" class="w-1/2 mx-auto text-2xl text-center">
            Uh oh! Something went wrong.
          </div>
          <div v-else>
            <div v-if="handles.results">
              <Message :text="handles.count + ` handle/s found`" />
              <div class="grid grid-cols-1 gap-12 my-8 sm:grid-cols-2 lg:grid-cols-2">
                <CardsHandle v-for="handle in handles.results" :data="handle" :key="handle.id" showUserLink />
              </div>
              <div v-if="handles.count" class="w-1/3 mx-auto space-x-4">
                <Paginate
                  :current_page="handles.current_page"
                  :last_page="handles.last_page"
                  :next="handles.next"
                  :previous="handles.previous"
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import { buildURLQuery } from '@/utils/filters';

export default Vue.extend({
  data() {
    return {
      handles: {}
    };
  },

  computed: {
    query() {
      return buildURLQuery({
        name: this.$route.query.name || '',
        game: this.$route.query.game || '',
        platform: this.$route.query.platform || '',
        page: this.$route.query.page || 1,
        includeSelf: false
      });
    }
  },

  async fetch() {
    this.handles = await this.$services.handle.list(this.query);
  },

  watch: {
    '$route.query': '$fetch'
  }
});
</script>
