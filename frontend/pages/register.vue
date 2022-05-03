<template>
  <div>
    <Title title="Register" />
    <div class="flex items-center justify-center mt-4">
      <div class="auth-form-box">
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
              />
              <FormInput
                v-model="password"
                rules="required|minmax:8,128"
                label="Password"
                name="password"
                type="password"
                vid="password"
                required
              />
              <FormInput
                v-model="password_confirm"
                rules="required|confirmed:password"
                label="Confirm password"
                name="confirm password"
                type="password"
                required
              />
              <FormInput
                v-model="email"
                rules="required|email"
                label="Email"
                name="email"
                vid="email"
                required
              />
              <Recaptcha />
              <FormButton
                text="Register"
                :disabled="invalid"
                :loading="loading"
              />
            </form>
          </ValidationObserver>
          <p class="flex justify-end mt-5 text-xs text-gray-400">
            <NuxtLink class="hover:underline hover:text-yellow-500" to="login"
              >Already registered? Login here</NuxtLink
            >
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  data() {
    return {
      username: "",
      password: "",
      password_confirm: "",
      email: "",
      loading: false,
    };
  },
  computed: {
    ...mapGetters("auth", ["isAuthenticated"]),
  },
  methods: {
    async register() {
      try {
        const captcha = await this.$recaptcha.getResponse();
        this.loading = true;
        await this.$userService.create({
          username: this.username,
          password: this.password,
          password_confirm: this.password_confirm,
          email: this.email,
          captcha,
        });
        await this.$recaptcha.reset();
      } catch (e) {
        this.$refs.form.setErrors(e.response.data);
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>
