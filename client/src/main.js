import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'
import store from './store';   // 确保正确导入
import './index.css'
import Vue3Lottie from 'vue3-lottie'



createApp(App)
    .use(router)
    .use(store)
    .use(Vue3Lottie)
    .mount('#app')
