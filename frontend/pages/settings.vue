<template>
  <div>
    <Heading :content="`Settings`" />
    <div class="justify-center w-3/5 p-4 mx-auto my-8">
      <div class="flex space-x-4">
        <div class="w-1/5 p-4">User Settings</div>
        <div class="w-full p-4 bg-white rounded-lg">
          <span class="text-xl font-bold">User</span>
          <hr class="my-2" />
          <ValidationObserver ref="form" v-slot="{ invalid, handleSubmit }">
            <form class="space-y-4" @submit.prevent="handleSubmit(save)">
              <div class="my-4">
                <FormInput v-model="form.email" rules="required|max:32|email" name="email" label="Email" hover />
              </div>
              <div class="my-4">
                <FormInput v-model="form.location" rules="max:32" name="location" label="Location" hover />
              </div>
              <div>
                <label class="block text-sm font-bold text-gray-800" for="bio">Bio</label>
                <textarea
                  v-model="form.profile.bio"
                  type="text"
                  placeholder="Enter some info about yourself (visible on your profile)"
                  maxlength="255"
                  class="w-full px-3 py-2 text-sm text-gray-900 placeholder-gray-500 transition duration-200 ease-in-out bg-gray-100 border-2 border-gray-100 rounded-md focus:outline-none focus:ring-yellow-400 focus:border-yellow-400 focus:bg-white"
                ></textarea>
              </div>
              <FormButton text="Update" :disabled="invalid" :loading="loading" />
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
