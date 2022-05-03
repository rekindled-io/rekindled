export default function ({ store, app: { $axios }, redirect }) {
  const IGNORED_PATHS = ['/auth/token/', '/auth/token/refresh/', '/games/', '/platforms/'];

  $axios.onRequest((request) => {
    const isIgnored = IGNORED_PATHS.some((path) => request.url.includes(path));
    if (store.state.auth.access_token && !isIgnored) {
      request.headers.Authorization = 'Bearer ' + store.state.auth.access_token;
    }
    return request;
  });

  $axios.onError((error) => {
    return new Promise((resolve, reject) => {
      const isIgnored = IGNORED_PATHS.some((path) => error.config.url.includes(path));

      const code = parseInt(error.response && error.response.status);

      if (code === 401 && !isIgnored) {
        const { data: { code } = { text_code: null } } = error.response || {};

        if (code === 'token_not_valid') {
          if (error.config.hasOwnProperty('retryAttempts')) {
            store.dispatch('auth/logout');

            return redirect('/login/');
          } else {
            try {
              store.dispatch('auth/refresh');

              return resolve($axios);
            } catch (e) {
              store.dispatch('auth/logout');

              return redirect('/');
            }
          }
        } else {
          store.dispatch('auth/logout');

          return redirect('/');
        }
      }

      return reject(error);
    });
  });
}
