import { GetterTree, ActionTree, MutationTree } from 'vuex';

export type State = ReturnType<typeof state>;

export const AUTH_MUTATIONS = {
  SET_PAYLOAD: 'SET_PAYLOAD',
  LOGOUT: 'LOGOUT'
};

export const state = () => ({
  access_token: null,
  username: null,
  profile: null
});

export const mutations: MutationTree<State> = {
  [AUTH_MUTATIONS.SET_PAYLOAD](state, { access }) {
    state.access_token = access;
  },
  [AUTH_MUTATIONS.LOGOUT](state) {
    state.access_token = null;
    state.username = null;
  }
};

export const actions: ActionTree<State, State> = {
  async login({ commit }, { username, password }) {
    const {
      data: { access }
    } = await this.$axios.post('/auth/token/', { username, password });

    commit(AUTH_MUTATIONS.SET_PAYLOAD, { access });
  },

  async refresh({ commit }) {
    const {
      data: { access }
    } = await this.$axios.post('/auth/token/refresh/');

    commit(AUTH_MUTATIONS.SET_PAYLOAD, { access });
  },

  async logout({ commit }) {
    await this.$axios.$post(`/auth/token/logout/`);

    commit(AUTH_MUTATIONS.LOGOUT);
  }
};

export const getters: GetterTree<State, State> = {
  isAuthenticated: (state) => {
    return state.access_token && state.access_token !== '';
  }
};
