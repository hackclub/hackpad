import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'
import mdx from "@mdx-js/rollup"

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    // {enforce: 'pre', ...mdx({
    //   extensions: ['.mdx'],
    // })},
    mdx(),
    react(),
  ],
})
