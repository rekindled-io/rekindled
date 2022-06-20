<template>
  <MenusBase>
    <template #head>
      <div class="hover:cursor-pointer">
        <Gravatar class="w-8 h-8 rounded-lg" :email="user.hashed_email" :size="80" type="number" />
      </div>
    </template>
    <template #body>
      <Nuxt-Link to="/user/admin" class="user-menu-item">
        My Profile <span class="text-gray-500">(@{{ user.username }})</span>
      </Nuxt-Link>
      <Nuxt-Link to="/dashboard" class="user-menu-item">Dashboard</Nuxt-Link>
      <Nuxt-Link to="/settings" class="user-menu-item"> Settings</Nuxt-Link>
      <div class="w-full border-t border-gray-300"></div>
      <div @click="logout" class="user-menu-item hover:cursor-pointer">Logout</div>
    </template>
  </MenusBase>
</template>

<script lang="ts">
import Vue from 'vue';
import { mapGetters } from 'vuex';

export default Vue.extend({
  computed: {
    ...mapGetters('auth', ['isAuthenticated', 'userInfo'])
  },

  data() {
    return {
      user: JSON.parse(localStorage.getItem('user') || '')
    };
  },

  methods: {
    async logout() {
      await this.$store.dispatch('auth/logout');
      this.$router.push('/');
    }
  }
});
</script>

<style>
.user-menu-item {
  @apply block px-4 py-3 text-sm text-gray-700 hover:text-gray-900 hover:bg-yellow-300;
}
</style>
