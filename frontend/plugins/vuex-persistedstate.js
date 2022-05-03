import createPersistedState from 'vuex-persistedstate';
import Cookies from 'js-cookie';

export default ({ store }) => {
  createPersistedState({
    key: 'session_cookie',
    paths: ['auth.access_token'],
    storage: {
      getItem: (key) => {
        return Cookies.get(key);
      },
      setItem: (key, value) => Cookies.set(key, value, { sameSite: 'lax', secure: false }),
      removeItem: (key) => Cookies.remove(key)
    }
  })(store);
};
