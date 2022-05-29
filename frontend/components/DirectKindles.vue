<template>
  <div>
    <div class="flex mx-4 mt-4 space-x-4">
      <label class="relative">
        <Icon class="absolute w-4 h-4 pointer-events-none left-2 top-2" name="search" />
        <input v-model="search.name" @keyup.enter="$fetch" class="search" type="text" placeholder="Search..." />
      </label>
    </div>
    <div v-if="$fetchState.pending">
      <Loading />
    </div>
    <div class="flex justify-center p-4 my-4" v-else-if="!this.kindles.count">
      <span class="text-xl font-semibold">No kindles found!</span>
    </div>
    <div v-else>
      <Datatable :data="kindles.results" :keys="kindles.results[0].dataTableKeys()" :total="kindles.count" />
    </div>

    <ModalsKindle v-if="modalHandleStatus" @cancel="modalHandleStatus = false" />
    <ModalsAction
      v-if="deleteModal"
      @action="deleteResource"
      @cancel="deleteModal = false"
      message="Are you sure you want to delete handle? This can't be undone."
    />
  </div>
</template>

<script>
import Vue from 'vue';

export default Vue.extend({
  data() {
    return {
      data: [],
      deleteModal: false,
      selectedItem: null,
      modalHandleStatus: false,
      kindles: [],
      search: {
        name: '',
        platform: '',
        game: ''
      }
    };
  },

  methods: {
    openModal() {
      this.modalHandleStatus = true;
    },
    closeMethod() {
      this.deleteModal = false;
    },
    deletePrompt(item) {
      this.selectedItem = item;
      this.deleteModal = true;
    },
    setActive(menuItem) {
      this.activeItem = menuItem;
    },
    async deleteResource() {
      try {
        await this.$axios.delete(`/kindles/${this.selectedItem}/`);
        this.closeMethod();
        this.deleteModal = false;
        this.selectedItem = '';
        this.$fetch();
      } catch (e) {}
    }
  },

  async fetch() {
    this.kindles = await this.$services.directKindle.list();
  }
});
</script>
