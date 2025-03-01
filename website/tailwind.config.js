/** @type {import('tailwindcss').Config} */

import typography from '@tailwindcss/typography';


export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      'backgroundColor': '#150C21',
    },
    fontFamily: {
      mono: ['Ubuntu Mono', 'monospace'],
      sans: ['Poppins', 'sans-serif'],
    }

  },
  plugins: [
    typography,
  ],
}

