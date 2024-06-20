// tailwind.config.js
module.exports = {
  corePlugins: {
    preflight: false,
  },
  content: [
    './main/templates/**/*.html',
    './main/templates/**/*.html',
    './main/static/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        'primary': '#fe7c42',
        'second': '#1b2a3f',
        'bg': '#f3f4f6',
      },
    }
  },
  plugins: [],
}
