export default {
  ssr: false,

  head: {
    title: 'rekindled-frontend',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }]
  },

  css: ['~/assets/css/main.css'],

  plugins: [{ src: '~/plugins/vee-validate.js' }, { src: '~/plugins/services.ts' }, { src: '~/plugins/tippy.js' }],

  components: true,

  buildModules: ['@nuxt/typescript-build', '@nuxtjs/tailwindcss', '@nuxtjs/svg'],

  modules: ['@nuxtjs/axios'],

  axios: {
    baseURL: process.env.BASE_URL || 'http://localhost:8000',
    proxyHeaders: false,
    credentials: true
  },

  build: {
    transpile: ['vee-validate/dist/rules']
  },

  publicRuntimeConfig: {
    baseURL: process.env.BASE_URL || 'localhost:8000'
  }
};
