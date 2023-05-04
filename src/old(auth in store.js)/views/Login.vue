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
    async loginUser() {
      try {
        await this.$store.dispatch('login', this.user)
        this.$router.push('/')
      } catch (error) {
        console.log(error)
      }
    }
  }
}
</script>
