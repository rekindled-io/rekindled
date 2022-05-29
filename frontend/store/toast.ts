import { GetterTree, ActionTree, MutationTree } from 'vuex';

export const state = () => ({
  type: '',
  message: ''
});

export type RootState = ReturnType<typeof state>;

export const mutations: MutationTree<RootState> = {
  SET_SUCCESS(state, message) {
    state.type = 'alert-success';
    state.message = message;
  },
  SET_ERROR(state, message) {
    state.type = 'alert-danger';
    state.message = message;
  },
  SET_CLEAR(state) {
    state.type = '';
    state.message = '';
  }
};

export const actions: ActionTree<RootState, RootState> = {
  success({ commit }, message) {
    commit('SET_SUCCESS', message);
  },
  error({ commit }, message) {
    commit('SET_ERROR', message);
  },
  clear({ commit }) {
    commit('SET_CLEAR');
  }
};
