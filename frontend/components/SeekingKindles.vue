<template>
  <div>
    <div class="flex mx-4 mt-4 space-x-4">
      <label class="relative">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          class="absolute w-4 h-4 pointer-events-none left-2 top-2"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
          ></path>
        </svg>
        <input v-model="search.name" @keyup.enter="$fetch" class="search" type="text" placeholder="Search..." />
      </label>
      <button @click="openModal" type="button" class="primary-button">+ New</button>
    </div>
    <div v-if="$fetchState.pending">
      <Loading />
    </div>
    <div class="flex justify-center p-4 my-4" v-else-if="!this.kindles.count">
      <span class="text-xl font-semibold">No kindles found!</span>
    </div>
    <table v-else class="w-full mt-5 table-fixed">
      <thead class="text-xs font-medium text-gray-600 uppercase bg-gray-100 border-t-2 border-b-2">
        <tr>
          <th class="w-12 text-center">#</th>
          <th class="w-1/3 py-4 text-left">Name/Game</th>
          <th class="w-1/4 py-4 text-left">Platform</th>
          <th class="w-1/4 py-4 text-left">Play Period</th>
          <th class="w-1/4 py-4 text-left">Region</th>
          <th class="w-1/4 py-4 text-center">Actions</th>
        </tr>
      </thead>
      <tbody class="text-sm font-normal text-gray-700">
        <tr
          v-for="(kindle, index) in kindles.results"
          :key="`${kindle.id}`"
          :class="[index + 1 != kindle.length ? 'border-b' : '']"
          class="hover:bg-gray-100"
        >
          <td class="w-8 py-6 font-semibold text-center">{{ kindles.results.length - index }}</td>
          <td class="w-1/3">
            <div class="flex align-items-center">
              <div class="ml-3">
                <div class="text-lg font-bold text-gray-600">
                  {{ kindle.source_handle }}
                </div>
                <div class="text-gray-500">{{ kindle.handle }}</div>
              </div>
            </div>
          </td>
          <td>
            <Pill :name="kindle.on_platform" />
          </td>
          <td>2008 - 2009</td>
          <td>Europe</td>
          <td class="text-center">
            <a
              disabled
              href="#"
              class="w-1/2 px-3 py-2 ml-2 text-base text-gray-800 rounded cursor-pointer hover:bg-gray-200"
            >
              edit
            </a>
            <a
              class="px-3 py-2 ml-2 text-base text-red-500 rounded cursor-pointer hover:bg-gray-200"
              @click="deletePrompt(kindle.id)"
            >
              delete
            </a>
          </td>
        </tr>
      </tbody>
    </table>
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
export default {
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
      await this.$axios.delete(`/kindles/${this.selectedItem}/`);
      this.closeMethod();
      this.deleteModal = false;
      this.selectedItem = '';
      this.$fetch();
    }
  },
  async fetch() {
    this.kindles = await this.$axios.$get(`/kindles/seeking/`);
  }
};
</script>
