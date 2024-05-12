/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{html,js,svelte,ts}"],

  theme: {
    extend: {
      fontFamily: {
        'merriweather': ['Merriweather']
      }
    }
  },
  daisyui: {
    themes: ["light", "dark", "cupcake", "dracula",
      {
        newtheme: {

          "primary": "#22c55e",

          "secondary": "#34d399",

          "accent": "#2dd4bf",

          "neutral": "#d1d5db",

          // "base-100": "#f5f5f4",

          "base-100": "#1c1917",

          "info": "#67e8f9",

          "success": "#00ff00",

          "warning": "#f59e0b",

          "error": "#f87171",
        }
      }
    ],
  },

  plugins: [require("daisyui")]
};