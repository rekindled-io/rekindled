<template>
  <div class="flex flex-col bg-gray-300 rounded-md">
    <div
      class="relative transition duration-500 transform bg-white border-2 border-gray-600 rounded -top-1 -left-1 hover:-translate-y-1"
    >
      <div
        class="h-12 bg-black rounded-t-sm"
        style="background-size: cover; background-repeat: no-repeat; background-position: center"
        :style="{ 'background-image': `url(${$config.baseURL}${data.game_and_platform.cover})` }"
      ></div>

      <div class="px-4 pt-1 pb-4">
        <div class="flex">
          <img
            :src="$config.baseURL + data.game_and_platform.icon"
            class="h-12 bg-white border-4 rounded-full border-gray-50 -mt-7"
          />
        </div>

        <div class="flex justify-between items-center my-0.5">
          <div class="flex space-x-1">
            <Pill :name="data.game_and_platform['game_name']" />
            <Pill :name="data.game_and_platform['platform_abbreviation']" />
          </div>
          <Pill :name="data.region" />
        </div>

        <hr class="my-2" />

        <div class="flex items-center justify-between">
          <div class="z-10 overflow-x-hidden">
            <tippy v-if="data.name.length > 16" :content="data.name" arrow>
              <template #trigger>
                <h3 class="text-lg font-black text-gray-700">
                  {{ data.name | truncate(32) }}
                </h3>
              </template>
            </tippy>
            <div v-else>
              <h3 class="text-lg font-black text-gray-700">
                {{ data.name }}
              </h3>
            </div>
          </div>

          <div class="flex flex-row space-x-2">
            <NuxtLink :to="`/user/${data.user}`" v-if="showProfileLink">
              <Icon
                class="w-6 h-6 p-1 bg-gray-200 rounded-full hover:bg-yellow-300"
                name="user"
                v-tippy="{ theme: 'tooltip' }"
                content="view user's profile"
              />
            </NuxtLink>
            <div @click="showModal(data)" v-if="isAuthenticated">
              <Icon
                class="w-6 h-6 p-1 bg-gray-200 rounded-full hover:bg-yellow-300"
                name="connect"
                v-tippy="{ theme: 'tooltip' }"
                content="connect with handle"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
    <LazyModalsConnect v-if="modalState" :data="selected" @cancel="closeModal" />
  </div>
</template>

<script lang="ts">
import Vue, { PropType } from 'vue';
import { mapGetters } from 'vuex';

import { Handle } from '~/modules/handle/Handle';

export default Vue.extend({
  props: {
    data: {
      type: Object as PropType<Handle>,
      required: true
    },
    showProfileLink: {
      type: Boolean,
      required: false,
      default: false
    }
  },

  data() {
    return {
      selected: {} as Handle,
      modalState: false
    };
  },

  computed: {
    ...mapGetters('auth', ['isAuthenticated'])
  },

  methods: {
    showModal(item: Handle) {
      this.selected = item;
      this.modalState = true;
    },
    closeModal() {
      this.modalState = false;
      this.selected = {} as Handle;
    }
  }
});
</script>
