/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
  theme: {
    extend: {
      colors: {
        color1: "#522AB8",
        color2: "#4E3985",
        color3: "#4806EA",
        color4: "#3C3352",
        color5: "#2D2A33",
      },
      backgroundImage: {
        "hero-pattern": "url('/src/assets/image/aegir-chat.png')",
        "footer-texture": "url('./assets/footer-texture.png')",
      },
    },
  },
  plugins: [],
};
