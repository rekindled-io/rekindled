import { shallowFilter, deepFilter } from '@/utils/filters';

import Vue from 'vue';

export default Vue.extend({
  data() {
    return {
      games: [],
      platforms: []
    };
  },
  computed: {
    gameFilter: {
      get() {
        return this.$store.state.filters.game;
      },
      set(v) {
        const game = v || '';
        this.$store.commit('filters/SET_GAME', game);
      }
    },
    platformFilter: {
      get() {
        const platform = this.$store.state.filters.platform;
        if (platform.hasOwnProperty('name')) {
          return platform.name;
        }
        return platform;
      },
      set(v) {
        const platform = v || '';
        this.$store.commit('filters/SET_PLATFORM', platform);
      }
    }
  },
  methods: {
    platformFilteredByGame() {
      const result = shallowFilter(this.games, this.gameFilter, 'name', 'platforms');
      return result || this.platforms;
    },
    gameFilteredByPlatform() {
      const result = deepFilter(this.games, this.platformFilter, 'platforms');
      return result || this.games;
    }
  }
});
