<template>
  <div id="app">
    <nav>
      <router-link to="/register">Register</router-link>
      <router-link to="/login">Login</router-link>
      <a href="https://github.com/login/oauth/authorize?client_id=89450a7c608bbd0300d8">github oauth</a>
      <v-btn @click="GitHubOAuth">GHB</v-btn>
    </nav>
    <router-view />
    <div>
      <!--div v-if="isLoggedIn"-->
      <div v-if="this.$store.state.auth.isLoggedIn">
        <p>Hello, {{ this.$store.state.auth.user_name }}</p>
        <v-btn v-on:click="jwtAccess">JWT Access</v-btn>
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

    GitHubOAuth() {
      const oauthUrl = 'https://github.com/login/oauth/authorize?client_id=89450a7c608bbd0300d8';
      // const oauthWindow = window.open(oauthUrl, '_blank', 'width=800,height=600');
      const oauthWindow = window.open(oauthUrl)

      // 监听 message 事件
      window.addEventListener('message', (event) => {
        const user_name = event.data.user_name
        const access_token = event.data.access_token
        const refresh_token = event.data.refresh_token
        if (user_name && access_token && refresh_token) {
          // 使用 access_token 进行后续操作，例如将其存储到 Vuex state
          console.log('User name:', user_name);
          console.log('Access token:', access_token);
          console.log('Refresh token:', refresh_token);

          // vuex setUser
          // this.$store.dispatch(
          //   'auth/login', { "oauth": true, "user_name": user_name, "token": access_token }
          // )
          this.$store.commit( // mutations belongs to commit
            'auth/setUser', { "user_name": user_name, "token": access_token, "refresh_token": refresh_token }
          )
        } else {
          console.error('Failed to get access token');
        }

        // 移除事件监听器
        window.removeEventListener('message', this);
      });
    },

    async jwtAccess() {
      // console.log(this.$store.state.auth.user)
      // baseURL is configured so there's no need to use full api path
      const response = await apiClient.get("test")
      console.log(response.data)
    },

    logout() { // actions belongs to dispatch
      this.$store.dispatch(
        'auth/logout'
      )
    },
  }
}
</script>