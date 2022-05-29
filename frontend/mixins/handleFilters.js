import { shallowFilter, deepFilter } from '@/utils/filters';

export default {
  methods: {
    filterPlatformByGame(games, game, platforms) {
      var result = shallowFilter(games, game, 'name', 'platforms');
      return result ? result : platforms;
    },
    filterGameByPlatform(games, platform) {
      var result = deepFilter(games, platform, 'platforms');
      return result ? result : games;
    }
  }
};
