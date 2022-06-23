<template>
  <ModalsBase title="Drop a Kindle" :open="open" v-on="$listeners">
    <template #body>
      <Loading v-if="$fetchState.pending" />
      <ValidationObserver v-else v-slot="{ passed, handleSubmit }" ref="form">
        <form class="space-y-6" @submit.prevent="handleSubmit(save)">
          <FormInput v-model="form.from_handle" rules="required|max:32" name="name" label="Name" />
          <v-select
            v-model="form.to_handle"
            placeholder="Connecting handle"
            label="name"
            :options="handles.results"
            class="style-chooser"
          >
            <template slot="option" slot-scope="option">
              {{ option.name }}
              <span class="font-normal"
                >- {{ option.game_and_platform['game_name'] }} ({{ option.game_and_platform['platform_name'] }})</span
              >
            </template>
          </v-select>

          <textarea
            v-model="form.message"
            type="text"
            name=""
            placeholder="Type in a short message to the recipient."
            class="textbox"
          />

          <FormButton :loading="$fetchState.pending" :disabled="!passed" />
        </form>
      </ValidationObserver>
    </template>
  </ModalsBase>
</template>

<script lang="ts">
import Vue from 'vue';
import { Game, GameList } from '~/modules/game/Game';
import { Handle, HandleList } from '~/modules/handle/Handle';
import { Platform } from '~/modules/platform/Platform';
import { User } from '~/modules/user/User';
import { buildURLQuery } from '~/utils/filters';

export default Vue.extend({
  props: {
    open: {
      type: Boolean,
      required: true
    }
  },

  data() {
    return {
      handles: {} as HandleList,
      games: {} as GameList,
      platforms: {} as Platform,
      form: {
        to_handle: {} as Handle,
        from_handle: '',
        for_game: {} as Game,
        on_platform: {} as Platform,
        from_user: {} as User,
        message: ''
      },
      loading: false
    };
  },

  computed: {
    query() {
      return buildURLQuery({
        user: JSON.parse(localStorage.getItem('user') || '')?.username,
        includeSelf: true
      });
    }
  },

  methods: {
    close() {
      this.$emit('cancel');
    },
    async save() {
      this.loading = true;
      let data = {
        source_handle_id: this.form.to_handle.id,
        target_handle: this.form.from_handle,
        game_and_platform: {
          game_name: this.form.to_handle.game_and_platform.game_name,
          platform_name: this.form.to_handle.game_and_platform.platform_name
        },
        sender: this.form.from_user,
        message: this.form.message
      };
      try {
        await this.$axios.$post(`/kindles/seeking/`, data);
        this.loading = false;
        this.close();
      } catch (e) {
        this.loading = false;
      }
    }
  },

  async fetch() {
    this.handles = await this.$services.handle.list(this.query);
    this.games = await this.$services.game.list();
    this.platforms = await this.$services.platform.list();
  }
});
</script>
