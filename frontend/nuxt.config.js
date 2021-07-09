export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: "taads",
    htmlAttrs: {
      lang: "en"
    },
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      { hid: "description", name: "description", content: "" }
    ],
    link: [{ rel: "icon", type: "image/x-icon", href: "/favicon.ico" }],
    link: [
      {
        rel: "stylesheet",
        href:
          "https://fonts.googleapis.com/css2?family=Ubuntu:ital,wght@0,300;0,400;0,700;1,300;1,700&display=swap"
      }
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/typescript
    "@nuxt/typescript-build"
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/bootstrap
    "bootstrap-vue/nuxt",
    "@nuxtjs/toast"
  ],
  toast: {
    position: "bottom-right",
    register: [
      // Register custom toasts
      {
        name: "my-error",
        message: "Oops...Something went wrong",
        duration: 3000,
        options: {
          type: "error"
        }
      }
    ]
  },
  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {},
  env: {
    BACKEND_BASE_URL: "https://project-taads-266ec.ondigitalocean.app/"
  },
  typescript: {
    typeCheck: false, // disable ForkTsCheckerWebpackPlugin type checking
    loaders: {
      loaders: {
        ts: {
          silent: true
        },
        tsx: {
          silent: true
        }
      }
    }
  }
};
