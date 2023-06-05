import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  base:'./',
  build:{
    outDir:'./../flask-dist'
  },
  server:{
    proxy:{
      '/api':{
        target:'http://127.0.0.1:5000',
        changeOrigin:true,
        ws:true,
        rewrite:(path)=>path.replace(/^\/api/,''),
      }
    }
  }
})
