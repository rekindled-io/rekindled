<template>
  <div class="flex flex-col rounded-md bg-gray-300">
    <div class="border-2 border-gray-600 bg-white relative -top-1 -left-1 rounded">
      <div
        class="h-12 rounded-t-sm bg-black"
        style="background-size: cover; background-repeat: no-repeat; background-position: center"
        :style="{ 'background-image': `url(${$config.baseURL}${data.game_and_platform.cover})` }"
      ></div>
      <div class="px-4 pb-4 pt-1">
        <div class="flex">
          <img
            :src="$config.baseURL + data.game_and_platform.icon"
            class="h-12 bg-white rounded-full border-4 border-gray-100 -mt-7"
          />
        </div>
        <div class="flex justify-between items-center my-0.5">
          <div class="space-x-1">
            <Pill :name="data.game_and_platform['game_name']" />
            <Pill :name="data.game_and_platform['platform_name']" />
          </div>
          <div>
            <Pill :name="data.region" />
          </div>
        </div>
        <hr class="my-2" />
        <div class="flex items-center justify-between">
          <div class="z-10 overflow-hidden">
            <tippy v-if="data.name.length > 16" :content="data.name" arrow>
              <template #trigger>
                <h3 class="text-gray-700 text-lg font-black text-gray-800">
                  {{ data.name | truncate(32) }}
                </h3>
              </template>
            </tippy>
            <div v-else>
              <h3 class="text-gray-700 text-lg font-black text-gray-800">
                {{ data.name }}
              </h3>
            </div>
          </div>
          <div class="flex flex-row space-x-2">
            <NuxtLink :to="`/user/${data.user}`">
              <Icon
                class="w-6 h-6 p-1 rounded-full bg-gray-200 hover:bg-yellow-300"
                name="user"
                v-tippy="{ theme: 'tooltip' }"
                content="view user's profile"
              />
            </NuxtLink>
            <div class="rounded-full bg-gray-200">
              <a @click="showModal(handle)">
                <Icon
                  class="w-6 h-6 p-1 rounded-full hover:bg-yellow-300"
                  name="connect"
                  v-tippy="{ theme: 'tooltip' }"
                  content="connect with handle"
                />
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
    <ModalsConnect
      v-if="modalKindleStatus"
      :data="selectedItem"
      :open="modalKindleStatus"
      @cancel="modalKindleStatus = false"
    />
  </div>
</template>

<script lang="ts">
import { mapGetters } from 'vuex';

import Vue from 'vue';

export default Vue.extend({
  props: {
    data: {
      type: Object,
      required: true
    }
  },
  computed: {
    ...mapGetters('auth', ['isAuthenticated'])
  },
  data() {
    return {
      selectedItem: null,
      modalKindleStatus: false
    };
  },
  methods: {
    showModal(item: any) {
      this.selectedItem = item;
      this.modalKindleStatus = true;
    }
  }
});
</script>
