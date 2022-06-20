<template>
  <ModalsBase :title="`Connect with ${data.name}`" v-on="$listeners">
    <template #body>
      <Loading v-if="$fetchState.pending" />
      <ValidationObserver v-else v-slot="{ invalid, handleSubmit }" ref="form">
        <form class="space-y-4" @submit.prevent="handleSubmit(save)">
          <div class="flex">
            <div class="w-full mr-2">
              <ValidationProvider slim rules="required" v-slot="{ errors, classes }">
                <label
                  class="text-sm font-semibold pointer-events-none"
                  :class="{
                    'text-gray-400': !errors[0],
                    'text-red-600': errors[0]
                  }"
                >
                  Select a handle
                </label>
                <v-select
                  v-model="form.handle"
                  placeholder="Select one of your handles"
                  :options="handles.results"
                  :get-option-label="getOptionLabel"
                  vid="handle_id"
                  class="style-chooser"
                >
                  <template slot="option" slot-scope="option">
                    <span class="font-bold">{{ option.name }}</span>
                    <span class="font-normal">
                      {{ option.game_and_platform['game_name'] }} ({{
                        option.game_and_platform['platform_name']
                      }})</span
                    >
                  </template>
                  <span :class="classes">{{ errors[0] }}</span>
                  <span slot="no-options">No matching handles found.</span>
                </v-select>
              </ValidationProvider>
            </div>
          </div>
          <div class="flex">
            <div class="w-full mr-2">
              <label class="text-sm font-semibold text-gray-400 pointer-events-none"> Message </label>
              <textarea
                v-model="form.message"
                type="text"
                placeholder="Type in a short message to the recipient"
                class="textbox"
              />
            </div>
          </div>
          <span class="text-xs text-gray-600">Submitting will send a notification.</span>
          <FormButton :loading="loading" :disabled="invalid" />
        </form>
      </ValidationObserver>
    </template>
  </ModalsBase>
</template>

<script lang="ts">
import Vue, { PropType } from 'vue';
import { Handle, HandleList } from '~/modules/handle/Handle';
import { VeeValidate } from '~/types';

import { buildURLQuery } from '@/utils/filters';

export default Vue.extend({
  props: {
    open: {
      type: Boolean,
      required: true
    },
    data: {
      type: Object as PropType<Handle>,
      required: true
    }
  },

  data() {
    return {
      loading: false,
      handles: {} as HandleList,
      form: {
        handle: null as Handle | null,
        message: ''
      }
    };
  },

  computed: {
    ref(): VeeValidate {
      return this.$refs.form as VeeValidate;
    },

    query(): string {
      return buildURLQuery({
        user: JSON.parse(localStorage.getItem('user') || '')?.username,
        game: this.data.game_and_platform.game_name,
        platform: this.data.game_and_platform.platform_name,
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

      let payload = {
        source_handle_id: this.form.handle!.id,
        target_handle_id: this.data.id,
        message: this.form.message
      };

      try {
        await this.$axios.$post('/kindles/direct/', payload);
        this.$store.dispatch('toast/success', 'Kindle successfully sent.');
        this.close();
      } catch (e: any) {
        this.$store.dispatch('toast/error', 'Error creating kindle.');
        this.$nextTick(() => {
          this.ref.setErrors(e.response.data);
        });
      } finally {
        this.loading = false;
      }
    },

    getOptionLabel(option: any) {
      return (option && option.name) || '';
    }
  },

  async fetch() {
    this.handles = await this.$services.handle.list(this.query);
  }
});
</script>
