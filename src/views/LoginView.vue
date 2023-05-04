<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="loginUser">
      <div>
        <label for="email">Email</label>
        <input type="email" id="email" v-model="user.email" required>
      </div>
      <div>
        <label for="password">Password</label>
        <input type="password" id="password" v-model="user.password" required>
      </div>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
// import { mapActions } from 'vuex'

export default {
  data() {
    return {
      user: {
        email: '',
        password: ''
      }
    }
  },
  methods: {
    // ...mapActions('auth', ['login']),
    async loginUser() {
      try {
        // await this.login(this.user)
        // 模块化的时候如果不配置namespaced: true的话就仍然是this.$store.dispatch('login', this.user)
        await this.$store.dispatch('auth/login', this.user)
        this.$router.push('/')
      } catch (error) {
        console.log(error)
      }
    }
  }
}
</script>
