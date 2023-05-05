import axios from "axios"
import jwtDecode from "jwt-decode"

const apiClient = axios.create({
  baseURL: "http://localhost:8000/api/", // 替换为您的API基础URL
  headers: {
    "Content-Type": "application/json",
  },
})

const exemptedApiList = ['register', 'login']

// 请求拦截器
apiClient.interceptors.request.use(async (config) => {
  // 如果不是豁免的URL
  if (!exemptedApiList.includes(config.url.replace(config.baseURL, ''))) {
    const token = localStorage.getItem("token")
    const refreshToken = localStorage.getItem("refresh_token")

    // 如果有访问令牌并且令牌过期
    if (token && isTokenExpired(token)) {
      try {
        // 使用刷新令牌获取新的访问令牌
        const response = await apiClient.post("/refresh_token", {}, { headers: { Authorization: `Bearer ${refreshToken}` } })
        const newAccessToken = response.data.access_token

        // 将新的访问令牌存储到localStorage
        localStorage.setItem("token", newAccessToken)

        // 用新的访问令牌更新请求头
        config.headers["Authorization"] = `Bearer ${newAccessToken}`
      } catch (error) {
        // 如果刷新失败，清除登陆状态并跳转到登录页面
        localStorage.removeItem('user_name')
        localStorage.removeItem('token')
        localStorage.removeItem('refresh_token')
        localStorage.removeItem('isLoggedIn')
        // 重定向
        // window.location.href = "/login";
      }
    } else if (token) {
      config.headers["Authorization"] = `Bearer ${token}`
    }
  }
  return config;
});

// 解码JWT令牌并检查是否过期
function isTokenExpired(token) {
  const tokenData = jwtDecode(token)
  const currentTime = Date.now() / 1000

  return tokenData.exp < currentTime
}

export default apiClient