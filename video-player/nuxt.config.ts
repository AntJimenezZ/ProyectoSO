// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: "2024-04-03",
  devtools: { enabled: true },
  modules: ["@nuxt/ui"],
  colorMode: {
    preference: "light"
  },

  devServer: {

    port: 3000, // default: 3000
    host: '0.0.0.0'
  },

  
});