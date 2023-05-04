<template>
  <div>
    <h1>Register</h1>
    <form @submit.prevent="registerUser">
      <div>
        <label for="user_name">Name</label>
        <!--If you want to change the record name, be careful with v-model-->
        <input type="text" id="user_name" v-model="user.user_name" required>
      </div>
      <div>
        <label for="email">Email</label>
        <input type="email" id="email" v-model="user.email" required>
      </div>
      <div>
        <label for="password">Password</label>
        <input type="password" id="password" v-model="user.password" required>
      </div>
      <button type="submit">Register</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user: {
        user_name: '',
        email: '',
        password: ''
      }
    }
  },
  methods: {
    async registerUser() {
      try {
        await this.$store.dispatch('auth/register', this.user)
        this.$router.push('/')
      } catch (error) {
        console.log(error)
      }
    }
  }
}
</script>
