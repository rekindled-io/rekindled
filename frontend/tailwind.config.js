module.exports = {
  mode: 'jit',
  content: ['./src/**/*.{html,js}'],
  theme: {
    extend: {
      transitionProperty: {
        width: 'width'
      }
    }
  },
  plugins: []
};
