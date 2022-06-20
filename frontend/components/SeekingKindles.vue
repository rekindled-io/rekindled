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
    <ModalsSeekingKindle v-if="modalHandleStatus" @cancel="modalHandleStatus = false" />
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
    }
  },

  async fetch() {
    this.kindles = await this.$axios.$get(`/kindles/seeking/`);
  }
};
</script>
