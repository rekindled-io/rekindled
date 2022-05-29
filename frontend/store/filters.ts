import { GetterTree, ActionTree, MutationTree } from 'vuex';
import { shallowFilter, deepFilter } from '@/utils/filters';

export type RootState = ReturnType<typeof state>;

export const state = () => ({
  name: '',
  game: '',
  platform: '',
  lists: {
    games: [],
    platforms: []
  }
});

export const mutations: MutationTree<RootState> = {
  SET_HANDLE: (state, payload) => (state.name = payload),
  SET_PLATFORM: (state, payload) => (state.platform = payload),
  SET_GAME: (state, payload) => (state.game = payload),
  SET_GAMES: (state, payload) => (state.lists.games = payload),
  SET_PLATFORMS: (state, payload) => (state.lists.platforms = payload)
};

export const actions: ActionTree<RootState, RootState> = {
  handle({ commit }, payload) {
    commit('SET_HANDLE', payload);
  },
  game({ commit }, payload) {
    commit('SET_GAME', payload);
  },
  platform({ commit }, payload) {
    commit('SET_PLATFORM', payload);
  },
  clearAll({ commit }) {
    commit('SET_HANDLE', '');
    commit('SET_GAMES', '');
    commit('SET_PLATFORM', '');
  }
};

export const getters: GetterTree<RootState, RootState> = {
  platformFilteredByGame: (state) => {
    return shallowFilter(state.lists.games, state.game, 'name', 'platforms') || state.lists.platforms;
  },
  gameFilteredByPlatforms: (state) => {
    return deepFilter(state.lists.games, state.platform, 'platforms') || state.lists.games;
  }
};
