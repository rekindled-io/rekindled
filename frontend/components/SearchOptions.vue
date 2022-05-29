<template>
  <form @submit.prevent="getSearchResults()">
    <div class="items-center justify-center border-gray-500 rounded">
      <span class="text-xs text-gray-500">Search options</span>
      <div class="flex flex-col w-full space-y-4">
        <div>
          <v-select
            v-model="gameFilter"
            placeholder="All games"
            label="name"
            :options="games.results"
            :reduce="(game) => game.name"
            class="style-chooser"
          />
        </div>
        <div>
          <v-select
            v-model="platformFilter"
            placeholder="All platforms"
            label="name"
            :options="platforms"
            :reduce="(platform) => platform.name"
            class="style-chooser"
          />
        </div>
      </div>
    </div>
  </form>
</template>

<script lang="ts">
import MixinFilters from '~/mixins/MixinFilters';

export default MixinFilters.extend({
  mixins: [MixinFilters],

  methods: {
    getSearchResults() {
      const filter = this.$store.state.filters;

      this.$router.push({
        path: '/search',
        query: {
          game: filter.game,
          platform: filter.platform
        }
      });
    }
  },

  watch: {
    gameFilter() {
      this.getSearchResults();
    },
    platformFilter() {
      this.getSearchResults();
    }
  },

  async fetch() {
    this.games = await this.$axios.$get('/games/?simple');
    this.platforms = await this.$axios.$get('/platforms/');
  },

  mounted() {
    const game = this.$router.currentRoute.query.game;
    this.gameFilter = game || '';

    const platform = this.$router.currentRoute.query.platform;
    this.platformFilter = platform || '';
  }
});
</script>
