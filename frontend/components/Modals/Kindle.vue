<template>
  <ModalsBase title="Drop a Kindle" :open="open" v-on="$listeners">
    <template #body>
      <Loading v-if="$fetchState.pending" />
      <ValidationObserver v-else v-slot="{ invalid, handleSubmit }" ref="form">
        <form class="space-y-6" @submit.prevent="handleSubmit(save)">
          <ValidationProvider slim rules="required|max:32" v-slot="{ errors, classes }" vid="name">
            <input
              class="w-full border-b-2 border-gray-500 px-2 font-bold text-sm py-0.5 pl-2 outline-none"
              v-model="form.from_handle"
              placeholder="I am looking for..."
              label="name"
            />
            <span :class="classes">{{ errors[0] }}</span>
          </ValidationProvider>
          <v-select
            v-model="form.to_handle"
            placeholder="Connecting handle"
            label="name"
            :options="handles.results"
            class="style-chooser"
            transition=""
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
          ></textarea>
          <FormButton :loading="$fetchState.pending" :disabled="invalid" />
        </form>
      </ValidationObserver>
    </template>
  </ModalsBase>
</template>

<script>
export default {
  props: {
    open: {
      type: Boolean,
      required: true
    }
  },

  data() {
    return {
      handles: [],
      games: [],
      platforms: [],
      form: {
        to_handle: '',
        from_handle: '',
        for_game: '',
        on_platform: '',
        from_user: '',
        message: ''
      },
      loading: false
    };
  },

  methods: {
    close() {
      this.$emit('cancel');
    },
    async save() {
      this.loading = true;
      let data = {
        source_handle_id: this.form.to_handle.id,
        handle: this.form.from_handle,
        game_and_platform: {
          game_name: this.form.for_game.name,
          platform_name: this.form.on_platform
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
    const user = JSON.parse(localStorage.getItem('user'));
    this.handles = await this.$axios.$get(`/handles/user/${user.username}/`);
    this.games = await this.$axios.$get(`/games/`);
    this.platforms = await this.$axios.$get(`/platforms/`);
  }
};
</script>
