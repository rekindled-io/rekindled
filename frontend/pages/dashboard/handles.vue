<template>
  <div>
    <div class="flex mx-4 mt-4 space-x-4">
      <label class="relative">
        <Icon class="absolute w-4 h-4 pointer-events-none left-2 top-2" name="search" />
        <input v-model="search.name" @keyup.enter="$fetch" class="search" type="text" placeholder="Search..." />
      </label>
      <button @click="openModal" type="button" class="primary-button">+ New</button>
    </div>

    <Loading v-if="$fetchState.pending" />

    <div v-else-if="!this.handles.count" class="py-2 mx-auto mb-4 font-semibold text-center">
      <span class="text-xl font-semibold">No handles found.</span>
    </div>

    <div class="mt-4" v-else>
      <Datatable :data="handles.results" :keys="handles.results[0].dataTableKeys()" :total="handles.count">
        <template #name="{ item }">
          <span class="text-lg font-bold text-gray-600">
            {{ item }}
          </span>
        </template>
        <template #game="{ item }">
          <div class="flex">
            <Pill :name="item" />
          </div>
        </template>
        <template #platform="{ item }">
          <div class="flex">
            <Pill :name="item" />
          </div>
        </template>
        <template #region="{ item }">
          <div class="flex">
            <Pill :name="item" />
          </div>
        </template>
      </Datatable>

      <div class="w-1/4 py-4 mx-auto">
        <Paginate
          :next="this.handles.next"
          :previous="this.handles.previous"
          :current_page="this.handles.current_page"
          :last_page="this.handles.last_page"
        />
      </div>
    </div>
    <LazyModalsHandle v-if="modalHandleStatus" @cancel="modalHandleStatus = false" @save="$fetch" />
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import { buildURLQuery } from '@/utils/filters';
import { HandleList } from '~/modules/handle/Handle';

export default Vue.extend({
  data() {
    return {
      modalHandleStatus: false,
      handles: {} as HandleList,
      search: {
        name: '',
        platform: '',
        game: '',
        ordering: 'created'
      },
      user: JSON.parse(localStorage.getItem('user') || '')?.username
    };
  },

  computed: {
    page() {
      return this.$route.query.page || 1;
    },
    query(): string {
      return buildURLQuery({
        name: this.search.name || '',
        page: this.page,
        ordering: this.search.ordering,
        includeSelf: true,
        user: JSON.parse(localStorage.getItem('user') || '')?.username
      });
    }
  },

  methods: {
    openModal() {
      this.modalHandleStatus = true;
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
