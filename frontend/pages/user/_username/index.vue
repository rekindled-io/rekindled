<template>
  <div>
    <div class="justify-center w-full p-4 py-5 bg-yellow-300 shadow-xl">
      <div class="relative flex items-center max-w-6xl mx-auto">
        <Gravatar class="object-cover w-16 h-16 rounded-full" :email="user.hashed_email" :size="80" />
        <div class="ml-4">
          <div class="flex my-1">
            <span class="px-2 py-1.5 text-2xl font-semibold text-white bg-black rounded">
              {{ user.username }}
            </span>
          </div>
          <div class="flex my-1">
            <span class="px-2 py-1 text-xs text-gray-800 bg-white rounded">
              <span class="font-semibold">Last online</span>
              <span v-if="user.last_login">{{ user.last_login | formatDate }}</span>
              <span v-else>Never</span>
            </span>
          </div>
        </div>
      </div>
    </div>
    <div class="justify-center w-3/5 mx-auto mt-12">
      <div class="flex space-x-4">
        <div class="w-1/4">
          <div class="mb-0.5">
            <span class="text-xl font-semibold">About</span>
            <p>
              <span class="text-sm" v-if="user.profile.bio">
                {{ user.profile.bio }}
              </span>
              <span class="text-sm italic" v-else>{{ user.username }} hasn't written anything about themself.</span>
            </p>
          </div>
          <div class="mb-0.5">
            <span class="text-xl font-semibold">IDs</span>
            <div class="flex flex-col">
              <div v-if="user.hasDiscord()">
                <label class="text-xs text-gray-600" for="discord">Discord</label>
                <input
                  class="text-sm bg-transparent rounded bg-gray-100 text-gray-500 px-1 py-0.5 focus:outline-none"
                  name="discord"
                  type="text"
                  :value="user.discordUser()"
                  readonly
                />
              </div>
              <div>
                <label class="text-xs text-gray-600" for="steam">Steam</label>
                <input
                  class="text-sm bg-transparent rounded bg-gray-100 text-gray-500 px-1 py-0.5 focus:outline-none"
                  name="steam"
                  type="text"
                  value="2348234"
                  readonly
                />
              </div>
            </div>
          </div>
          <div class="mb-0.5">
            <span class="text-xl font-semibold">Links</span>
            <p class="flex space-x-2">
              <a :href="this.user.discordLink()" target="_blank">
                <Icon class="w-5 h-5" name="discord" />
              </a>
              <a :href="this.user.steamLink()" target="_blank">
                <Icon class="w-5 h-5" name="steam" />
              </a>
            </p>
          </div>
        </div>
        <Loading v-if="$fetchState.pending" />
        <div v-else-if="$fetchState.error" class="w-1/2 mx-auto text-2xl text-center">Uh oh! Something went wrong.</div>
        <div class="w-full" v-else-if="!handles.count">
          <Message text="User has not created any handles yet." />
        </div>
        <div class="w-full" v-else>
          <div v-if="handles.results">
            <div class="grid grid-cols-3 gap-4 my-8">
              <CardsHandle v-for="handle in handles.results" :data="handle" :key="handle.id" />
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
</template>

<script lang="ts">
import Vue from 'vue';
import { HandleList } from '~/modules/handle/Handle';
import { buildURLQuery } from '~/utils/filters';

export default Vue.extend({
  async asyncData({ $services, error, params }) {
    try {
      const user = await $services.user.retrieve(params.username);
      return { user };
    } catch (e) {
      error({ statusCode: 404, message: e as string });
    }
  },

  data() {
    return {
      handles: {} as HandleList
    };
  },

  computed: {
    page() {
      return this.$route.query.page || 1;
    },
    query(): string {
      return buildURLQuery({
        includeSelf: true,
        user: this.$route.params.username
      });
    }
  },

  async fetch() {
    this.handles = await this.$services.handle.list(this.query);
  }
});
</script>
