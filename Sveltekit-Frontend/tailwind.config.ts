/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{html,js,svelte,ts}"],

  theme: {
    extend: {}
  },
  daisyui: {
    themes: ["light", "dark", "cupcake", "dracula"],
  },

  plugins: [require("daisyui")]
};