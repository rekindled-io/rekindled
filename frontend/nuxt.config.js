export default {
  ssr: false,

  head: {
    title: 'Rekindled | Reconnecting long lost gamers',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      {
        rel: 'stylesheet preload prefetch',
        href: 'https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900'
      },
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  css: ['~/assets/css/main.css'],

  plugins: [
    { src: '~/plugins/vee-validate.js' },
    { src: '~/plugins/services.ts' },
    { src: '~/plugins/tippy.js' },
    { src: '~/plugins/axios.js' },
    { src: '~/plugins/vuex-persistedstate.js' },
    { src: '~/plugins/truncate.js' },
    { src: '~/plugins/vue-select.js' }
  ],

  components: true,

  buildModules: ['@nuxt/typescript-build', '@nuxtjs/tailwindcss', '@nuxtjs/svg'],

  modules: ['@nuxtjs/axios', '@nuxtjs/recaptcha'],

  axios: {
    baseURL: process.env.BASE_URL || 'http://localhost:8000',
    proxyHeaders: false,
    credentials: true
  },

  build: {
    transpile: ['vee-validate/dist/rules']
  },

  publicRuntimeConfig: {
    baseURL: process.env.BASE_URL || 'localhost:8000',
    title: 'Rekindled'
  },

  recaptcha: {
    siteKey: process.env.RECAPTCHA_SITE_KEY,
    version: 'v2',
    hideBadge: true,
    size: 'invisible'
  }
};
