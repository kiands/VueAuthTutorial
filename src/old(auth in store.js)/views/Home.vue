<template>
  <div>
    <div v-if="isLoggedIn">
      <p>Hello, {{ username }}</p>
      <button v-on:click="printUsername">state.user</button>
    </div>
    <div v-else>
      <p>Please Login</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: this.$store.state.user,
      isLoggedIn: this.$store.state.isLoggedIn
    }
  },
  methods: {
    printUsername() {
      console.log(this.$store.state.user)
    }
  }
}
</script>