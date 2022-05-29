<template>
  <nav class="top-0 w-full z-50 bg-[#061028]">
    <div class="max-w-6xl py-4 mx-auto">
      <div class="flex items-center justify-between">
        <div class="flex flex-col items-center font-semibold">
          <Logo />
        </div>
        <div class="relative w-1/3 rounded-sm">
          <form @submit.prevent="search">
            <input
              v-model="handleFilter"
              label="Search"
              placeholder="Search..."
              class="w-1/3 h-10 p-2 duration-500 ease-in-out bg-gray-700 rounded-lg appearance-none text-gray-50 focus:outline-none font-lg transition-width focus:text-black focus:bg-gray-100 focus:w-full focus:border-0"
            />
          </form>
        </div>
        <div class="flex items-center ml-4 md:ml-6">
          <div class="flex items-center space-x-4" v-if="isAuthenticated">
            <MenusNotification />
            <MenusUser />
          </div>
          <div class="space-x-2" v-else>
            <Nuxt-Link
              tag="button"
              to="/login"
              type="button"
              class="bg-transparent border border-gray-200 text-gray-200 font-semibold text-sm rounded px-4 py-1.5 transform hover:-translate-y-0.5 transition duration-200"
            >
              Login
            </Nuxt-Link>
            <Nuxt-Link
              tag="button"
              to="/register"
              type="button"
              class="bg-yellow-400 font-semibold text-sm rounded px-4 py-1.5 text-black transform hover:-translate-y-0.5 transition duration-200"
              >Register
            </Nuxt-Link>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script lang="ts">
import Vue from 'vue';

import { mapGetters } from 'vuex';

export default Vue.extend({
  computed: {
    ...mapGetters('auth', ['isAuthenticated']),
    handleFilter: {
      get(): string {
        return this.$store.state.filters.name;
      },
      set(handle: string): void {
        this.$store.commit('filters/SET_HANDLE', handle);
      }
    }
  },

  methods: {
    async logout() {
      await this.$store.dispatch('auth/logout');
      this.$router.push('/');
    },
    search() {
      this.$router.push({
        path: '/search',
        query: {
          name: this.handleFilter
        }
      });
    }
  },

  created() {
    const name = this.$router.currentRoute.query.name as string;
    this.handleFilter = name || '';
  }
});
</script>
