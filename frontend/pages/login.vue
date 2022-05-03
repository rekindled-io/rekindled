<template>
  <div>
    <Title title="Login" />
    <div class="flex items-center justify-center mt-4">
      <div class="auth-form-box">
        <ValidationObserver ref="form" v-slot="{ invalid, handleSubmit }">
          <form class="space-y-8" @submit.prevent="handleSubmit(login)">
            <FormInput
              v-model="username"
              required
              rules="required"
              label="Username"
              name="username"
            />
            <FormInput
              v-model="password"
              required
              rules="required"
              label="Password"
              name="password"
              type="password"
            />
            <FormButton text="Login" :disabled="invalid" :loading="loading" />
          </form>
        </ValidationObserver>
        <p class="flex justify-end mt-5 space-x-1 text-xs text-gray-400">
          <NuxtLink
            class="hover:underline hover:text-yellow-500"
            to="reset-password"
            >Forgot your password?</NuxtLink
          >
          <span>|</span>
          <NuxtLink class="hover:underline hover:text-yellow-500" to="register"
            >Sign up</NuxtLink
          >
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from "vue";
import { mapGetters } from "vuex";

export default Vue.extend({
  middleware({ store, redirect }) {
    const isLoggedIn = store.getters["auth/isAuthenticated"];
    if (isLoggedIn) {
      return redirect("/");
    }
  },
  data() {
    return {
      username: "",
      password: "",
      loading: false,
    };
  },
  computed: {
    ...mapGetters("auth", ["isAuthenticated"]),
  },
  methods: {
    async login() {
      try {
        this.loading = true;
        await this.$store.dispatch("auth/login", {
          username: this.username,
          password: this.password,
        });
        const response = await this.$axios.get("/users/me/");
        localStorage.setItem("user", JSON.stringify(response.data));
        this.$router.push("/dashboard/");
      } catch (e) {
        this.$refs.form.setErrors(e.response.data);
        this.loading = false;
      }
    },
  },
});
</script>
