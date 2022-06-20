<template>
  <div>
    <Heading content="Register" />
    <div class="flex items-center justify-center mt-8">
      <div class="auth-form-box">
        <div class="flex items-center justify-center mb-4 font-semibold text-gray-600">
          Create an account and get started!
        </div>

        <div v-if="isAuthenticated">You are already registered ;)</div>

        <div v-else>
          <ValidationObserver ref="form" v-slot="{ invalid, handleSubmit }">
            <form class="space-y-8" @submit.prevent="handleSubmit(register)">
              <FormInput
                v-model="username"
                rules="required|alpha_num|minmax:3,32"
                label="Username"
                name="username"
                vid="username"
                required
                hover
              />

              <FormInput v-model="email" rules="required|email" label="Email" name="email" vid="email" required hover />

              <FormInput
                v-model="password"
                rules="required|minmax:8,128"
                label="Password"
                name="password"
                type="password"
                vid="password"
                required
                hover
              />

              <FormInput
                v-model="password_confirm"
                rules="required|confirmed:password"
                label="Confirm password"
                name="confirm password"
                type="password"
                required
                hover
              />

              <Recaptcha />

              <FormButton text="Register" :disabled="invalid" :loading="loading" />
            </form>
          </ValidationObserver>

          <div class="py-4">
            <div class="w-full border-t border-gray-300"></div>
          </div>

          <p class="flex justify-end text-xs text-gray-400">
            <NuxtLink class="hover:underline hover:text-yellow-500" to="login">Already registered? Login here</NuxtLink>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue';

import { mapGetters } from 'vuex';

export default Vue.extend({
  data() {
    return {
      username: '',
      password: '',
      password_confirm: '',
      email: '',
      loading: false
    };
  },

  computed: {
    ...mapGetters('auth', ['isAuthenticated'])
  },

  methods: {
    async register() {
      try {
        this.loading = true;
        const captcha = await this.$recaptcha.getResponse();

        await this.$services.user.create({
          username: this.username,
          password: this.password,
          password_confirm: this.password_confirm,
          email: this.email,
          captcha
        });

        this.$store.dispatch('toast/success', 'Account successfully created.');
      } catch (e) {
        this.$refs.form.setErrors(e.response.data);
      } finally {
        this.$store.dispatch('toast/error', 'Error creating account.');
        await this.$recaptcha.reset();
        this.loading = false;
      }
    }
  }
});
</script>
