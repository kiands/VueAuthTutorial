<template>
  <div style="height: 260px; display: flex; flex-direction: column; justify-content: center; align-items: center">
    <div
      v-if="!this.$store.state.auth.isLoggedIn"
      style="height: 100px; width: 200px; display: flex; flex-direction: column; justify-content: space-around;"
    >
      <v-btn @click="GoogleOAuth">Login via Google</v-btn>
    </div>
    <div>
      <!--div v-if="isLoggedIn"-->
      <div v-if="this.$store.state.auth.isLoggedIn" style="display: flex; flex-direction: column; align-items: center">
        <p>Hello, {{ this.$store.state.auth.user_name }}!</p>
        <v-btn v-on:click="logout">Logout</v-btn>
      </div>
      <div v-else>
        <p>Please Login</p>
      </div>
    </div>
  </div>
</template>

<script>
import apiClient from "@/api.js"
export default {
  name: 'AuthComponent',
  // this should cooperate with window.open to oauth provider at front end, shouldn't be a <a> tag
  // mounted() {
  //   window.addEventListener('message', this.show, false)
  // },
  methods: {
    // openGithub() {
    //   window.open('https://github.com/login/oauth/authorize?client_id=89450a7c608bbd0300d8')
    // },
    // show() {
    //   console.log(1)
    // },

    GoogleOAuth() {
      const oauthUrl = 'https://accounts.google.com/o/oauth2/auth?client_id=998548956155-pk7d91gdk0pevvub0m6u7ffrn9hqbnb5.apps.googleusercontent.com&response_type=code&scope=openid%20email%20profile&redirect_uri=https://hzf.ngrok.dev/api/google/oauth';
      // const oauthWindow = window.open(oauthUrl, '_blank', 'width=800,height=600');
      const oauthWindow = window.open(oauthUrl)

      // 监听 message 事件
      window.addEventListener('message', (event) => {
        const user_id = event.data.user_id
        const user_name = event.data.user_name
        const access_token = event.data.access_token
        const refresh_token = event.data.refresh_token
        if (user_name && access_token && refresh_token) {
          // 使用 access_token 进行后续操作，例如将其存储到 Vuex state
          console.log('User id:', user_id);
          console.log('User name:', user_name);
          console.log('Access token:', access_token);
          console.log('Refresh token:', refresh_token);

          // vuex setUser
          // this.$store.dispatch(
          //   'auth/login', { "oauth": true, "user_name": user_name, "token": access_token }
          // )
          this.$store.commit( // mutations belongs to commit
            'auth/setUser', { "user_id": user_id, "user_name": user_name, "token": access_token, "refresh_token": refresh_token }
          )
        } else {
          console.error('Failed to get access token');
        }

        // 移除事件监听器
        window.removeEventListener('message', this);
      });
    },

    // This component calls Vuex, Vuex uses the interceptor named apiClient
    logout() { // actions belongs to dispatch
      this.$store.dispatch(
        'auth/logout'
      )
    },
  }
}
</script>