<template>
  <div>
    <Heading :content="`Settings`" />
    <div class="justify-center w-3/5 p-4 mx-auto my-8">
      <div class="flex space-x-4">
        <div class="w-1/5 p-4">User Settings</div>
        <div class="w-full p-4 bg-white border-2 border-black rounded">
          <span class="text-xl font-bold">User</span>
          <hr class="my-2" />
          <ValidationObserver ref="form" v-slot="{ passed, handleSubmit }">
            <form class="space-y-4" @submit.prevent="handleSubmit(save)">
              <FormInput
                v-model="form.original_email"
                rules="required|max:32|email"
                name="email"
                label="Email"
                placeholder="whoami@example.com"
                hover
              />
              <FormInput
                v-model="form.profile.location"
                rules="max:32"
                name="location"
                label="Location"
                placeholder="The Moon"
                hover
              />
              <FormTextarea label="Bio" v-model="form.profile.bio" />
              <FormButton text="Update" :disabled="!passed" />
            </form>
          </ValidationObserver>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  async asyncData(context) {
    const data = await context.$axios.$get(`users/me`);
    return { form: data };
  },

  data() {
    return {
      form: {
        username: '',
        email: '',
        bio: ''
      }
    };
  },

  methods: {
    async save() {
      try {
        await this.$axios.$patch(`/users/me/`, this.form);
      } catch (e) {}
    }
  }
});
</script>
