<template>
  <ModalsBase title="Create a new handle" :open="open" v-on="$listeners">
    <template #body>
      <Loading v-if="$fetchState.pending" />
      <div v-else>
        <ValidationObserver v-slot="{ invalid, handleSubmit }" ref="form">
          <form class="space-y-8" @submit.prevent="handleSubmit(save)">
            <div class="w-full">
              <FormInput v-model="form.name" rules="required|max:32" name="name" label="Name" />
            </div>
            <div v-for="item in gameandplatforms" :key="item.game_name + item.platform_name" class="flex space-x-4">
              <div class="w-full">
                <ValidationProvider slim rules="required" v-slot="{ errors, classes }">
                  <label
                    class="text-sm font-semibold pointer-events-none"
                    for="handle"
                    :class="{
                      'text-gray-400': !errors[0],
                      'text-red-600': errors[0]
                    }"
                  >
                    Select a game
                  </label>
                  <v-select
                    v-model="item.game_name"
                    placeholder="Game"
                    label="name"
                    :options="filterGameByPlatform(games.results, item.platform_name)"
                    :reduce="(game) => game.name"
                    class="style-chooser"
                  />
                  <span :class="classes">{{ errors[0] }}</span>
                </ValidationProvider>
              </div>
              <div class="w-full">
                <ValidationProvider slim rules="required" v-slot="{ errors, classes }">
                  <label
                    class="text-sm font-semibold pointer-events-none"
                    for="handle"
                    :class="{
                      'text-gray-400': !errors[0],
                      'text-red-600': errors[0]
                    }"
                  >
                    Select a platform
                  </label>
                  <v-select
                    v-model="item.platform_name"
                    placeholder="Platform"
                    label="name"
                    :options="filterPlatformByGame(games.results, item.game_name, platforms)"
                    :reduce="(platform) => platform.name"
                    class="style-chooser"
                  />
                  <span :class="classes">{{ errors[0] }}</span>
                </ValidationProvider>
              </div>
            </div>
            <div class="flex items-center space-x-2">
              <span class="text-sm font-semibold text-gray-400">Additional game/platform</span>
              <button
                class="w-1/3 p-0 text-lg font-semibold duration-100 bg-gray-200 rounded"
                :class="{
                  'bg-gray-200 text-gray-300 cursor-not-allowed': invalid,
                  'bg-gray-100 hover:bg-yellow-400': !invalid
                }"
                @click.prevent="addRow"
                :disabled="invalid"
              >
                +
              </button>
              <button
                class="w-1/3 p-0 text-lg font-semibold duration-100 bg-gray-200 rounded"
                :class="{
                  'bg-gray-200 text-gray-300 cursor-not-allowed': invalid,
                  'bg-gray-100 hover:bg-yellow-400': !invalid
                }"
                @click.prevent="removeRow"
                :disabled="gameandplatforms.length <= 1"
              >
                -
              </button>
            </div>
            <FormButton :loading="$fetchState.pending" :disabled="invalid" />
          </form>
        </ValidationObserver>
      </div>
    </template>
  </ModalsBase>
</template>

<script>
import Vue from 'vue';

import test from '@/mixins/handleFilters.js';

export default Vue.extend({
  mixins: [test],

  props: {
    open: {
      type: Boolean,
      required: true
    }
  },

  data() {
    return {
      loading: false,
      handles: [],
      games: [],
      platforms: [],
      platform: '',
      gameandplatforms: [{ game_name: '', platform_name: '' }],
      form: {
        name: '',
        user: 'admin'
      }
    };
  },

  methods: {
    addRow() {
      this.gameandplatforms.push({ game_name: '', platform_name: '' });
    },
    removeRow() {
      this.gameandplatforms.pop();
    },
    close() {
      this.$emit('cancel');
    },
    async save() {
      this.loading = true;

      let payload = [];

      const user = JSON.parse(localStorage.getItem('user'));

      this.gameandplatforms.forEach((elem) => {
        payload.push({
          name: this.form.name,
          user: user.username,
          game_and_platform: {
            game_name: elem['game_name'],
            platform_name: elem['platform_name']
          }
        });
      });

      try {
        await this.$axios.$post(`/handles/`, payload);
        this.loading = false;
        this.close();
        this.$emit('save');

        this.$store.dispatch('toast/success', 'Handle successfully created.');

        for (const field in this.form) {
          this.form[field] = '';
        }

        this.gameandplatforms = [{ game_name: '', platform_name: '' }];
      } catch (e) {
        this.$store.dispatch('toast/error', e);

        this.loading = false;

        this.$nextTick(() => {
          this.$refs.form.setErrors(e.response.data);
        });
      }
    }
  },

  async fetch() {
    this.games = await this.$axios.$get(`/games/`);
    this.platforms = await this.$axios.$get(`/platforms/`);
  }
});
</script>
