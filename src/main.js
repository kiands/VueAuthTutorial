import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios';
import store from './store'
import vuetify from './plugins/vuetify'

// Interceptor for JWT token (add access_token into each request's header)
// 配置 Axios 基础 URL 和请求头
axios.defaults.baseURL = 'http://localhost:8000/api/';
const exemptedApiList = ['register', 'login'];

// 添加请求拦截器
axios.interceptors.request.use(
  (config) => {
    // 如果请求的 API 不在豁免列表中，添加 JWT 到请求头
    if (!exemptedApiList.includes(config.url.replace(config.baseURL, ''))) {
      const token = localStorage.getItem('token');
      if (token) {
        config.headers['Authorization'] = `Bearer ${token}`;
      }
    }
    return config;
  },
  (error) => {
    // 对请求错误做些什么
    return Promise.reject(error);
  }
);

Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
