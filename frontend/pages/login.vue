<template>
  <div>
    <Heading content="Login" />
    <div class="flex items-center justify-center mt-8">
      <div class="auth-form-box">
        <div class="flex items-center justify-center mb-4 text-sm font-semibold text-gray-600">Welcome back!</div>
        <ValidationObserver ref="form" v-slot="{ handleSubmit, passed }">
          <form class="space-y-8" @submit.prevent="handleSubmit(login)">
            <FormInput
              v-model="username"
              rules="required"
              label="Username"
              name="username"
              vid="detail"
              required
              hover
            />
            <FormInput
              v-model="password"
              rules="required"
              label="Password"
              name="password"
              type="password"
              vid="detail"
              required
              hover
            />
            <FormButton text="Login" :disabled="!passed" :loading="loading" />
          </form>
        </ValidationObserver>
        <hr class="my-4" />
        <p class="flex justify-end space-x-1 text-xs text-gray-400">
          <NuxtLink class="font-semibold hover:underline hover:text-yellow-500" to="reset-password">
            Forgot your password?
          </NuxtLink>
          <span>|</span>
          <NuxtLink class="font-semibold hover:underline hover:text-yellow-500" to="register">Sign up</NuxtLink>
        </p>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import { mapGetters } from 'vuex';

import { VeeValidate } from '~/types';

export default Vue.extend({
  middleware({ store, redirect }) {
    const isLoggedIn = store.getters['auth/isAuthenticated'];
    if (isLoggedIn) {
      return redirect('/');
    }
  },

  data() {
    return {
      username: '',
      password: '',
      loading: false
    };
  },

  computed: {
    ...mapGetters('auth', ['isAuthenticated']),
    form(): VeeValidate {
      return this.$refs.form as VeeValidate;
    }
  },

  methods: {
    async login() {
      const { dispatch } = this.$store;

      try {
        this.loading = true;
        await this.$store.dispatch('auth/login', {
          username: this.username,
          password: this.password
        });

        const response = await this.$axios.get('/users/me/');

        localStorage.setItem('user', JSON.stringify(response.data));
        this.$router.push('/dashboard/');
      } catch (error: any) {
        dispatch('toast/error', error.response.data.detail);
      } finally {
        this.loading = false;
      }
    }
  }
});
</script>
