import axios from "axios"
import auth from "@/auth.js"
import jwtDecode from "jwt-decode"

const apiClient = axios.create({
  // baseURL: "http://127.0.0.1:8000/api/",
  baseURL: "https://hzf.ngrok.dev/api/",
  headers: {
    "Content-Type": "application/json",
  },
})

// 这个专用的axios实例是用来防止apiClient上设计的拦截器在需要刷新token时触发循环而设计的
const refreshClient = axios.create({
  baseURL: "http://127.0.0.1:8000/api/",
  // baseURL: "https://hzf.ngrok.dev/api/",
  headers: {
    "Content-Type": "application/json",
  },
})

// 豁免JWT token的URL列表
const exemptedApiList = ['register', 'login', 'services', 'contact', 'contacts', 'carousels', 'cms']

const isTokenExpired = (token) => {
  const decoded = jwtDecode(token)
  const currentTime = Date.now() / 1000
  return decoded.exp < currentTime
}

// 请求拦截器
apiClient.interceptors.request.use(async (config) => {
  const url = config.url.split('/').pop()
  const cmsFeature = config.url.split('/')[0]
  const accessToken = localStorage.getItem('token')
  const refreshToken = localStorage.getItem('refresh_token')

  // 豁免token的URL，不改动直接放行
  // if (exemptedApiList.includes(url) || !accessToken) {
  if (exemptedApiList.includes(url) || exemptedApiList.includes(cmsFeature)) {
    return config
  }

  // 需要token的URL，如果token没过期，加入token后放行
  if (!isTokenExpired(accessToken)) {
    config.headers['Authorization'] = `Bearer ${accessToken}`
    return config
  }

  // 以上两种情况都不是的话，进入此处的判断。需要token的URL，如果token过期，成功申请新的token的话加入后放行。申请失败直接清空状态并退出登录
  if (refreshToken && !isTokenExpired(refreshToken)) {
    try {
      console.log('token expired, refreshing')
      const response = await refreshClient.post('refresh_token', {}, {
        headers: {
          'Authorization': `Bearer ${refreshToken}`
        }
      })
      const newAccessToken = response.data.access_token
      // Update with the new token
      auth.state.token = newAccessToken
      localStorage.setItem('token', newAccessToken)
      config.headers['Authorization'] = `Bearer ${newAccessToken}`
      return config
    } catch (error) {
      console.error('Error refreshing token', error)
      auth.state.user_id = ''
      auth.state.user_name = ''
      auth.state.token = ''
      auth.state.refresh_token = ''
      auth.state.isLoggedIn = false
      localStorage.removeItem('user_id')
      localStorage.removeItem('user_name')
      localStorage.removeItem('token')
      localStorage.removeItem('refresh_token')
      localStorage.removeItem('isLoggedIn')
      // window.location.href = '/logout'
    }
  } else {
    console.error('Error refreshing token', error)
    auth.state.user_id = ''
    auth.state.user_name = ''
    auth.state.token = ''
    auth.state.refresh_token = ''
    auth.state.isLoggedIn = false
    localStorage.removeItem('user_id')
    localStorage.removeItem('user_name')
    localStorage.removeItem('token')
    localStorage.removeItem('refresh_token')
    localStorage.removeItem('isLoggedIn')
    // window.location.href = '/logout'
  }
})

export default apiClient